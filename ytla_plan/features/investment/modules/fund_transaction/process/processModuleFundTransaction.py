# coding=utf-8
from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.frame.router.instance.instanceProcessToRoutes import Response
from features.investment.modules.fund_transaction.process import processTransactionMatchGroup


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
