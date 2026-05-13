# coding=utf-8
# 检索交易
from ..dao import daoTransactionHistory
from ...fund_info.dao import daoFundHistory, daoCurrencyFundList
from ...fund_info.script import scriptFundInfo, scriptFundHistory

"""
交易种类
1结尾 生成该交易
8结尾 结算该交易
9结尾 完成该交易
"""

# 买入
code_buy_in = "01"
# 买入生效
code_buy_in_confirm = "08"
# 买入成功
code_buy_in_success = "09"
# 卖出
code_sell_out = "11"
# 卖出生效
code_sell_out_confirm = "18"
# 卖出成功
code_sell_out_success = "19"
# 份额变动
code_share_change = "21"
# 份额变动确认
code_share_change_confirm = "28"
# 份额变动成功
code_share_change_success = "29"
# 分红-份额
code_profit_share = "31"
# 分红-份额确认
code_profit_share_confirm = "38"
# 分红-份额成功
code_profit_share_success = "39"
# 分红-现金
code_profit_fund = "41"
# 分红-现金确认
code_profit_fund_confirm = "48"
# 分红-现金成功
code_profit_fund_success = "49"


"""
获取交易记录
"""


def get_single(code):
    transaction_id = daoTransactionHistory.transaction_history_get_id(code)[0][0]
    return transaction_id


def get_unconfirmed(code):
    transaction_id_list = daoTransactionHistory.transaction_history_get_id_all(code)
    return transaction_id_list


def get_all(code):
    transactions = daoTransactionHistory.transaction_history_select(code)
    return transactions


def get_single_from_transaction_id(transaction_id):
    transaction = daoTransactionHistory.transaction_history_select_id(transaction_id)
    return transaction


"""
输入交易记录
"""


# 插入一条完整的交易记录
def log_on(code, transaction_date, transaction_type, amount, share, price, transaction_fee):
    amount = round(float(amount), 2)
    share = round(float(share), 4)
    price = round(float(price), 4)
    # unknown price:
    if price == 0 and transaction_type in ('01', '08', '09', '11', '18', '19'):
        share_price = daoFundHistory.fund_history_get_latest_price(code, transaction_date)
        if share_price == 0:
            scriptFundHistory.get_history(code)
            share_price = daoFundHistory.fund_history_get_latest_price(code, transaction_date)
        ratio = scriptFundInfo.get_ratio(code)
        price = round(share_price * ratio, 4)
    # unknown share:
    if share == 0 and transaction_type in ('01', '11'):
        accuracy = scriptFundInfo.get_share_accuracy(code)
        if price > 0:
            share = round(float(amount / price), int(accuracy))
    # unknown amount:
    if amount == 0 and transaction_type in ('01', '11'):
        amount = round(float(share * price), 2)
    transaction_fee = round(float(transaction_fee), 2)
    fund_name = scriptFundInfo.get_name(code)

    if daoCurrencyFundList.check_if_currency_fund(code):
        price = 1

    # 执行插入
    daoTransactionHistory.transaction_history_new_full_insert(code, transaction_date, transaction_type, amount, share,
                                                              price, transaction_fee, fund_name)
    transaction_id = daoTransactionHistory.transaction_history_get_id(code)[0][0]
    return transaction_id


# 插入一条只包含买入总金额的数据
def pre_buy_in(code, transaction_date, total_price):
    total_price = round(total_price, 2)
    # 执行插入
    daoTransactionHistory.transaction_history_new_insert(code, transaction_date, code_buy_in, total_price, 0)
    transaction_id = daoTransactionHistory.transaction_history_get_id(code)[0][0]
    return transaction_id


# 插入一条只包含卖出总份额的记录
def pre_sell_out(code, transaction_date, share):
    share = round(share, 4)
    # 执行插入
    daoTransactionHistory.transaction_history_new_insert(code, transaction_date, code_sell_out, 0, share)
    transaction_id = daoTransactionHistory.transaction_history_get_id(code)[0][0]
    return transaction_id


# 插入一条份额变动记录
def pre_share_change(code, transaction_date, share):
    share = round(share, 4)
    # 执行插入
    daoTransactionHistory.transaction_history_new_insert(code, transaction_date, code_share_change, 0, share)
    transaction_id = daoTransactionHistory.transaction_history_get_id(code)[0][0]
    return transaction_id


# 关于分红的处理比较复杂，先生成一条空记录，然后再更新所有字段会比较好
# 可能会知道总分红金额，所以留下金额字段可输入，不知道就输入0就可以了
def pre_profit(code, transaction_date, total_price):
    total_price = round(total_price, 2)
    # 执行插入
    daoTransactionHistory.transaction_history_new_insert(code, transaction_date, code_profit_fund, total_price, 0)
    transaction_id = daoTransactionHistory.transaction_history_get_id(code)[0][0]
    return transaction_id


def maintain_add_fund_name():
    code_list = daoTransactionHistory.select_plain_fund_name_list()
    for code in code_list:
        fund_name = scriptFundInfo.get_name(code[0])
        daoTransactionHistory.update_fund_name(code[0], fund_name)
