# Vue3 UI 组件 AI 生成规范 - 产品需求文档

## Overview - 概要
本规范旨在为 YTLA 项目中的 Vue3 UI 组件（位于 `uis` 文件夹下的 `.vue` 组件）提供一套完整的 AI 生成规范。通过分析现有 sideCard 组件的实际结构和项目规范文档 rule.md，定义 UI 组件及其配套文件的命名规则、文件结构、代码模板、生成流程和验证标准，使 AI 能够按照统一规范生成高质量的 UI 组件代码。

## Goals - 目标
1. 提供清晰的 UI 组件命名规则，包括元件类型、命名约定和示例
2. 定义 UI 组件的标准文件结构，包括组件文件、组合式函数、样式文件、类型定义等配套文件
3. 提供可复用的代码模板和 AI 提示词，指导 AI 生成符合项目规范的代码
4. 建立验证清单，确保生成的组件符合项目质量和一致性要求
5. 基于现有 sideCard 组件实例和 rule.md 规范，确保新规范与项目现有标准兼容

## Non-Goals - 非目标（边界）
1. **不涵盖其他类型组件**：本规范仅适用于 `uis` 文件夹下的 UI 组件，不包含 `components`、`layouts`、`avatar` 等其他类型组件
2. **不涉及业务逻辑**：规范关注组件结构和代码风格，不涉及具体业务逻辑实现
3. **不替代人工审查**：规范提供自动生成指南，但最终代码仍需人工审查
4. **不覆盖项目整体架构**：仅针对 UI 组件级别，不涉及模块间通信、状态管理等高层架构

## Background & Context - 背景和上下文
- **现有规范**：项目已有 `rule.md` 文件定义了 Vue3 工程与文件规范，但未专门针对 UI 组件的 AI 生成提供详细指导
- **分析对象**：`sideCard` 组件是一个典型的 UI 组件集合，包含多个 `uis` 文件夹下的组件（如 `BarTitle.vue`、`ButtonPin.vue`）及其配套文件（composables、styles 等）
- **用户需求**：需要一套专门针对 UI 组件的 AI 生成规范，以提高代码生成的一致性和质量
- **参考文档**：`rule_harness_instructions.md` 提供了 harness 工程规范，本任务需按照该规范执行

## Functional Requirements - 功能需求
### FR-1: 规范文档结构
系统 SHALL 提供完整的规范文档结构，包含以下章节：
- 概述与适用范围
- 命名规则
- 文件结构与组织
- 代码模板与示例
- 生成流程与步骤
- AI 提示词模板
- 验证清单
- 附录（术语表、参考资源）

### FR-2: 详细命名规则
系统 SHALL 提供详细的 UI 组件命名规则，包括：
- 元件类型列表（Bar、Button、Container 等）
- 复合组合词命名规则（元件类型名+元件名+元件功能名）
- 命名示例和反例
- 文件命名约定（.vue、.ts、.scss 文件）

### FR-3: 完整配套文件规范
系统 SHALL 定义 UI 组件的完整配套文件，包括：
- `.vue` 组件文件（位于 `uis` 文件夹下，包含模板、脚本、样式）
- `.ts` 组合式函数文件（位于 `composables` 文件夹下，与 UI 组件相关）
- `.scss` 样式文件（位于 `styles` 文件夹下，与 UI 组件相关）

### FR-4: AI 提示词模板
系统 SHALL 提供完整的 AI 提示词模板，包括：
- 组件生成提示词（描述 UI 组件功能、props、事件等）
- 配套文件生成提示词（composable、样式）
- 验证和测试提示词

### FR-5: 基于现有实例的规范
系统 SHALL 基于 `sideCard` 组件的实际代码示例，确保规范符合项目现有实践

## Non-Functional Requirements - 非功能需求
### NFR-1: 可读性
规范文档 SHALL 易于理解和参考，使用清晰的语言和丰富的代码示例

### NFR-2: 一致性
规范 SHALL 与现有 `rule.md` 文档保持一致，不引入冲突的约定

### NFR-3: 实用性
规范 SHALL 提供实际可用的模板和示例，能够直接用于 AI 生成任务

### NFR-4: 可维护性
规范文档 SHALL 结构清晰，便于后续更新和维护

## Constraints - 约束条件
1. **技术栈约束**：必须基于 Vue 3 和 TypeScript，符合项目现有技术栈
2. **项目结构约束**：必须遵循 YTLA 项目的目录结构规范
3. **命名约束**：必须遵循现有的复合组合词命名规则
4. **代码风格约束**：必须使用 `<script setup>` 语法和组合式 API

## Assumptions - 假设
1. AI 生成工具能够理解并遵循本规范中的详细指导
2. 开发人员具备基本的 Vue 3 和 TypeScript 知识
3. 规范文档将作为 AI 生成 UI 组件的主要参考依据
4. sideCard 组件的实现代表了项目中的最佳实践

## Acceptance Criteria - 验收标准

### AC-1: 规范文档结构完整性
- **Given**: 规范文档已生成
- **When**: 审查文档结构
- **Then**: 文档应包含概述、命名规则、文件结构、代码模板、生成流程、AI 提示词、验证清单等所有要求的章节
- **Verification**: `human-judgment`
- **Notes**: 章节顺序可调整，但所有必需章节必须存在

### AC-2: 命名规则详细程度
- **Given**: 命名规则章节
- **When**: 检查命名规则内容
- **Then**: 应包含元件类型列表、复合组合词规则、至少 5 个正例和 2 个反例
- **Verification**: `human-judgment`
- **Notes**: 示例应基于 sideCard 组件中的实际组件

### AC-3: 配套文件覆盖度
- **Given**: 文件结构章节
- **When**: 检查配套文件描述
- **Then**: 应明确说明 .vue、.ts（composable）、.scss、.ts（类型定义）文件的组织方式和命名规则
- **Verification**: `human-judgment`
- **Notes**: 应引用 sideCard 组件中的实际文件作为示例

### AC-4: AI 提示词实用性
- **Given**: AI 提示词章节
- **When**: 检查提示词模板
- **Then**: 应提供至少 2 个完整的 UI 组件生成提示词示例，涵盖不同元件类型
- **Verification**: `human-judgment`
- **Notes**: 提示词应包含明确的输入要求和输出格式

### AC-5: 与现有规范一致性
- **Given**: 生成的规范文档
- **When**: 对比现有 rule.md 文档
- **Then**: 不应与 rule.md 中的现有规范冲突，且应明确引用相关部分
- **Verification**: `human-judgment`
- **Notes**: 可扩展但不能 contradict 现有规范

### AC-6: 基于 sideCard 实例
- **Given**: 规范文档中的示例
- **When**: 检查示例来源
- **Then**: 至少 70% 的示例应来自 sideCard 组件的实际代码
- **Verification**: `programmatic`
- **Notes**: 可通过文件路径引用验证

## Open Questions - 待解决问题
1. 是否需要在规范中定义组件的测试文件生成规则？
2. 是否要包含国际化（locales）和可访问性（ARIA）的生成指导？
3. 规范文档的版本管理机制如何与现有文档体系集成？

spec mode logging