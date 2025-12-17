# encode=utf-8
import json

from core.domain.area.plans.dao import daoPlans
from core.domain.area.frame.dao import daoGlobalPersistence
from core.domain.area.frame.func.loggerConfig import process_log
from core.domain.area.frame.instance.instanceProcessToRoutes import Response

"""
" global_persistence_keys
" The consistence of the global persistence key should be like
" { the values in the global_persistence_keys[] }_{ the values in the {keys}[] }
" e.g.: layout_swapped, side_card_pinned, side_card_expanded, side_card_order, plan_card_pinned, plan_card_order
"""

global_persistence_keys = ['layout', 'cards', 'planCards']
layout_keys = ['swapped', 'sidebar_visible', 'user_language', 'has_plan']
side_card_keys = ['pinned', 'expanded', 'order']
plan_card_keys = ['pinned', 'order']
plan_current_module_id = 'current_module_id'

blank_global_persistence = {
    "layout": {
        "swapped": False,
        "sidebar_visible": False,
        "user_language": 'zh',
        "has_plan": False,
    },
    "cards": {
        "pinned": {},
        "expanded": {},
        "order": [],
    },
    "planCards": {
        "pinned": {},
        "order": [],
    },
    "plans": {
        "plan_system": {},
        "user": []
    }
}

"""
" return the full global persistence keys
"""


@process_log
def get_global_persistence():
    stored_global_persistence = daoGlobalPersistence.load_full_persistence()
    ret = blank_global_persistence.copy()
    for stored in stored_global_persistence:
        stored_key = stored['PERSISTENCE_KEY']
        stored_value = stored['PERSISTENCE_VALUE']
        global_persistence_key, sub_key = stored_key.split('_', 1)
        if global_persistence_key in global_persistence_keys:
            if sub_key in ret[global_persistence_key]:
                if isinstance(ret[global_persistence_key][sub_key], bool):
                    ret[global_persistence_key][sub_key] = True if stored_value == 'true' else False
                elif isinstance(ret[global_persistence_key][sub_key], list):
                    ret[global_persistence_key][sub_key] = json.loads(stored_value)
                else:
                    ret[global_persistence_key][sub_key] = stored_value
    response = Response()
    response.data = ret
    return response


@process_log
def update_global_persistence(key: str, value: any):
    persistence = daoGlobalPersistence.Instance(persistence_key=key)
    if isinstance(value, bool):
        persistence.persistence_value = 'true' if value else 'false'
    else:
        persistence.persistence_value = str(value)
    daoGlobalPersistence.save_persistence(persistence)
    response = Response()
    return response


"""
 for side card persistence
"""

@process_log
def update_card_global_persistence(persistence_key: str, value: bool | list, card_id: int = 0):
    persistence = daoGlobalPersistence.Instance(persistence_key=persistence_key)
    persistence.set_instance(persistence.load_persistence())
    if persistence_key in ['sideCard_pinned', 'sideCard_expanded', 'planCard_pinned']:
        data = json.loads('{}' if persistence.persistence_value == '' else str(persistence.persistence_value))
        data[str(card_id)] = value
        persistence.persistence_value = (str(data).replace('True', 'true')
                                         .replace('False', 'false')
                                         .replace("'", '"'))
    if persistence_key in ['sideCard_order', 'planCard_order']:
        persistence.persistence_value = str([] if not isinstance(value, list) else value)
    daoGlobalPersistence.save_persistence(persistence)
    response = Response()
    return response


"""
 for plan current module persistence
"""

@process_log
def get_plan_current_module_id(plan_id: str):
    response = plan_id_check(plan_id)
    if not response.success:
        return response

    persistence_key = f"{plan_id}_current_module_id"
    persistence = daoGlobalPersistence.Instance(persistence_key=persistence_key)
    persistence.set_instance(persistence.load_persistence())

    if persistence.delete_flag == '1':
        response.fail(400, "Plan has been deleted.")
        return response

    # TODO: vvv this is hard-coding. Should be refined after the system module modes are determined
    if persistence.persistence_value == '':
        if plan_id == 'plan_manage':
            persistence.persistence_value = 'welcome'
        else:
            persistence.persistence_value = 'planDashboard'
        daoGlobalPersistence.save_persistence(persistence)
    # TODO ^^^
    response.data = {"current_module_id": persistence.persistence_value}
    return response


@process_log
def update_plan_current_module_id(plan_id: str, module_id: str):
    response = plan_id_check(plan_id)
    if not response.success:
        return response
    persistence_key = f"{plan_id}_current_module_id"
    persistence = daoGlobalPersistence.Instance(persistence_key=persistence_key)
    persistence.persistence_value = module_id
    daoGlobalPersistence.save_persistence(persistence)
    response = Response()
    return response


@process_log
def delete_plan(plan_id: str):
    response = plan_id_check(plan_id)
    if not response.success:
        return response
    persistence_key = f"{plan_id}_current_module_id"
    persistence = daoGlobalPersistence.Instance(persistence_key=persistence_key)
    persistence.delete_flag = '1'
    daoGlobalPersistence.save_persistence(persistence)
    response = Response()
    return response


def plan_id_check(plan_id: str):
    """
    this check is used to check if the plan id is valid
    for definition: get_plan_current_module_id, update_plan_current_module_id, delete_plan
    :param plan_id:
    :return: response
    """
    response = Response()

    def is_integer(s):
        # check if the plan_id is valid
        try:
            int(s)
            return True
        except ValueError:
            return False

    id_part = plan_id.split('_')[1]
    # TODO: the hard-coding problem also appeared here
    if plan_id.split('_')[0] != 'plan' or (id_part != 'manage' and not is_integer(id_part)):
        response.fail(400, "Invalid plan id")
        return response
    plan_status = daoPlans.check_plan_delete_status(int(id_part))
    if plan_status == '1':
        response.fail(400, "Plan has been deleted or not exist.")
        return response
    return response