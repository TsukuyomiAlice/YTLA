# coding=utf-8

# 必须调用
import requests

"""
请求部分
"""

url = 'http://api.fund.eastmoney.com/pinzhong/TLPMPercent'


def request(code, r):
    """
    基金交易用获取基金历史排名百分位的方法
    :param code:
    :param r: 3y, 6y, 1n
    :return:
    """

    # 构建API
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
                      "Chrome/77.0.3865.120 Safari/537.36 ",
        "Host":
            "api.fund.eastmoney.com",
        "Referer":
            "http://fund.eastmoney.com/"
    }
    params = {
        "fundcode": code,
        "range": r,
        "callback": "jQuery183024328695780162812_1683951048400",
        "_": "1683951110848"
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
