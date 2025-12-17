# encode = utf-8

from core.domain.area.frame.func.loggerConfig import process_log
from core.domain.area.cards.process.processCardHandler import CardHandler

class CardHandlerSample(CardHandler):
    def __init__(self, card_sub_type):
        self.card_sub_type = card_sub_type

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update a card"""
        return True

    @process_log
    def parse_detail(self, detail):
        """To parse card detail data according to the card subtype"""
        return {}

    @process_log
    def soft_update(self, card_id, action):
        """To soft update a card according to the card subtype and the action"""
        pass

    @staticmethod
    def get_default_name(self) -> str:
        return {
            'handler': '新的工厂',
        }.get(self.card_sub_type, '工厂卡片')
