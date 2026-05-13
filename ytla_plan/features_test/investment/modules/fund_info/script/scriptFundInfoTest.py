# encode = utf-8
from ytla_plan.features.investment.modules.fund_info.script import scriptFundInfo

def test_get_name():
    name = scriptFundInfo.get_name('161226')
    print(name)

if __name__ == '__main__':
    test_get_name()