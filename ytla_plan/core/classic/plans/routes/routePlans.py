from flask import Blueprint, jsonify, request
from core.classic.frame.func.loggerConfig import router_log
from core.classic.modules.process import processModules
from core.classic.plans.process import processPlans
from core.classic.plans.dao import daoPlans

plans_bp = Blueprint('planCards', __name__)

@plans_bp.route('/get_plans')
@router_log
def get_plans():
    try:
        plans = processPlans.get_plans()
        return jsonify({'success': True, 'plans': plans})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'error': str(e)}), 500


@plans_bp.route('/add_plan', methods=['POST'])
@router_log
def add_plan():
    data = request.json
    plan_name = data.get('name')
    return processPlans.add_plan(plan_name)


@plans_bp.route('/update_plan/<int:plan_id>', methods=['POST'])
@router_log
def update_plan(plan_id):
    try:
        data = request.json

        # 调用处理逻辑
        success = processPlans.update_plan(plan_id, data)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@plans_bp.route('/update_plan/<int:plan_id>/tags', methods=['POST', 'DELETE'])
@router_log
def update_plan_tags(plan_id):
    try:
        data = request.json

        # 调用处理逻辑
        success = processPlans.update_plan(plan_id, data)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@plans_bp.route('/update_plan/<int:plan_id>/module_groups', methods=['POST', 'DELETE'])
@router_log
def update_plan_module_groups(plan_id):
    try:
        data = request.json
        # 调用处理逻辑
        success = processPlans.update_plan(plan_id, data)
        if request.method == 'POST':
            success = processModules.update_module_belong_group(plan_id, data)
        if request.method == 'DELETE':
            success = processModules.delete_module_belong_group(plan_id, data)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@plans_bp.route('/delete_plan/<int:plan_id>', methods=['POST'])
@router_log
def delete_plan(plan_id):
    try:
        # 检查卡片是否存在
        if not daoPlans.get_plan_name_by_plan_id(plan_id):
            return jsonify({'success': False, 'error': '卡片不存在'}), 404

        processPlans.soft_delete_plan(plan_id)
        # 验证删除操作
        if daoPlans.check_plan_delete_status(plan_id) == '1':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '删除操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@plans_bp.route('/deactivate_plan/<int:plan_id>', methods=['POST'])
@router_log
def deactivate_plan(plan_id):
    try:
        # 检查卡片是否存在
        if not daoPlans.get_plan_name_by_plan_id(plan_id):
            return jsonify({'success': False, 'error': '卡片不存在'}), 404

        processPlans.deactivate_plan(plan_id)
        # 验证弃用操作
        if daoPlans.check_plan_active_status(plan_id) == '0':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '弃用操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@plans_bp.route('/activate_plan/<int:plan_id>', methods=['POST'])
@router_log
def activate_plan(plan_id):
    try:
        # 检查卡片是否存在
        if not daoPlans.get_plan_name_by_plan_id(plan_id):
            return jsonify({'success': False, 'error': '卡片不存在'}), 404

        processPlans.activate_plan(plan_id)
        # 验证删除操作
        if daoPlans.check_plan_active_status(plan_id) == '1':
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': '启用操作未生效'}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500