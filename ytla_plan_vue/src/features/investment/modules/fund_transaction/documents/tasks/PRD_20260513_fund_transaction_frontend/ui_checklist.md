# UI组件生成检查清单 - 基金交易模块

## 本次UI生成形式
- **新建**: 为基金交易模块创建UI组件

## 拟生成的UI列表

### 交易记录相关UI组件
- **TransactionList.vue**
  - **生成原因**: 展示交易记录列表
  - **用途**: 显示所有交易记录，支持筛选
  - **包含的派生文件**:
    - composables/useTransactionList.ts
    - styles/transaction-list.scss

- **TransactionForm.vue**
  - **生成原因**: 添加新交易记录
  - **用途**: 表单形式输入交易信息
  - **包含的派生文件**:
    - composables/useTransactionForm.ts
    - styles/transaction-form.scss

### 交易分析相关UI组件
- **GroupAnalysisCard.vue**
  - **生成原因**: 展示分组交易分析结果
  - **用途**: 清晰展示各组交易情况和盈亏
  - **包含的派生文件**:
    - composables/useGroupAnalysisCard.ts
    - styles/group-analysis-card.scss

- **HoldingStats.vue**
  - **生成原因**: 展示持仓统计信息
  - **用途**: 显示持仓数量、价值等统计信息
  - **包含的派生文件**:
    - composables/useHoldingStats.ts
    - styles/holding-stats.scss

- **ProfitChart.vue**
  - **生成原因**: 可视化展示盈亏统计
  - **用途**: 图表形式展示盈亏情况
  - **包含的派生文件**:
    - composables/useProfitChart.ts
    - styles/profit-chart.scss

### 通用UI组件
- **ButtonPrimary.vue**
  - **生成原因**: 主要操作按钮
  - **用途**: 提交、执行等主要操作
  - **包含的派生文件**:
    - composables/useButtonPrimary.ts
    - styles/button-primary.scss

- **ButtonSecondary.vue**
  - **生成原因**: 次要操作按钮
  - **用途**: 取消、返回等次要操作
  - **包含的派生文件**:
    - composables/useButtonSecondary.ts
    - styles/button-secondary.scss

- **CardContainer.vue**
  - **生成原因**: 内容卡片容器
  - **用途**: 包装内容形成统一的卡片样式
  - **包含的派生文件**:
    - composables/useCardContainer.ts
    - styles/card-container.scss
