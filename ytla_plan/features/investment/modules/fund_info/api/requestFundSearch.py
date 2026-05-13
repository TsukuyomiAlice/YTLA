# coding=utf-8

# 必须调用
import requests

"""
请求部分
"""

url = 'https://fundsuggest.eastmoney.com/FundSearch/api/FundSearchAPI.ashx'


def request(code):

    # 构建API
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
                      "Chrome/77.0.3865.120 Safari/537.36 "
    }
    params = {
        "callback": "jQuery18308931939742260158_1683822226136",
        "m": 10,
        "t": 700,
        "IsNeedBaseInfo": 0,
        "IsNeedZTInfo": 0,
        "key": code,
        "_": "1683822231167"
    }

    # 呼出请求
    res = requests.get(url, params=params, headers=headers)

    # 返回结果
    return res


"""
请求发送前数据预处理
"""


def pre_process():
    pass
