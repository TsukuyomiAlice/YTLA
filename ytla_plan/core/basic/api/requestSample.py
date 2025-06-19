# coding=utf-8

# 必须调用
import requests
"""
如果需要更多的API，可在git上访问以下资源：
https://github.com/public-apis/public-apis
https://github.com/TonnyL/Awesome_APIs
"""

"""
请求部分
"""

url = ' '


def request():

    # 构建API
    headers = {

    }
    params = {

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
