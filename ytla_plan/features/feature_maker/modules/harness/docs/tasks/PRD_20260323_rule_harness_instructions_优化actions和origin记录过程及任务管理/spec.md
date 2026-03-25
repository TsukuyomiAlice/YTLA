# Harness 工程规范优化 - Product Requirement Document

## Overview
- **Summary**: 本次项目旨在改进和优化 harness 工程中对 actions.md 和 origin.md 文档的记录过程，提升任务管理和文档记录的效率与准确性。
- **Purpose**: 解决当前文档记录过程中的问题，包括：AI 追问未记录、文档更新采用覆盖写入而非追加、PRD 文档检索缺乏明确标志、任务完成判定不够灵活等。
- **Target Users**: 使用 harness 工程规范的 AI 代理和开发人员。

## Goals
- 确保 AI 向用户发起追问的操作在执行前被正确记录到 actions.md
- 优化文档更新方式，对 actions.md 和 origin.md 采用追加写入而非覆盖
- 在 tasks.md 第一行添加任务进度标记，方便 Start Stage 检索判断
- 调整任务完成依据，改为 AI 主动询问用户确认完成
- 完善 actions.md 的记录规范，确保所有重要操作都被记录

## Non-Goals (Out of Scope)
- 不修改除 rule_harness_instructions.md 以外的其他文档
- 不重构现有代码结构
- 不添加新的功能模块

## Background & Context
- 当前 harness 工程规范中，actions.md 和 origin.md 的更新方式主要采用覆盖写入，容易造成版本混淆
- 缺乏明确的 PRD 任务完成状态标记，导致 Start Stage 检索时判断不准确
- AI 向用户发起追问的操作未被记录，导致行动记录不完整
- 任务完成判定机制不够灵活，需要调整为以用户确认为准

## Functional Requirements
- **FR-1**: AI 发起用户追问前，必须将该操作记录到 actions.md
- **FR-2**: 更新 actions.md 和 origin.md 时，采用在文件末尾追加的方式，而非覆盖写入
- **FR-3**: tasks.md 第一行必须包含 "本任务进度: [已完成/未完成]" 标记
- **FR-4**: 任务执行完毕时，AI 必须主动询问用户确认任务是否完成
- **FR-5**: 用户确认完成后，更新 tasks.md 第一行标记为 "已完成"

## Non-Functional Requirements
- **NFR-1**: 所有文档修改必须保持向后兼容
- **NFR-2**: 规范说明必须清晰明确，易于理解和执行
- **NFR-3**: 文档记录过程必须保持可追溯性

## Constraints
- **Technical**: 仅修改 rule_harness_instructions.md 文档
- **Business**: 必须保持与现有 harness 工作流程的兼容性
- **Dependencies**: 依赖 rule_harness_instructions.md 文档的现有结构

## Assumptions
- 用户在任务执行完毕时能够正确确认是否完成
- 追加写入方式不会影响文档的可读性
- Start Stage 能够正确解析 tasks.md 第一行的进度标记

## Acceptance Criteria

### AC-1: AI 追问操作记录
- **Given**: AI 准备向用户发起追问
- **When**: AI 执行追问操作
- **Then**: 在提问之前，该操作已被记录到 actions.md
- **Verification**: `human-judgment`
- **Notes**: 记录格式应符合 actions.md 的标准 ACT- 格式

### AC-2: 文档追加写入
- **Given**: 需要更新 actions.md 或 origin.md
- **When**: 执行文档更新操作
- **Then**: 新内容直接追加到文件末尾，而非覆盖整个文件
- **Verification**: `human-judgment`
- **Notes**: 但初始创建或完全重写规划文档时仍可使用覆盖写入

### AC-3: tasks.md 进度标记
- **Given**: 新创建或更新的 tasks.md 文档
- **When**: 查看 tasks.md 第一行
- **Then**: 第一行必须包含 "本任务进度: [已完成/未完成]" 标记
- **Verification**: `programmatic`
- **Notes**: 新任务初始状态为 "未完成"

### AC-4: 任务完成确认流程
- **Given**: 所有任务已执行完毕
- **When**: AI 准备结束任务
- **Then**: AI 主动向用户发起提问，确认任务是否全部完成
- **Verification**: `human-judgment`
- **Notes**: 只有用户明确确认后，才执行最终完成步骤

### AC-5: 用户确认后更新状态
- **Given**: 用户确认任务已完成
- **When**: 执行最终完成步骤
- **Then**: tasks.md 第一行更新为 "本任务进度: 已完成"，并记录用户确认到 actions.md
- **Verification**: `human-judgment`

## Open Questions
- [ ] 是否需要为其他规划文档也添加进度标记？
- [ ] 追加写入时是否需要添加特定的分隔符来区分不同阶段的内容？
