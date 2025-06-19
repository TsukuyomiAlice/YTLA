from flask import Blueprint, jsonify, request
from core.frame.func.loggerConfig import router_log
from core.modules.process import processModules
from core.modules.dao import daoModules

modules_bp = Blueprint('modules', __name__)

@modules_bp.route('/get_modules/<int:plan_id>')
@router_log
def get_modules(plan_id):
    try:
        modules = processModules.get_modules(plan_id=plan_id)
        return jsonify({'success': True, 'modules': modules})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': str(e)}), 500


@modules_bp.route('/add_module', methods=['POST'])
@router_log
def add_module():
    data = request.json
    return processModules.module_router(data, 'add')


@modules_bp.route('/update_module_detail/<int:module_id>', methods=['POST'])
@router_log
def update_module_detail(module_id):
    data = request.json
    return processModules.module_router(data, 'update', module_id=module_id)


@modules_bp.route('/module_action/<int:module_id>/<action>', methods=['POST'])
@router_log
def handle_module_action(module_id, action):
    try:
        result = processModules.soft_update_module(module_id, action)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@modules_bp.route('/update_module/<int:module_id>', methods=['POST'])
@router_log
def update_module(module_id):
    try:
        data = request.json

        # 调用处理逻辑
        success = processModules.update_module(module_id, data)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@modules_bp.route('/update_module/<int:module_id>/tags', methods=['POST', 'DELETE'])
@router_log
def update_module_tags(module_id):
    try:
        data = request.json

        # 调用处理逻辑
        success = processModules.update_module(module_id, data)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@modules_bp.route('/delete_module/<int:module_id>', methods=['POST'])
@router_log
def delete_module(module_id):
    try:
        # 检查模组是否存在
        if not daoModules.get_module_name_by_module_id(module_id):
            return jsonify({'success': False, 'error': '模组不存在'}), 404

        processModules.soft_delete_module(module_id)
        # 验证删除操作
        if daoModules.check_module_delete_status(module_id) == '1':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '删除操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@modules_bp.route('/deactivate_module/<int:module_id>', methods=['POST'])
@router_log
def deactivate_module(module_id):
    try:
        # 检查模组是否存在
        if not daoModules.get_module_name_by_module_id(module_id):
            return jsonify({'success': False, 'error': '模组不存在'}), 404

        processModules.deactivate_module(module_id)
        # 验证失效操作
        if daoModules.check_module_active_status(module_id) == '0':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '失效操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@modules_bp.route('/activate_module/<int:module_id>', methods=['POST'])
@router_log
def activate_module(module_id):
    try:
        # 检查模组是否存在
        if not daoModules.get_module_name_by_module_id(module_id):
            return jsonify({'success': False, 'error': '模组不存在'}), 404

        processModules.activate_module(module_id)
        # 验证激活操作
        if daoModules.check_module_active_status(module_id) == '1':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '激活操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500