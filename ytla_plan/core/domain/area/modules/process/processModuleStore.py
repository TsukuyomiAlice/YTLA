# encode=utf-8

from core.domain.area.modules.dao import daoModulePersistence
from core.domain.area.frame.func.loggerConfig import process_log
from core.domain.area.frame.instance.instanceProcessToRoutes import Response

"""
" module store is considered as a collection about modules' detailed data.
" it is not mandatory to store the data in the daoModulePersistence.
" this process just provides a way to access the data to the default module data storage position.
" 
"""

@process_log
def get_module_data(plan_id: int, module_id: int, record_id: int = None):
    stored_module_data = daoModulePersistence.get_content(plan_id, module_id, record_id)
    response = Response()
    response.data = stored_module_data
    return response


@process_log
def insert_module_data(plan_id: int, module_id: int, creator: str="", content: any=None):
    response = Response()
    if content is None:
        content = "{}"
    else:
        content = str(content)
    instance = daoModulePersistence.Instance()
    instance.creator = creator
    instance.updater = creator
    instance.content = content
    record_id = daoModulePersistence.insert_content(plan_id, module_id, instance)
    response.data = {"record_id": record_id}
    return response


@process_log
def update_module_data(plan_id: int, module_id: int, record_id: int, updater: str="", content: any=None):
    response = Response()
    if content is None:
        content = "{}"
    else:
        content = str(content)
    instance = daoModulePersistence.Instance(record_id)
    instance.updater = updater
    instance.content = content
    daoModulePersistence.update_content(plan_id, module_id, instance)
    return response


@process_log
def delete_module_data(plan_id: int, module_id: int, record_id: int):
    response = Response()
    instance = daoModulePersistence.Instance()
    instance.record_id = record_id
    daoModulePersistence.delete_content(plan_id, module_id, instance)
    return response
