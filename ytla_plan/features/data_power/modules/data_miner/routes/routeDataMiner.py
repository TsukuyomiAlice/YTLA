# encode = utf-8

from flask import Blueprint, jsonify, request
from core.classic.frame._type.func.loggerConfig import router_log
from features.data_power.modules.data_miner.process import processDataMiner

data_miner_bp = Blueprint('data_miner', __name__)


@data_miner_bp.route('/data_miner/source_files', methods=['GET'])
@router_log
def list_source_files():
    """
    GET /data_miner/source_files?plan_id=X
    List raw source data files under the specified plan.
    """
    try:
        plan_id = request.args.get('plan_id', type=int)
        if plan_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: plan_id'}), 400

        files = processDataMiner.get_source_files(plan_id)
        return jsonify({'success': True, 'files': files})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@data_miner_bp.route('/data_miner/view', methods=['GET'])
@router_log
def view_processed_file():
    """
    GET /data_miner/view?plan_id=X&file_path=path/to/file
    View content of a processed file.
    """
    try:
        plan_id = request.args.get('plan_id', type=int)
        file_path = request.args.get('file_path')

        if plan_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: plan_id'}), 400
        if not file_path:
            return jsonify({'success': False, 'error': '缺少必要参数: file_path'}), 400

        result = processDataMiner.view_processed_file(plan_id, file_path)
        return jsonify(result)

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@data_miner_bp.route('/data_miner/delete', methods=['DELETE'])
@router_log
def delete_processed_file():
    """
    DELETE /data_miner/delete
    Delete a processed file.
    Request body: { plan_id: int, file_path: str }
    """
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': '请求体不能为空'}), 400

        plan_id = data.get('plan_id')
        file_path = data.get('file_path')

        if plan_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: plan_id'}), 400
        if not file_path:
            return jsonify({'success': False, 'error': '缺少必要参数: file_path'}), 400

        result = processDataMiner.delete_processed_file(plan_id, file_path)
        return jsonify(result)

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@data_miner_bp.route('/data_miner/process', methods=['POST'])
@router_log
def process_data_file():
    """
    POST /data_miner/process
    Analyze and process a specified data file.
    Request body: { plan_id: int, source_file_path: str, module_id: int }
    """
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': '请求体不能为空'}), 400

        plan_id = data.get('plan_id')
        source_file_path = data.get('source_file_path')
        module_id = data.get('module_id')

        if plan_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: plan_id'}), 400
        if not source_file_path:
            return jsonify({'success': False, 'error': '缺少必要参数: source_file_path'}), 400
        if module_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: module_id'}), 400

        result = processDataMiner.process_file(plan_id, source_file_path, module_id)
        return jsonify({'success': True, 'data': result})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@data_miner_bp.route('/data_miner/processed_files', methods=['GET'])
@router_log
def list_processed_files():
    """
    GET /data_miner/processed_files?plan_id=X&module_id=Y
    List processed data files under the specified plan.
    如果提供 module_id，只返回该模组的文件；否则返回所有 data_miner 模组的文件。
    """
    try:
        plan_id = request.args.get('plan_id', type=int)
        if plan_id is None:
            return jsonify({'success': False, 'error': '缺少必要参数: plan_id'}), 400

        module_id = request.args.get('module_id', type=int)
        files = processDataMiner.get_processed_files(plan_id, module_id)
        return jsonify({'success': True, 'files': files})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
