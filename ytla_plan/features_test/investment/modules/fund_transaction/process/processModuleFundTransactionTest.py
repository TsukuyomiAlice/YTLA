from ytla_plan.features.investment.modules.fund_transaction.process import processModuleFundTransaction

def test():
    res = processModuleFundTransaction.get_transaction_analysis('161226')
    print(res.data)

if __name__ == '__main__':
    test()
