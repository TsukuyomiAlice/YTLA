# encode = utf-8

from ytla_fund.func import scheduleAndScript
from ytla_fund.script import scriptFundHistory
from ytla_fund.dao import daoTransactionHistory


@scheduleAndScript.plan('workday', '21:45:00')
def auto_schedule():
    schedule()


def schedule():
    fund_code_list = daoTransactionHistory.transaction_fund_code_get()
    for code in fund_code_list:
        scriptFundHistory.get_history(code[0])
    scheduleAndScript.show_current_time()


if __name__ == '__main__':
    auto_schedule()
