# encode = utf-8

from ytla_ai.client import contentHandler
from ytla_plan.core.basic.func import timeFormat
from features.divination.modules.plum_yi.dataset import permanentCalendar, hexagram_data
from features.divination.modules.plum_yi.prompt import promptPlumYi


def trigram_generator_by_datetime(input_date=None):
    """Generates trigrams based on datetime (current or provided) for Plum Blossom Yi Jing divination.

    This function calculates the necessary components (year, month, day, hour orders) from a given or current datetime,
    converts them to lunar calendar values, and computes the upper trigram, lower trigram, and change line (动爻) using
    traditional Plum Blossom Yi Jing algorithms.

    Parameters:
        input_date (str, optional): A datetime string in the format "xxxx年xx月xx日 xx时xx分". If None, uses current time
            retrieved via timeFormat.get_current_time_cn(). Defaults to None.

    Returns:
        tuple: A tuple containing 9 elements in the following order:
            - current_time (str): The input or current datetime string used for calculation
            - lunar_date (str): Corresponding lunar calendar date string (e.g., "庚子年闰四月初五")
            - year_order (int): Ordinal value of the lunar year's earthly branch
            - month_order (int): Ordinal value of the lunar month's branch (adjusted for leap months)
            - day_order (int): Ordinal value of the lunar day's branch
            - hour_order (int): Ordinal value of the hour's earthly branch
            - upper_gram (int): Upper trigram number (0-7) calculated from (year_order + month_order + day_order) % 8
            - lower_gram (int): Lower trigram number (0-7) calculated from (year_order + month_order + day_order + hour_order) % 8
            - change_gram (int): Change line number (1-6) calculated from (year_order + month_order + day_order + hour_order) % 6
    """
    if input_date is None:
        current_time = timeFormat.get_current_time_cn()
    else:
        current_time = input_date
    day_part = current_time.split(' ')[0].replace('年0','年').replace('月0','月')
    lunar_date = permanentCalendar.dictionary.get(day_part)[0]

    lunar_year = lunar_date.split('年')[0][-1]
    year_order = hexagram_data.earthly_branches.get(lunar_year)
    lunar_month = lunar_date.split('年')[1].split('月')[0].replace('閏', '')
    month_order = hexagram_data.month_branch.get(lunar_month)
    lunar_day = lunar_date.split('月')[1].split('日')[0]
    day_order = hexagram_data.day_branch.get(lunar_day)

    hour_part = current_time.split(' ')[1].split('时')[0]
    hour_order = hexagram_data.earthly_branches.get(hexagram_data.hour_branch.get(hour_part))

    # generate the upper_gram, lower_gram and change_gram
    upper_gram = (year_order + month_order + day_order) % 8
    lower_gram = (year_order + month_order + day_order + hour_order) % 8
    change_gram = (year_order + month_order + day_order + hour_order) % 6
    if change_gram == 0:
        change_gram = 6

    return current_time, lunar_date, year_order, month_order, day_order, hour_order, upper_gram, lower_gram, change_gram


def hexagram_generator(upper_gram, lower_gram, change_gram):
    """
    Generates original, mutual, and change hexagrams based on input trigrams and change line.

    This function combines upper and lower trigrams to form the original hexagram,
    derives the mutual hexagram from specific lines of the original, and creates
    the change hexagram by modifying the specified line in the original hexagram.

    Parameters:
        upper_gram (int): Numeric identifier for the upper trigram
        lower_gram (int): Numeric identifier for the lower trigram
        change_gram (int): The line number (1-6) that changes in the hexagram

    Returns:
        tuple: A tuple containing three strings:
            - original_hexagram_name: Name of the original hexagram
            - mutual_hexagram_name: Name of the mutual hexagram
            - change_hexagram_name: Name of the changed hexagram
            - opposite_hexagram_name: Name of the opposite hexagram
            - inverted_hexagram_name: Name of the inverted hexagram
    """
    original_hexagram = tuple(hexagram_data.trigram_order.get(upper_gram) + hexagram_data.trigram_order.get(lower_gram))
    original_hexagram_name = hexagram_data.hexagram_table.get(original_hexagram)[0]

    mutual_hexagram = (
        original_hexagram[-5], original_hexagram[-4], original_hexagram[-3],
        original_hexagram[-4], original_hexagram[-3], original_hexagram[-2]
    )
    mutual_hexagram_name = hexagram_data.hexagram_table.get(mutual_hexagram)[0]

    change_hexagram = list(original_hexagram)
    change_hexagram[-change_gram] = int(not change_hexagram[-change_gram])
    change_hexagram = tuple(change_hexagram)
    change_hexagram_name = hexagram_data.hexagram_table.get(change_hexagram)[0]

    opposite_hexagram = (
        int(not original_hexagram[0]), int(not original_hexagram[1]), int(not original_hexagram[2]),
        int(not original_hexagram[3]), int(not original_hexagram[4]), int(not original_hexagram[5]),
    )
    opposite_hexagram_name = hexagram_data.hexagram_table.get(opposite_hexagram)[0]

    inverted_hexagram =  (
        original_hexagram[-1], original_hexagram[-2], original_hexagram[-3],
        original_hexagram[-4], original_hexagram[-5], original_hexagram[-6]
    )
    inverted_hexagram_name = hexagram_data.hexagram_table.get(inverted_hexagram)[0]

    # return
    return (original_hexagram_name, mutual_hexagram_name, change_hexagram_name, opposite_hexagram_name, inverted_hexagram_name,
            original_hexagram, mutual_hexagram, change_hexagram, opposite_hexagram, inverted_hexagram)


def hexagram_solver(input_date=None, debug=False, lan='cn'):
    """
    Solve the hexagram for the given date.
    :param input_date: string of the date to generate the hexagram.
        input_date: xxxx年xx月xx日 xx时xx分
    :param debug: boolean. set True to print the correct result for getting the info
    :param lan: str. 'cn' for chinese, 'en' for english
    :return:
    """
    date = trigram_generator_by_datetime(input_date)
    hexagram = hexagram_generator(date[6], date[7], date[8])

    language = '中文' if lan == 'cn' else '英文'

    prompt = promptPlumYi.agent_prompt(language, date, hexagram)

    if debug:
        print(f'''
====== processor 调试信息 ======
现在是{date[0]}，{date[1]}。
正确的年序数、月序数、日序数、时序数分别为{str(date[2])}、{str(date[3])}、{str(date[4])}、{str(date[5])}
正确的本卦、互卦、变卦、错卦、综卦的结果为{hexagram[0]}卦、{hexagram[1]}卦、{hexagram[2]}卦、{hexagram[3]}卦、{hexagram[4]}卦。
==============================
        ''')

    dummy_user_background = """
# 用户背景
## 用户今天没有提到特殊安排
## 用户没有特殊情况
"""

    messages = contentHandler.add_system_message([], dummy_user_background)

    print(f"""
====== 用户背景 ======
{dummy_user_background}
=====================    
    """)

    message = contentHandler.chat(messages, prompt)
    print(message[-1].get('content'))
