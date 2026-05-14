<p>
  Language
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="./readme.md"> English </a>
</p>


# investment

### YTLA Application

### Frank Wang

version 1.0

Backend Language & Framework: Python-Flask  
YTLA core version: **classic**  
Last updated: 2026-05-14

## Concept

Domestic fund transaction analysis system, providing fund information query, historical net value display, transaction group matching analysis, holding statistics, continuous rise and fall analysis and other functions for investment decision reference.

## Application Package Directory

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

## Change Log

### 2026-05-14
- Completed backend API development for fund transaction analysis system
- Added fund_info module, providing fund information and historical net value query API
- Added fund_transaction module, providing transaction group analysis API
- Modified database access layer, unified use of dictionary key names instead of index access
- Updated author name to Frank Wang
