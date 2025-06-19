from flask import Blueprint, jsonify, request
from core.frame.func.loggerConfig import router_log
from core.frame.process import processGlobalPersistence

globalPersistence_bp = Blueprint('globalPersistence', __name__)


@globalPersistence_bp.route('/get_global_persistence', methods=['GET'])
@router_log
def get_global_persistence():
    try:
        response = processGlobalPersistence.get_global_persistence()
        if response.success:
            return jsonify({'success': True, 'data': response.data})
        return jsonify({'success': False, 'error': response.error}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@globalPersistence_bp.route('/update_global_persistence', methods=['POST'])
@router_log
def update_global_persistence():
    try:
        data = request.json
        key = data.get('key')
        value = data.get('value')
        if not key or value is None:
            return jsonify({'success': False, 'error': 'Missing key or value'}), 400

        response = processGlobalPersistence.update_global_persistence(key, value)
        return jsonify({'success': response.success})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@globalPersistence_bp.route('/update_card_persistence', methods=['POST'])
@router_log
def update_card_persistence():
    try:
        data = request.json
        card_id = data.get('card_id')
        key = data.get('key')
        value = data.get('value')
        if value is None:
            return jsonify({'success': False, 'error': 'Missing value'}), 400

        response = processGlobalPersistence.update_card_global_persistence(key, value, card_id)
        return jsonify({'success': response.success})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@globalPersistence_bp.route('/get_plan_current_module_id/<plan_id>', methods=['GET'])
@router_log
def get_plan_current_module_id(plan_id):
    try:
        response = processGlobalPersistence.get_plan_current_module_id(plan_id)
        if response.success:
            return jsonify({'success': True, 'data': response.data})
        return jsonify({'success': False, 'error': response.error}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@globalPersistence_bp.route('/update_plan_current_module_id/<plan_id>', methods=['POST'])
@router_log
def update_plan_current_module_id(plan_id):
    try:
        module_id = request.json.get('module_id')
        if not module_id:
            return jsonify({'success': False, 'error': 'Missing module_id'}), 400

        response = processGlobalPersistence.update_plan_current_module_id(plan_id, module_id)
        return jsonify({'success': response.success})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
