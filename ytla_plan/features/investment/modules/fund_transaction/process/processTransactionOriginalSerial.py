# coding=utf-8

from ytla_fund.dao import daoTransactionHistory, daoAnalyzeTransactionOriginalSerial
from ytla_fund.script import scriptFundInfo


def analyze(code):

    daoAnalyzeTransactionOriginalSerial.clear_records(code)

    price_accuracy = scriptFundInfo.get_ratio(code)
    share_accuracy = scriptFundInfo.get_share_accuracy(code)

    transaction_records = daoTransactionHistory.transaction_history_select_asc(code)
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

        latest_label = daoAnalyzeTransactionOriginalSerial.get_latest_label(code)
        label = latest_label + 1

        if transaction_type in ('01', '08', '09') and transaction_share != 0:
            transaction_type_str = 'BUY'
            if transaction_type == '01':
                transaction_type_str = 'BUY*'
            daoAnalyzeTransactionOriginalSerial.insert_record(code, name,
                                                              transaction_date, transaction_type_str, transaction_price,
                                                              transaction_share, transaction_amount,
                                                              0, 0,
                                                              transaction_share, 0,
                                                              label, transaction_id, transaction_date,
                                                              transaction_id, '0')

        if transaction_type in ('11', '18', '19') and transaction_amount != 0:
            transaction_type_str = 'SELL'
            if transaction_type == '11':
                transaction_type_str = 'SELL*'
            transaction_share_remain = transaction_share
            transaction_amount_remain = transaction_amount

            open_transactions = daoAnalyzeTransactionOriginalSerial.get_open_transactions(code)
            '''
            [0] LABEL
            [1] TRANSACTION_BUY_IN_ID
            [2] TRANSACTION_BUY_IN_DATE
            [3] TRANSACTION_REMAIN_SHARE
            [4] TRANSACTION_GAINED_AMOUNT
            '''

            for open_transaction in open_transactions:
                if transaction_share_remain > 0:
                    # transaction_effective_share = 0
                    # transaction_effective_amount = 0
                    actual_transaction_price = round((transaction_amount / transaction_share), 4)
                    open_transaction_label = open_transaction[0]
                    open_transaction_buy_in_id = open_transaction[1]
                    open_transaction_buy_in_date = open_transaction[2]
                    open_transaction_remain_share = open_transaction[3]
                    open_transaction_gained_amount = open_transaction[4]

                    if transaction_share_remain >= open_transaction_remain_share:
                        transaction_effective_share = open_transaction_remain_share
                        transaction_effective_amount = round((open_transaction_remain_share * actual_transaction_price),
                                                             2)
                        transaction_share_remain = round((transaction_share_remain - open_transaction_remain_share),
                                                         share_accuracy)
                        transaction_remained_share = 0
                        transaction_gained_amount = round((open_transaction_gained_amount +
                                                           transaction_effective_amount), 2)
                        transaction_amount_remain = round((transaction_amount_remain -
                                                           transaction_effective_amount), 2)
                        status = 1
                    else:
                        transaction_effective_share = transaction_share_remain
                        transaction_effective_amount = transaction_amount_remain
                        transaction_remained_share = round((open_transaction_remain_share - transaction_share_remain),
                                                           share_accuracy)
                        transaction_gained_amount = round((open_transaction_gained_amount +
                                                           transaction_amount_remain), 2)
                        transaction_share_remain = 0
                        status = 0

                    daoAnalyzeTransactionOriginalSerial.insert_record(code, name,
                                                                      transaction_date, transaction_type_str,
                                                                      transaction_price,
                                                                      transaction_share, transaction_amount,
                                                                      transaction_effective_share,
                                                                      transaction_effective_amount,
                                                                      transaction_remained_share,
                                                                      transaction_gained_amount,
                                                                      label,
                                                                      open_transaction_buy_in_id,
                                                                      open_transaction_buy_in_date,
                                                                      transaction_id,
                                                                      status)
                    daoAnalyzeTransactionOriginalSerial.update_status(code, open_transaction_label, '1')
                    label = label + 1

        if transaction_type in ('28', '29', '38', '39', '48', '49'):
            transaction_type_str = ''
            transaction_share_remain = transaction_share
            transaction_amount_remain = transaction_amount
            open_holding_share = 0
            open_holding_amount = 0

            if transaction_type in ('28', '29'):
                transaction_type_str = 'SHARE_CHANGE'

            if transaction_type in ('38', '39'):
                transaction_type_str = 'PROFIT_SHARE'

            if transaction_type in ('48', '49'):
                transaction_type_str = 'PROFIT_AMOUNT'

            open_transactions = daoAnalyzeTransactionOriginalSerial.get_open_transactions(code)
            for open_transaction in open_transactions:
                # open_transaction_label = open_transaction[0]
                # open_transaction_buy_in_id = open_transaction[1]
                # open_transaction_buy_in_date = open_transaction[2]
                open_transaction_remain_share = open_transaction[3]
                open_transaction_gained_amount = open_transaction[4]
                if transaction_type in ('28', '29', '38', '39', '48', '49'):
                    open_holding_share = open_holding_share + open_transaction_remain_share
                if transaction_type in ('48', '49'):
                    open_holding_amount = open_holding_amount + open_transaction_gained_amount

            open_transaction_count = 1
            for open_transaction in open_transactions:
                open_transaction_label = open_transaction[0]
                open_transaction_buy_in_id = open_transaction[1]
                open_transaction_buy_in_date = open_transaction[2]
                open_transaction_remain_share = open_transaction[3]
                open_transaction_gained_amount = open_transaction[4]

                remain_share_change = 0
                gained_amount = 0
                transaction_remained_share = 0
                transaction_gained_amount = 0

                if transaction_type in ('28', '29', '38', '39'):
                    transaction_gained_amount = open_transaction_gained_amount
                    remain_share_change = round(open_transaction_remain_share / open_holding_share * transaction_share,
                                                share_accuracy)
                    if open_transaction_count < len(open_transactions):
                        transaction_remained_share = round((open_transaction_remain_share + remain_share_change),
                                                           share_accuracy)
                        transaction_share_remain = transaction_share_remain - remain_share_change
                        open_transaction_count = open_transaction_count + 1
                    else:
                        transaction_remained_share = round((open_transaction_remain_share + transaction_share_remain),
                                                           share_accuracy)

                if transaction_type in ('48', '49'):
                    transaction_remained_share = open_transaction_remain_share
                    gained_amount = round(open_transaction_remain_share / open_holding_share * transaction_amount, 2)
                    if open_transaction_count < len(open_transactions):
                        transaction_gained_amount = round((open_transaction_gained_amount + gained_amount), 2)
                        transaction_amount_remain = transaction_amount_remain - gained_amount
                        open_transaction_count = open_transaction_count + 1
                    else:
                        transaction_gained_amount = round((open_transaction_gained_amount + transaction_amount_remain),
                                                          2)

                daoAnalyzeTransactionOriginalSerial.insert_record(code, name,
                                                                  transaction_date, transaction_type_str,
                                                                  transaction_price,
                                                                  transaction_share, transaction_amount,
                                                                  remain_share_change,
                                                                  gained_amount,
                                                                  transaction_remained_share,
                                                                  transaction_gained_amount,
                                                                  label,
                                                                  open_transaction_buy_in_id,
                                                                  open_transaction_buy_in_date,
                                                                  transaction_id,
                                                                  '0')
                daoAnalyzeTransactionOriginalSerial.update_status(code, open_transaction_label, '1')
                label = label + 1
