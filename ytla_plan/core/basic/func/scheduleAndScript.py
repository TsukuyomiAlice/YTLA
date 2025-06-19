# encode: utf-8
import datetime
import functools
import time
from concurrent import futures

executor = futures.ThreadPoolExecutor(1)


def timeout(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            future = executor.submit(func, *args, **kw)
            return future.result(timeout=seconds)
        return wrapper
    return decorator


def looper(seconds):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            while True:
                print('-' * 64)
                show_current_time()
                try:
                    future = executor.submit(func, *args, **kw)
                except Exception as e:
                    print(e)
                show_current_time()
                print('-' * 64)
                time.sleep(seconds)
        return wrapper
    return decorator


def show_current_time():
    time_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f'current time: {time_string}')


def plan(mode, time_str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            while True:
                await_time = calculate_await_seconds(mode, time_str)
                time.sleep(await_time + 3)
                print('-' * 64)
                show_current_time()
                print('-' * 64)
                try:
                    future = executor.submit(func, *args, **kw)
                except Exception as e:
                    print(e)
        return wrapper
    return decorator


def calculate_await_seconds(mode, time_str):
    if mode not in ('workday', 'weekend', 'everyday',
                    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        mode = 'everyday'
    switch_hour = int(time_str.split(':')[0])
    switch_minute = int(time_str.split(':')[1])
    switch_second = int(time_str.split(':')[2])

    datetime_now = datetime.datetime.now()
    datetime_target = datetime_now
    datetime_target = datetime_target.replace(hour=switch_hour)
    datetime_target = datetime_target.replace(minute=switch_minute)
    datetime_target = datetime_target.replace(second=switch_second)

    weekday_today = datetime_now.weekday()
    if mode == 'workday':
        if weekday_today > 4:
            day_delta = datetime.timedelta(days=(7 - weekday_today))
            datetime_target = datetime_target + day_delta

    if mode == 'weekend':
        if weekday_today < 5:
            day_delta = datetime.timedelta(days=(5 - weekday_today))
            datetime_target = datetime_target + day_delta

    if mode in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_target = week_list.index(mode)
        days = weekday_target - weekday_today
        if days < 0:
            days = days + 7
        day_delta = datetime.timedelta(days=days)
        datetime_target = datetime_target + day_delta
        if datetime_target < datetime_now:
            day_delta = datetime.timedelta(days=7)
            datetime_target = datetime_target + day_delta

    if datetime_target < datetime_now:
        day_delta = datetime.timedelta(days=1)
        datetime_target = datetime_target + day_delta

    delta = datetime_target - datetime_now
    seconds = int(delta.total_seconds())

    datetime_target_str = datetime_target.strftime('%Y-%m-%d %H:%M:%S')
    print(f'next time: {datetime_target_str} (after {str(seconds)} seconds)')

    return seconds
