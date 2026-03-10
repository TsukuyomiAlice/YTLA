# encode = utf-8

import json
from core.classic.cards.sideCard.dao import daoCards
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.cards.sideCard.process.processCardHandler import CardHandler


class AlarmCardHandler(CardHandler):
    card_type = 'timer'
    card_sub_type = 'alarm'
    DEFAULT_NAME = '新的闹钟'

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update an alarm card"""
        card_type = 'timer'
        card_sub_type = 'alarm'
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
        """To parse alarm card detail data"""
        return {
            'alarm_time': detail.get('alarm_time'),
            'alarm_days': detail.get('alarm_days', []),
            'start_time': detail.get('start_time')
        }

    @process_log
    def soft_update(self, card_id, action):
        """To soft update an alarm card"""
        try:
            card_name = daoCards.get_card_name_by_card_id(card_id)
            if not card_name:
                return {'success': False, 'error': '卡片不存在'}
            card_instance = daoCards.Instance(card_name, 'timer', card_id=card_id)
            db_record = card_instance.get_instance_by_pk()
            card_instance.set_instance(db_record)
            
            return {'success': False, 'error': '不支持的操作'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

