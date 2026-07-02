# encode = utf-8

import datetime
import json
import os
import sqlite3

import pandas as pd
import openpyxl
from flask import current_app
from werkzeug.utils import secure_filename

from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.modules.module.dao import daoModules
from features.data_power.modules.data_miner.script import scriptDataMiner
from features.data_power.modules.data_miner.dao import daoDataMiner

ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'csv', 'json', 'db', 'sqlite', 'sqlite3'}


def get_data_storage_path():
    """
    Get the base data storage path from app config.
    """
    return current_app.config.get('DATA_SOURCE_PATH', os.path.join(current_app.root_path, 'data_storage'))


def _sanitize_table_name(name):
    """
    将 sheet/table 名称安全化为合法的 sqlite 表名。
    替换特殊字符为下划线，去除多余空格。
    """
    safe = secure_filename(name)
    # secure_filename 可能去除中文等字符，若结果为空则用默认名
    if not safe:
        return 'data_table'
    # 替换可能的空格
    safe = safe.replace(' ', '_').replace('-', '_')
    return safe


def _clean_dataframe(df):
    """
    对单个 DataFrame 执行数据清洗：
    - 去除完全为空的列和行
    - 列名去除首尾空格并转为英文大写
    - 去除完全重复的行
    """
    df = df.dropna(axis=1, how='all')
    df = df.dropna(axis=0, how='all')
    df = df.drop_duplicates()
    # 列名标准化：去空格 + 大写
    if len(df.columns) > 0:
        df.columns = df.columns.astype(str).str.strip().str.upper()
    return df


def _clean_data(data):
    """
    对 script 返回的 data dict 中所有 DataFrame 执行清洗。
    返回清洗后的 data dict 和总记录数。
    """
    total_records = 0
    cleaned_data = {}
    for key, value in data.items():
        if isinstance(value, pd.DataFrame):
            cleaned_df = _clean_dataframe(value)
            cleaned_data[key] = cleaned_df
            total_records += len(cleaned_df)
        else:
            cleaned_data[key] = value
    return cleaned_data, total_records


@process_log
def get_source_files(plan_id):
    """
    获取指定 plan 下所有 data_manager 模块的源数据文件列表。

    Args:
        plan_id (int): 计划 ID

    Returns:
        list: 文件信息列表，每项包含 file_name, file_path, file_size,
              upload_time, module_id, module_name
    """
    try:
        modules = daoModules.get_modules(plan_id=plan_id)
    except Exception as e:
        raise Exception(f"获取模组列表失败: {str(e)}")

    data_storage_path = get_data_storage_path()
    files = []

    for module in modules:
        if module.get('module_sub_type', '') != 'data_manager':
            continue

        module_id = module.get('module_id')
        module_name = module.get('name')
        module_dir = os.path.join(data_storage_path, f'plan_{plan_id}', f'module_{module_id}')

        if not os.path.exists(module_dir):
            continue

        for root, dirs, filenames in os.walk(module_dir):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                try:
                    file_stat = os.stat(file_path)
                    rel_path = os.path.relpath(file_path, data_storage_path)
                    # 从目录结构中提取时间戳：data_storage/plan_{plan_id}/module_{module_id}/{timestamp}/{filename}
                    path_parts = rel_path.replace('\\', '/').split('/')
                    upload_time = ''
                    if len(path_parts) >= 3:
                        upload_time = path_parts[2]

                    # 格式化时间：YYYYMMDDHHMMSS -> yyyy-mm-dd hh:mm:ss
                    formatted_time = ''
                    if upload_time and len(upload_time) >= 14:
                        formatted_time = (f'{upload_time[0:4]}-{upload_time[4:6]}-{upload_time[6:8]} '
                                         f'{upload_time[8:10]}:{upload_time[10:12]}:{upload_time[12:14]}')
                    else:
                        formatted_time = upload_time

                    file_ext = os.path.splitext(filename)[1].lower().lstrip('.')

                    files.append({
                        'file_name': filename,
                        'file_path': rel_path.replace('\\', '/'),
                        'file_size': file_stat.st_size,
                        'upload_time': formatted_time,
                        'module_id': module_id,
                        'module_name': module_name,
                        'file_type': file_ext
                    })
                except OSError:
                    continue

    return files


@process_log
def get_processed_files(plan_id, module_id=None):
    """
    获取指定 plan 下 data_miner 模块的处理后文件列表。
    如果指定了 module_id，只返回该模组的文件；否则返回所有 data_miner 模组的文件。

    Args:
        plan_id (int): 计划 ID
        module_id (int, optional): 模组 ID，若提供则只返回该模组的文件

    Returns:
        list: 文件信息列表
    """
    try:
        modules = daoModules.get_modules(plan_id=plan_id)
    except Exception as e:
        raise Exception(f"获取模组列表失败: {str(e)}")

    data_storage_path = get_data_storage_path()
    files = []

    for module in modules:
        # 如果指定了 module_id，只处理对应模组；否则只处理 data_miner 模组
        mod_id = module.get('module_id')
        if module_id is not None:
            if mod_id != module_id:
                continue
        else:
            if module.get('module_sub_type', '') != 'data_miner':
                continue

        module_name = module.get('name')
        module_dir = os.path.join(data_storage_path, f'plan_{plan_id}', f'module_{mod_id}')

        if not os.path.exists(module_dir):
            continue

        for root, dirs, filenames in os.walk(module_dir):
            # 先读取元数据文件（如果有）
            meta_info = {}
            for fn in filenames:
                if fn.endswith('.meta.json'):
                    try:
                        meta_path = os.path.join(root, fn)
                        with open(meta_path, 'r', encoding='utf-8') as f:
                            meta_info = json.load(f)
                    except Exception:
                        meta_info = {}
                    break

            for filename in filenames:
                # 仅筛选 .db 和 .json 文件（排除 .meta.json）
                ext = os.path.splitext(filename)[1].lower()
                if ext not in ('.db', '.json'):
                    continue

                file_path = os.path.join(root, filename)
                try:
                    file_stat = os.stat(file_path)
                    rel_path = os.path.relpath(file_path, data_storage_path)
                    path_parts = rel_path.replace('\\', '/').split('/')
                    processed_time = ''
                    if len(path_parts) >= 3:
                        processed_time = path_parts[2]

                    formatted_time = ''
                    if processed_time and len(processed_time) >= 14:
                        formatted_time = (f'{processed_time[0:4]}-{processed_time[4:6]}-{processed_time[6:8]} '
                                         f'{processed_time[8:10]}:{processed_time[10:12]}:{processed_time[12:14]}')
                    else:
                        formatted_time = processed_time

                    output_format = 'sqlite' if ext == '.db' else 'json'

                    files.append({
                        'file_name': filename,
                        'file_path': rel_path.replace('\\', '/'),
                        'file_size': file_stat.st_size,
                        'processed_time': formatted_time,
                        'module_id': mod_id,
                        'module_name': module_name,
                        'output_format': output_format,
                        'source_file': meta_info.get('source_file', '')
                    })
                except OSError:
                    continue

    return files


@process_log
def process_file(plan_id, source_file_path, module_id):
    """
    处理指定源文件，执行读取 -> 清洗 -> 转换 -> 保存的主流程。

    流程：
    1. 安全验证（路径穿越防护、文件存在性、扩展名支持）
    2. 使用 script 层读取文件数据
    3. 统一数据清洗（去空、标准化列名、去重）
    4. 根据数据格式类型决定输出为 sqlite 或 json
    5. 保存到目标路径并返回处理结果

    Args:
        plan_id (int): 计划 ID
        source_file_path (str): 源文件相对路径（相对于 DATA_SOURCE_PATH）
        module_id (int): 目标 data_miner 模块 ID

    Returns:
        dict: 处理结果，包含 source_file, source_file_type, output_file_path,
              output_file_type, output_format, record_count, processed_at
    """
    # --- a) 安全验证 ---
    if '..' in source_file_path:
        raise Exception("非法的文件路径：包含路径穿越字符")

    data_storage_path = get_data_storage_path()
    full_source_path = os.path.abspath(os.path.join(data_storage_path, source_file_path))

    if not os.path.exists(full_source_path):
        raise Exception(f"源文件不存在: {source_file_path}")

    if not os.path.isfile(full_source_path):
        raise Exception(f"指定路径不是文件: {source_file_path}")

    # 获取文件扩展名并验证
    ext = os.path.splitext(full_source_path)[1].lower().lstrip('.')
    if ext not in ALLOWED_EXTENSIONS:
        raise Exception(f"不支持的文件类型: .{ext}")

    # --- b) 读取数据 ---
    reader_method_name = scriptDataMiner.get_reader_for_file(full_source_path)
    if reader_method_name is None:
        raise Exception(f"无法获取文件读取方法: .{ext}")

    reader_method = getattr(scriptDataMiner, reader_method_name)
    read_result = reader_method(full_source_path)

    if not read_result.get('success'):
        error_msg = read_result.get('metadata', {}).get('error', '未知错误')
        raise Exception(f"文件读取失败: {error_msg}")

    data = read_result['data']
    format_type = read_result.get('format_type', 'relational')

    # --- c) 数据清洗（FR-5）---
    cleaned_data, total_records = _clean_data(data)

    # --- d) 判断输出格式 ---
    if format_type == 'relational':
        output_file_type = 'db'
        output_format = 'sqlite'
    else:
        output_file_type = 'json'
        output_format = 'json'

    # --- e) 生成输出路径 ---
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    source_filename = os.path.basename(full_source_path)
    source_name_no_ext = os.path.splitext(source_filename)[0]
    safe_filename = secure_filename(source_name_no_ext)
    if not safe_filename:
        safe_filename = 'output'

    output_dir = os.path.join(data_storage_path, f'plan_{plan_id}', f'module_{module_id}', timestamp)
    output_filename = f'{safe_filename}.{output_file_type}'
    output_path = os.path.join(output_dir, output_filename)

    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        raise Exception(f"创建输出目录失败: {str(e)}")

    # --- f) 保存数据 ---
    if output_format == 'sqlite':
        # 关系型 -> sqlite
        for key, df in cleaned_data.items():
            if not isinstance(df, pd.DataFrame):
                continue

            # 确定表名
            # 多表情况（xlsx 多 sheet / db 多 table）：使用 key（sheet/table 名称）
            # 单表情况（csv、单 sheet xlsx、单表 json）：使用原始文件名
            if len(cleaned_data) == 1:
                table_name = _sanitize_table_name(source_name_no_ext)
            else:
                table_name = _sanitize_table_name(key)
                if not table_name:
                    table_name = _sanitize_table_name(key)

            daoDataMiner.create_table_from_dataframe(output_path, df, table_name)
    else:
        # 非关系型 -> json
        with open(output_path, 'w', encoding='utf-8') as f:
            # 将 DataFrame 转为可序列化格式
            serializable_data = {}
            for key, value in cleaned_data.items():
                if isinstance(value, pd.DataFrame):
                    serializable_data[key] = value.to_dict(orient='records')
                else:
                    serializable_data[key] = value
            json.dump(serializable_data, f, ensure_ascii=False, indent=2)

    # 保存元数据文件，用于后续 get_processed_files 读取 source_file 信息
    meta = {
        'source_file': source_file_path,
        'source_file_type': ext,
        'processed_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'record_count': total_records,
        'output_format': output_format
    }
    meta_path = os.path.join(output_dir, f'{safe_filename}.meta.json')
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    # --- g) 返回结果 ---
    rel_output_path = os.path.relpath(output_path, data_storage_path).replace('\\', '/')
    processed_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        'source_file': source_file_path,
        'source_file_type': ext,
        'output_file_path': rel_output_path,
        'output_file_type': output_file_type,
        'output_format': output_format,
        'record_count': total_records,
        'processed_at': processed_at
    }


@process_log
def view_processed_file(plan_id, file_path):
    """
    查看已处理文件的内容

    根据文件扩展名决定读取方式：
    - .db 文件：扫描所有表并返回每张表的数据
    - .json 文件：直接读取文件内容
    - 其他类型返回错误

    Args:
        plan_id (int): 计划 ID
        file_path (str): 文件相对路径（相对于 DATA_SOURCE_PATH）

    Returns:
        dict: {"success": True, "data": ...}
    """
    if plan_id is None:
        raise Exception("缺少必要参数: plan_id")
    if not file_path:
        raise Exception("缺少必要参数: file_path")
    if '..' in file_path:
        raise Exception("非法的文件路径：包含路径穿越字符")

    data_storage_path = get_data_storage_path()
    full_path = os.path.abspath(os.path.join(data_storage_path, file_path))

    if not os.path.exists(full_path):
        raise Exception(f"文件不存在: {file_path}")
    if not os.path.isfile(full_path):
        raise Exception(f"指定路径不是文件: {file_path}")

    ext = os.path.splitext(full_path)[1].lower()

    if ext == '.db':
        conn = sqlite3.connect(full_path)
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            table_names = [row[0] for row in cursor.fetchall()]
        finally:
            conn.close()

        tables_data = {}
        for table_name in table_names:
            tables_data[table_name] = daoDataMiner.query_table_data(full_path, table_name)

        return {'success': True, 'data': {'tables': tables_data}}

    elif ext == '.json':
        with open(full_path, 'r', encoding='utf-8') as f:
            content = json.load(f)
        return {'success': True, 'data': content}

    else:
        raise Exception(f"不支持查看的文件类型: {ext}")


@process_log
def delete_processed_file(plan_id, file_path):
    """
    删除已处理文件

    删除指定文件及其对应的 .meta.json 文件，
    并尝试删除空父目录。

    Args:
        plan_id (int): 计划 ID
        file_path (str): 文件相对路径（相对于 DATA_SOURCE_PATH）

    Returns:
        dict: {"success": True, "message": "文件已删除"}
    """
    if plan_id is None:
        raise Exception("缺少必要参数: plan_id")
    if not file_path:
        raise Exception("缺少必要参数: file_path")
    if '..' in file_path:
        raise Exception("非法的文件路径：包含路径穿越字符")

    data_storage_path = get_data_storage_path()
    full_path = os.path.abspath(os.path.join(data_storage_path, file_path))

    if not os.path.exists(full_path):
        raise Exception(f"文件不存在: {file_path}")

    if not os.path.isfile(full_path):
        raise Exception(f"指定路径不是文件: {file_path}")

    # 删除主文件
    os.remove(full_path)

    # 删除同目录下的 .meta.json 文件
    file_dir = os.path.dirname(full_path)
    file_name_no_ext = os.path.splitext(os.path.basename(full_path))[0]
    meta_path = os.path.join(file_dir, f'{file_name_no_ext}.meta.json')
    if os.path.exists(meta_path):
        os.remove(meta_path)

    # 尝试删除空父目录
    try:
        os.rmdir(file_dir)
    except OSError:
        # 目录非空或删除失败，忽略
        pass

    return {'success': True, 'message': '文件已删除'}
