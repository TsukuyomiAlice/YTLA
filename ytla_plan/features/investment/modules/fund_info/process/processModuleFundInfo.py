# coding=utf-8
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.frame.router.instance.instanceProcessToRoutes import Response
from ..dao import daoFundInfo, daoFundHistory


@process_log
def get_fund_info(code):
    """获取基金基本信息

    Args:
        code: 基金代码

    Returns:
        Response: 包含基金信息的响应
    """
    response = Response()
    try:
        db_res = daoFundInfo.fund_info_select(code)
        if len(db_res) == 1:
            fund_info = {
                'code': db_res[0]['CODE'],
                'name': db_res[0]['NAME'],
                'fund_type': db_res[0]['FUND_TYPE'],
                'ratio': db_res[0]['RATIO'],
                'share_accuracy': db_res[0]['SHARE_ACCURACY'],
                'fee_free_limit': db_res[0]['FEE_FREE_LIMIT'],
            }
            # 获取最新净值
            latest_price_res = daoFundHistory.fund_history_select_latest_price(code)
            if len(latest_price_res) > 0:
                fund_info['latest_price'] = latest_price_res[0]['CURRENT_PRICE']
            else:
                fund_info['latest_price'] = 0
            response.data = fund_info
            response.success = True
        else:
            response.success = False
            response.msg = '基金信息未找到'
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response


@process_log
def get_fund_history(code):
    """获取基金历史净值数据

    Args:
        code: 基金代码

    Returns:
        Response: 包含历史净值数据的响应
    """
    response = Response()
    try:
        db_res = daoFundHistory.get_fund_history_full_list(code)
        history_list = []
        for row in db_res:
            history_item = {
                'transaction_date': row['TRANSACTION_DATE'],
                'current_price': row['CURRENT_PRICE'],
                'origin_price': row['ORIGIN_PRICE'],
                'fluctuation': row['FLUCTUATION'],
                'share_change_ratio': row['SHARE_CHANGE_RATIO'],
                'share_change_note': row['SHARE_CHANGE_NOTE']
            }
            history_list.append(history_item)
        response.data = history_list
        response.success = True
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response


@process_log
def get_fund_latest_price(code):
    """获取基金最新净值

    Args:
        code: 基金代码

    Returns:
        Response: 包含最新净值的响应
    """
    response = Response()
    try:
        db_res = daoFundHistory.fund_history_select_latest_price(code)
        if len(db_res) > 0:
            response.data = {
                'latest_price': db_res[0]['CURRENT_PRICE'],
                'origin_price': db_res[0]['ORIGIN_PRICE']
            }
        else:
            response.data = {
                'latest_price': 0,
                'origin_price': 0
            }
        response.success = True
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response
