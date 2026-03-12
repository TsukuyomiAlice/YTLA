# encode = utf-8

import json
from core.classic.cards.sideCard.dao import daoCards
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.cards.sideCard.process.processCardHandler import CardHandler


class Sample1CardHandler(CardHandler):
    card_type = 'sample'
    card_sub_type = 'sample1'

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update a card"""
        card_type = 'sample'
        try:
            card_sub_type = data.get('card_sub_type')
            default_name = '新的示例卡片'

            if mode == 'add':
                data.update(
                    {'name': default_name, 'tags': '', 'description': '', 'icon_path': '', 'background_path': ''})
                daoCards.add_card(card_type, card_sub_type, data)

            if mode == 'update':
                from core.classic.cards.sideCard.dao.daoCards import Instance
                ins = Instance(data['name'], card_type, card_id=card_id)
                ins.card_sub_type = card_sub_type
                ins.tags = data['tags']
                ins.description = data['description']
                ins.icon_path = data['icon_path']
                ins.background_path = data['background_path']
                ins.detail_params = json.dumps(data, ensure_ascii=False)

                daoCards.update_card_detail(ins)
        except Exception:
            return False
        return True

    @process_log
    def parse_detail(self, detail):
        """To parse card detail data according to the card subtype"""
        return {
            'sample_data_1': detail.get('sample_data_1'),
            'sample_data_2': detail.get('sample_data_2'),
            'sample_data_3': detail.get('sample_data_3'),
        }

    @process_log
    def soft_update(self, card_id, action):
        """To soft update a card according to the card subtype and the action"""
        pass

    @staticmethod
    def get_default_name(self) -> str:
        return '新的样例卡片'
