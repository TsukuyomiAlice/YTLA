# sideCardEditor ButtonCancel和ButtonScale组件重构规范化 - Product Requirement Document

## Overview
- **Summary**: 对sideCardEditor模块中的ButtonCancel和ButtonScale组件进行重构，使其完全符合rule_ui_instructions.md和rule_ui_standards.md规范，实现关注点分离原则。根据最新规则，composables文件中不应包含类型定义，类型定义应该移到definitions目录。
- **Purpose**: 解决ButtonCancel.vue和ButtonScale.vue中存在的不符合规范问题，包括：Vue文件中包含computed属性定义、composables文件中包含类型定义，确保代码结构统一、可维护性提升。
- **Target Users**: YTLA项目开发团队

## Goals
- 为ButtonCancel和ButtonScale创建完整的definitions类型定义文件
- 将Vue文件中的computed属性移动到对应的composables文件
- 将composables文件中的类型定义移动到definitions目录
- 重构Vue文件使其仅负责视图（模板、导入语句、样式导入）
- 确保所有组件符合关注点分离原则
- 保持现有功能完全向后兼容
- 参照ButtonAction的实现方式

## Non-Goals (Out of Scope)
- 不修改组件的现有功能和行为
- 不重构ButtonAction组件（已完成重构）
- 不修改其他非UI组件（layouts、factories、stores等）
- 不涉及样式代码的修改（仅移动样式导入）

## Background & Context
- **项目结构**: sideCardEditor模块已有初步的UI组件结构，ButtonAction组件已完成规范化重构
- **现有规范**: rule_ui_instructions.md和rule_ui_standards.md定义了完整的UI组件生成和重构规范
- **最新规则调整**（关键！）：composables文件中不应包含类型定义内容，类型定义应正确地移到definitions目录
- **当前状态**: 
  - ButtonCancel.vue和ButtonScale.vue已有对应的composables和styles文件
  - 但Vue文件中仍包含computed属性定义
  - composables文件中包含类型定义（不符合最新规则）
- **技术栈**: Vue 3 + TypeScript + SCSS + Composition API
- **参照实现**: ButtonAction组件已经是正确的实现方式

## Functional Requirements
- **FR-1**: 创建ButtonCancelType.ts类型定义文件，包含ButtonCancelProps、ButtonCancelEmits、ButtonCancelOptions
- **FR-2**: 重构useButtonCancel.ts，移除类型定义，从definitions导入类型
- **FR-3**: 重构ButtonCancel.vue，从definitions导入类型，移除Vue文件中的computed属性定义
- **FR-4**: 创建ButtonScaleType.ts类型定义文件，包含ButtonScaleProps、ButtonScaleEmits
- **FR-5**: 重构useButtonScale.ts，移除类型定义，从definitions导入类型
- **FR-6**: 重构ButtonScale.vue，从definitions导入类型，移除Vue文件中的computed属性定义

## Non-Functional Requirements
- **NFR-1**: 所有重构必须保持100%向后兼容
- **NFR-2**: TypeScript类型检查必须无错误
- **NFR-3**: 代码必须符合项目编码规范
- **NFR-4**: 重构后的组件必须通过所有现有测试
- **NFR-5**: 实现方式必须与ButtonAction保持一致

## Constraints
- **Technical**: 必须使用Vue 3 Composition API、TypeScript、SCSS
- **Business**: 必须在不破坏现有功能的前提下完成
- **Dependencies**: 依赖于rule_ui_instructions.md和rule_ui_standards.md规范
- **参照实现**: 必须参照ButtonAction的实现方式

## Assumptions
- 现有的composables文件功能正确
- 现有的样式文件可以直接使用
- 没有调用方依赖于Vue文件中的内部实现细节
- i18n处理保持不变

## Acceptance Criteria

### AC-1: ButtonCancelType.ts创建成功
- **Given**: sideCardEditor模块存在
- **When**: 创建definitions/ButtonCancelType.ts文件
- **Then**: 文件包含ButtonCancelProps、ButtonCancelEmits、ButtonCancelOptions完整类型定义
- **Verification**: `programmatic`
- **Notes**: 保持接口完全向后兼容，参照ButtonActionType.ts的实现方式

### AC-2: useButtonCancel.ts重构完成
- **Given**: ButtonCancelType.ts已创建
- **When**: 重构composables/useButtonCancel.ts
- **Then**: 从definitions导入类型，移除composables中的类型定义，包含所有计算属性和方法
- **Verification**: `programmatic`
- **Notes**: 保持现有功能不变，参照useButtonAction.ts的实现方式

### AC-3: ButtonCancel.vue重构完成
- **Given**: ButtonCancelType.ts和useButtonCancel.ts已就绪
- **When**: 重构ui/ButtonCancel.vue
- **Then**: 从definitions导入类型，Vue文件仅包含模板、导入语句和样式导入，无直接定义的computed或methods
- **Verification**: `human-judgment`

### AC-4: ButtonScaleType.ts创建成功
- **Given**: sideCardEditor模块存在
- **When**: 创建definitions/ButtonScaleType.ts文件
- **Then**: 文件包含ButtonScaleProps和ButtonScaleEmits完整类型定义
- **Verification**: `programmatic`
- **Notes**: 保持接口完全向后兼容，参照ButtonActionType.ts的实现方式

### AC-5: useButtonScale.ts重构完成
- **Given**: ButtonScaleType.ts已创建
- **When**: 重构composables/useButtonScale.ts
- **Then**: 从definitions导入类型，移除composables中的类型定义，包含所有计算属性和方法
- **Verification**: `programmatic`
- **Notes**: 保持现有功能不变，参照useButtonAction.ts的实现方式

### AC-6: ButtonScale.vue重构完成
- **Given**: ButtonScaleType.ts和useButtonScale.ts已就绪
- **When**: 重构ui/ButtonScale.vue
- **Then**: 从definitions导入类型，Vue文件仅包含模板、导入语句和样式导入，无直接定义的computed或methods
- **Verification**: `human-judgment`

### AC-7: TypeScript类型检查通过
- **Given**: 所有重构完成
- **When**: 运行TypeScript编译检查
- **Then**: 无类型错误，所有导入路径正确解析
- **Verification**: `programmatic`

## Open Questions
- 无
