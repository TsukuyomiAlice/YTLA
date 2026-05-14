<p>
  Language
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="./readme.md"> English </a>
</p>


# investment

### YTLA Application

### Frank Wang

version 1.0

Frontend Language & Framework: Vue3, TypeScript  
YTLA core version: **classic**  
Last updated: 2026-05-14

## Concept

Domestic fund transaction analysis system frontend, providing fund information query, historical net value chart display, transaction group analysis, position statistics and other interface functions, supporting user interaction to view investment details.

## Application Package Directory

```
investment/
├── readme.md
├── documents/
│   └── readme/
│       ├── zh-CN/
│       │   └── readme.md
│       └── en-US/
│           └── readme.md
├── modules/
│   ├── _type/
│   │   ├── locales/
│   │   ├── styles/
│   │   ├── ui/
│   │   └── readme.md
│   ├── fund_info/
│   │   ├── avatar/
│   │   │   └── Avatar.vue
│   │   ├── components/
│   │   │   ├── Fund_infoMain.vue
│   │   │   ├── Fund_infoMain_00.vue
│   │   │   ├── Fund_infoSub.vue
│   │   │   ├── Fund_infoSub_00.vue
│   │   │   ├── FundInfoCard.vue
│   │   │   ├── FundPriceChart.vue
│   │   │   └── FundInfoView.vue
│   │   ├── documents/
│   │   │   ├── readme/
│   │   │   └── tasks/
│   │   ├── flows/
│   │   │   └── fund_infoFlowManager.ts
│   │   ├── locales/
│   │   ├── registries/
│   │   ├── services/
│   │   │   └── fundInfoService.ts
│   │   └── stores/
│   │       └── fundInfoStore.ts
│   └── fund_transaction/
│       ├── avatar/
│       │   └── Avatar.vue
│       ├── components/
│       │   ├── Fund_transactionMain.vue
│       │   ├── Fund_transactionMain_00.vue
│       │   ├── Fund_transactionSub.vue
│       │   ├── Fund_transactionSub_00.vue
│       │   ├── HoldingStats.vue
│       │   ├── ContinuousStats.vue
│       │   └── GroupAnalysisCard.vue
│       ├── documents/
│       │   ├── readme/
│       │   └── tasks/
│       ├── flows/
│       │   └── fund_transactionFlowManager.ts
│       ├── locales/
│       ├── registries/
│       ├── services/
│       │   └── fundTransactionService.ts
│       └── stores/
│           └── fundTransactionStore.ts
```

## Change Log

### 2026-05-14
- Completed frontend interface development for fund transaction analysis system
- Added fund_info module, including fund info card and net value chart
- Added fund_transaction module, including position statistics and group analysis
- Implemented left-right split layout for transaction analysis interface
- Implemented collapsible transaction group card component
- Updated author name to Frank Wang
