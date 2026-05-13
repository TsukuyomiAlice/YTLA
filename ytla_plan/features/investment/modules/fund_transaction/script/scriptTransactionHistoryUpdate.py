# encode = utf-8

from ..dao import daoTransactionHistory


def execute():
    daoTransactionHistory.update_transactions_to_confirmed()


if __name__ == "__main__":
    execute()
