# 基金模块页面显示修正 - 实施计划

## [ ] Task 1: 修改 fund_info 模块的主组件
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 修改 Fund_infoMain_00.vue，保留基金代码输入区域
  - 移除标签页切换功能
  - 移除对 investmentStore 的依赖
  - 只保留基金基础信息和基金历史净值的显示
  - 移除交易分析相关的代码
  - 确保组件能正常从 store 中获取并显示数据
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `human-judgement` TR-1.1: fund_info 页面只显示基金基础信息和基金历史净值
  - `human-judgement` TR-1.2: fund_info 页面有基金代码输入区域
- **Notes**: 需要确保组件仍然能正常工作，可能需要调整数据加载逻辑

## [ ] Task 2: 修改 fund_transaction 模块的主组件
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 修改 Fund_transactionMain_00.vue，添加基金代码输入区域
  - 添加基金基础信息和基金历史净值的显示
  - 保留原有的基金交易记录显示
  - 确保数据能正常加载和显示
- **Acceptance Criteria Addressed**: [AC-2, AC-3]
- **Test Requirements**:
  - `human-judgement` TR-2.1: fund_transaction 页面显示完整信息
  - `human-judgement` TR-2.2: fund_transaction 页面有基金代码输入区域
- **Notes**: 需要引入 fund_info 的 store 和组件

## [ ] Task 3: 清理多余文件
- **Priority**: P1
- **Depends On**: [Task 1, Task 2]
- **Description**: 
  - 删除 InvestmentMain.vue
  - 删除 investmentStore.ts
  - 删除 investment/stores 目录（如果为空）
- **Acceptance Criteria Addressed**: [AC-4]
- **Test Requirements**:
  - `programmatic` TR-3.1: 确认 InvestmentMain.vue 已删除
  - `programmatic` TR-3.2: 确认 investmentStore.ts 已删除
- **Notes**: 确保删除这些文件不会影响其他功能
