# encode = utf-8

import json
from core.classic.modules.dao import daoModulePersistence
from core.classic.frame.func.loggerConfig import process_log
from core.classic.frame.instance.instanceProcessToRoutes import Response

vocabulary_book_sheet = {
    "record_id": 0,
    "vocabulary_book_name": "",
    "word_list": []
}

cefr_word_sheet = {
    "word": "",
    "cefr_level": ""
}

@process_log
def create_new_vocabulary_book(plan_id, module_id, user_name, word_list: list):

    instance = daoModulePersistence.Instance()
    instance.creator = user_name
    instance.updater = user_name
    instance.content = '{}'
    new_record_id = daoModulePersistence.insert_content(plan_id, module_id, instance)
    instance.record_id = new_record_id

    sheet = vocabulary_book_sheet.copy()
    sheet["record_id"] = new_record_id
    sheet["word_list"] = word_list
    instance.content = json.dumps(sheet)
    daoModulePersistence.update_content(plan_id, module_id, instance)
    response = Response()
    return response


@process_log
def get_vocabulary_book_by_creator(plan_id, module_id, user_name):

    records = daoModulePersistence.get_content_by_creator(plan_id, module_id, user_name)
    response = Response()
    response.data = {"records": records}
    return response


@process_log
def update_vocabulary_book_name(plan_id, module_id, record_id, book_name):
    instance = daoModulePersistence.Instance(record_id=record_id)
    instance.load_persistence(plan_id, module_id)

    content = json.loads(instance.content)
    content["vocabulary_book_name"] = book_name
    instance.content = json.dumps(content)
    daoModulePersistence.update_content(plan_id, module_id, instance)
    response = Response()
    return response


@process_log
def update_vocabulary_book_word_list(plan_id, module_id, record_id, word_list: list):
    instance = daoModulePersistence.Instance(record_id=record_id)
    instance.load_persistence(plan_id, module_id)

    content = json.loads(instance.content)
    content["word_list"] = word_list
    instance.content = json.dumps(content)
    daoModulePersistence.update_content(plan_id, module_id, instance)
    response = Response()
    return response
