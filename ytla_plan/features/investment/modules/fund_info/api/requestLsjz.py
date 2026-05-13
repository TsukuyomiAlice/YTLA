# coding=utf-8

# 必须调用
import requests

"""
请求部分
"""

url = 'http://api.fund.eastmoney.com/f10/lsjz'


def request(code, page, size, start_date, end_date):

    # 构建API
    referer = 'http://fundf10.eastmoney.com/jjjz_{}.html'.format(code)
    headers = {
        "Referer": referer,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3865.120 Safari/537.36 "
    }
    params = {
        "callback": "jQuery183017965026301076215_1714297413500",
        "fundCode": code,
        "pageIndex": page,
        "pageSize": size,
        "startDate": start_date,
        "endDate": end_date,
        "_": "1714297413500"
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
