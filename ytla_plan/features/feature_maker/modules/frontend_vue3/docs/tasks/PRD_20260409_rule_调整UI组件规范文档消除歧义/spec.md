# 调整 UI 组件规范文档消除歧义 - Product Requirement Document

## Overview
- **Summary**: 修改 rule_ui_instructions.md 和 rule_ui_standards.md 两份文档，明确区分两种 UI 组件使用场景，消除之前导致的歧义
- **Purpose**: 解决之前对 sideCard 模块 UI 组件的误解，通过完善文档说明，让 AI 代理和开发者能够准确理解规范的意图
- **Target Users**: AI 代理、开发者

## Goals
- 明确区分两种 UI 组件使用场景
- 在文档中添加清晰的场景说明和示例
- 确保文档表述准确、无歧义
- 提供判断指南，帮助读者确定何时使用哪种模式

## Non-Goals (Out of Scope)
- 不修改任何实际代码（仅修改文档）
- 不改变规范的核心原则
- 不重构任何 UI 组件

## Background & Context
- 之前在检查 sideCard 模块 UI 组件时，AI 代理误解了规范文档的意图
- 用户澄清了规范的原意：存在两种不同的 UI 组件使用场景
- 需要在文档中明确补充这些说明，避免未来再次发生类似误解

## Functional Requirements
- **FR-1**: 在 rule_ui_instructions.md 中添加两种 UI 组件使用场景的明确说明
- **FR-2**: 在 rule_ui_standards.md 中添加两种 UI 组件使用场景的明确说明
- **FR-3**: 在文档中提供 sideCard 模块类似场景的示例
- **FR-4**: 在文档中提供独立 UI 组件场景的示例
- **FR-5**: 添加判断指南，帮助确定何时使用哪种模式

## Non-Functional Requirements
- **NFR-1**: 文档修改应保持向后兼容，不改变现有规范的核心含义
- **NFR-2**: 新增说明应清晰、易懂、无歧义
- **NFR-3**: 示例应具体、真实，能够准确反映项目中的实际情况

## Constraints
- **Technical**: 仅修改 markdown 文档，不涉及代码变更
- **Business**: 必须保持现有规范的核心原则不变
- **Dependencies**: 无外部依赖

## Assumptions
- 假设用户澄清的两种使用场景是正确的规范原意
- 假设文档的其他部分不需要修改
- 假设修改后的文档能够被 AI 代理和开发者准确理解

## Acceptance Criteria

### AC-1: rule_ui_instructions.md 添加两种场景说明
- **Given**: rule_ui_instructions.md 文档存在
- **When**: 完成文档修改
- **Then**: 文档中包含两种 UI 组件使用场景的明确说明
- **Verification**: `human-judgment`
- **Notes**: 说明应清晰区分两种场景的特点和适用条件

### AC-2: rule_ui_standards.md 添加两种场景说明
- **Given**: rule_ui_standards.md 文档存在
- **When**: 完成文档修改
- **Then**: 文档中包含两种 UI 组件使用场景的明确说明
- **Verification**: `human-judgment`
- **Notes**: 说明应与 rule_ui_instructions.md 保持一致

### AC-3: 提供 sideCard 模块类似场景的示例
- **Given**: 文档修改完成
- **When**: 阅读文档
- **Then**: 文档中包含类似 sideCard 模块这种"UI 作为主组件子组件"场景的具体示例
- **Verification**: `human-judgment`
- **Notes**: 示例应展示 UI 组件如何直接使用主组件的 props 和 emits

### AC-4: 提供独立 UI 组件场景的示例
- **Given**: 文档修改完成
- **When**: 阅读文档
- **Then**: 文档中包含"UI 作为独立组件"场景的具体示例
- **Verification**: `human-judgment`
- **Notes**: 示例应展示 UI 组件如何使用自己的 composable 和定义接口

### AC-5: 添加判断指南
- **Given**: 文档修改完成
- **When**: 需要确定使用哪种模式
- **Then**: 文档中包含清晰的判断指南，帮助读者确定何时使用哪种模式
- **Verification**: `human-judgment`
- **Notes**: 指南应提供具体的判断标准和问题

## Open Questions
- [ ] 是否需要更新文档版本号？
- [ ] 是否需要在文档中记录本次修改的变更历史？
