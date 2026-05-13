# encode = utf-8

from ytla_fund.dao import daoCurrencyFundList, daoAnalyzeTransactionMatchSerial, daoAnalyzeTransactionMatchSerialRemain
from ytla_fund.script import scriptFundInfo


def add_currency_fund(code):
    name = scriptFundInfo.get_name(code)
    daoCurrencyFundList.insert(code, name)
    daoAnalyzeTransactionMatchSerial.clear_records(code)
    daoAnalyzeTransactionMatchSerialRemain.clear_records(code)


if __name__ == '__main__':
    add_currency_fund('001234')
