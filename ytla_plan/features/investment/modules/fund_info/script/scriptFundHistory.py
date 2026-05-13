# encode = utf-8

import time
import datetime
from ytla_plan.core.classic.frame._type.func import timeFormat
from ..dao import daoFundHistory
from ..api import requestLsjz, requestLsjzModify


def get_history(code):
    """
    获取基金历史记录
    @param code: 基金代码
    @return count: 更新记录数
    """
    last_date = daoFundHistory.fund_history_select_latest_date(code)
    last_date_string = "1989-01-01"
    res = 0
    if len(last_date):
        count = timeFormat.diff_date(time.strftime("%Y-%m-%d", time.localtime()), last_date[0][0])
        last_date_string = (
                datetime.datetime.strptime(last_date[0][0], "%Y-%m-%d") + datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d")
    else:
        fst_trial = requestLsjz.request(code, 1, 1, "", "")
        count = requestLsjzModify.modify_total_count(fst_trial)
    today_string = time.strftime("%Y-%m-%d", time.localtime())
    if count:
        trial = requestLsjz.request(code, 1, count, last_date_string, today_string)
        requestLsjzModify.modify(trial, code)
        res = count
    return res
