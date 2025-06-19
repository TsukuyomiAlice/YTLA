# encode = utf-8

import json
from core.cards.dao import daoCards
from core.frame.func.loggerConfig import process_log
from core.cards.process.processCardHandler import CardHandler


class SampleCardHandler(CardHandler):
    def __init__(self, card_sub_type):
        self.card_sub_type = card_sub_type

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update a card"""
        card_type = 'sample'
        try:
            card_sub_type = data.get('card_sub_type')
            default_name = ''
            if card_sub_type in ('sample1', 'sample2', 'sample3'):
                default_name = '新的示例卡片'

            if mode == 'add':
                data.update(
                    {'name': default_name, 'tags': '', 'description': '', 'icon_path': '', 'background_path': ''})
                daoCards.add_card(card_type, card_sub_type, data)

            if mode == 'update':
                from core.cards.dao.daoCards import Instance
                ins = Instance(data['name'], card_type, card_id=card_id)
                ins.card_sub_type = card_sub_type
                ins.tags = data['tags']
                ins.description = data['description']
                ins.icon_path = data['icon_path']
                ins.background_path = data['background_path']
                ins.detail_params = json.dumps(data, ensure_ascii=False)

                # 调用 daoCards 中的 update_card_detail 方法
                daoCards.update_card_detail(ins)
        except Exception:
            return False
        return True

    @process_log
    def parse_detail(self, detail):
        """To parse card detail data according to the card subtype"""
        if self.card_sub_type in ('sample1', 'sample2', 'sample3'):
            return {
                'sample_data_1': detail.get('sample_data_1'),
                'sample_data_2': detail.get('sample_data_2'),
                'sample_data_3': detail.get('sample_data_3'),
            }
        return {}

    @process_log
    def soft_update(self, card_id, action):
        """To soft update a card according to the card subtype and the action"""
        pass

    @staticmethod
    def get_default_name(self) -> str:
        return {
            'sample': '新的样例卡片',
        }.get(self.card_sub_type, '样例卡片')
