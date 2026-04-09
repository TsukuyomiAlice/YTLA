# SideCardFilter UI组件重构 - Product Requirement Document（修正版）

## Overview
- **Summary**: 对sideCardFilter模块ui目录下的UI组件进行重构，使其符合项目统一的UI组件规范，包括命名规范、关注点分离等，仅关注规范范围内的内容
- **Purpose**: 解决sideCardFilter模块ui目录下现有UI组件不符合规范的问题，提高代码质量和可维护性
- **Target Users**: 开发团队维护人员

## Goals
- 将ui目录下的UI组件重命名为符合规范的名称
- 实现关注点分离，确保UI组件中的i18n使用通过props接收
- 为UI组件添加相应的composables文件
- 完善样式文件

## Non-Goals (Out of Scope)
- 不修改avatar目录下的文件
- 不修改locales目录下的文件
- 不修改layouts目录下的文件（布局文件）
- 不修改主组件的composables（useSideCardFilter.ts）
- 不修改主组件的类型定义（sideCardFilterType.ts）
- 不修改功能逻辑，仅进行代码结构和规范调整

## Background & Context
- sideCardFilter模块位于ytla_plan_vue项目中
- 项目有明确的UI组件规范文档（rule_ui_instructions.md、rule_ui_standards.md）
- 规范范围仅限于：ui目录下的Vue文件、相关的composables和styles文件
- 现有ui目录下的代码存在命名不规范、使用i18n等问题
- 需要按照Harness工程规范进行重构

## Functional Requirements
- **FR-1**: 重命名UI组件 ButtonClear.vue 为 ButtonFilterClear.vue
- **FR-2**: 重命名UI组件 FilterInput.vue 为 BarFilterInput.vue
- **FR-3**: 移除UI组件中的i18n使用，通过props接收文本
- **FR-4**: 为UI组件添加相应的composables文件
- **FR-5**: 完善样式文件

## Non-Functional Requirements
- **NFR-1**: 重构后的代码必须通过TypeScript类型检查
- **NFR-2**: 重构后功能保持不变
- **NFR-3**: 代码结构清晰，符合项目规范

## Constraints
- **Technical**: Vue 3 + TypeScript + SCSS
- **Business**: 保持向后兼容性
- **Dependencies**: 布局组件（layouts/SideCardFilter.vue）需要相应调整以适配新的UI组件

## Assumptions
- 现有功能逻辑是正确的
- 不需要修改业务逻辑，仅调整代码结构
- 布局组件（layouts/SideCardFilter.vue）需要调用方相应调整

## Acceptance Criteria

### AC-1: UI组件重命名完成
- **Given**: sideCardFilter模块ui目录下存在不符合命名规范的UI组件
- **When**: 执行重构任务
- **Then**: ButtonClear.vue 重命名为 ButtonFilterClear.vue，FilterInput.vue 重命名为 BarFilterInput.vue
- **Verification**: `programmatic`
- **Notes**: 检查文件是否存在且命名正确

### AC-2: UI组件移除i18n使用
- **Given**: UI组件中直接使用了i18n
- **When**: 执行重构任务
- **Then**: UI组件通过props接收文本，不再直接使用 $t()
- **Verification**: `programmatic`
- **Notes**: 检查UI组件代码是否移除了i18n调用

### AC-3: Composables文件添加完成
- **Given**: UI组件缺少相应的composables文件
- **When**: 执行重构任务
- **Then**: 为ButtonFilterClear和BarFilterInput添加相应的composables文件
- **Verification**: `programmatic`
- **Notes**: 检查composables文件是否存在且符合规范

### AC-4: 样式文件完善
- **Given**: 样式文件不完整
- **When**: 执行重构任务
- **Then**: 样式文件包含所有必要的样式定义
- **Verification**: `human-judgment`
- **Notes**: 人工检查样式文件是否完整

## Open Questions
- [ ] 是否需要保持向后兼容性（提供旧组件名称的别名）？
