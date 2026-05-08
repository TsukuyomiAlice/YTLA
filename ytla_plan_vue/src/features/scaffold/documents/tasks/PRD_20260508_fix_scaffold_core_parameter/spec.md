# Scaffold Core 参数修复 - Product Requirement Document

## Overview
- **Summary**: 修复脚手架创建时的参数传递逻辑，当选择Core模块时正确映射参数，并相应修改UI标签
- **Purpose**: 解决前端向后端发送请求时对请求内容的误解，确保Core模块类型的脚手架能正确生成
- **Target Users**: 项目开发者、模块创建者

## Goals
- 修复Core模块选择时的参数传递逻辑
- 根据Core/Feature选择动态修改UI标签
- 保持Feature模块的现有行为不变
- 确保整个修改不影响后端

## Non-Goals (Out of Scope)
- 不修改后端API
- 不修改Feature模块的参数传递逻辑
- 不添加新功能

## Background & Context
- 当前脚手架在选择Core模块时，参数传递逻辑有误
- 当is_core为True时，type_name应固定为'classic'（版本名），用户输入的类型名称应传递给structure参数
- UI需要相应调整：Core模块时显示"模块名称"，Feature模块时显示"类型名称"

## Functional Requirements
- **FR-1**: 修复create_card模块的参数传递逻辑
  - 当isCore为true时，typeName设为'classic'，structure设为用户输入的类型名称
  - 当isCore为false时，保持现有行为不变
- **FR-2**: 修复create_module模块的参数传递逻辑
  - 同上
- **FR-3**: 动态修改UI标签
  - Core模块：显示"模块名称"
  - Feature模块：显示"类型名称"

## Non-Functional Requirements
- **NFR-1**: 保持现有UI/UX的一致性
- **NFR-2**: 代码修改最小化，不引入额外复杂性
- **NFR-3**: TypeScript类型安全

## Constraints
- **Technical**: 必须使用现有的Vue 3 + TypeScript + Pinia架构
- **Business**: 必须与后端API保持兼容
- **Dependencies**: 不依赖任何新的外部库

## Assumptions
- 后端API保持不变
- 现有Feature模块的参数传递是正确的

## Acceptance Criteria

### AC-1: Core模块参数传递正确
- **Given**: 用户选择Core模块并填写表单
- **When**: 用户提交表单
- **Then**: 发送到后端的请求中type_name为'classic'，structure为用户输入的内容，sub_type_name不变
- **Verification**: programmatic

### AC-2: Feature模块参数传递不变
- **Given**: 用户选择Feature模块并填写表单
- **When**: 用户提交表单
- **Then**: 发送到后端的请求保持现有行为不变
- **Verification**: programmatic

### AC-3: UI标签根据选择动态变化
- **Given**: 用户在表单上进行操作
- **When**: 用户选择Core模块
- **Then**: 标签显示为"模块名称"
- **Verification**: human-judgment

### AC-4: UI标签根据选择动态变化
- **Given**: 用户在表单上进行操作
- **When**: 用户选择Feature模块
- **Then**: 标签显示为"类型名称"
- **Verification**: human-judgment

### AC-5: 两个模块(create_card和create_module)都正常工作
- **Given**: 用户使用任一模块
- **When**: 用户完成操作
- **Then**: 所有功能正常
- **Verification**: human-judgment

## Open Questions
- 无
