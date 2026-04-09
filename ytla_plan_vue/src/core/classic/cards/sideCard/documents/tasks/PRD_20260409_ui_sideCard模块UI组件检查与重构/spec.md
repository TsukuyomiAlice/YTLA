# sideCard 模块 UI 组件检查与重构 - Product Requirement Document

## Overview
- **Summary**: 对 sideCard 模块的所有 UI 组件进行全面检查，识别不符合 UI 组件规范的部分，并进行重构，确保所有组件都遵循关注点分离、命名规范和架构标准。
- **Purpose**: 提高代码质量、可维护性和可复用性，让 sideCard 模块的 UI 组件符合项目统一的架构规范。
- **Target Users**: 开发团队成员、维护人员

## Goals
- 全面检查 sideCard 模块的所有 UI 组件
- 识别不符合规范的组件和代码结构
- 重构不符合规范的组件，实现关注点分离
- 确保所有组件遵循命名规范和架构标准
- 保持向后兼容性，避免破坏性变更

## Non-Goals (Out of Scope)
- 不修改 components 目录下的主组件
- 不修改 layouts 目录下的布局组件
- 不修改 avatar 目录下的图标组件
- 不修改 locales、services、stores、factories 等非 UI 相关模块
- 不添加新功能，仅重构现有代码结构

## Background & Context
- sideCard 模块已有完整的 UI 组件体系，包括 ui/ 目录下的多个 Vue 组件
- 项目已建立了完善的 UI 组件规范（rule_ui_instructions.md、rule_ui_standards.md）
- 当前部分组件可能未完全遵循关注点分离原则
- 需要重构让 Vue 文件仅负责视图，逻辑在 composables 的 TS 文件中实现

## Functional Requirements
- **FR-1**: 检查所有 ui/ 目录下的 Vue 组件是否符合规范
- **FR-2**: 识别需要重构的组件（关注点未分离、命名不规范等）
- **FR-3**: 重构不符合规范的组件，实现关注点分离
- **FR-4**: 确保重构后的组件与现有调用方兼容

## Non-Functional Requirements
- **NFR-1**: 重构后的组件必须保持功能不变
- **NFR-2**: 重构后的组件必须通过 TypeScript 类型检查
- **NFR-3**: 重构过程中保持 git 历史记录完整
- **NFR-4**: 重构后的代码结构清晰、易读易懂

## Constraints
- **Technical**: Vue 3 + TypeScript + SCSS + Composition API
- **Business**: 必须在现有代码基础上重构，不能引入新功能
- **Dependencies**: 依赖项目现有的 UI 组件规范文档

## Assumptions
- 现有组件的功能是正确的，只需重构结构
- 所有调用方都能适应重构后的组件接口
- 项目有完整的测试覆盖来验证功能正确性

## Acceptance Criteria

### AC-1: 所有UI组件检查完成
- **Given**: sideCard 模块的所有 UI 组件
- **When**: 完成所有组件的规范检查
- **Then**: 有完整的检查报告，明确哪些组件符合规范，哪些需要重构
- **Verification**: `human-judgment`
- **Notes**: 检查报告应记录每个组件的状态

### AC-2: 关注点分离实现
- **Given**: 需要重构的 UI 组件
- **When**: 完成重构后
- **Then**: Vue 文件仅包含模板、导入语句和样式导入，所有逻辑在 composables 的 TS 文件中
- **Verification**: `programmatic`
- **Notes**: 检查 Vue 文件中是否包含业务逻辑、响应式数据定义等

### AC-3: 命名规范符合要求
- **Given**: 所有 UI 组件文件
- **When**: 完成检查和重构后
- **Then**: 所有文件命名符合规范（PascalCase for .vue, useCamelCase for .ts, kebab-case for .scss）
- **Verification**: `programmatic`
- **Notes**: 组件名应符合"元件类型+功能描述"模式

### AC-4: 向后兼容性保持
- **Given**: 重构后的组件
- **When**: 现有调用方使用重构后的组件
- **Then**: 所有调用方都能正常工作，无需修改
- **Verification**: `programmatic`
- **Notes**: 如必要，提供过渡期兼容层

### AC-5: 样式文件正确关联
- **Given**: 重构后的组件
- **When**: 检查样式导入
- **Then**: Vue 文件仅导入样式文件，不包含具体样式代码
- **Verification**: `programmatic`
- **Notes**: 所有样式代码在 styles 目录的 SCSS 文件中

### AC-6: TypeScript 类型安全
- **Given**: 重构后的组件
- **When**: 运行 TypeScript 类型检查
- **Then**: 没有类型错误，所有 Props、Emits 都有完整的类型定义
- **Verification**: `programmatic`
- **Notes**: 使用 import type 导入纯类型

## Open Questions
- [ ] 是否需要为重构提供过渡期兼容层？
- [ ] 是否需要更新文档以反映重构后的变化？
