# encode = utf-8

from ..script import scriptFundInfo, scriptFundHistory


def execute(code):
    print('========== 自动分析开始 ==========')

    print('========== 获取基金名称 ==========')
    scriptFundInfo.get_name(code)
    print('========== 获取最新净值中 ==========')
    scriptFundHistory.get_history(code)
