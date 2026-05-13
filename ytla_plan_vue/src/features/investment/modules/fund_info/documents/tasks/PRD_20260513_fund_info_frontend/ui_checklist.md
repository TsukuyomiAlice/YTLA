# UI组件生成检查清单 - 基金信息模块

## 本次UI生成形式
- **新建**: 为基金信息模块创建UI组件

## 拟生成的UI列表

### 基金信息相关UI组件
- **FundInfoCard.vue**
  - **生成原因**: 展示基金基本信息
  - **用途**: 以卡片形式展示基金代码、名称、最新净值等
  - **包含的派生文件**:
    - composables/useFundInfoCard.ts
    - styles/fund-info-card.scss

- **FundPriceChart.vue**
  - **生成原因**: 核心需求 - 展示基金净值折线图
  - **用途**: 可视化展示基金历史净值走势
  - **包含的派生文件**:
    - composables/useFundPriceChart.ts
    - styles/fund-price-chart.scss

### 通用UI组件
- **ButtonPrimary.vue**
  - **生成原因**: 主要操作按钮
  - **用途**: 查询等主要操作
  - **包含的派生文件**:
    - composables/useButtonPrimary.ts
    - styles/button-primary.scss

- **CardContainer.vue**
  - **生成原因**: 内容卡片容器
  - **用途**: 包装内容形成统一的卡片样式
  - **包含的派生文件**:
    - composables/useCardContainer.ts
    - styles/card-container.scss
