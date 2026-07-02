# encode = utf-8

import os
import datetime

from flask import current_app
from werkzeug.utils import secure_filename
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.modules.module.dao import daoModules

DATA_MODULE_SUB_TYPES = ['data_manager', 'data_miner', 'data_analyzer', 'data_demonstrator']
ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'csv', 'json', 'db', 'sqlite', 'sqlite3'}


def get_data_storage_path():
    """
    Get the base data storage path from app config.
    Uses DATA_SOURCE_PATH from config.py as the root directory.
    Falls back to a default if not configured.

    Returns:
        str: Base data storage directory path
    """
    return current_app.config.get('DATA_SOURCE_PATH', os.path.join(current_app.root_path, 'data_storage'))


def is_data_sub_type(module_sub_type):
    """
    Check if module sub_type is a data-related type.

    Args:
        module_sub_type (str): Module subtype to check

    Returns:
        bool: True if it's a data-related subtype
    """
    return module_sub_type in DATA_MODULE_SUB_TYPES


def is_allowed_file(filename):
    """
    Check if file extension is in the allowed list.

    Args:
        filename (str): Original filename

    Returns:
        bool: True if file extension is allowed
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@process_log
def get_data_files(plan_id):
    """
    Get all data files from data-related modules under the specified plan.
    Scans module data directories for files and returns their information.

    Args:
        plan_id (int): Plan ID to query

    Returns:
        list: List of file info dicts containing file_name, file_path, file_size,
              upload_time, module_id, module_name
    """
    try:
        # Get all modules under the plan
        modules = daoModules.get_modules(plan_id=plan_id)
    except Exception as e:
        raise Exception(f"获取模组列表失败: {str(e)}")

    data_storage_path = get_data_storage_path()
    files = []

    for module in modules:
        # Filter data-related modules only
        if not is_data_sub_type(module.get('module_sub_type', '')):
            continue

        module_id = module.get('module_id')
        module_name = module.get('name')
        module_dir = os.path.join(data_storage_path, f'plan_{plan_id}', f'module_{module_id}')

        if not os.path.exists(module_dir):
            continue

        # Scan module data directory recursively for files
        for root, dirs, filenames in os.walk(module_dir):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                try:
                    file_stat = os.stat(file_path)
                    # Build relative path from data_storage_path
                    rel_path = os.path.relpath(file_path, data_storage_path)
                    # Extract timestamp from directory structure:
                    # data_storage/plan_{plan_id}/module_{module_id}/{timestamp}/{filename}
                    path_parts = rel_path.replace('\\', '/').split('/')
                    upload_time = ''
                    if len(path_parts) >= 3:
                        upload_time = path_parts[2]

                    # Format upload_time from YYYYMMDDHHMMSS to yyyy-mm-dd hh:mm:ss
                    formatted_time = ''
                    if upload_time and len(upload_time) >= 14:
                        formatted_time = f'{upload_time[0:4]}-{upload_time[4:6]}-{upload_time[6:8]} ' \
                                        f'{upload_time[8:10]}:{upload_time[10:12]}:{upload_time[12:14]}'
                    else:
                        formatted_time = upload_time

                    files.append({
                        'file_name': filename,
                        'file_path': rel_path.replace('\\', '/'),
                        'file_size': file_stat.st_size,
                        'upload_time': formatted_time,
                        'module_id': module_id,
                        'module_name': module_name,
                        'module_subtype_name': module.get('module_sub_type', '')
                    })
                except OSError:
                    continue

    return files


@process_log
def upload_data_file(module_id, file):
    """
    Upload a data file to the specified module's data storage directory.
    plan_id is derived from module's belong_plan_id.
    Validates module type, file extension, and saves with timestamp prefix.

    Args:
        module_id (int): Target module ID
        file: File object from request.files

    Returns:
        dict: File info dict containing file_name, file_path, module_id, upload_time
              or error dict on failure
    """
    # Validate file presence
    if file is None or file.filename == '':
        return {'success': False, 'error': '未选择文件'}

    # Validate file extension
    if not is_allowed_file(file.filename):
        return {'success': False, 'error': '不支持的文件类型'}

    # Get module info by module_id (derive belong_plan_id from module data)
    try:
        all_modules = daoModules.get_modules()
    except Exception as e:
        return {'success': False, 'error': f'获取模组列表失败: {str(e)}'}

    target_module = None
    for m in all_modules:
        if m.get('module_id') == module_id:
            target_module = m
            break

    if target_module is None:
        return {'success': False, 'error': '模组不存在'}

    if not is_data_sub_type(target_module.get('module_sub_type', '')):
        return {'success': False, 'error': '目标模块不是数据模块'}

    # Derive plan_id from module's belong_plan_id
    plan_id = target_module.get('belong_plan_id')
    if plan_id is None:
        return {'success': False, 'error': '模组未关联到任何计划'}

    # Build storage path
    data_storage_path = get_data_storage_path()
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    upload_dir = os.path.join(data_storage_path, f'plan_{plan_id}', f'module_{module_id}', timestamp)

    # Ensure directory exists
    try:
        os.makedirs(upload_dir, exist_ok=True)
    except OSError as e:
        return {'success': False, 'error': f'创建存储目录失败: {str(e)}'}

    # Secure and save file
    safe_filename = secure_filename(file.filename)
    save_path = os.path.join(upload_dir, safe_filename)
    try:
        file.save(save_path)
    except Exception as e:
        return {'success': False, 'error': f'文件保存失败: {str(e)}'}

    # Build relative path for response
    rel_path = os.path.relpath(save_path, data_storage_path).replace('\\', '/')

    return {
        'success': True,
        'file_info': {
            'file_name': safe_filename,
            'file_path': rel_path,
            'module_id': module_id,
            'upload_time': timestamp
        }
    }


@process_log
def delete_data_file(file_path):
    """
    Delete an uploaded data file from the storage path.
    Performs security validation to prevent path traversal attacks
    and ensures the file is within the allowed storage range.

    Args:
        file_path (str): Relative path of the file to delete

    Returns:
        dict: Success or error response
    """
    if not file_path:
        return {'success': False, 'error': '未指定文件路径'}

    # Prevent path traversal
    if '..' in file_path:
        return {'success': False, 'error': '非法的文件路径'}

    data_storage_path = get_data_storage_path()
    full_path = os.path.abspath(os.path.join(data_storage_path, file_path))

    # Security check: ensure resolved path is within data storage path
    if not full_path.startswith(os.path.abspath(data_storage_path)):
        return {'success': False, 'error': '文件不在可删除范围内'}

    # Check if file exists
    if not os.path.exists(full_path):
        return {'success': False, 'error': '文件不存在'}

    # Ensure it's a file, not a directory
    if not os.path.isfile(full_path):
        return {'success': False, 'error': '指定路径不是文件'}

    # Execute deletion
    try:
        os.remove(full_path)
    except Exception as e:
        return {'success': False, 'error': f'文件删除失败: {str(e)}'}

    # Verify deletion
    if os.path.exists(full_path):
        return {'success': False, 'error': '文件删除未完全生效'}

    return {'success': True, 'message': '文件删除成功'}
