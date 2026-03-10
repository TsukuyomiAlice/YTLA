# encode = utf-8

import datetime
import json
from core.classic.cards.sideCard.dao import daoCards
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.cards.sideCard.process.processCardHandler import CardHandler
from features.timer.func.funcTimer import calculate_end_time


class CountCardHandler(CardHandler):
    card_type = 'timer'
    card_sub_type = 'count'
    DEFAULT_NAME = '新的计时'

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update a count card"""
        card_type = 'timer'
        card_sub_type = 'count'
        try:
            start_time = data.get('start_time')
            end_time = data.get('end_time')

            if end_time == '':
                count_single_length_value = data.get('count_single_length_value')
                count_single_length_unit = data.get('count_single_length_unit')
                end_time = calculate_end_time(start_time,
                                              count_single_length_unit,
                                              count_single_length_value)
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
        """To parse count card detail data"""
        return {
            'count_mode': detail.get('count_mode'),
            'count_single_length_unit': detail.get('count_single_length_unit'),
            'count_single_length_value': detail.get('count_single_length_value'),
            'start_time': detail.get('start_time'),
            'end_time': detail.get('end_time'),
        }

    @process_log
    def soft_update(self, card_id, action):
        """To soft update a count card"""
        try:
            card_name = daoCards.get_card_name_by_card_id(card_id)
            if not card_name:
                return {'success': False, 'error': '卡片不存在'}
            card_instance = daoCards.Instance(card_name, 'timer', card_id=card_id)
            db_record = card_instance.get_instance_by_pk()
            card_instance.set_instance(db_record)
            card_dict = daoCards.convert_to_dict(card_instance)
            details = card_dict['detail_params']

            if action == 'timer_count_reset':
                if card_instance.card_type != 'timer' or card_instance.card_sub_type != 'count':
                    return {'success': False, 'error': '卡片类型不符'}

                new_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                details['backup_start_time'] = details['start_time']
                details['start_time'] = new_start_time
                card_instance.detail_params = json.dumps(details, ensure_ascii=False)
                daoCards.update_card_detail(card_instance)
                return {'success': True, 'new_start_time': new_start_time}

            if action == 'timer_count_undo':
                if card_instance.card_type != 'timer' or card_instance.card_sub_type != 'count':
                    return {'success': False, 'error': '卡片类型不符'}

                if 'backup_start_time' not in details.keys():
                    return {'success': False, 'error': '未找到备份的开始时间'}

                if details['backup_start_time'] is None:
                    return {'success': False, 'error': '未找到备份的开始时间'}
                else:
                    details['start_time'] = details['backup_start_time']
                    new_start_time = details['start_time']
                card_instance.detail_params = json.dumps(details, ensure_ascii=False)
                daoCards.update_card_detail(card_instance)
                return {'success': True, 'new_start_time': new_start_time}

            return {'success': False, 'error': '不支持的操作'}
        except Exception as e:
            return {'success': False, 'error': str(e)}

