# ButtonAction 组件重构 - Product Requirement Document

## Overview
- **Summary**: 对 sideCardEditor 模块中的 ButtonAction 组件进行规范化重构，使其符合 YTLA 项目的 UI 组件设计规范。主要工作包括：关注点分离、类型定义提取、逻辑封装等。
- **Purpose**: 解决当前 ButtonAction.vue 组件不符合 UI 组件规范的问题，实现 Vue 文件仅负责视图，逻辑在 composables 中，类型定义在 definitions 中的目标。
- **Target Users**: YTLA 项目的开发人员

## Goals
- 实现 ButtonAction 组件的关注点分离
- 将类型定义提取到 definitions 目录
- 将计算属性和逻辑封装到 composables
- 保持组件的向后兼容性
- 确保所有功能正常工作

## Non-Goals (Out of Scope)
- 不修改组件的外部 Props 和 Emits 接口
- 不改变组件的视觉样式
- 不添加新的功能特性
- 不重构其他相关组件（如 ButtonCancel、ButtonScale）

## Background & Context
- ButtonAction 组件是 sideCardEditor 模块的核心 UI 组件之一
- 当前组件虽然已经有 useButtonAction composable，但仍有部分逻辑在 Vue 文件中
- 项目已有 rule_ui_instructions.md 规范文档，明确了 UI 组件的设计标准
- 之前已有 PRD_20260402 完成了部分组件的规范化工作

## Functional Requirements
- **FR-1**: 提取 ButtonAction 组件的 Props 和 Emits 类型定义到 definitions 目录
- **FR-2**: 将 Vue 文件中的 computed 属性（defaultAriaLabel、computedAriaLabel、computedTitle）移动到 composables
- **FR-3**: 更新 ButtonAction.vue 仅负责视图，逻辑全部在 composables 中
- **FR-4**: 确保所有现有功能保持正常

## Non-Functional Requirements
- **NFR-1**: 保持向后兼容，不破坏现有调用方
- **NFR-2**: 保持 TypeScript 类型安全
- **NFR-3**: 遵循项目编码规范和最佳实践

## Constraints
- **Technical**: Vue 3 + TypeScript + SCSS + Composition API
- **Business**: 需要在现有架构基础上进行重构，保持代码库一致性
- **Dependencies**: 依赖项目现有的 i18n、composables 等基础设施

## Assumptions
- 组件的外部接口不需要变更
- 所有现有调用方可以继续正常使用
- useButtonAction.ts 可以扩展来包含更多逻辑
- i18n 资源已经存在且正常工作

## Acceptance Criteria

### AC-1: 类型定义提取成功
- **Given**: ButtonAction.vue 组件已存在
- **When**: 完成类型定义提取
- **Then**: definitions 目录下存在 ButtonActionType.ts 文件，包含完整的 Props 和 Emits 类型定义
- **Verification**: `programmatic`
- **Notes**: 保持现有 Props 和 Emits 接口不变

### AC-2: 逻辑封装到 composables
- **Given**: ButtonAction.vue 组件已存在
- **When**: 完成逻辑迁移
- **Then**: useButtonAction.ts 包含所有计算属性和业务逻辑，Vue 文件仅负责视图
- **Verification**: `programmatic`
- **Notes**: 确保 defaultAriaLabel、computedAriaLabel、computedTitle 都在 composables 中

### AC-3: Vue 文件符合关注点分离
- **Given**: 重构已完成
- **When**: 检查 ButtonAction.vue
- **Then**: Vue 文件仅包含模板、导入语句、样式导入，没有业务逻辑
- **Verification**: `human-judgment`
- **Notes**: 验证没有直接定义 computed、methods 等

### AC-4: 向后兼容性保持
- **Given**: 重构已完成
- **When**: 运行现有代码
- **Then**: 所有现有功能正常工作，调用方无需修改
- **Verification**: `programmatic`
- **Notes**: 确保 Props、Emits、Slots 接口保持不变

### AC-5: TypeScript 类型检查通过
- **Given**: 重构已完成
- **When**: 运行 TypeScript 编译
- **Then**: 没有类型错误
- **Verification**: `programmatic`
- **Notes**: 确保类型定义正确且完整

## Open Questions
- [ ] 是否需要为 ButtonAction 组件创建单独的目录结构？
- [ ] 是否需要同时重构 ButtonCancel 和 ButtonScale 组件以保持一致性？
