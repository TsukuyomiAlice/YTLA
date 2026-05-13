# 基金模块页面显示修正 - PRD

## Overview
- **Summary**: 修正 fund_info 和 fund_transaction 两个模块的页面显示逻辑，确保每个页面显示正确的内容，同时清理多余文件
- **Purpose**: 解决当前页面显示内容反了，以及 fund_transaction 页面缺少基金代码输入区域的问题，同时清理多余的文件
- **Target Users**: 使用基金分析功能的用户

## Goals
- fund_info 页面只显示基金基础信息和基金历史净值
- fund_transaction 页面显示基金基础信息、基金历史净值和基金交易记录，并包含基金代码输入区域
- 清理多余的 InvestmentMain.vue 和 investmentStore.ts
- 保持代码运行正常，只修正显示逻辑和清理代码

## Non-Goals (Out of Scope)
- 修改数据获取逻辑
- 修改组件样式（除非必要）
- 添加新功能

## Background & Context
当前代码结构存在以下问题：
- fund_info 页面同时显示了基金信息和交易分析，并有标签页切换
- fund_transaction 页面只显示交易分析，没有基金代码输入区域
- 这与用户期望的显示方式相反
- 存在多余的文件：InvestmentMain.vue（没有被引用）和 investmentStore.ts（只在旧组件中使用）

## Functional Requirements
- **FR-1**: fund_info 页面只显示基金基础信息和基金历史净值
- **FR-2**: fund_transaction 页面显示基金基础信息、基金历史净值和基金交易记录
- **FR-3**: fund_transaction 页面包含基金代码输入区域
- **FR-4**: 清理多余的 InvestmentMain.vue 和 investmentStore.ts

## Non-Functional Requirements
- **NFR-1**: 页面加载速度保持不变
- **NFR-2**: 用户体验保持流畅

## Constraints
- **Technical**: 使用现有的 Vue 3 + TypeScript 架构
- **Dependencies**: 使用现有的 store 和组件

## Assumptions
- 现有的数据获取逻辑正常工作
- 现有的组件可以正常使用

## Acceptance Criteria

### AC-1: fund_info 页面显示正确内容
- **Given**: 用户进入 fund_info 页面
- **When**: 页面加载完成
- **Then**: 只显示基金基础信息和基金历史净值
- **Verification**: `human-judgment`

### AC-2: fund_transaction 页面显示正确内容
- **Given**: 用户进入 fund_transaction 页面
- **When**: 页面加载完成
- **Then**: 显示基金基础信息、基金历史净值和基金交易记录
- **Verification**: `human-judgment`

### AC-3: fund_transaction 页面有基金代码输入区域
- **Given**: 用户进入 fund_transaction 页面
- **When**: 页面加载完成
- **Then**: 存在基金代码输入框和查询按钮
- **Verification**: `human-judgment`

### AC-4: 清理多余文件
- **Given**: 代码修改完成
- **When**: 检查项目文件
- **Then**: InvestmentMain.vue 和 investmentStore.ts 已被删除
- **Verification**: `programmatic`

## Open Questions
- 无
