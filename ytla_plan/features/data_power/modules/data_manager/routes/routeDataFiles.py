# encode = utf-8

from flask import Blueprint, jsonify, request
from core.classic.frame._type.func.loggerConfig import router_log
from features.data_power.modules.data_manager.process import processDataFiles

data_manager_bp = Blueprint('data_manager', __name__)


@data_manager_bp.route('/data_manager/files', methods=['GET'])
@router_log
def list_data_files():
    """
    GET /data_manager/files?plan_id=X
    Get list of data files from data-related modules under the specified plan.
    """
    try:
        plan_id = request.args.get('plan_id', type=int)
        if plan_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: plan_id'}), 400

        files = processDataFiles.get_data_files(plan_id)
        return jsonify({'success': True, 'files': files})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@data_manager_bp.route('/data_manager/upload', methods=['POST'])
@router_log
def upload_data_file():
    """
    POST /data_manager/upload
    Upload a data file to the specified module.
    Form data: file (file), module_id (int)
    plan_id is derived from the module's belong_plan_id.
    """
    try:
        # Validate request contains file
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': '未包含文件'}), 400

        file = request.files['file']
        module_id = request.form.get('module_id', type=int)

        if module_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: module_id'}), 400

        result = processDataFiles.upload_data_file(module_id, file)

        if result.get('success'):
            return jsonify(result)
        else:
            return jsonify(result), 400

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@data_manager_bp.route('/data_manager/files/delete', methods=['POST'])
@router_log
def delete_data_file():
    """
    POST /data_manager/files/delete
    Delete an uploaded data file.
    JSON body: {"file_path": "plan_1/module_5/20260702120000/data.xlsx"}
    """
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'success': False, 'error': '请求体不能为空'}), 400

        file_path = data.get('file_path', '')

        result = processDataFiles.delete_data_file(file_path)

        if result.get('success'):
            return jsonify(result)
        else:
            return jsonify(result), 400

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
