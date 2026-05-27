# encode = utf-8

# from ..func import scheduleAndScript
from ytla_plan.features.investment.modules.fund_info.script import scriptFundHistory
from ytla_plan.features.investment.modules.fund_transaction.dao import daoTransactionHistory

"""
@scheduleAndScript.plan('workday', '21:45:00')
def auto_schedule():
    schedule()
"""


def schedule():
    fund_code_list = daoTransactionHistory.transaction_fund_code_get()
    for code in fund_code_list:
        scriptFundHistory.get_history(code['CODE'])
    # scheduleAndScript.show_current_time()


if __name__ == '__main__':
    schedule()
