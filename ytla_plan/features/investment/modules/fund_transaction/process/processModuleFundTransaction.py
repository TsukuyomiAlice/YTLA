# coding=utf-8
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.frame.router.instance.instanceProcessToRoutes import Response
from ..dao import daoTransactionHistory
from ..script import scriptTransactionHistory
from . import processTransactionMatchGroup


@process_log
def get_transaction_analysis(code):
    """获取基金交易分析数据

    Args:
        code: 基金代码

    Returns:
        Response: 包含基金交易分析数据
    """
    response = Response()
    try:
        brief, match_list_sorted, profit_list = processTransactionMatchGroup.analyze_transaction_match_group(code)
        continuous_history = processTransactionMatchGroup.analyze_continuous_history(code)

        # 构建返回数据
        data = {
            'brief': brief.to_dict(),
            'match_list': [],
            'profit_list': [],
            'continuous_history': {
                'buy_side': continuous_history[0],
                'sell_side': continuous_history[1],
                'fund_days': continuous_history[2],
                'buy_side_grades': continuous_history[3],
                'sell_side_grades': continuous_history[4],
                'latest_flows': continuous_history[5]
            }
        }

        # 转换match_list
        for transaction_list in match_list_sorted:
            match_group = []
            for ins in transaction_list:
                match_group.append(ins.to_dict())
            data['match_list'].append(match_group)

        # 转换profit_list
        for profit in profit_list:
            data['profit_list'].append(profit.to_dict())

        response.data = data
        response.success = True
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response


@process_log
def update_transaction(transaction_id, code, transaction_date, transaction_type, amount, share, price, transaction_fee):
    response = Response()
    try:
        daoTransactionHistory.transaction_history_full_update(
            transaction_id, code, transaction_date, transaction_type, 
            amount, share, price, transaction_fee
        )
        response.success = True
        response.msg = '更新成功'
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response


@process_log
def get_transactions(code):
    response = Response()
    try:
        transactions = daoTransactionHistory.transaction_history_select(code)
        # 转换数据格式
        data = []
        for t in transactions:
            data.append({
                'transaction_id': t['TRANSACTION_ID'],
                'code': t['CODE'],
                'transaction_date': t['TRANSACTION_DATE'],
                'transaction_type': t['TRANSACTION_TYPE'],
                'amount': t['TOTAL_PRICE'],
                'share': t['SHARE'],
                'price': t['UNIT_PRICE'],
                'transaction_fee': t['TRANSACTION_FEE'],
                'fund_name': t['FUND_NAME']
            })
        response.data = data
        response.success = True
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response


@process_log
def get_transaction(transaction_id):
    response = Response()
    try:
        transaction = daoTransactionHistory.transaction_history_select_id(transaction_id)
        if len(transaction) == 1:
            t = transaction[0]
            response.data = {
                'transaction_id': t['TRANSACTION_ID'],
                'code': t['CODE'],
                'transaction_date': t['TRANSACTION_DATE'],
                'transaction_type': t['TRANSACTION_TYPE'],
                'amount': t['TOTAL_PRICE'],
                'share': t['SHARE'],
                'price': t['UNIT_PRICE'],
                'transaction_fee': t['TRANSACTION_FEE'],
                'fund_name': t['FUND_NAME']
            }
        response.success = True
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response


@process_log
def add_transaction(code, transaction_date, transaction_type, amount, share, price, transaction_fee):
    response = Response()
    try:
        # 使用 scriptTransactionHistory 来处理交易记录的添加
        transaction_id = scriptTransactionHistory.log_on(
            code, transaction_date, transaction_type, amount, share, price, transaction_fee
        )
        response.data = {'transaction_id': transaction_id}
        response.success = True
        response.msg = '添加成功'
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response


@process_log
def delete_transaction(transaction_id):
    response = Response()
    try:
        daoTransactionHistory.transaction_history_delete(transaction_id)
        response.success = True
        response.msg = '删除成功'
    except Exception as e:
        response.success = False
        response.msg = str(e)
    return response
