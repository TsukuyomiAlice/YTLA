# sideCardEditor UI组件规范修复 - Product Requirement Document

## Overview
- **Summary**: 修复sideCardEditor目录下UI组件的规范问题，包括导入语句、Props定义、类型定义位置、样式导入等方面的问题
- **Purpose**: 确保所有UI组件完全符合项目的UI组件规范，实现关注点分离和代码一致性
- **Target Users**: 开发团队、代码维护者

## Goals
- 修复ButtonCancel.vue的导入语句、Props定义和参数传递问题
- 移除useButtonCancel.ts和useButtonScale.ts中的内部接口定义
- 规范useButtonScale.ts的emit类型定义
- 修复ButtonScale.vue的样式导入问题
- 确保所有组件与ButtonAction的实现方式保持一致

## Non-Goals (Out of Scope)
- 不修改组件的功能逻辑
- 不修改组件的模板结构
- 不修改组件的样式内容
- 不添加新功能

## Background & Context
- sideCardEditor目录下已有ButtonAction、ButtonCancel、ButtonScale三个UI组件
- ButtonAction已经符合规范，可以作为参考
- 之前的PRD虽然标记为"已完成"，但实际文件仍存在规范问题
- 需要参照rule_ui_instructions.md和rule_ui_standards.md进行修复

## Functional Requirements
- **FR-1**: 修复ButtonCancel.vue的导入语句（移除.ts后缀）
- **FR-2**: 修复ButtonCancel.vue的Props定义（移除冗余定义）
- **FR-3**: 修复ButtonCancel.vue的参数传递（只传递props和emit）
- **FR-4**: 移除useButtonCancel.ts中的UseButtonCancelReturn接口定义
- **FR-5**: 移除useButtonScale.ts中的UseButtonScaleReturn接口定义
- **FR-6**: 规范useButtonScale.ts的emit类型定义（从definitions导入）
- **FR-7**: 修复ButtonScale.vue的样式导入（移除as *）

## Non-Functional Requirements
- **NFR-1**: 所有修改必须保持向后兼容
- **NFR-2**: TypeScript类型检查必须通过
- **NFR-3**: 代码风格必须与ButtonAction保持一致
- **NFR-4**: 所有功能必须正常工作

## Constraints
- **Technical**: Vue 3 + TypeScript + SCSS
- **Business**: 必须遵循项目UI组件规范
- **Dependencies**: 参照ButtonAction的实现方式

## Assumptions
- 组件的现有功能逻辑是正确的
- 只需要修复规范问题，不需要修改功能
- 所有调用方不会受到影响

## Acceptance Criteria

### AC-1: ButtonCancel.vue导入语句修复
- **Given**: ButtonCancel.vue文件存在
- **When**: 检查导入语句
- **Then**: 导入useButtonCancel时不包含.ts后缀
- **Verification**: `programmatic`

### AC-2: ButtonCancel.vue Props定义修复
- **Given**: ButtonCancel.vue文件存在
- **When**: 检查Props定义
- **Then**: 直接使用ButtonCancelProps，没有冗余定义
- **Verification**: `programmatic`

### AC-3: ButtonCancel.vue参数传递修复
- **Given**: ButtonCancel.vue文件存在
- **When**: 检查useButtonCancel调用
- **Then**: 只传递props和emit两个参数
- **Verification**: `programmatic`

### AC-4: useButtonCancel.ts移除内部接口
- **Given**: useButtonCancel.ts文件存在
- **When**: 检查文件内容
- **Then**: 没有UseButtonCancelReturn接口定义
- **Verification**: `programmatic`

### AC-5: useButtonScale.ts移除内部接口
- **Given**: useButtonScale.ts文件存在
- **When**: 检查文件内容
- **Then**: 没有UseButtonScaleReturn接口定义
- **Verification**: `programmatic`

### AC-6: useButtonScale.ts emit类型规范
- **Given**: useButtonScale.ts文件存在
- **When**: 检查emit参数类型
- **Then**: 从definitions导入ButtonScaleEmits类型
- **Verification**: `programmatic`

### AC-7: ButtonScale.vue样式导入修复
- **Given**: ButtonScale.vue文件存在
- **When**: 检查样式导入
- **Then**: 不使用as *语法
- **Verification**: `programmatic`

### AC-8: TypeScript类型检查通过
- **Given**: 所有修复完成
- **When**: 运行TypeScript编译检查
- **Then**: 没有类型错误
- **Verification**: `programmatic`

## Open Questions
- 无
