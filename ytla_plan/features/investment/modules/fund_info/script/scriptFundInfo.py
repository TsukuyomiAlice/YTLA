# encode = utf-8

from ..dao import daoFundInfo
from ..api import requestFundSearch, requestFundSearchModify


# 获取基金名称
def get_name(code):
    res = daoFundInfo.fund_info_select(code)
    if res:
        name = res[0]
    else:
        res = requestFundSearch.request(code)
        name = requestFundSearchModify.modify(res)
        if name != "error":
            daoFundInfo.fund_info_insert(code, name)
    return name


# 更新基金名称
def update_name(code):
    res = daoFundInfo.fund_info_select(code)
    if res:
        res = requestFundSearch.request(code)
        name = requestFundSearchModify.modify(res)
        if name != "error":
            daoFundInfo.fund_info_update(code, name)
    else:
        return -1
    return f"{code}: {name}"


# 净值乘算比例查询
def get_ratio(code):
    res = daoFundInfo.fund_info_select(code)
    if res:
        ratio = res[0][3]
    else:
        name = get_name(code)
        if name != "error":
            ratio = get_ratio(code)
        else:
            ratio = 0
    return int(ratio)


# 份额精度查寻
def get_share_accuracy(code):
    res = daoFundInfo.fund_info_select(code)
    if res:
        accuracy = res[0][4]
    else:
        name = get_name(code)
        if name != "error":
            accuracy = get_share_accuracy(code)
        else:
            accuracy = 0
    return int(accuracy)
