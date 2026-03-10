# encode = utf-8

import json
from core.classic.cards.sideCard.dao import daoCards
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.cards.sideCard.process.processCardHandler import CardHandler


class WordleCardHandler(CardHandler):
    card_type = 'relax'
    card_sub_type = 'wordle'
    DEFAULT_NAME = '新的wordle'

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update a wordle card"""
        card_type = 'relax'
        card_sub_type = 'wordle'
        try:
            if mode == 'add':
                data.update(
                    {'name': self.DEFAULT_NAME, 'tags': '', 'description': '', 'icon_path': '', 'background_path': ''})
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
        """To parse wordle card detail data"""
        return {}

    @process_log
    def soft_update(self, card_id, action):
        """To soft update a wordle card"""
        pass
    
    @staticmethod
    def get_default_name(self) -> str:
        return '新的wordle'
