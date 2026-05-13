from  ytla_plan.features.investment.modules.fund_info.process import processModuleFundInfo

def test():
    res = processModuleFundInfo.get_fund_info('161226')
    print(res.data)

if __name__ == '__main__':
    test()