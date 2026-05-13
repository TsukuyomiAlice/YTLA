# coding=utf-8
import os

from ytla_plan.core.classic.frame._type.func import utilConfigs
from ..dao import daoFundHistory, daoFundInfo, daoTransactionHistory

def _slash():
    s = '/'
    if os.name == 'posix':
        s = '/'
    if os.name == 'nt':
        s = '\\'
    return s

slash = _slash()

class Instance:

    def __init__(self, transaction_id: int, order_id: int):
        self.transaction_id = transaction_id
        self.code: str = ''
        self.fund_name: str = ''
        self.transaction_date: str = ''
        self.transaction_type: str = ''
        self.transaction_price: float = 0
        self.transaction_amount: float = 0
        self.transaction_share: float = 0
        self.transaction_profit: float = 0
        self.transaction_profit_pct: float = 0
        self.transaction_base_price: float = 0
        self.transaction_base_amount: float = 0
        self.transaction_base_share: float = 0
        self.transaction_profit_to_base: float = 0
        self.transaction_profit_pct_to_base: float = 0
        self.order_id = order_id
        self.memo: str = ''
        self.analyze_transaction_profit: float = 0
        self.transaction_profit_amount: float = 0
        self.transaction_profit_share: float = 0
        self.analyze_transaction_profit_pct: float = 0
        # analyze_transaction_type: BUY or SELL
        self.analyze_transaction_type: str = ''
        # analyze_transaction_stage: 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
        self.analyze_transaction_stage: str = ''
        self.analyze_group_profit_amount: float = 0
        self.analyze_group_profit_share: float = 0


class InstanceForProfit:

    def __init__(self, date: str):
        self.date = date
        self.profit_amount: float = 0
        self.profit_share: float = 0
        self.total_profit_amount: float = 0
        self.total_profit_share: float = 0


class InstanceForBrief:

    def __init__(self, code: str):
        self.code = code
        self.fund_name: str = ''
        self.last_transaction_date: str = ''
        self.latest_price: float = 0
        self.holding_amount: float = 0
        self.holding_share: float = 0
        self.holding_average_price: float = 0
        self.shown_amount: float = 0
        self.shown_share: float = 0
        self.profit_in_amount: float = 0
        self.profit_in_share: float = 0
        self.long_position_amount: float = 0
        self.long_position_share: float = 0
        self.short_position_share: float = 0
        self.short_position_amount: float = 0


def analyze_transaction_match_group(code):
    fund_info = daoFundInfo.Instance(code)
    fund_info.get_instance_by_pk()
    fund_name = fund_info.fund_name
    ratio = fund_info.ratio
    share_accuracy = fund_info.share_accuracy

    brief = InstanceForBrief(code)
    brief.fund_name = fund_name
    match_list = []
    profit_list = []

    # share change list
    share_change_ratio_list = daoFundHistory.fund_history_get_share_change_history_list(code)
    share_change_ratio_node = 0
    share_change_date = '9999-10-31'
    share_change_ratio = 1
    if len(share_change_ratio_list) > 0:
        share_change_date = share_change_ratio_list[share_change_ratio_node][0]
        share_change_ratio = share_change_ratio_list[share_change_ratio_node][1]

    # transaction_history_list
    transaction_history_list = daoTransactionHistory.instance_list_by_code(code)
    brief.last_transaction_date = transaction_history_list[-1].transaction_date

    transaction_history_node = 0
    current_transaction_date = '9999-10-31'
    if len(transaction_history_list) > 0:
        current_transaction_date = transaction_history_list[0].transaction_date

    # the main structure for processing match group
    while transaction_history_node < len(transaction_history_list):

        # pull the transactions on current transaction day
        current_transaction_day_list = []
        while (transaction_history_node < len(transaction_history_list) and
               transaction_history_list[transaction_history_node].transaction_date == current_transaction_date):
            current_transaction_day_list.append(transaction_history_list[transaction_history_node])
            transaction_history_node += 1

        # create the profit instance
        profit_list.append(InstanceForProfit(current_transaction_date))
        if len(profit_list) > 1:
            profit_list[-1].total_profit_amount = profit_list[-2].total_profit_amount
            profit_list[-1].total_profit_share = profit_list[-2].total_profit_share

        # initialize the current transaction day usage flags
        current_transaction_day_flag = [False for _ in range(len(current_transaction_day_list))]

        # solve the share change
        while current_transaction_date >= share_change_date:
            for transaction_list in match_list:
                ins = Instance(transaction_list[-1].transaction_id, len(transaction_list) + 1)

                ins.code = transaction_list[-1].code
                ins.fund_name = transaction_list[-1].fund_name
                ins.transaction_date = share_change_date
                ins.transaction_type = transaction_list[-1].transaction_type
                ins.transaction_amount = transaction_list[-1].transaction_amount
                ins.transaction_profit_pct = transaction_list[-1].transaction_profit_pct
                ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                ins.transaction_profit_pct_to_base = transaction_list[-1].transaction_profit_pct_to_base
                ins.memo = f'SHARE CHANGE (1 -> {str(share_change_ratio)})'
                ins.analyze_transaction_profit_pct = transaction_list[-1].analyze_transaction_profit_pct
                ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                ins.analyze_transaction_stage = transaction_list[-1].analyze_transaction_stage
                ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                ins.transaction_profit = transaction_list[-1].transaction_profit
                ins.transaction_profit_to_base = transaction_list[-1].transaction_profit_to_base
                if ((transaction_list[-1].analyze_transaction_type == 'SELL'
                     and transaction_list[-1].analyze_transaction_stage in ('1', '2', '3', '4', '5'))
                        or (transaction_list[-1].analyze_transaction_type == 'BUY'
                            and transaction_list[-1].analyze_transaction_stage in ('1', '2', '3', '4', '5'))):
                    ins.transaction_profit = round(ins.transaction_profit *
                                                   share_change_ratio, share_accuracy)
                    ins.transaction_profit_to_base = round(ins.transaction_profit_to_base *
                                                           share_change_ratio, share_accuracy)

                ins.analyze_transaction_profit = transaction_list[-1].analyze_transaction_profit
                ins.analyze_transaction_profit = round(ins.analyze_transaction_profit *
                                                       share_change_ratio, share_accuracy)
                new_share = round(transaction_list[-1].transaction_share * share_change_ratio, share_accuracy)
                new_price = round(abs((transaction_list[-1].transaction_amount / new_share)), 4)
                new_base_share = round(transaction_list[-1].transaction_base_share * share_change_ratio, share_accuracy)
                new_base_price = round(abs((transaction_list[-1].transaction_base_amount / new_base_share)), 4)
                ins.transaction_share = new_share
                ins.transaction_price = new_price
                ins.transaction_base_share = new_base_share
                ins.transaction_base_price = new_base_price
                transaction_list.append(ins)

            if len(share_change_ratio_list) > share_change_ratio_node + 1:
                share_change_ratio_node = share_change_ratio_node + 1
                share_change_date = share_change_ratio_list[share_change_ratio_node][0]
                share_change_ratio = share_change_ratio_list[share_change_ratio_node][1]
            else:
                share_change_date = '9999-10-31'

        # solve the profit in amount / share
        p = len(current_transaction_day_list)
        for i in range(p):
            transaction = current_transaction_day_list[i]

            ins = Instance(transaction.transaction_id, 0)
            ins = copy_transaction(ins, transaction)
            ins.transaction_base_price = ins.transaction_price
            ins.transaction_base_amount = ins.transaction_amount
            ins.transaction_base_share = ins.transaction_share

            if transaction.transaction_type in ('41', '48', '49'):
                brief.profit_in_amount = round((brief.profit_in_amount + transaction.amount), 2)
                profit_list[-1].profit_amount += transaction.amount
                profit_list[-1].total_profit_amount += transaction.amount
                current_transaction_day_flag[i] = True

            if transaction.transaction_type in ('31', '38', '39') and not current_transaction_day_flag[i]:
                brief.profit_in_share = round((brief.profit_in_share + transaction.share), share_accuracy)
                brief.holding_share = round((brief.holding_share + transaction.share), share_accuracy)
                brief.shown_share = round((brief.shown_share + transaction.share), share_accuracy)
                profit_list[-1].profit_share += transaction.share
                profit_list[-1].total_profit_share += transaction.share
                current_transaction_day_flag[i] = True

            if transaction.transaction_type in ('21', '28', '29') and not current_transaction_day_flag[i]:
                brief.holding_share = round((brief.holding_share + transaction.share), share_accuracy)
                brief.shown_share = round((brief.shown_share + transaction.share), share_accuracy)
                current_transaction_day_flag[i] = True

            if transaction.transaction_type in ('11', '18', '19') and not current_transaction_day_flag[i]:
                for transaction_list in match_list:
                    if (transaction_list[-1].transaction_share == transaction.share and
                            ((transaction_list[-1].analyze_transaction_type == 'BUY' and
                              transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                             (transaction_list[-1].analyze_transaction_type == 'SELL' and
                              transaction_list[-1].analyze_transaction_stage in ('2a', '4', '5'))) and
                            not current_transaction_day_flag[i]):
                        brief.holding_share = round((brief.holding_share - transaction.share), share_accuracy)
                        if transaction.transaction_type == '19':
                            brief.shown_share = round((brief.shown_share - transaction.share), share_accuracy)
                        ins.order_id = len(transaction_list) + 1

                        # analyze_transaction_type: BUY or SELL
                        ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                        # analyze_transaction_stage:
                        # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                        if ins.analyze_transaction_type == 'BUY':
                            ins.analyze_transaction_stage = '2a'
                        else:
                            if transaction_list[-1].analyze_transaction_stage == '2a':
                                transaction_list[-1].analyze_transaction_stage = '2'
                                ins.analyze_transaction_stage = '2'
                            else:
                                ins.analyze_transaction_stage = '3'

                        if ins.analyze_transaction_stage != '2':
                            ins.transaction_base_price = transaction_list[-1].transaction_base_price
                            ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                            ins.transaction_base_share = transaction_list[-1].transaction_base_share
                            if ins.transaction_price != 0:
                                ins.transaction_profit_amount = (
                                    round((ins.transaction_amount - ins.transaction_base_amount), 2))
                                ins.transaction_profit_share = (
                                    round((ins.transaction_base_share - ins.transaction_share), share_accuracy))
                                ins.analyze_transaction_profit = ins.transaction_profit_amount
                                ins.analyze_transaction_profit_pct = (
                                    round((ins.analyze_transaction_profit /
                                           transaction_list[-1].transaction_amount * 100), 2))
                                ins.analyze_group_profit_amount = (
                                    round((transaction_list[-1].analyze_group_profit_amount +
                                           ins.transaction_profit_amount), 2))
                                ins.analyze_group_profit_share = (
                                    round((transaction_list[-1].analyze_group_profit_share +
                                           ins.transaction_profit_share), 2))
                        else:
                            ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                            ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                        transaction_list.append(ins)
                        current_transaction_day_flag[i] = True

            if transaction.transaction_type in ('01', '08', '09') and not current_transaction_day_flag[i]:
                for transaction_list in match_list:
                    if (transaction_list[-1].transaction_amount == transaction.amount and
                            ((transaction_list[-1].analyze_transaction_type == 'SELL' and
                              transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                             (transaction_list[-1].analyze_transaction_type == 'BUY' and
                              transaction_list[-1].analyze_transaction_stage in ('2a', '4', '5'))) and
                            not current_transaction_day_flag[i]):
                        brief.holding_share = round((brief.holding_share + transaction.share), share_accuracy)
                        if transaction.transaction_type == '09':
                            brief.shown_share = round((brief.shown_share + transaction.share), share_accuracy)
                        ins.order_id = len(transaction_list) + 1

                        # analyze_transaction_type: BUY or SELL
                        ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                        # analyze_transaction_stage:
                        # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                        if ins.analyze_transaction_type == 'SELL':
                            ins.analyze_transaction_stage = '2a'
                        else:
                            if transaction_list[-1].analyze_transaction_stage == '2a':
                                transaction_list[-1].analyze_transaction_stage = '2'
                                ins.analyze_transaction_stage = '2'
                            else:
                                ins.analyze_transaction_stage = '3'

                        if ins.analyze_transaction_stage != '2':
                            ins.transaction_base_price = transaction_list[-1].transaction_base_price
                            ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                            ins.transaction_base_share = transaction_list[-1].transaction_base_share
                            if ins.transaction_price != 0:
                                ins.transaction_profit_share = (
                                    round((ins.transaction_share - ins.transaction_base_share), share_accuracy))
                                ins.transaction_profit_amount = (
                                    round((ins.transaction_base_amount - ins.transaction_amount), 2))
                                ins.analyze_transaction_profit = ins.transaction_profit_share
                                ins.analyze_transaction_profit_pct = (
                                    round((ins.analyze_transaction_profit /
                                           transaction_list[-1].transaction_share * 100), 2))
                                ins.analyze_group_profit_amount = (
                                    round((transaction_list[-1].analyze_group_profit_amount +
                                           ins.transaction_profit_amount), 2))
                                ins.analyze_group_profit_share = (
                                    round((transaction_list[-1].analyze_group_profit_share +
                                           ins.transaction_profit_share), 2))

                        else:
                            ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                            ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                        transaction_list.append(ins)
                        current_transaction_day_flag[i] = True

        for i in range(p):
            transaction = current_transaction_day_list[i]

            ins = Instance(transaction.transaction_id, 0)
            ins = copy_transaction(ins, transaction)
            ins.transaction_base_price = ins.transaction_price
            ins.transaction_base_amount = ins.transaction_amount
            ins.transaction_base_share = ins.transaction_share

            if transaction.transaction_type in ('11', '18', '19') and not current_transaction_day_flag[i]:
                for transaction_list in match_list:
                    if (transaction_list[-1].transaction_base_share == transaction.share and
                            ((transaction_list[-1].analyze_transaction_type == 'BUY' and
                              transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                             (transaction_list[-1].analyze_transaction_type == 'SELL' and
                              transaction_list[-1].analyze_transaction_stage == '2a')) and
                            not current_transaction_day_flag[i]):
                        brief.holding_share = round((brief.holding_share - transaction.share), share_accuracy)
                        if transaction.transaction_type == '19':
                            brief.shown_share = round((brief.shown_share - transaction.share), share_accuracy)
                        ins.order_id = len(transaction_list) + 1

                        # analyze_transaction_type: BUY or SELL
                        ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                        # analyze_transaction_stage:
                        # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                        if ins.analyze_transaction_type == 'BUY':
                            ins.analyze_transaction_stage = '2a'
                        else:
                            if transaction_list[-1].analyze_transaction_stage == '2a':
                                transaction_list[-1].analyze_transaction_stage = '2'
                                ins.analyze_transaction_stage = '2'
                            else:
                                ins.analyze_transaction_stage = '3'

                        if ins.analyze_transaction_stage != '2':
                            ins.transaction_base_price = transaction_list[-1].transaction_base_price
                            ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                            ins.transaction_base_share = transaction_list[-1].transaction_base_share
                            if ins.transaction_price != 0:
                                ins.transaction_profit_amount = (
                                    round((ins.transaction_amount - ins.transaction_base_amount), 2))
                                ins.transaction_profit_share = (
                                    round((ins.transaction_base_share - ins.transaction_share), share_accuracy))
                                ins.analyze_transaction_profit = ins.transaction_profit_amount
                                ins.analyze_transaction_profit_pct = (
                                    round((ins.analyze_transaction_profit /
                                           transaction_list[-1].transaction_base_amount * 100), 2))
                                ins.analyze_group_profit_amount = (
                                    round((transaction_list[-1].analyze_group_profit_amount +
                                           ins.transaction_profit_amount), 2))
                                ins.analyze_group_profit_share = (
                                    round((transaction_list[-1].analyze_group_profit_share +
                                           ins.transaction_profit_share), 2))

                        else:
                            ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                            ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                        transaction_list.append(ins)
                        current_transaction_day_flag[i] = True

            if transaction.transaction_type in ('01', '08', '09') and not current_transaction_day_flag[i]:
                for transaction_list in match_list:
                    if (transaction_list[-1].transaction_base_amount == transaction.amount and
                            ((transaction_list[-1].analyze_transaction_type == 'SELL' and
                              transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                             (transaction_list[-1].analyze_transaction_type == 'BUY' and
                              transaction_list[-1].analyze_transaction_stage == '2a')) and
                            not current_transaction_day_flag[i]):
                        brief.holding_share = round((brief.holding_share + transaction.share), share_accuracy)
                        if transaction.transaction_type == '09':
                            brief.shown_share = round((brief.shown_share + transaction.share), share_accuracy)
                        ins.order_id = len(transaction_list) + 1

                        # analyze_transaction_type: BUY or SELL
                        ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                        # analyze_transaction_stage:
                        # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                        if ins.analyze_transaction_type == 'SELL':
                            ins.analyze_transaction_stage = '2a'
                        else:
                            if transaction_list[-1].analyze_transaction_stage == '2a':
                                transaction_list[-1].analyze_transaction_stage = '2'
                                ins.analyze_transaction_stage = '2'
                            else:
                                ins.analyze_transaction_stage = '3'
                        if ins.analyze_transaction_stage != '2':
                            ins.transaction_base_price = transaction_list[-1].transaction_base_price
                            ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                            ins.transaction_base_share = transaction_list[-1].transaction_base_share
                            if ins.transaction_price != 0:
                                ins.transaction_profit_share = (
                                    round((ins.transaction_share - ins.transaction_base_share), share_accuracy))
                                ins.transaction_profit_amount = (
                                    round((ins.transaction_base_amount - ins.transaction_amount), 2))
                                ins.analyze_transaction_profit = ins.transaction_profit_share
                                ins.analyze_transaction_profit_pct = (
                                    round((ins.analyze_transaction_profit /
                                           transaction_list[-1].transaction_base_amount * 100), 2))
                                ins.analyze_group_profit_amount = (
                                    round((transaction_list[-1].analyze_group_profit_amount +
                                           ins.transaction_profit_amount), 2))
                                ins.analyze_group_profit_share = (
                                    round((transaction_list[-1].analyze_group_profit_share +
                                           ins.transaction_profit_share), 2))
                        else:
                            ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                            ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                        transaction_list.append(ins)
                        current_transaction_day_flag[i] = True

        for i in range(p):
            transaction = current_transaction_day_list[i]

            ins = Instance(transaction.transaction_id, 0)
            ins = copy_transaction(ins, transaction)
            ins.transaction_base_price = ins.transaction_price
            ins.transaction_base_amount = ins.transaction_amount
            ins.transaction_base_share = ins.transaction_share

            if transaction.transaction_type in ('11', '18', '19') and not current_transaction_day_flag[i]:
                for transaction_list in match_list:
                    if (transaction_list[-1].transaction_share == transaction.share and
                            ((transaction_list[-1].analyze_transaction_type == 'BUY' and
                              transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                             (transaction_list[-1].analyze_transaction_type == 'SELL' and
                              transaction_list[-1].analyze_transaction_stage in ('2a', '4', '5'))) and
                            not current_transaction_day_flag[i]):
                        brief.holding_share = round((brief.holding_share - transaction.share), share_accuracy)
                        if transaction.transaction_type == '19':
                            brief.shown_share = round((brief.shown_share - transaction.share), share_accuracy)
                        ins.order_id = len(transaction_list) + 1

                        # analyze_transaction_type: BUY or SELL
                        ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                        # analyze_transaction_stage:
                        # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                        if ins.analyze_transaction_type == 'BUY':
                            ins.analyze_transaction_stage = '2a'
                        else:
                            if transaction_list[-1].analyze_transaction_stage == '2a':
                                transaction_list[-1].analyze_transaction_stage = '2'
                                ins.analyze_transaction_stage = '2'
                            else:
                                ins.analyze_transaction_stage = '3'

                        if ins.analyze_transaction_stage != '2':
                            ins.transaction_base_price = transaction_list[-1].transaction_base_price
                            ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                            ins.transaction_base_share = transaction_list[-1].transaction_base_share
                            if ins.transaction_price != 0:
                                ins.transaction_profit_amount = (
                                    round((ins.transaction_amount - ins.transaction_base_amount), 2))
                                ins.transaction_profit_share = (
                                    round((ins.transaction_base_share - ins.transaction_share), share_accuracy))
                                ins.analyze_transaction_profit = ins.transaction_profit_amount
                                ins.analyze_transaction_profit_pct = (
                                    round((ins.analyze_transaction_profit /
                                           transaction_list[-1].transaction_amount * 100), 2))
                                ins.analyze_group_profit_amount = (
                                    round((transaction_list[-1].analyze_group_profit_amount +
                                           ins.transaction_profit_amount), 2))
                                ins.analyze_group_profit_share = (
                                    round((transaction_list[-1].analyze_group_profit_share +
                                           ins.transaction_profit_share), 2))
                        else:
                            ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                            ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                        transaction_list.append(ins)
                        current_transaction_day_flag[i] = True

                if not current_transaction_day_flag[i]:
                    for transaction_list in match_list:
                        if (transaction_list[-1].transaction_base_share == transaction.share and
                                ((transaction_list[-1].analyze_transaction_type == 'BUY' and
                                  transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                                 (transaction_list[-1].analyze_transaction_type == 'SELL' and
                                  transaction_list[-1].analyze_transaction_stage == '2a')) and
                                not current_transaction_day_flag[i]):
                            brief.holding_share = round((brief.holding_share - transaction.share), share_accuracy)
                            if transaction.transaction_type == '19':
                                brief.shown_share = round((brief.shown_share - transaction.share), share_accuracy)
                            ins.order_id = len(transaction_list) + 1

                            # analyze_transaction_type: BUY or SELL
                            ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                            # analyze_transaction_stage:
                            # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                            if ins.analyze_transaction_type == 'BUY':
                                ins.analyze_transaction_stage = '2a'
                            else:
                                if transaction_list[-1].analyze_transaction_stage == '2a':
                                    transaction_list[-1].analyze_transaction_stage = '2'
                                    ins.analyze_transaction_stage = '2'
                                else:
                                    ins.analyze_transaction_stage = '3'

                            if ins.analyze_transaction_stage != '2':
                                ins.transaction_base_price = transaction_list[-1].transaction_base_price
                                ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                                ins.transaction_base_share = transaction_list[-1].transaction_base_share
                                if ins.transaction_price != 0:
                                    ins.transaction_profit_amount = (
                                        round((ins.transaction_amount - ins.transaction_base_amount), 2))
                                    ins.transaction_profit_share = (
                                        round((ins.transaction_base_share - ins.transaction_share), share_accuracy))
                                    ins.analyze_transaction_profit = ins.transaction_profit_amount
                                    ins.analyze_transaction_profit_pct = (
                                        round((ins.analyze_transaction_profit /
                                               transaction_list[-1].transaction_base_amount * 100), 2))
                                    ins.analyze_group_profit_amount = (
                                        round((transaction_list[-1].analyze_group_profit_amount +
                                               ins.transaction_profit_amount), 2))
                                    ins.analyze_group_profit_share = (
                                        round((transaction_list[-1].analyze_group_profit_share +
                                               ins.transaction_profit_share), 2))

                            else:
                                ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                                ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                            transaction_list.append(ins)
                            current_transaction_day_flag[i] = True

                if not current_transaction_day_flag[i]:
                    brief.holding_share = round((brief.holding_share - transaction.share), share_accuracy)
                    if transaction.transaction_type == '19':
                        brief.shown_share = round((brief.shown_share - transaction.share), share_accuracy)
                    ins.order_id = 1

                    # analyze_transaction_type: BUY or SELL
                    ins.analyze_transaction_type = 'SELL'
                    # analyze_transaction_stage:
                    # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                    ins.analyze_transaction_stage = '1'
                    ins.analyze_group_profit_amount = 0
                    ins.analyze_group_profit_share = 0

                    new_transaction_list = [ins]
                    match_list.append(new_transaction_list)
                    current_transaction_day_flag[i] = True

            if transaction.transaction_type in ('01', '08', '09') and not current_transaction_day_flag[i]:
                for transaction_list in match_list:
                    if (transaction_list[-1].transaction_amount == transaction.amount and
                            ((transaction_list[-1].analyze_transaction_type == 'SELL' and
                              transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                             (transaction_list[-1].analyze_transaction_type == 'BUY' and
                              transaction_list[-1].analyze_transaction_stage in ('2a', '4', '5'))) and
                            not current_transaction_day_flag[i]):
                        brief.holding_share = round((brief.holding_share + transaction.share), share_accuracy)
                        if transaction.transaction_type == '09':
                            brief.shown_share = round((brief.shown_share + transaction.share), share_accuracy)
                        ins.order_id = len(transaction_list) + 1

                        # analyze_transaction_type: BUY or SELL
                        ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                        # analyze_transaction_stage:
                        # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                        if ins.analyze_transaction_type == 'SELL':
                            ins.analyze_transaction_stage = '2a'
                        else:
                            if transaction_list[-1].analyze_transaction_stage == '2a':
                                transaction_list[-1].analyze_transaction_stage = '2'
                                ins.analyze_transaction_stage = '2'
                            else:
                                ins.analyze_transaction_stage = '3'

                        if ins.analyze_transaction_stage != '2':
                            ins.transaction_base_price = transaction_list[-1].transaction_base_price
                            ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                            ins.transaction_base_share = transaction_list[-1].transaction_base_share
                            if ins.transaction_price != 0:
                                ins.transaction_profit_share = (
                                    round((ins.transaction_share - ins.transaction_base_share), share_accuracy))
                                ins.transaction_profit_amount = (
                                    round((ins.transaction_base_amount - ins.transaction_amount), 2))
                                ins.analyze_transaction_profit = ins.transaction_profit_share
                                ins.analyze_transaction_profit_pct = (
                                    round((ins.analyze_transaction_profit /
                                           transaction_list[-1].transaction_share * 100), 2))
                                ins.analyze_group_profit_amount = (
                                    round((transaction_list[-1].analyze_group_profit_amount +
                                           ins.transaction_profit_amount), 2))
                                ins.analyze_group_profit_share = (
                                    round((transaction_list[-1].analyze_group_profit_share +
                                           ins.transaction_profit_share), 2))

                        else:
                            ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                            ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                        transaction_list.append(ins)
                        current_transaction_day_flag[i] = True

                if not current_transaction_day_flag[i]:
                    for transaction_list in match_list:
                        if (transaction_list[-1].transaction_base_amount == transaction.amount and
                                ((transaction_list[-1].analyze_transaction_type == 'SELL' and
                                  transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                                 (transaction_list[-1].analyze_transaction_type == 'BUY' and
                                  transaction_list[-1].analyze_transaction_stage == '2a')) and
                                not current_transaction_day_flag[i]):
                            brief.holding_share = round((brief.holding_share + transaction.share), share_accuracy)
                            if transaction.transaction_type == '09':
                                brief.shown_share = round((brief.shown_share + transaction.share), share_accuracy)
                            ins.order_id = len(transaction_list) + 1

                            # analyze_transaction_type: BUY or SELL
                            ins.analyze_transaction_type = transaction_list[-1].analyze_transaction_type
                            # analyze_transaction_stage:
                            # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                            if ins.analyze_transaction_type == 'SELL':
                                ins.analyze_transaction_stage = '2a'
                            else:
                                if transaction_list[-1].analyze_transaction_stage == '2a':
                                    transaction_list[-1].analyze_transaction_stage = '2'
                                    ins.analyze_transaction_stage = '2'
                                else:
                                    ins.analyze_transaction_stage = '3'
                            if ins.analyze_transaction_stage != '2':
                                ins.transaction_base_price = transaction_list[-1].transaction_base_price
                                ins.transaction_base_amount = transaction_list[-1].transaction_base_amount
                                ins.transaction_base_share = transaction_list[-1].transaction_base_share
                                if ins.transaction_price != 0:
                                    ins.transaction_profit_share = (
                                        round((ins.transaction_share - ins.transaction_base_share), share_accuracy))
                                    ins.transaction_profit_amount = (
                                        round((ins.transaction_base_amount - ins.transaction_amount), 2))
                                    ins.analyze_transaction_profit = ins.transaction_profit_share
                                    ins.analyze_transaction_profit_pct = (
                                        round((ins.analyze_transaction_profit /
                                               transaction_list[-1].transaction_base_amount * 100), 2))
                                    ins.analyze_group_profit_amount = (
                                        round((transaction_list[-1].analyze_group_profit_amount +
                                               ins.transaction_profit_amount), 2))
                                    ins.analyze_group_profit_share = (
                                        round((transaction_list[-1].analyze_group_profit_share +
                                               ins.transaction_profit_share), 2))
                            else:
                                ins.analyze_group_profit_amount = transaction_list[-1].analyze_group_profit_amount
                                ins.analyze_group_profit_share = transaction_list[-1].analyze_group_profit_share

                            transaction_list.append(ins)
                            current_transaction_day_flag[i] = True

                if not current_transaction_day_flag[i]:
                    brief.holding_share = round((brief.holding_share + transaction.share), share_accuracy)
                    if transaction.transaction_type == '09':
                        brief.shown_share = round((brief.shown_share + transaction.share), share_accuracy)
                    ins.order_id = 1
                    # analyze_transaction_type: BUY or SELL
                    ins.analyze_transaction_type = 'BUY'
                    # analyze_transaction_stage:
                    # 1 - new, 2 - looping, 3 - open, 4 - closed in loss, 5 - closed in profit
                    ins.analyze_transaction_stage = '1'

                    new_transaction_list = [ins]
                    match_list.append(new_transaction_list)
                    current_transaction_day_flag[i] = True

            if transaction.transaction_type in ('01', '08', '09', '11', '18', '19'):
                profit_list[-1].profit_share += ins.transaction_profit_share
                profit_list[-1].total_profit_share += ins.analyze_transaction_profit
                profit_list[-1].profit_amount += ins.transaction_profit_amount
                profit_list[-1].total_profit_amount += ins.analyze_transaction_profit

        for transaction_list in match_list:
            if transaction_list[-1].analyze_transaction_stage == '2a':
                if (transaction_list[-1].analyze_transaction_profit >= 0 and
                        transaction_list[-1].analyze_group_profit_amount >= 0 and
                        transaction_list[-1].analyze_group_profit_share >= 0):
                    transaction_list[-1].analyze_transaction_stage = '5'
                else:
                    transaction_list[-1].analyze_transaction_stage = '4'

        # move the current transaction date to the next transaction date
        if transaction_history_node < len(transaction_history_list):
            current_transaction_date = transaction_history_list[transaction_history_node].transaction_date

    latest_price = round((daoFundHistory.fund_history_select_latest_price(code)[0][0] * ratio), 4)
    brief.latest_price = latest_price
    for transaction_list in match_list:
        if ((transaction_list[-1].analyze_transaction_type == 'BUY' and
             transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                (transaction_list[-1].analyze_transaction_type == 'SELL' and
                 transaction_list[-1].analyze_transaction_stage in ('4', '5'))):
            if transaction_list[-1].transaction_price != 0:
                transaction_list[-1].transaction_profit = (
                    round((transaction_list[-1].transaction_share * latest_price -
                           transaction_list[-1].transaction_amount), 2))
                transaction_list[-1].transaction_profit_pct = (
                    round((transaction_list[-1].transaction_profit / transaction_list[-1].transaction_amount * 100), 2))
                transaction_list[-1].transaction_profit_to_base = (
                    round((transaction_list[-1].transaction_base_share * latest_price -
                           transaction_list[-1].transaction_base_amount), 2))
                transaction_list[-1].transaction_profit_pct_to_base = (
                    round((transaction_list[-1].transaction_profit_to_base /
                           transaction_list[-1].transaction_base_amount * 100), 2))
        if ((transaction_list[-1].analyze_transaction_type == 'SELL' and
             transaction_list[-1].analyze_transaction_stage in ('1', '2', '3')) or
                (transaction_list[-1].analyze_transaction_type == 'BUY' and
                 transaction_list[-1].analyze_transaction_stage in ('4', '5'))):
            if transaction_list[-1].transaction_price != 0:
                transaction_list[-1].transaction_profit = (
                    round((transaction_list[-1].transaction_amount / latest_price -
                           transaction_list[-1].transaction_share), share_accuracy))
                transaction_list[-1].transaction_profit_pct = (
                    round((transaction_list[-1].transaction_profit / transaction_list[-1].transaction_share * 100), 2))

                transaction_list[-1].transaction_profit_to_base = (
                    round((transaction_list[-1].transaction_base_amount / latest_price -
                           transaction_list[-1].transaction_base_share), share_accuracy))
                transaction_list[-1].transaction_profit_pct_to_base = (
                    round((transaction_list[-1].transaction_profit_to_base /
                           transaction_list[-1].transaction_base_share * 100), 2))

    for transaction_list in match_list:
        brief.profit_in_share = round(
            (brief.profit_in_share + transaction_list[-1].analyze_group_profit_share), share_accuracy)
        brief.profit_in_amount = round((brief.profit_in_amount + transaction_list[-1].analyze_group_profit_amount), 2)
        for i in range(len(transaction_list)):
            if transaction_list[i].analyze_transaction_type == 'BUY':
                if i == 0:
                    brief.long_position_amount = (brief.long_position_amount +
                                                  transaction_list[i].transaction_base_amount)
                    brief.long_position_share = (brief.long_position_share +
                                                 transaction_list[i].transaction_base_share)
                elif i == len(transaction_list) - 1 and transaction_list[i].analyze_transaction_stage in ('4', '5'):
                    brief.long_position_amount = (brief.long_position_amount -
                                                  transaction_list[i - 1].transaction_base_amount)
                    brief.long_position_share = (brief.long_position_share -
                                                 transaction_list[i - 1].transaction_base_share)
                else:
                    brief.long_position_amount = (brief.long_position_amount -
                                                  transaction_list[i - 1].transaction_base_amount)
                    brief.long_position_share = (brief.long_position_share -
                                                 transaction_list[i - 1].transaction_base_share)
                    brief.long_position_amount = (brief.long_position_amount +
                                                  transaction_list[i].transaction_base_amount)
                    brief.long_position_share = (brief.long_position_share +
                                                 transaction_list[i].transaction_base_share)
            if transaction_list[i].analyze_transaction_type == 'SELL':
                if i == 0:
                    brief.short_position_amount = (brief.short_position_amount +
                                                   transaction_list[i].transaction_base_amount)
                    brief.short_position_share = (brief.short_position_share +
                                                  transaction_list[i].transaction_base_share)
                elif i == len(transaction_list) - 1 and transaction_list[i].analyze_transaction_stage in ('4', '5'):
                    brief.short_position_amount = (brief.short_position_amount -
                                                   transaction_list[i - 1].transaction_base_amount)
                    brief.short_position_share = (brief.short_position_share -
                                                  transaction_list[i - 1].transaction_base_share)
                else:
                    brief.short_position_amount = (brief.short_position_amount -
                                                   transaction_list[i - 1].transaction_base_amount)
                    brief.short_position_share = (brief.short_position_share -
                                                  transaction_list[i - 1].transaction_base_share)
                    brief.short_position_amount = (brief.short_position_amount +
                                                   transaction_list[i].transaction_base_amount)
                    brief.short_position_share = (brief.short_position_share +
                                                  transaction_list[i].transaction_base_share)

    brief.holding_amount = round((brief.holding_share * latest_price), 2)
    brief.shown_amount = round((brief.shown_share * latest_price), 2)

    # sort the transaction lists in profit percentage order
    list_in_latest = []
    list_in_transaction = []
    list_in_solved = []
    for i in range(len(match_list)):
        if match_list[i][-1].analyze_transaction_stage == '5':
            if match_list[i][-1].transaction_date == brief.last_transaction_date:
                list_in_latest.append(i)
            else:
                list_in_solved.append(i)
        else:
            if match_list[i][-1].transaction_date == brief.last_transaction_date:
                list_in_latest.append(i)
            else:
                list_in_transaction.append(i)
    for i in range(len(list_in_transaction)):
        for j in range(len(list_in_transaction) - 1):
            if (match_list[list_in_transaction[j]][-1].transaction_profit_pct <
                    match_list[list_in_transaction[j + 1]][-1].transaction_profit_pct):
                list_in_transaction[j], list_in_transaction[j + 1] = list_in_transaction[j + 1], list_in_transaction[j]
    for i in range(len(list_in_solved)):
        for j in range(len(list_in_solved) - 1):
            if (match_list[list_in_solved[j]][-1].transaction_date <
                    match_list[list_in_solved[j + 1]][-1].transaction_date):
                list_in_solved[j], list_in_solved[j + 1] = list_in_solved[j + 1], list_in_solved[j]
    match_list_sorted = []
    for i in list_in_latest:
        match_list_sorted.append(match_list[i])
    for i in list_in_transaction:
        match_list_sorted.append(match_list[i])
    for i in list_in_solved:
        match_list_sorted.append(match_list[i])

    return brief, match_list_sorted, profit_list


def copy_transaction(ins: Instance, transaction: daoTransactionHistory.Instance):
    ins.transaction_date = transaction.transaction_date
    ins.transaction_type = transaction.transaction_type
    ins.transaction_price = transaction.price
    ins.transaction_amount = transaction.amount
    ins.transaction_share = transaction.share
    return ins


def analyze_continuous_history(code):
    fund_history_list = daoFundHistory.get_fund_history_full_list(code)
    buy_side = [[] for _ in range(11)]
    sell_side = [[] for _ in range(11)]
    latest_lists = [[] for _ in range(7)]
    counter = 0
    ratio = 1
    flg = True
    for i in range(len(fund_history_list)):
        if fund_history_list[i][3] > 0 and not flg:
            if counter < 10:
                sell_side[counter].append(round((ratio * 100 - 100), 2))
            else:
                sell_side[10].append(round((ratio * 100 - 100), 2))
            flg = True
            if len(latest_lists) == 7:
                latest_lists.pop(0)
            latest_lists.append([fund_history_list[i - counter + 1][0], counter, round((ratio * 100 - 100), 2)])
            counter = 0
            ratio = 1
        if fund_history_list[i][3] < 0 and flg:
            if counter < 10:
                buy_side[counter].append(round((ratio * 100 - 100), 2))
            else:
                buy_side[10].append(round((ratio * 100 - 100), 2))
            if len(latest_lists) == 7:
                latest_lists.pop(0)
            latest_lists.append([fund_history_list[i - counter + 1][0], counter, round((ratio * 100 - 100), 2)])
            flg = False
            counter = 0
            ratio = 1
        counter += 1
        ratio = ratio * (1 + fund_history_list[i][3] / 100)

    if flg:
        if counter < 10:
            buy_side[counter].append(round((ratio * 100 - 100), 2))
        else:
            buy_side[10].append(round((ratio * 100 - 100), 2))
    else:
        if counter < 10:
            sell_side[counter].append(round((ratio * 100 - 100), 2))
        else:
            sell_side[10].append(round((ratio * 100 - 100), 2))
    latest_lists.pop(0)
    latest_lists.append([fund_history_list[-counter][0], counter, round((ratio * 100 - 100), 2)])
    buy_side_grades = [0 for _ in range(11)]
    sell_side_grades = [0 for _ in range(11)]
    for part in buy_side:
        for ratio in part:
            grade = int(ratio) // 3
            if grade < 10:
                buy_side_grades[grade] += 1
            else:
                buy_side_grades[10] += 1
    for part in sell_side:
        for ratio in part:
            grade = int(-ratio) // 3
            if grade < 10:
                sell_side_grades[grade] += 1
            else:
                sell_side_grades[10] += 1
    return buy_side, sell_side, len(fund_history_list), buy_side_grades, sell_side_grades, latest_lists


def analyze_report_output(code: str, order: int, brief: InstanceForBrief, match_list: list):
    fund_info = daoFundInfo.Instance(code)
    fund_info.get_instance_by_pk()
    fund_name = fund_info.fund_name.replace('/', '-')
    share_accuracy = fund_info.share_accuracy
    latest_price = brief.latest_price
    order_string = str(order).rjust(3, '0')
    file_name = f"{utilConfigs.daily_report_path}{slash}{order_string}_{code}_{fund_name}.txt"

    continuous_history = analyze_continuous_history(code)
    buy_side = continuous_history[0]
    sell_side = continuous_history[1]
    fund_days = continuous_history[2]
    buy_side_grades = continuous_history[3]
    sell_side_grades = continuous_history[4]
    latest_flows = continuous_history[5]

    print_rows = ['=' * 96]
    line = (' ' * 2
            + '基金代码\u3000' + ' ' * 2 + code
            + ' ' * 2
            + '基金名称\u3000' + ' ' * 2 + brief.fund_name)
    print_rows.append(line)
    line = (' ' * 2
            + '最新净值\u3000' + ' ' * 2 + str('%.4f' % brief.latest_price).rjust(6, ' ')
            + ' ' * 2
            + '基金运行天数\u3000\u3000\u3000\u3000' + ' ' * 2 + str(fund_days).rjust(6, ' '))
    print_rows.append(line)
    line = (' ' * 2
            + '当前实际持有份额\u3000\u3000' + ' ' * 2 + str(f'%.{str(share_accuracy)}f' % brief.holding_share).rjust(
                12, ' ')
            + ' ' * 2
            + '当前实际持有金额\u3000\u3000' + ' ' * 2 + str('%.2f' % brief.holding_amount).rjust(12, ' '))
    print_rows.append(line)
    line = (' ' * 2
            + '显示持有份额' + '\u3000' * 4 + ' ' * 2
            + str(f'%.{str(share_accuracy)}f' % brief.shown_share).rjust(12, ' ')
            + ' ' * 2
            + '显示持有金额' + '\u3000' * 4 + ' ' * 2 + str('%.2f' % brief.shown_amount).rjust(12, ' '))
    print_rows.append(line)
    line = (' ' * 2
            + '买仓标的金额' + '\u3000' * 4 + ' ' * 2
            + str('%.2f' % brief.long_position_amount).rjust(12, ' ')
            + ' ' * 2
            + '卖仓标的份额' + '\u3000' * 4 + ' ' * 2 + str(
                f'%.{str(share_accuracy)}f' % brief.short_position_share).rjust(12, ' '))
    print_rows.append(line)
    line = (' ' * 2
            + '买仓持有份额' + '\u3000' * 4 + ' ' * 2
            + str(f'%.{str(share_accuracy)}f' % brief.long_position_share).rjust(12, ' ')
            + ' ' * 2
            + '卖仓持有金额' + '\u3000' * 4 + ' ' * 2
            + str('%.2f' % brief.short_position_amount).rjust(12, ' '))
    print_rows.append(line)
    line = (' ' * 2
            + '获利金额' + '\u3000' * 6 + ' ' * 2 + str('%.2f' % brief.profit_in_amount).rjust(12, ' ')
            + ' ' * 2
            + '获利份额' + '\u3000' * 6 + ' ' * 2
            + str(f'%.{str(share_accuracy)}f' % brief.profit_in_share).rjust(12, ' '))
    print_rows.append(line)

    print_rows.append('=' * 96)
    print_rows.append('  开始日期\u3000' + str(latest_flows[0][0]).ljust(12) + str(latest_flows[1][0]).ljust(12)
                      + str(latest_flows[2][0]).ljust(12) + str(latest_flows[3][0]).ljust(12)
                      + str(latest_flows[4][0]).ljust(12) + str(latest_flows[5][0]).ljust(12)
                      + str(latest_flows[6][0]).ljust(12)
                      )
    print_rows.append('  持续天数\u3000' + str(latest_flows[0][1]).ljust(12) + str(latest_flows[1][1]).ljust(12)
                      + str(latest_flows[2][1]).ljust(12) + str(latest_flows[3][1]).ljust(12)
                      + str(latest_flows[4][1]).ljust(12) + str(latest_flows[5][1]).ljust(12)
                      + str(latest_flows[6][1]).ljust(12)
                      )
    print_rows.append('  累积幅度\u3000' + str(latest_flows[0][2]).ljust(12) + str(latest_flows[1][2]).ljust(12)
                      + str(latest_flows[2][2]).ljust(12) + str(latest_flows[3][2]).ljust(12)
                      + str(latest_flows[4][2]).ljust(12) + str(latest_flows[5][2]).ljust(12)
                      + str(latest_flows[6][2]).ljust(12)
                      )
    print_rows.append('-' * 96)
    # print_rows.append('  主副\u3000\u3000\u30001/0     1/1     1+1/0+1 2+1/1+1 3+2/2+1 5+3/3+2 5/5 ')
    print_rows.append('  累积天数\u30001       2       3       4       5       6       7       8       9       10+')
    print_rows.append('  买侧次数\u3000' + str(len(buy_side[1])).ljust(8) + str(len(buy_side[2])).ljust(8)
                      + str(len(buy_side[3])).ljust(8) + str(len(buy_side[4])).ljust(8)
                      + str(len(buy_side[5])).ljust(8) + str(len(buy_side[6])).ljust(8)
                      + str(len(buy_side[7])).ljust(8) + str(len(buy_side[8])).ljust(8)
                      + str(len(buy_side[9])).ljust(8) + str(len(buy_side[10])).ljust(8)
                      )
    print_rows.append('  卖侧次数\u3000' + str(len(sell_side[1])).ljust(8) + str(len(sell_side[2])).ljust(8)
                      + str(len(sell_side[3])).ljust(8) + str(len(sell_side[4])).ljust(8)
                      + str(len(sell_side[5])).ljust(8) + str(len(sell_side[6])).ljust(8)
                      + str(len(sell_side[7])).ljust(8) + str(len(sell_side[8])).ljust(8)
                      + str(len(sell_side[9])).ljust(8) + str(len(sell_side[10])).ljust(8)
                      )
    print_rows.append('-' * 96)
    print_rows.append('  累积幅度\u30000       3       6       9       12      15      18      21      24      27      30+')
    print_rows.append('  买侧次数\u3000' + str(buy_side_grades[0]).ljust(8) + str(buy_side_grades[1]).ljust(8)
                      + str(buy_side_grades[2]).ljust(8) + str(buy_side_grades[3]).ljust(8)
                      + str(buy_side_grades[4]).ljust(8) + str(buy_side_grades[5]).ljust(8)
                      + str(buy_side_grades[6]).ljust(8) + str(buy_side_grades[7]).ljust(8)
                      + str(buy_side_grades[8]).ljust(8) + str(buy_side_grades[9]).ljust(8)
                      + str(buy_side_grades[10]).ljust(8)
                      )
    print_rows.append('  卖侧次数\u3000' + str(sell_side_grades[0]).ljust(8) + str(sell_side_grades[1]).ljust(8)
                      + str(sell_side_grades[2]).ljust(8)+ str(sell_side_grades[3]).ljust(8)
                      + str(sell_side_grades[4]).ljust(8)+ str(sell_side_grades[5]).ljust(8)
                      + str(sell_side_grades[6]).ljust(8)+ str(sell_side_grades[7]).ljust(8)
                      + str(sell_side_grades[8]).ljust(8)+ str(sell_side_grades[9]).ljust(8)
                      + str(sell_side_grades[10]).ljust(8)
                      )
    print_rows.append('  说明：连续涨跌天数反应该基金单边行情的持续性，连续涨跌幅度反应该基金单边行情的波动程度。')
    print_rows.append('=' * 96)
    for transaction_list in match_list:

        # 8 * 12 ~ 5 * 12
        print_rows.append('\u3000序号\u3000'
                          '交易编号\u3000'
                          '交易日期\u3000'
                          '\u3000交易组别'
                          '/阶段\u3000\u3000\u3000\u3000'
                          '交易金额\u3000\u3000\u3000'
                          '交易价格\u3000\u3000\u3000'
                          '交易份额\u3000\u3000\u3000'
                          '浮盈\u3000\u3000\u3000浮盈(%)'
                          )
        for ins in transaction_list:
            line = (' ' * 2 + str(ins.order_id).ljust(4, ' ') + ' '
                    + str(ins.transaction_id).ljust(6, ' ') + '\u3000'
                    + ins.transaction_date + ' '
                    + ins.analyze_transaction_type.ljust(4, ' ') + ' '
                    + ins.analyze_transaction_stage + ' '
                    + '交易'
                    + str('%.2f' % ins.transaction_amount).rjust(12, ' ')
                    + str('%.4f' % ins.transaction_price).rjust(12, ' ')
                    + str(f'%.{str(share_accuracy)}f' % ins.transaction_share).rjust(12, ' ')
                    + str('%.4f' % ins.transaction_profit).rjust(12, ' ')
                    + str('%.2f' % ins.transaction_profit_pct).rjust(8, ' ') + '%'
                    )
            print_rows.append(line)
            if ins.transaction_id == transaction_list[-1].transaction_id:
                line = (' ' * 8
                        + '最新净值\u3000'
                        + str('%.4f' % latest_price).rjust(9, ' ') + ' ' * 4
                        )
            else:
                line = ' ' * 21 + '\u3000' * 5
            line = line + ('\u3000\u3000基准'
                           + str('%.2f' % ins.transaction_base_amount).rjust(12, ' ')
                           + str('%.4f' % ins.transaction_base_price).rjust(12, ' ')
                           + str(f'%.{str(share_accuracy)}f' % ins.transaction_base_share).rjust(12, ' ')
                           + str('%.4f' % ins.transaction_profit_to_base).rjust(12, ' ')
                           + str('%.2f' % ins.transaction_profit_pct_to_base).rjust(8, ' ') + '%'
                           )
            print_rows.append(line)
            line = ('  收益\u3000'
                    + str('%.4f' % ins.analyze_transaction_profit).rjust(12, ' ')
                    + ' 收益(%)\u3000'
                    + str('%.2f' % ins.analyze_transaction_profit_pct).rjust(6, ' ') + '%'
                    + ' 合计盈利金\u3000'
                    + str('%.2f' % ins.analyze_group_profit_amount).rjust(12, ' ')
                    + ' 合计盈利份\u3000'
                    + str(f'%.{str(share_accuracy)}f' % ins.analyze_group_profit_share).rjust(12, ' ')
                    )
            print_rows.append(line)
            if ins.memo != '':
                print_rows.append('  备注\u3000\u3000' + ins.memo)
        print_rows.append('-' * 96)

    with open(file_name, 'w') as f:
        for row in print_rows:
            f.write(row + '\n')
        f.close()


def execute(code):
    res = analyze_transaction_match_group(code)
    analyze_report_output(code, 0, res[0], res[1])
    return res[0]


def change_files_name(brief_list: list, check_list: list):
    for i in range(len(brief_list)):
        for j in range(len(brief_list) - 1):
            if brief_list[j].holding_amount < brief_list[j + 1].holding_amount:
                brief_list[j], brief_list[j + 1] = brief_list[j + 1], brief_list[j]
    t = 1
    for code in check_list:
        for brief in brief_list:
            if brief.code == code:
                fund_name = brief.fund_name.replace('/', '-')
                old_file_name = f"{utilConfigs.daily_report_path}{slash}000_{brief.code}_{fund_name}.txt"
                order = str(t).rjust(3, '0')
                new_file_name = f"{utilConfigs.daily_report_path}{slash}{order}_{brief.code}_{fund_name}.txt"
                os.rename(old_file_name, new_file_name)
                t += 1

    for brief in brief_list:
        if brief.code not in check_list:
            fund_name = brief.fund_name.replace('/', '-')
            old_file_name = f"{utilConfigs.daily_report_path}{slash}000_{brief.code}_{fund_name}.txt"
            order = str(t).rjust(3, '0')
            new_file_name = f"{utilConfigs.daily_report_path}{slash}{order}_{brief.code}_{fund_name}.txt"
            os.rename(old_file_name, new_file_name)
            t += 1


def brief_report(brief_list: list):
    file_name = f"{utilConfigs.daily_report_path}{slash}/brief.txt"
    print_rows = ['=' * 96]
    line = '  ' + '基金代码\u3000' + '基金名称\u3000'
    print_rows.append(line)
    line = ('  ' + '\u3000' * 5 + '最新净值\u3000' + '\u3000' * 5 + '当前实际持有金额\u3000\u3000' +
            '买仓标的金额' + '\u3000' * 4 + '买仓持有份额' + '\u3000' * 4 + '获利金额')
    print_rows.append(line)
    line = ('  ' + '\u3000' * 15 + '当前实际持有份额\u3000\u3000' + '卖仓标的份额' + '\u3000' * 4 +
            '卖仓标的金额' + '\u3000' * 4 + '获利份额')
    print_rows.append(line)
    print_rows.append('=' * 96)
    for brief in brief_list:
        fund_info = daoFundInfo.Instance(brief.code)
        fund_info.get_instance_by_pk()
        share_accuracy = fund_info.share_accuracy
        line = '  ' + brief.code + '  ' + brief.fund_name
        print_rows.append(line)
        line = (' ' * 10 + str('%.4f' % brief.latest_price).rjust(16, ' ') +
                str('%.2f' % brief.holding_amount).rjust(16, ' ') +
                str('%.2f' % brief.long_position_amount).rjust(16, ' ') +
                str(f'%.{str(share_accuracy)}f' % brief.long_position_share).rjust(16, ' ') +
                str('%.2f' % brief.profit_in_amount).rjust(16, ' '))
        print_rows.append(line)
        line = (' ' * 26 +
                str(f'%.{str(share_accuracy)}f' % brief.holding_share).rjust(16, ' ') +
                str(f'%.{str(share_accuracy)}f' % brief.short_position_share).rjust(16, ' ') +
                str('%.2f' % brief.short_position_amount).rjust(16, ' ') +
                str(f'%.{str(share_accuracy)}f' % brief.profit_in_share).rjust(16, ' '))
        print_rows.append(line)
        print_rows.append('-' * 96)

    with open(file_name, 'w') as f:
        for row in print_rows:
            f.write(row + '\n')
        f.close()
