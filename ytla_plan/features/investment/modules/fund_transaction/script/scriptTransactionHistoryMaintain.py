# encode = utf-8

from ..dao import daoTransactionHistory


def execute():
    old_list = daoTransactionHistory.maintain_get_transaction_list()
    counter = 1000001
    for old_record in old_list:
        old_id = old_record[0]
        daoTransactionHistory.maintain_update_transaction_list(old_id, counter)
        counter = counter + 1
    temp_list = daoTransactionHistory.maintain_get_transaction_list()
    counter = 1
    for temp_record in temp_list:
        temp_id = temp_record[0]
        daoTransactionHistory.maintain_update_transaction_list(temp_id, counter)
        counter = counter + 1


if __name__ == "__main__":
    execute()
