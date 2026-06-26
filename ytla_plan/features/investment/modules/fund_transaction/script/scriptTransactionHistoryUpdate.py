# encode = utf-8

from ..dao import daoTransactionHistory


def execute(plan_id, module_id):
    daoTransactionHistory.update_transactions_to_confirmed(plan_id, module_id)
