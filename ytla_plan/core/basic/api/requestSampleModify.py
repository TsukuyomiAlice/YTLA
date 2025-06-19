# coding=utf-8

# 选择调用
import json

"""
数据处理部分
"""


def modify(res):
    data_string = res.content.decode("UTF-8").__str__()

    # 去壳
    str1 = data_string.split('(', 1)[1]
    data_string = str1[:-1]

    # 返回数据
    json_dict = json.loads(data_string)
    v = json_dict["Data"]
    if v:
        return v
    else:
        return "error"
