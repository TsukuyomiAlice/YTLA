<p>
  语言
 <a href="./readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>


# investment

### YTLA应用

### Frank Wang

version 1.0

后端语言及开发框架: Python-Flask  
适用YTLA core版本: **classic**  
文件更新日期: 2026-05-14

## 概念

国内基金交易分析系统，提供基金信息查询、历史净值展示、交易分组匹配分析、持仓统计、连续涨跌分析等功能，用于投资决策参考。

## 应用包目录

```
investment/
├── __init__.py
├── readme.md
├── docs/
│   └── readme/
│       ├── zh-CN/
│       │   └── readme.md
│       └── en-US/
│           └── readme.md
└── modules/
    ├── __init__.py
    ├── _type/
    │   ├── __init__.py
    │   ├── ai_tools/
    │   ├── api/
    │   ├── caller/
    │   ├── const/
    │   ├── dao/
    │   ├── dataset/
    │   ├── docs/
    │   ├── func/
    │   ├── instance/
    │   ├── process/
    │   ├── prompts/
    │   ├── readme.md
    │   ├── routes/
    │   ├── schedule/
    │   ├── script/
    │   └── utils/
    ├── fund_info/
    │   ├── __init__.py
    │   ├── readme.md
    │   ├── ai_tools/
    │   ├── api/
    │   ├── caller/
    │   ├── const/
    │   ├── dao/
    │   │   ├── __init__.py
    │   │   ├── daoCurrencyFundList.py
    │   │   ├── daoFundHistory.py
    │   │   └── daoFundInfo.py
    │   ├── dataset/
    │   ├── docs/
    │   │   ├── readme/
    │   │   └── tasks/
    │   │       └── PRD_20260513_fund_info_frontend/
    │   ├── func/
    │   ├── instance/
    │   ├── process/
    │   │   ├── __init__.py
    │   │   └── processModuleFundInfo.py
    │   ├── prompts/
    │   ├── routes/
    │   │   ├── __init__.py
    │   │   └── routeModuleFundInfo.py
    │   ├── schedule/
    │   ├── script/
    │   └── utils/
    │       ├── __init__.py
    │       └── config_database_sqlite.py
    └── fund_transaction/
        ├── __init__.py
        ├── readme.md
        ├── ai_tools/
        ├── api/
        ├── caller/
        ├── const/
        ├── dao/
        │   ├── __init__.py
        │   ├── daoAnalyzeTransactionBalance.py
        │   ├── daoAnalyzeTransactionMatchQuantitative.py
        │   ├── daoAnalyzeTransactionMatchSerial.py
        │   ├── daoAnalyzeTransactionMatchSerialRemain.py
        │   ├── daoAnalyzeTransactionOriginalSerial.py
        │   └── daoTransactionHistory.py
        ├── dataset/
        ├── docs/
        │   ├── readme/
        │   └── tasks/
        │       └── PRD_20260513_fund_transaction_frontend/
        ├── func/
        ├── instance/
        ├── process/
        │   ├── __init__.py
        │   ├── processModuleFundTransaction.py
        │   ├── processTransactionMatchGroup.py
        │   ├── processTransactionMatchGroupExecuter.py
        │   ├── processTransactionMatchSerial.py
        │   └── processTransactionOriginalSerial.py
        ├── prompts/
        ├── routes/
        │   ├── __init__.py
        │   └── routeModuleFundTransaction.py
        ├── schedule/
        ├── script/
        └── utils/
            ├── __init__.py
            └── config_database_sqlite.py
```

## 变更记录

### 2026-05-14
- 完成基金交易分析系统后端API开发
- 新增 fund_info 模块，提供基金信息和历史净值查询API
- 新增 fund_transaction 模块，提供交易分组分析API
- 修改数据库访问层，统一使用字典键名替代索引访问
- 更新作者名为 Frank Wang
