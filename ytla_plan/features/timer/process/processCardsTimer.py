# encode = utf-8

import datetime
import json
from core.cards.dao import daoCards
from core.frame.func.loggerConfig import process_log
from core.cards.process.processCardHandler import CardHandler


def calculate_end_time(start_time, length_unit, length_value):
    start_time_dt = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    if length_unit == 'minute':
        end_time_dt = start_time_dt + datetime.timedelta(minutes=int(length_value))
    elif length_unit == 'hour':
        end_time_dt = start_time_dt + datetime.timedelta(hours=int(length_value))
    elif length_unit == 'day':
        end_time_dt = start_time_dt + datetime.timedelta(days=int(length_value))
    else:
        end_time_dt = start_time_dt
    return end_time_dt.strftime('%Y-%m-%d %H:%M:%S')


class TimerCardHandler(CardHandler):
    def __init__(self, card_sub_type):
        self.card_sub_type = card_sub_type

    @process_log
    def handle(self, data, mode, card_id=0):
        """To add or update a card"""
        card_type = 'timer'
        try:
            # card_sub_type处理
            card_sub_type = data.get('card_sub_type')
            default_name = ''
            start_time = data.get('start_time')
            end_time = data.get('end_time')

            if card_sub_type == 'alarm':
                default_name = '新的闹钟'

            if card_sub_type == 'countdown':
                default_name = '新的倒计时'
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

            if card_sub_type == 'count':
                default_name = '新的计时'
                if end_time == '':
                    count_single_length_value = data.get('count_single_length_value')
                    count_single_length_unit = data.get('count_single_length_unit')
                    end_time = calculate_end_time(start_time,
                                                  count_single_length_unit,
                                                  count_single_length_value)
                    data.update({'end_time': end_time})

            if mode == 'add':
                # daoCards格式
                data.update(
                    {'name': default_name, 'tags': '', 'description': '', 'icon_path': '', 'background_path': ''})
                daoCards.add_card(card_type, card_sub_type, data)

            if mode == 'update':
                # 创建 Instance 对象
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
        if self.card_sub_type == 'alarm':
            return {
                'alarm_time': detail.get('alarm_time'),
                'alarm_days': detail.get('alarm_days', []),
                'start_time': detail.get('start_time')
            }
        elif self.card_sub_type == 'countdown':
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
        elif self.card_sub_type == 'count':
            return {
                'count_mode': detail.get('count_mode'),
                'count_single_length_unit': detail.get('count_single_length_unit'),
                'count_single_length_value': detail.get('count_single_length_value'),
                'start_time': detail.get('start_time'),
                'end_time': detail.get('end_time'),
            }
        return {}

    @process_log
    def soft_update(self, card_id, action):
        """To soft update a card according to the card subtype and the action"""
        try:
            # 获取卡片原始数据
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

                # 更新 start_time 为当前时间
                new_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                details['backup_start_time'] = details['start_time']
                details['start_time'] = new_start_time
                # 更新数据库
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
                # 更新数据库
                card_instance.detail_params = json.dumps(details, ensure_ascii=False)
                daoCards.update_card_detail(card_instance)
                return {'success': True, 'new_start_time': new_start_time}

        except Exception as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def get_default_name(self):
        return {
            'alarm': '新的闹钟',
            'countdown': '新的倒计时',
            'count': '新的计时'
        }.get(self.card_sub_type, '计时卡片')
