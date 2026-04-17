# SideCardEditor UI组件规范化 - Product Requirement Document

## Overview
- **Summary**: 对sideCardEditor模块的UI组件进行规范化整改，使其符合rule_ui_instructions.md规范要求，包括文件结构调整、命名规范统一、样式分离、组合式函数补充等
- **Purpose**: 解决当前sideCardEditor UI组件不符合项目规范的问题，提高代码可维护性、可复用性和一致性，参照sideCard模块的最佳实践
- **Target Users**: 项目开发团队、维护人员

## Goals
- 解决样式内联问题，实现关注点分离
- 为所有UI组件补充对应的composables
- 优化命名规范，提高语义清晰度
- 提升可访问性，添加ARIA标签
- 使sideCardEditor UI组件符合项目统一规范

## Non-Goals (Out of Scope)
- 不修改业务逻辑（仅重构代码结构）
- 不修改definitions、factories、stores等非规范范围文件
- 不改变现有功能行为
- 不重构layouts目录下的组件（除非必要）

## Background & Context
- sideCardEditor是YTLA项目中用于编辑卡片的核心模块
- 项目已有明确的UI组件规范（rule_ui_instructions.md）
- 相邻模块sideCard已完全符合规范，可作为最佳实践参考
- 当前sideCardEditor合规性评分为70%，存在多个改进空间

## Functional Requirements
- **FR-1**: 将ButtonCancel.vue的内联样式提取到独立的SCSS文件
- **FR-2**: 将ButtonScale.vue的内联样式提取到独立的SCSS文件
- **FR-3**: 创建useButtonAction.ts组合式函数
- **FR-4**: 创建useButtonCancel.ts组合式函数
- **FR-5**: 创建useButtonScale.ts组合式函数
- **FR-6**: 为所有UI组件添加ARIA标签提升可访问性

## Non-Functional Requirements
- **NFR-1**: 所有修改必须保持现有功能不变
- **NFR-2**: 代码必须通过TypeScript类型检查
- **NFR-3**: 样式表现必须与修改前一致
- **NFR-4**: 所有新增文件必须符合项目命名规范

## Constraints
- **Technical**: 必须使用Vue 3 + TypeScript + SCSS + Composition API
- **Business**: 必须遵循rule_ui_instructions.md规范
- **Dependencies**: 参照sideCard模块的实现方式

## Assumptions
- 假设ButtonAction主要用于提交操作（可根据实际用途调整）
- 假设现有功能无需修改
- 假设用户接受渐进式改进

## Acceptance Criteria

### AC-1: ButtonCancel样式分离
- **Given**: ButtonCancel.vue存在内联样式
- **When**: 将样式提取到styles/button-cancel.scss并在组件中导入
- **Then**: 组件样式表现一致，且样式文件独立存在
- **Verification**: `programmatic`
- **Notes**: 确保CSS自定义属性和响应式设计保持不变

### AC-2: ButtonScale样式分离
- **Given**: ButtonScale.vue存在内联样式
- **When**: 将样式提取到styles/button-scale.scss并在组件中导入
- **Then**: 组件样式表现一致，且样式文件独立存在
- **Verification**: `programmatic`
- **Notes**: 确保所有媒体查询都正确迁移

### AC-3: useButtonAction创建
- **Given**: ButtonAction.vue没有对应的composable
- **When**: 创建composables/useButtonAction.ts并在组件中使用
- **Then**: 组件逻辑封装在composable中，可独立测试和复用
- **Verification**: `human-judgment`
- **Notes**: 保持现有emit和props接口不变

### AC-4: useButtonCancel创建
- **Given**: ButtonCancel.vue没有对应的composable
- **When**: 创建composables/useButtonCancel.ts并在组件中使用
- **Then**: 组件逻辑封装在composable中，可独立测试和复用
- **Verification**: `human-judgment`
- **Notes**: 保持现有emit和props接口不变

### AC-5: useButtonScale创建
- **Given**: ButtonScale.vue没有对应的composable
- **When**: 创建composables/useButtonScale.ts并在组件中使用
- **Then**: 组件逻辑封装在composable中，可独立测试和复用
- **Verification**: `human-judgment`
- **Notes**: 保持现有emit和props接口不变

### AC-6: ARIA标签添加
- **Given**: UI组件缺少可访问性标签
- **When**: 为所有按钮组件添加aria-label、title等属性
- **Then**: 组件支持屏幕阅读器，可访问性提升
- **Verification**: `human-judgment`
- **Notes**: 使用合理的默认值，允许通过props覆盖

### AC-7: 规范符合性验证
- **Given**: 所有改进任务已完成
- **When**: 对照rule_ui_instructions.md进行全面检查
- **Then**: 合规性评分从70%提升到95%以上
- **Verification**: `human-judgment`
- **Notes**: 参照sideCard模块的实现方式

## Open Questions
- [ ] ButtonAction的具体用途是什么？是否需要重命名为ButtonSubmit或其他更具体的名称？
- [ ] 是否需要对ButtonAction进行重命名？
