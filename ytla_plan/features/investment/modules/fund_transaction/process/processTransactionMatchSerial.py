# coding=utf-8

from ...fund_info.dao import daoFundHistory, daoFundInfo, daoCurrencyFundList
from ...fund_info.script import scriptFundInfo
from ..dao import (
    daoTransactionHistory,
    daoAnalyzeTransactionBalance, daoAnalyzeTransactionOriginalSerial,
    daoAnalyzeTransactionMatchSerial, daoAnalyzeTransactionMatchSerialRemain,
    daoAnalyzeTransactionMatchQuantitative)
from ytla_plan.core.classic.frame._type.func import timeFormat


def analyze(plan_id, module_id, code):
    daoAnalyzeTransactionMatchSerial.clear_records(plan_id, module_id, code)

    share_accuracy = scriptFundInfo.get_share_accuracy(code)

    # share change list
    share_change_ratio_list = daoFundHistory.fund_history_get_share_change_history_list(code)
    share_change_ratio_node = 0
    share_change_date = '9999-10-31'
    share_change_ratio = 1
    if len(share_change_ratio_list) > 0:
        share_change_date = share_change_ratio_list[share_change_ratio_node][0]
        share_change_ratio = share_change_ratio_list[share_change_ratio_node][1]

    transaction_records = daoTransactionHistory.transaction_history_select_asc(plan_id, module_id, code)
    '''
    [0] TRANSACTION_ID
    [1] CODE
    [2] TRANSACTION_DATE
    [3] TRANSACTION_TYPE
    [4] TOTAL_PRICE
    [5] SHARE
    [6] UNIT_PRICE
    [7] TRANSACTION_FEE
    [8] FUND_NAME
    '''

    for transaction_record in transaction_records:

        transaction_id = transaction_record[0]
        name = transaction_record[8]
        transaction_date = transaction_record[2]
        transaction_type = transaction_record[3]
        transaction_price = round(transaction_record[6], 4)
        transaction_amount = round(transaction_record[4], 2)
        transaction_share = round(transaction_record[5], share_accuracy)

        latest_label = daoAnalyzeTransactionMatchSerial.get_latest_label(plan_id, module_id, code)
        label = latest_label + 1

        # share change
        while transaction_date >= share_change_date:
            transaction_share_change_list = (daoAnalyzeTransactionMatchSerial.
                                             select_active_transactions(plan_id, module_id, code, share_change_date))
            # [0] TRN_DATE, [1] TRN_TYPE [2] TRN_SHARE [3] TRN_AMOUNT
            # [4] TRN_REMAIN_SHARE [5] TRN_GAINED_AMOUNT
            # [6] LABEL [7] FIRST_TRN_ID [8] FIRST_TRN_DATE [9] TRN_ID [10] STATUS
            for transaction in transaction_share_change_list:
                new_share = round((transaction[4]) * share_change_ratio, share_accuracy)
                new_price = round(abs((transaction[3] / new_share)), 4)

                if transaction[10] == '00':
                    daoAnalyzeTransactionMatchSerial.update_status_by_label(plan_id, module_id, code, transaction[6], '10')
                if transaction[10] == '01':
                    daoAnalyzeTransactionMatchSerial.update_status_by_label(plan_id, module_id, code, transaction[6], '20')

                daoAnalyzeTransactionMatchSerial.insert_record(plan_id, module_id, code, name, share_change_date, transaction[1],
                                                               new_price, transaction[2], transaction[3],
                                                               new_share, transaction[5], label,
                                                               transaction[7], transaction[8], transaction[9],
                                                               transaction[10])
                label = label + 1

            if len(share_change_ratio_list) > share_change_ratio_node + 1:
                share_change_ratio_node = share_change_ratio_node + 1
                share_change_date = share_change_ratio_list[share_change_ratio_node][0]
                share_change_ratio = share_change_ratio_list[share_change_ratio_node][1]
            else:
                share_change_date = '9999-10-31'

        if transaction_type in ('01', '08', '09') and transaction_share != 0:

            match_transaction = daoAnalyzeTransactionMatchSerial.match_transaction_amount(plan_id, module_id, code, transaction_amount,
                                                                                          "'01'")
            if len(match_transaction) == 0:
                match_transaction = (daoAnalyzeTransactionMatchSerial.
                                     match_transaction_amount_remain(plan_id, module_id, code, transaction_amount, "'01'"))
            '''
            [0] LABEL
            [1] TRN_ID
            [2] FIRST_TRN_ID
            [3] FIRST_TRN_DATE
            [4] TRN_TYPE
            [5] TRN_SHARE / TRN_AMOUNT
            [6] TRN_REMAIN_SHARE
            [7] TRN_GAINED_AMOUNT
            '''
            if len(match_transaction) > 0:
                match_transaction_label = match_transaction[0][0]
                match_transaction_id = match_transaction[0][1]
                match_transaction_first_id = match_transaction[0][2]
                match_transaction_first_date = match_transaction[0][3]
                match_transaction_share = match_transaction[0][5]
                match_transaction_remain_share = match_transaction[0][6]
                match_transaction_gained_amount = match_transaction[0][7]

            else:
                match_transaction = daoAnalyzeTransactionMatchSerial.match_transaction_amount(plan_id, module_id, code, transaction_amount,
                                                                                              "'00', '10'")
                if len(match_transaction) == 0:
                    match_transaction = (daoAnalyzeTransactionMatchSerial.
                                         match_transaction_amount_remain(plan_id, module_id, code, transaction_amount, "'00', '10'"))

                if len(match_transaction) > 0:
                    match_transaction_label = match_transaction[0][0]
                    match_transaction_id = match_transaction[0][1]
                    match_transaction_first_id = match_transaction[0][2]
                    match_transaction_first_date = match_transaction[0][3]
                    match_transaction_share = match_transaction[0][5]
                    match_transaction_remain_share = match_transaction[0][6]
                    match_transaction_gained_amount = match_transaction[0][7]
                    current_transaction_type = (daoAnalyzeTransactionMatchSerial.
                                                check_transaction_type(plan_id, module_id, code, match_transaction_first_id))
                    if len(current_transaction_type) > 0:
                        if current_transaction_type[0][0] in ('AMOUNT_BUY', 'SHARE_BUY'):
                            match_transaction = []
                        else:
                            match_transaction_remain_share = current_transaction_type[0][1]
                            match_transaction_gained_amount = current_transaction_type[0][2]

                if len(match_transaction) == 0:
                    match_transaction_label = label
                    match_transaction_id = 0
                    match_transaction_first_id = 0
                    match_transaction_first_date = transaction_date
                    match_transaction_share = 0
                    match_transaction_remain_share = 0
                    match_transaction_gained_amount = 0

            transaction_remain_share = round((match_transaction_remain_share + transaction_share), share_accuracy)
            transaction_gained_amount = round((match_transaction_gained_amount - transaction_amount), 2)

            if transaction_share > match_transaction_share > 0:
                transaction_type_str = 'SHARE_BUY'
            else:
                transaction_type_str = 'AMOUNT_BUY'
            if transaction_type == '01':
                transaction_type_str = transaction_type_str + '*'

            if transaction_remain_share >= 0 and transaction_gained_amount >= 0:
                daoAnalyzeTransactionMatchSerial.update_status_by_label(plan_id, module_id, code, match_transaction_label, '20')
                daoAnalyzeTransactionMatchSerial.update_status_by_first_transaction_id(plan_id, module_id, code, match_transaction_first_id,
                                                                                       '90')
                status = '99'
            else:
                if match_transaction_first_id != match_transaction_id:
                    daoAnalyzeTransactionMatchSerial.update_status_by_label(plan_id, module_id, code, match_transaction_label, '20')
                    (daoAnalyzeTransactionMatchSerial.
                     update_status_by_first_transaction_id(plan_id, module_id, code, match_transaction_first_id, '10'))
                    status = '01'
                if match_transaction_first_id == match_transaction_id and match_transaction_id != 0:
                    (daoAnalyzeTransactionMatchSerial.
                     update_status_by_first_transaction_id(plan_id, module_id, code, match_transaction_first_id, '10'))
                    status = '01'
                if match_transaction_id == 0:
                    match_transaction_id = transaction_id
                    match_transaction_first_id = transaction_id
                    status = '00'
            daoAnalyzeTransactionMatchSerial.insert_record(plan_id, module_id, code, name, transaction_date, transaction_type_str,
                                                           transaction_price, transaction_share, transaction_amount,
                                                           transaction_remain_share, transaction_gained_amount,
                                                           label,
                                                           match_transaction_first_id, match_transaction_first_date,
                                                           transaction_id, status)

        if transaction_type in ('11', '18', '19') and transaction_amount != 0:

            match_transaction = daoAnalyzeTransactionMatchSerial.match_transaction_share(plan_id, module_id, code, transaction_share,
                                                                                         "'01'")
            if len(match_transaction) == 0:
                match_transaction = (daoAnalyzeTransactionMatchSerial.
                                     match_transaction_share_remain(plan_id, module_id, code, transaction_share, "'01'"))
            '''
            [0] LABEL
            [1] TRN_ID
            [2] FIRST_TRN_ID
            [3] FIRST_TRN_DATE
            [4] TRN_TYPE
            [5] TRN_SHARE / TRN_AMOUNT
            [6] TRN_REMAIN_SHARE
            [7] TRN_GAINED_AMOUNT
            '''
            if len(match_transaction) > 0:
                match_transaction_label = match_transaction[0][0]
                match_transaction_id = match_transaction[0][1]
                match_transaction_first_id = match_transaction[0][2]
                match_transaction_first_date = match_transaction[0][3]
                match_transaction_amount = match_transaction[0][5]
                match_transaction_remain_share = match_transaction[0][6]
                match_transaction_gained_amount = match_transaction[0][7]

            else:
                match_transaction = daoAnalyzeTransactionMatchSerial.match_transaction_share(plan_id, module_id, code, transaction_share,
                                                                                             "'00', '10'")
                if len(match_transaction) == 0:
                    match_transaction = (daoAnalyzeTransactionMatchSerial.
                                         match_transaction_share_remain(plan_id, module_id, code, transaction_share, "'00', '10'"))
                if len(match_transaction) > 0:
                    match_transaction_label = match_transaction[0][0]
                    match_transaction_id = match_transaction[0][1]
                    match_transaction_first_id = match_transaction[0][2]
                    match_transaction_first_date = match_transaction[0][3]
                    match_transaction_amount = match_transaction[0][5]
                    match_transaction_remain_share = match_transaction[0][6]
                    match_transaction_gained_amount = match_transaction[0][7]
                    current_transaction_type = (daoAnalyzeTransactionMatchSerial.
                                                check_transaction_type(plan_id, module_id, code, match_transaction_first_id))
                    if len(current_transaction_type) > 0:
                        if current_transaction_type[0][0] in ('AMOUNT_SELL', 'SHARE_SELL'):
                            match_transaction = []
                        else:
                            match_transaction_remain_share = current_transaction_type[0][1]
                            match_transaction_gained_amount = current_transaction_type[0][2]

                if len(match_transaction) == 0:
                    match_transaction_label = label
                    match_transaction_id = 0
                    match_transaction_first_id = 0
                    match_transaction_first_date = transaction_date
                    match_transaction_amount = 0
                    match_transaction_remain_share = 0
                    match_transaction_gained_amount = 0

            transaction_remain_share = round((match_transaction_remain_share - transaction_share), share_accuracy)
            transaction_gained_amount = round((match_transaction_gained_amount + transaction_amount), 2)

            if transaction_amount > match_transaction_amount > 0:
                transaction_type_str = 'AMOUNT_SELL'
            else:
                transaction_type_str = 'SHARE_SELL'
            if transaction_type == '11':
                transaction_type_str = transaction_type_str + '*'

            if transaction_remain_share >= 0 and transaction_gained_amount >= 0:
                daoAnalyzeTransactionMatchSerial.update_status_by_label(plan_id, module_id, code, match_transaction_label, '20')
                daoAnalyzeTransactionMatchSerial.update_status_by_first_transaction_id(plan_id, module_id, code, match_transaction_first_id,
                                                                                       '90')
                status = '99'
            else:
                if match_transaction_first_id != match_transaction_id:
                    daoAnalyzeTransactionMatchSerial.update_status_by_label(plan_id, module_id, code, match_transaction_label, '20')
                    (daoAnalyzeTransactionMatchSerial.
                     update_status_by_first_transaction_id(plan_id, module_id, code, match_transaction_first_id, '10'))
                    status = '01'
                if match_transaction_first_id == match_transaction_id and match_transaction_id != 0:
                    (daoAnalyzeTransactionMatchSerial.
                     update_status_by_first_transaction_id(plan_id, module_id, code, match_transaction_first_id, '10'))
                    status = '01'
                if match_transaction_id == 0:
                    match_transaction_id = transaction_id
                    match_transaction_first_id = transaction_id
                    status = '00'
            daoAnalyzeTransactionMatchSerial.insert_record(plan_id, module_id, code, name, transaction_date, transaction_type_str,
                                                           transaction_price, transaction_share, transaction_amount,
                                                           transaction_remain_share, transaction_gained_amount,
                                                           label,
                                                           match_transaction_first_id, match_transaction_first_date,
                                                           transaction_id, status)

        if transaction_type in ('38', '39'):
            transaction_type_str = 'PROFIT_SHARE'
            daoAnalyzeTransactionMatchSerial.insert_record(plan_id, module_id, code, name, transaction_date, transaction_type_str,
                                                           transaction_price, transaction_share, transaction_amount,
                                                           transaction_share, 0,
                                                           label,
                                                           transaction_id, transaction_date,
                                                           transaction_id, '99')

        if transaction_type in ('48', '49'):
            transaction_type_str = 'PROFIT_AMOUNT'
            daoAnalyzeTransactionMatchSerial.insert_record(plan_id, module_id, code, name, transaction_date, transaction_type_str,
                                                           transaction_price, transaction_share, transaction_amount,
                                                           0, transaction_amount,
                                                           label,
                                                           transaction_id, transaction_date,
                                                           transaction_id, '99')


def analyze_remain(plan_id, module_id, code):
    daoAnalyzeTransactionMatchSerialRemain.clear_records(plan_id, module_id, code)
    fund_name = daoFundInfo.fund_info_select(code)[0][1]

    price_accuracy = scriptFundInfo.get_ratio(code)
    share_accuracy = scriptFundInfo.get_share_accuracy(code)

    latest_price = round((daoFundHistory.fund_history_select_latest_price(code)[0][0] * price_accuracy), 4)

    remain_transactions = daoAnalyzeTransactionMatchSerial.select_active_transactions(plan_id, module_id, code, '9999-12-31')
    # [0] TRN_DATE, [1] TRN_TYPE [2] TRN_SHARE [3] TRN_AMOUNT
    # [4] TRN_REMAIN_SHARE [5] TRN_GAINED_AMOUNT
    # [6] LABEL [7] FIRST_TRN_ID [8] FIRST_TRN_DATE [9] TRN_ID [10] STATUS
    for remain_transaction in remain_transactions:
        trn_date = remain_transaction[0]
        trn_type = str(remain_transaction[1])
        trn_share = remain_transaction[2]
        trn_amount = remain_transaction[3]

        trn_price = round((trn_amount / trn_share), 4)
        trn_profit = 0
        trn_profit_pct = 0
        if trn_type.endswith('BUY'):
            trn_profit = round((latest_price * trn_share - trn_amount), 2)
            trn_profit_pct = round((trn_profit / trn_amount * 100), 2)
        if trn_type.endswith('SELL'):
            trn_profit = round((trn_amount / latest_price - trn_share), share_accuracy)
            trn_profit_pct = round((trn_profit / trn_share * 100), 2)

        trn_remain_share = remain_transaction[4]
        trn_gained_amount = remain_transaction[5]

        label = remain_transaction[6]
        frs_trn_id = remain_transaction[7]
        frs_date = remain_transaction[8]
        trn_id = remain_transaction[9]
        status = remain_transaction[10]

        frs_type = trn_type
        frs_price = trn_price
        frs_share = trn_share
        frs_amount = trn_amount
        frs_profit = trn_profit
        frs_profit_pct = trn_profit_pct

        if status == '01':
            first_transaction = daoAnalyzeTransactionMatchSerial.select_first_transaction(plan_id, module_id, code, frs_trn_id)[0]
            frs_type = first_transaction[1]
            frs_share = first_transaction[2]
            frs_amount = first_transaction[3]

            frs_price = round((frs_amount / frs_share), 4)
            frs_profit = 0
            frs_profit_pct = 0
            if frs_type.endswith('BUY'):
                frs_profit = round((latest_price * frs_share - frs_amount), 2)
                frs_profit_pct = round((frs_profit / frs_amount * 100), 2)
            if frs_type.endswith('SELL'):
                frs_profit = round((frs_amount / latest_price - frs_share), share_accuracy)
                frs_profit_pct = round((frs_profit / frs_share * 100), 2)

        daoAnalyzeTransactionMatchSerialRemain.insert(plan_id, module_id, code, fund_name, latest_price,
                                                      trn_type, trn_price, trn_share, trn_amount,
                                                      trn_profit, trn_profit_pct,
                                                      trn_remain_share, trn_gained_amount,
                                                      frs_type, frs_price, frs_share, frs_amount,
                                                      frs_profit, frs_profit_pct,
                                                      trn_date, frs_date, trn_id)


def analyze_quantity(plan_id, module_id, code):
    share_accuracy = scriptFundInfo.get_share_accuracy(code)

    old_record = daoAnalyzeTransactionMatchQuantitative.select_quantity_info(plan_id, module_id, code)
    current_holding = daoAnalyzeTransactionBalance.select_current_holding(plan_id, module_id, code)
    name = current_holding[0][0]
    holding_share = current_holding[0][1]
    holding_amount = current_holding[0][2]
    returning_amount = (daoTransactionHistory.transaction_sum(plan_id, module_id, code, "'11'")[1] +
                        daoTransactionHistory.transaction_sum(plan_id, module_id, code, "'18'")[1])
    shown_amount = round(holding_amount + returning_amount, 2)
    if len(old_record) > 0:
        fee_free_limit = old_record[0][0]

        fee_free_date = timeFormat.calculate_date(timeFormat.get_today(), -fee_free_limit)
        fee_free_share = round((daoAnalyzeTransactionOriginalSerial.get_sum_remain_share(plan_id, module_id, code, fee_free_date)), 2)

        daily_amount = 0
        daily_share = 0
        if holding_amount > 2000:
            if fee_free_limit == 7:
                daily_amount = round((holding_amount / 5), 2)
                daily_share = round((holding_share / 5), share_accuracy)
            if fee_free_limit == 30:
                daily_amount = round((holding_amount / 22), 2)
                daily_share = round((holding_share / 22), share_accuracy)
        daoAnalyzeTransactionMatchQuantitative.update_daily_quantity(plan_id, module_id, code, holding_share, fee_free_share,
                                                                     holding_amount, shown_amount,
                                                                     daily_share, daily_amount)
    else:
        daoAnalyzeTransactionMatchQuantitative.insert_new(plan_id, module_id, code, name, holding_share, holding_amount, shown_amount)


def update_transaction_priority(plan_id, module_id):
    code_priority_list = daoAnalyzeTransactionMatchQuantitative.select_code_priority_list(plan_id, module_id)
    priority = 0
    for code in code_priority_list:
        priority = priority + 1
        daoAnalyzeTransactionMatchSerialRemain.update_transaction_priority(plan_id, module_id, code[0], priority)


def analyze_balance(plan_id, module_id, code):
    daoAnalyzeTransactionBalance.clear_records(plan_id, module_id, code)
    fund_name = scriptFundInfo.get_name(code)

    price_ratio = scriptFundInfo.get_ratio(code)
    share_accuracy = scriptFundInfo.get_share_accuracy(code)
    current_price = round((daoFundHistory.fund_history_select_latest_price(code)[0][0] * price_ratio), 4)

    buy = daoTransactionHistory.transaction_sum(plan_id, module_id, code, "'01', '08', '09'")
    sell = daoTransactionHistory.transaction_sum(plan_id, module_id, code, "'11', '18', '19'")
    share_change = daoTransactionHistory.transaction_sum(plan_id, module_id, code, "'21', '28', '29'")
    profit_share = daoTransactionHistory.transaction_sum(plan_id, module_id, code, "'31', '38', '39'")

    holding_share = round((buy[0] - sell[0] + share_change[0] + profit_share[0]), share_accuracy)
    current_amount = round((holding_share * current_price), 2)

    holding_original_amount = 0
    open_transactions = daoAnalyzeTransactionOriginalSerial.get_open_transactions(plan_id, module_id, code)
    # LABEL, TRN_BUY_IN_ID, TRN_BUY_IN_DATE, TRN_REMAIN_SHARE, TRN_GAINED_AMOUNT
    for open_transaction in open_transactions:
        open_transaction_price = daoAnalyzeTransactionOriginalSerial.get_transaction_price(plan_id, module_id, code, open_transaction[1])
        holding_original_amount = round(holding_original_amount +
                                        round((open_transaction_price * price_ratio * open_transaction[3]), 2), 2)
    holding_avg_price = 0
    if holding_share > 0:
        holding_avg_price = round((holding_original_amount / holding_share), 4)

    match_profit = daoAnalyzeTransactionMatchSerial.select_sum_profit(plan_id, module_id, code)
    match_share_profit = round(match_profit[0], share_accuracy)
    match_amount_profit = round(match_profit[1], 2)

    match_share_hold = round(daoAnalyzeTransactionMatchSerialRemain.get_sum_share(plan_id, module_id, code, '>'), share_accuracy)
    match_share_sold = round(daoAnalyzeTransactionMatchSerialRemain.get_sum_share(plan_id, module_id, code, '<'), 2)
    match_amount_hold = round(daoAnalyzeTransactionMatchSerialRemain.get_sum_amount(plan_id, module_id, code, '>'), share_accuracy)
    match_amount_paid = round(daoAnalyzeTransactionMatchSerialRemain.get_sum_amount(plan_id, module_id, code, '<'), 2)

    if daoCurrencyFundList.check_if_currency_fund(code):
        current_price = 1
        holding_avg_price = 1
        current_amount = holding_share

    daoAnalyzeTransactionBalance.insert(plan_id, module_id, code, fund_name, current_price, current_amount,
                                        holding_share, holding_avg_price,
                                        match_share_profit, match_amount_profit,
                                        match_share_hold, match_amount_paid, match_share_sold, match_amount_hold)
