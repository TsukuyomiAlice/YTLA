# encode = utf-8

import json

from flask import jsonify

from core.domain.area.cards.dao import daoCards
from core.domain.area.frame.func.loggerConfig import process_log
from core.domain.area.cards.process.processCardHandlerFactory import CardHandlerFactory


def get_cards(**kwargs):
    if 'card_type' in kwargs:
        card_type = kwargs['card_type']
        raw_cards = daoCards.get_cards(card_type=card_type)
    else:
        raw_cards = daoCards.get_cards()
    return [parse_card_data(c) for c in raw_cards]


"""
update card
只可用于更新card db中出现的字段，且需要同时更新detail_params内的字段
"""


@process_log
def update_card(card_id, update_params: dict):
    try:
        # 获取卡片原始数据
        card_name = daoCards.get_card_name_by_card_id(card_id)
        if card_name is None:
            return {'success': False, 'error': '卡片不存在'}
        card_instance = daoCards.Instance(card_name, '', card_id=card_id)
        db_record = card_instance.get_instance_by_pk()
        card_instance.set_instance(db_record)
        card_dict = daoCards.convert_to_dict(card_instance)
        details = card_dict['detail_params']

        for key, value in update_params.items():
            if key == 'name':
                card_instance.name = value
                details['name'] = value
            if key == 'description':
                card_instance.description = value
                details['description'] = value
            if key == 'tags':
                card_instance.tags = value
                details['tags'] = value
            if key == 'tag':
                card_instance.tags = card_instance.tags.replace(
                    f'{value}, ' if f'{value}, ' in card_instance.tags else value, '', 1)
                details['tags'] = card_instance.tags
            if key == 'icon':
                card_instance.icon_path = value
                details['icon_path'] = value
            if key == 'background':
                card_instance.background_path = value
                details['background_path'] = value
        # 更新数据库
        card_instance.detail_params = json.dumps(details, ensure_ascii=False)
        daoCards.update_card_detail(card_instance)
        return {'success': True}

    except Exception as e:
        return {'success': False, 'error': str(e)}


@process_log
def soft_delete_card(card_id):
    daoCards.soft_delete_card(card_id)


@process_log
def deactivate_card(card_id):
    daoCards.deactivate_card(card_id)


"""
下方代码均涉及具体业务，注意划分
"""


@process_log
def card_router(data, mode, card_id=0):
    try:
        card_sub_type = data.get('card_sub_type')
        card_type = data.get('card_type', _infer_card_type(card_sub_type))

        handler = CardHandlerFactory.get_handler(card_type, card_sub_type)
        success = handler.handle(data, mode, card_id)
        return jsonify({'success': success})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


def parse_card_data(card):
    """根据卡片子类型解析detail_params"""
    base_data = {
        'card_id': card.get('card_id'),
        'name': card.get('name'),
        'card_type': card.get('card_type'),
        'card_sub_type': card.get('card_sub_type'),
        'tags': card.get('tags'),
        'description': card.get('description'),
        'icon_path': card.get('icon_path'),
        'background_path': card.get('background_path'),
        'delete_flag': card.get('delete_flag'),
        'active_flag': card.get('active_flag', '0')
    }
    card_type = card.get('card_type')
    card_sub_type = card.get('card_sub_type')
    detail = card.get('detail_params', {})

    try:
        handler = CardHandlerFactory.get_handler(card_type, card_sub_type)
        detail_data = handler.parse_detail(detail)
    except ValueError:
        detail_data = {}

    return {**base_data, **detail_data}


"""
soft update card
只可以用于更新存在于detail_params内的字段!!!
"""


@process_log
def soft_update_card(card_id, action):
    try:
        card_info = daoCards.get_card_type_info(card_id)
        if not card_info:
            return {'success': False, 'error': '卡片不存在'}

        card_type, card_sub_type = card_info
        handler = CardHandlerFactory.get_handler(card_type, card_sub_type)
        return handler.soft_update(card_id, action)

    except Exception as e:
        return {'success': False, 'error': str(e)}


def _infer_card_type(card_sub_type):
    type_mapping = {
        'alarm': 'timer',
        'countdown': 'timer',
        'count': 'timer',
        'sample1': 'sample',
        'sample2': 'sample',
        'sample3': 'sample',
        'wordle': 'relax'
    }
    return type_mapping.get(card_sub_type, 'unknown')
