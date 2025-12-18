# encode = utf-8

import json

from core.classic.modules.dao import daoModules
from core.classic.frame.func.loggerConfig import process_log


@process_log
def get_modules(**kwargs):
    if 'module_type' in kwargs:
        module_type = kwargs['module_type']
        raw_modules = daoModules.get_modules(module_type=module_type)
    elif 'plan_id' in kwargs:
        plan_id = kwargs['plan_id']
        raw_modules = daoModules.get_modules(plan_id=plan_id)
    else:
        raw_modules = daoModules.get_modules()
    return [parse_module_data(c) for c in raw_modules]


@process_log
def add_module(module_data):
    try:
        module_data.update({'icon_path': '', 'background_path': ''})
        daoModules.add_module(module_data['module_type'], module_data['module_sub_type'], module_data)
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': str(e)}


"""
update module
只可用于更新module db中出现的字段，且需要同时更新detail_params内的字段
"""
@process_log
def update_module(module_id, update_params: dict):
    try:
        # 获取模组原始数据
        module_name = daoModules.get_module_name_by_module_id(module_id)
        if module_name is None:
            return {'success': False, 'error': '模组不存在'}
        module_instance = daoModules.Instance(module_name, '', module_id=module_id)
        module_instance.set_instance(module_instance.get_instance_by_pk())
        module_dict = daoModules.convert_to_dict(module_instance)
        details = module_dict['detail_params']

        for key, value in update_params.items():
            if key == 'belong_group_name':
                module_instance.belong_group_name = value
                details['belong_group_name'] = value
            if key == 'name':
                module_instance.name = value
                details['name'] = value
            if key == 'description':
                module_instance.description = value
                details['description'] = value
            if key == 'message':
                module_instance.message = value
                details['message'] = value
            if key == 'tags':
                module_instance.tags = value
                details['tags'] = value
            if key == 'tag':
                module_instance.tags = module_instance.tags.replace(f'{value}, ' if f'{value}, ' in module_instance.tags else value, '', 1)
                details['tags'] = module_instance.tags
            if key == 'icon':
                module_instance.icon_path = value
                details['icon_path'] = value
            if key =='background':
                module_instance.background_path = value
                details['background_path'] = value
        # 更新数据库
        module_instance.detail_params = json.dumps(details, ensure_ascii=False)
        daoModules.update_module_detail(module_instance)
        return {'success': True}

    except Exception as e:
        return {'success': False, 'error': str(e)}


@process_log
def soft_delete_module(module_id):
    daoModules.soft_delete_module(module_id)


@process_log
def deactivate_module(module_id):
    daoModules.deactivate_module(module_id)

@process_log
def activate_module(module_id):
    daoModules.activate_module(module_id)

"""
下方代码均涉及具体业务，注意划分
"""
@process_log
def module_router(data, mode, module_id=0):
    try:
        # 必要字段验证
        required_fields = ['module_sub_type']
        for field in required_fields:
            if field not in data:
                return {'success': False, 'error': f'缺少必要字段: {field}'}

        # 模组类型校验
        valid_subtypes = ['time', 'space', 'definition', 'relation', 'interaction',
                          'sample',
                          'timer',
                          'bible', 'meetings', 'userStory', 'prototype', 'vsm',
                          'dmd', 'whiteboard', 'ganttChart', 'backlog', 'kanban',
                          'dashboard', 'risk', 'burndownChart', 'property', 'features',
                          'rating','dictionary','assessment','vocabulary','readings','learning',
                          'sphere', 'matrix']
        if data['module_sub_type'] not in valid_subtypes:
            return {'success': False, 'error': f'无效模组类型: {data["module_sub_type"]}'}

        # 调用处理逻辑
        success = False
        if mode == 'add':
            success = add_module(data)
        return {'success': success}

    except Exception as e:
        return {'success': False, 'error': str(e)}


@process_log
def parse_module_data(module):
    """根据模组子类型解析detail_params"""
    base_data = {
        'module_id': module.get('module_id'),
        "belong_plan_id": module.get('belong_plan_id'),
        'belong_group_name': module.get('belong_group_name'),
        'name': module.get('name'),
        'module_type': module.get('module_type'),
        'module_sub_type': module.get('module_sub_type'),
        'tags': module.get('tags'),
        'description': module.get('description'),
        'message': module.get('message'),
        'icon_path': module.get('icon_path'),
        'background_path': module.get('background_path'),
        'delete_flag': module.get('delete_flag'),
        'active_flag': module.get('active_flag', '0')
    }
    module_type = module.get('module_type')
    module_sub_type = module.get('module_sub_type')
    detail = module.get('detail_params', {})
    detail_data = {}


    module_data = {**base_data, **detail_data}
    return module_data

"""
update / delete module belong group
只能用于从routePlans传来的特定请求！！！
"""
@process_log
def update_module_belong_group(plan_id, data: dict):
    try:
        old_module_group_name = ''
        new_module_group_name = ''
        for key, value in data.items():
            if key == 'old_module_group_name':
                old_module_group_name = value
            if key == 'new_module_group_name':
                new_module_group_name = value
        daoModules.update_module_belong_group(plan_id, old_module_group_name, new_module_group_name)
        return {'success': True}

    except Exception as e:
        return {'success': False, 'error': str(e)}


@process_log
def delete_module_belong_group(plan_id, data: dict):
    try:
        for key, value in data.items():
            if key == 'module_group':
                group_name = value
                daoModules.delete_module_belong_group(plan_id, group_name)
        return {'success': True}

    except Exception as e:
        return {'success': False, 'error': str(e)}


"""
soft update module
只可以用于更新存在于detail_params内的字段!!!
"""
@process_log
def soft_update_module(module_id, action):
    pass
