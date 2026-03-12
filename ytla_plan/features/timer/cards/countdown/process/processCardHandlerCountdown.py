# encode = utf-8

import json
from core.classic.cards.sideCard.dao import daoCards
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.cards.sideCard.process.processCardHandler import CardHandler
from features.timer.cards._type.func.funcTimer import calculate_end_time


class CountdownCardHandler(CardHandler):
    card_type = 'timer'
    card_sub_type = 'countdown'
    DEFAULT_NAME = '新的倒计时'

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update a countdown card"""
        card_type = 'timer'
        card_sub_type = 'countdown'
        try:
            start_time = data.get('start_time')
            end_time = data.get('end_time')
            countdown_mode = data.get('countdown_mode')

            if countdown_mode == 'single':
                if end_time == '':
                    countdown_single_length_value = data.get('countdown_single_length_value')
                    countdown_single_length_unit = data.get('countdown_single_length_unit')
                    end_time = calculate_end_time(start_time,
                                                  countdown_single_length_unit,
                                                  countdown_single_length_value)
                    data.update({'end_time': end_time})

            elif countdown_mode == 'repeat':
                if end_time == '':
                    countdown_repeat_period_value = data.get('countdown_repeat_period_value')
                    countdown_repeat_period_unit = data.get('countdown_repeat_period_unit')
                    end_time = calculate_end_time(start_time,
                                                  countdown_repeat_period_unit,
                                                  countdown_repeat_period_value)
                    data.update({'end_time': end_time})

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
        """To parse countdown card detail data"""
        return {
            'countdown_mode': detail.get('countdown_mode'),
            'countdown_single_mode': detail.get('countdown_single_mode'),
            'countdown_single_length_unit': detail.get('countdown_single_length_unit'),
            'countdown_single_length_value': detail.get('countdown_single_length_value'),
            'countdown_repeat_period_unit': detail.get('countdown_repeat_period_unit'),
            'countdown_repeat_period_value': detail.get('countdown_repeat_period_value'),
            'countdown_repeat_next_time': detail.get('countdown_repeat_next_time'),
            'start_time': detail.get('start_time'),
            'end_time': detail.get('end_time'),
        }

    @process_log
    def soft_update(self, card_id, action):
        """To soft update a countdown card"""
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

