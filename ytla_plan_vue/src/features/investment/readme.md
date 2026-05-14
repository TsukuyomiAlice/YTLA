<p>
  语言
 <a href="./documents/readme/zh-CN/readme.md"> 简体中文 </a>
 <a href="./documents/readme/en-US/readme.md"> English </a>
</p>


# investment

### YTLA Application

### Frank Wang

version 1.0

Frontend Language & Framework: Vue3, TypeScript  
YTLA core version: **classic**  
File update date: 2026-05-14

## 概念

国内基金交易分析系统前端，提供基金信息查询、历史净值图表展示、交易分组分析、持仓统计等界面功能，支持用户交互查看投资详情。

## 应用包目录

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

## 变更记录

### 2026-05-14
- 完成基金交易分析系统前端界面开发
- 新增 fund_info 模块，包含基金信息卡片和净值图表
- 新增 fund_transaction 模块，包含持仓统计和分组分析
- 实现左右分栏布局的交易分析界面
- 实现可折叠的交易分组卡片组件
- 更新作者名为 Frank Wang
