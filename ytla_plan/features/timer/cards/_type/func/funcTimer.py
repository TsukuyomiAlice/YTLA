# encode = utf-8

import datetime


def calculate_end_time(start_time, length_unit, length_value):
    """
    Calculate end time based on start time, length unit and value
    """
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

