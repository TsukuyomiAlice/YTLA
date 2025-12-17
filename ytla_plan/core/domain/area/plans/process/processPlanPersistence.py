# encode=utf-8

from core.domain.area.plans.dao import daoPlanPersistence
from core.domain.area.frame.func.loggerConfig import process_log
from core.domain.area.frame.instance.instanceProcessToRoutes import Response

"""
" plan_persistence is considered as a collection about modules' persistence
" 
"""

module_persistence_keys = ["main_frame_page", "sub_frame_page", "main_frame_stored", "sub_frame_stored"]

blank_module_persistence = {
    "main_frame_page": 0,
    "sub_frame_page": 0,
    "main_frame_stored": {},
    "sub_frame_stored": {},
}

@process_log
def get_module_persistence(plan_id: int, module_id: int):
    stored_plan_persistence = daoPlanPersistence.load_persistence_by_module_id(plan_id, module_id)
    ret = blank_module_persistence.copy()
    for stored in stored_plan_persistence:
        stored_key = stored[1]
        stored_value = stored[2]
        if stored_key in module_persistence_keys:
            ret[stored_key] = stored_value
    response = Response()
    response.data = ret
    return response


@process_log
def update_module_persistence(plan_id: int, module_id: int, persistence: dict):
    response = Response()
    if not check_persistence(persistence):
        response.fail(400, "The persistence is illegal.")
        return response
    for key in persistence.keys():
        value = persistence[key]
        instance = daoPlanPersistence.Instance(module_id, key)
        instance.persistence_value = value
        daoPlanPersistence.save_persistence_by_module_id(plan_id, instance)
    return response


@process_log
def delete_module_persistence(plan_id: int, module_id: int):
    response = Response()
    daoPlanPersistence.delete_all_persistence_by_module_id(plan_id, module_id)
    return response


def check_persistence(persistence: dict):
    if len(persistence) != 4:
        return False
    count = 0
    for key in persistence.keys():
        if key in module_persistence_keys:
            count += 1
    if count != 4:
        return False
    return True