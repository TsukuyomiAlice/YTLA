# encode = utf-8

import math
import time
import datetime
from ytla_plan.core.classic.frame._type.func import timeFormat
from ytla_plan.features.investment.modules.fund_info.dao import daoFundHistory
from ytla_plan.features.investment.modules.fund_info.api import requestLsjz, requestLsjzModify


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
        count = timeFormat.diff_date(time.strftime("%Y-%m-%d", time.localtime()), last_date[0]['TRANSACTION_DATE'])
        last_date_string = (
                datetime.datetime.strptime(last_date[0]['TRANSACTION_DATE'], "%Y-%m-%d") + datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d")
    else:
        fst_trial = requestLsjz.request(code, 1, 1, "", "")
        count = requestLsjzModify.modify_total_count(fst_trial)
    today_string = time.strftime("%Y-%m-%d", time.localtime())
    if count:
        if count > 20:
            total_pages = math.ceil(count / 20)
            for page in range(1, total_pages + 1):
                trial = requestLsjz.request(code, page, 20, "", "")
                requestLsjzModify.modify(trial, code)
                if page < total_pages:
                    time.sleep(2)
            res = count
        else:
            trial = requestLsjz.request(code, 1, count, last_date_string, today_string)
            requestLsjzModify.modify(trial, code)
            res = count
    return res
