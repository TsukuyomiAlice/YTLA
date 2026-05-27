# coding=utf-8

# 选择调用
import json
from ..dao import daoFundHistory
"""
数据处理部分
"""


def modify(res, code):
    data_string = res.content.decode("UTF-8").__str__()

    # 去壳
    str1 = data_string.split('(', 1)[1]
    data_string = str1[:-1]

    try:
        json_dict = json.loads(data_string)
        data = json_dict["Data"]
        dic = data.get("LSJZList")
        for i in range(0, len(dic)):
            d = dic[i].get("FSRQ")
            p1 = dic[i].get("DWJZ")
            p2 = dic[i].get("LJJZ")
            if not p1:
                p1 = p2
            if not p2:
                p2 = p1
            f = dic[i].get("JZZZL")
            if not f:
                f = 0
            sc = dic[i].get("FHFCZ")
            if not sc:
                sc = 0
            note = dic[i].get("FHSP")
            daoFundHistory.fund_history_insert(code, d, p1, p2, f, sc, note)
            print(code, d, p1, p2, f, sc, note)
        return len(dic)
    except Exception as e:
        print('error', data_string)


def modify_total_count(res):
    data_string = res.content.decode("UTF-8").__str__()

    # 去壳
    str1 = data_string.split('(', 1)[1]
    data_string = str1[:-1]

    json_dict = json.loads(data_string)
    total_count = json_dict["TotalCount"]
    # 返回数据
    return total_count
