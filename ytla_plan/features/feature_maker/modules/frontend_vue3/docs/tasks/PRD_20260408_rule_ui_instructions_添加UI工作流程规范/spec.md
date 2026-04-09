# UI工作流程规范添加 - Product Requirement Document

## Overview
- **Summary**: 在 rule_ui_instructions.md 文档中添加 AI 代理工作流程调整规范，包括 Planning Stage 的 UI 需求分析、ui_checklist.md 生成要求和 Action Stage 的核对清单使用规范
- **Purpose**: 规范 AI 代理在处理 UI 相关任务时的工作流程，确保在生成/重构 UI 组件时有明确的分析和核对机制
- **Target Users**: AI 代理、YTLA 项目的开发人员

## Goals
- 在 rule_ui_instructions.md 中添加 UI 工作流程调整章节
- 定义当读取到 rule_ui_instructions.md 时的特殊处理流程
- 规范 Planning Stage 中的 UI 需求分析步骤
- 定义 ui_checklist.md 的标准格式和内容要求
- 规范 Action Stage 中使用 ui_checklist.md 作为核对清单的要求

## Non-Goals (Out of Scope)
- 不修改 rule_ui_standards.md 文档
- 不修改 harness 规则文档
- 不添加新的 UI 组件规范内容

## Background & Context
- 刚刚完成了 UI 规范文档的拆分工作
- 现在需要进一步规范 AI 代理在处理 UI 相关任务时的工作流程
- 需要在 Planning Stage 增加 UI 需求分析，并在 Action Stage 前生成 ui_checklist.md
- ui_checklist.md 将作为 Action Stage 的核对清单

## Functional Requirements
- **FR-1**: 在 rule_ui_instructions.md 中添加 UI 工作流程调整章节
- **FR-2**: 定义当读取到 rule_ui_instructions.md 时的特殊处理流程
- **FR-3**: 规范 Planning Stage 中的 UI 需求分析步骤
- **FR-4**: 定义 ui_checklist.md 的标准格式和内容要求
- **FR-5**: 规范 Action Stage 中使用 ui_checklist.md 作为核对清单的要求

## Non-Functional Requirements
- **NFR-1**: 新增内容必须与现有文档风格保持一致
- **NFR-2**: ui_checklist.md 格式必须清晰、易用
- **NFR-3**: 工作流程规范必须可执行、可验证

## Constraints
- **Technical**: 只能修改 rule_ui_instructions.md 文档
- **Business**: 必须保持向后兼容，不影响现有规范的使用
- **Dependencies**: 依赖于 harness 规则文档的现有工作流程

## Assumptions
- AI 代理能够读取并理解新增的工作流程规范
- ui_checklist.md 的格式能够满足实际使用需求
- 在 Action Stage 使用 ui_checklist.md 作为核对清单是可行的

## Acceptance Criteria

### AC-1: rule_ui_instructions.md 中添加了 UI 工作流程调整章节
- **Given**: rule_ui_instructions.md 文档
- **When**: 查看文档内容
- **Then**: 文档中包含 UI 工作流程调整的章节
- **Verification**: `programmatic`
- **Notes**: 检查新增章节是否存在

### AC-2: 定义了读取 rule_ui_instructions.md 时的特殊处理流程
- **Given**: rule_ui_instructions.md 文档
- **When**: 查看新增章节内容
- **Then**: 文档中明确说明了当读取到 rule_ui_instructions.md 时的特殊处理流程
- **Verification**: `human-judgment`
- **Notes**: 检查流程说明是否清晰

### AC-3: 规范了 Planning Stage 中的 UI 需求分析步骤
- **Given**: rule_ui_instructions.md 文档
- **When**: 查看新增章节内容
- **Then**: 文档中明确说明了 Planning Stage 中结合目录分析用户 UI 实际需求的步骤
- **Verification**: `human-judgment`
- **Notes**: 检查分析步骤是否完整

### AC-4: 定义了 ui_checklist.md 的标准格式和内容要求
- **Given**: rule_ui_instructions.md 文档
- **When**: 查看新增章节内容
- **Then**: 文档中明确说明了 ui_checklist.md 应包含的信息：UI 生成形式、拟生成 UI 列表、需要重构的 UI 列表
- **Verification**: `human-judgment`
- **Notes**: 检查格式要求是否清晰

### AC-5: 规范了 Action Stage 中使用 ui_checklist.md 作为核对清单的要求
- **Given**: rule_ui_instructions.md 文档
- **When**: 查看新增章节内容
- **Then**: 文档中明确说明了在 Action Stage 应当将 ui_checklist.md 作为核对清单
- **Verification**: `human-judgment`
- **Notes**: 检查核对清单使用要求是否明确

## Open Questions
- 无
