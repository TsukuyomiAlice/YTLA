# encode = utf-8
import json

from flask import jsonify

from core.classic.plans.dao import daoPlans
from core.classic.frame.process import processGlobalPersistence
from core.classic.frame.func.loggerConfig import process_log


@process_log
def get_plans():
    raw_plans = daoPlans.get_plans()
    return [parse_plan_data(c) for c in raw_plans]


@process_log
def add_plan(plan_name: str):
    try:
        plan_instance = daoPlans.Instance(plan_name)
        plan_instance.detail_params = '{}'
        daoPlans.add_plan(plan_instance)
        plan_id = daoPlans.get_last_new_plan_id()
        return jsonify({'success': True, 'plan_id': plan_id})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


"""
update plan
plan db中出现的字段，且需要同时更新detail_params内的字段
"""


@process_log
def update_plan(plan_id, update_params: dict):
    try:
        plan_name = daoPlans.get_plan_name_by_plan_id(plan_id)
        if plan_name is None:
            return {'success': False, 'error': '计划不存在'}
        plan_instance = daoPlans.Instance(plan_name, plan_id=plan_id)
        plan_instance.set_instance(plan_instance.get_instance_by_pk())
        plan_dict = daoPlans.convert_to_dict(plan_instance)
        details = plan_dict['detail_params']

        for key, value in update_params.items():
            if key == 'name':
                plan_instance.name = value
                details['name'] = value
            if key == 'description':
                plan_instance.description = value
                details['description'] = value
            if key == 'tags':
                plan_instance.tags = value
                details['tags'] = value
            if key == 'tag':
                plan_instance.tags = plan_instance.tags.replace(
                    f'{value}, ' if f'{value}, ' in plan_instance.tags else value, '', 1)
                details['tags'] = plan_instance.tags
            if key == 'module_groups':
                plan_instance.module_groups = value
                details['module_groups'] = value
            if key == 'module_group':
                plan_instance.module_groups = plan_instance.module_groups.replace(
                    f'{value}, ' if f'{value}, ' in plan_instance.module_groups else value, '', 1)
                details['module_groups'] = plan_instance.module_groups
            if key == 'icon':
                plan_instance.icon_path = value
                details['icon_path'] = value
            if key == 'background':
                plan_instance.background_path = value
                details['background_path'] = value
        # 更新数据库
        plan_instance.detail_params = json.dumps(details, ensure_ascii=False)
        daoPlans.update_plan_detail(plan_instance)
        return {'success': True}

    except Exception as e:
        return {'success': False, 'error': str(e)}


@process_log
def soft_delete_plan(plan_id):
    daoPlans.soft_delete_plan(plan_id)
    processGlobalPersistence.delete_plan(f"plan_{str(plan_id)}")


@process_log
def deactivate_plan(plan_id):
    daoPlans.deactivate_plan(plan_id)


@process_log
def activate_plan(plan_id):
    daoPlans.activate_plan(plan_id)


def parse_plan_data(plan):
    """根据卡片子类型解析detail_params"""
    base_data = {
        'plan_id': plan.get('plan_id'),
        'name': plan.get('name'),
        'tags': plan.get('tags'),
        'module_groups': plan.get('module_groups'),
        'description': plan.get('description'),
        'icon_path': plan.get('icon_path'),
        'background_path': plan.get('background_path'),
        'detail_params': plan.get('detail_params'),
        'delete_flag': plan.get('delete_flag'),
        'active_flag': plan.get('active_flag', '0')
    }
    detail = plan.get('detail_params', {})
    detail_data = {}
    return base_data
