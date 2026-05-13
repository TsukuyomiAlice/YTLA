# encode = utf-8

from ytla_fund.dao import daoTransactionHistory, daoCurrencyFundList
from ytla_fund.script import scriptFundHistory
from ytla_fund.process import processTransactionMatchGroup

# 保持关注的基金列表
# 即便清仓了也保持关注

focus_code_list = [

    # 港股
    # 013128 汇添富恒生科技C 7天
    # 010789 汇添富恒生C 7天
    '013128', '010789',
    # 成长风格股指
    # 011609 易方达科创50C 7天
    # 001593 天弘创业板C 7天
    # 013442 建信中证1000E 7天
    # 005314 万家中证1000C 30天
    # 018113 北证50C 7天
    '011609', '001593', '013442', '005314', '018113',

    # 金银
    # 161226 国投瑞银白银A 7天0.5
    # 002611 博时人民币金C 7天0.1/30天
    '161226', '002611',
    # 大宗（长持）
    # 160216 国泰大宗
    # 163208 诺安油气
    # 161217 国投瑞银中证资源
    # 161715 招商中证大宗
    '160216', '163208', '161217', '161715',
    # 原油
    # 006476 南方原油C 30天
    '006476',
    # 化工期货
    # 008828 建信郑商所能源化工期货C 7天
    # 015226 汇添富中证细分化工C 7天
    '008828', '015226',
    # 豆粕
    # 007937 华夏豆粕饲料A 7天0.1/30天
    '007937',

    # 贵金属
    # 002207 前海开源金银珠宝C 30天
    '002207',
    # 工业金属
    # 004433 南方有色有色金属C 7天
    # 010990 南方有色有色金属E 7天
    # 007911 大成有色金属期货C 7天0.1/30天
    '004433', '010990', '007911',
    # 钢铁
    # 012810 鹏华国证钢铁C 7天
    '012810',
    # 煤炭
    # 008280 国泰中证煤炭C 7天0.1/30天
    '008280',

    # 医药
    # 006229 中欧医疗创新 30天
    # 010710 安信医药健康股票C 30天
    # 501010 汇添富生物 7天0.1/30天
    # 501012 汇添富中药 7天0.1/30天
    # 014425 博时恒生医疗保健ETF发起式联接(QDII)C 7天
    '006229', '010710', '501010', '501012', '014425',
    # 农业
    # 010770 天弘中证农业主题C 7天
    # 012725 国泰中证畜牧养殖C 7天0.1/30天
    # 014064 银华农业C 30天
    '010770', '012725', '014064',
    # 军工
    # 010364 鹏华军工C 7天
    '010364',
    # 新能源大板块
    # 002984 广发环保(ETF)C 7天
    # 011329 景顺长城新能源C 30天
    '002984', '011329',
    # 基建
    # 005224 广发中证基建C 7天0.1/30天
    '005224',
    # 房地产
    # 004643 南方中证房地产C 30天
    '004643',
    # 银行
    # 004598 南方中证银行C 30天
    '004598',
    # 券商
    # 013597 招商中证券商C 7天
    '013597',
    # 白酒/消费
    # 012043 鹏华酒C 7天
    # 011309 富国消费C 30天
    '012043', '011309',
    # 传媒娱乐
    # 004753 广发中证传媒C 30天
    # 015667 银河文体娱乐C 30天
    '004753', '015667',
    # 互联网
    # 006328 易方达海外中国互联网(QDII)C 30天
    '006328',
    # 人工智能
    # 005963 宝盈人工智能C 30天
    '005963', ]


def execute():
    print('========== 自动处理开始 ==========')
    # scriptTransactionHistoryMaintain.execute()

    print('========== 统计持有份额中 ==========')
    # 获取所有有交易记录的基金
    fund_code_list = daoTransactionHistory.transaction_fund_code_get()

    fund_history_list = []
    for code in fund_code_list:
        fund_history_list.append(code[0])
    for code in focus_code_list:
        if code not in fund_history_list:
            fund_history_list.append(code)

    print('========== 获取最新净值中 ==========')
    for code in fund_history_list:
        print(code)
        scriptFundHistory.get_history(code)

    print('========== 分析交易记录中 ==========')
    brief_list = []

    check_list = [
        # 股指
        '021207',  # 易方达中证A50ETF联接发起式C
        '001593',  # 天弘创业板ETF联接基金C
        '011609',  # 易方达科创板50ETF联接C
        '018113',  # 工银北证50成份指数C
        '010789',  # 汇添富恒生指数(QDII-LOF)C
        '013128',  # 汇添富恒生科技ETF联接发起式(QDII)C
        '006328',  # 易方达中证海外50ETF联接人民币C
        # 大宗期货
        '161226',  # 国投瑞银白银期货(LOF)
        '007911',  # 大成有色金属期货ETF联接C
        '008828',  # 建信易盛郑商所能源化工期货ETF联接C
        '007937',  # 华夏饲料豆粕期货ETF联接A
        # 红利
        '019312',  # 南方富时中国国企开放共赢ETF发起联接C
        '007467',  # 华泰柏瑞中证红利低波ETF联接C
        '013275',  # 富国中证煤炭指数(LOF)C
        # 银行证券
        '001595',  # 天弘中证银行ETF联接C
        '013597',  # 招商中证全指证券公司指数(LOF)C
        # 行业
        '501010',  # 汇添富中证生物科技指数C
        '006229',  # 中欧医疗创新股票C
        '012043',  # 鹏华酒C
        '014194',  # 汇添富中证芯片产业指数增强发起C
        '002984',  # 广发中证环保ETF联接C
        '015042',  # 国泰国证房地产行业指数C
        '012810',  # 鹏华国证钢铁行业指数(LOF)C
        '010364',  # 鹏华空天军工指数(LOF)C
        '010770',  # 天弘中证农业主题C
        '010990',  # 南方有色金属ETF联接E
    ]
    for code in fund_code_list:
        print(code[0])
        if not daoCurrencyFundList.check_if_currency_fund(code[0]):
            brief_list.append(processTransactionMatchGroup.execute(code[0]))
    processTransactionMatchGroup.change_files_name(brief_list, check_list)
    processTransactionMatchGroup.brief_report(brief_list)

    # processTransactionMatchSerial.update_transaction_priority()

    print('========== 分析基金中 ==========')


if __name__ == "__main__":
    execute()
