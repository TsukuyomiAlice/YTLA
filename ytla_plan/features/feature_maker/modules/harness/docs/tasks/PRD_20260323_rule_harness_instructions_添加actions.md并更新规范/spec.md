# 更新 Harness 工程规范添加 actions.md - Product Requirement Document

## Overview
- **Summary**: 本项目旨在更新 YTLA Harness 工程规范文档，新增 actions.md 行动记录文档的规范定义，并调整 harness 模式的执行流程，增加 Start Stage 阶段。同时本次任务将按照更新后的规范执行，作为新规范的首次应用示例。
- **Purpose**: 解决当前 harness 模式缺少执行过程记录的问题，通过 actions.md 文档记录每一步的思考、目标、工具和文件操作，便于追溯和复盘。同时优化执行流程，明确 Start Stage 的职责。
- **Target Users**: YTLA 项目团队成员，特别是使用 harness 模式进行开发和文档维护的 AI 代理和人工审核人员。

## Goals
- 在 rule_harness_instructions.md 中新增 actions.md 的规范定义
- 定义 actions.md 的三个阶段结构（Start Stage, Planning Stage, Action Stage）
- 定义每个行动记录的格式（Thought, Target, Tool, Touches）
- 更新 harness 模式执行流程，增加 Start Stage
- 按照更新后的规范完整执行本次 spec 模式任务

## Non-Goals (Out of Scope)
- 不修改现有 origin.md, spec.md, tasks.md, checklist.md 的格式
- 不涉及除 rule_harness_instructions.md 以外的其他文档更新
- 不实现自动化 actions.md 记录功能（仅规范定义）
- 不修改 harness 模块的代码实现

## Background & Context
- 当前 harness 工程规范定义了 spec.md, tasks.md, checklist.md 等文档的格式，但缺少对执行过程的记录
- 用户在使用 harness 模式时需要能够追溯 AI 代理的思考过程和操作轨迹
- 现有规范中，PRD 目录的创建和文档生成没有明确的阶段划分，导致执行流程不够清晰
- 需要通过本次更新，使 harness 模式的执行过程更加透明和可追溯

## Functional Requirements
- **FR-1**: 在 rule_harness_instructions.md 中新增 actions.md 规范章节
- **FR-2**: 定义 actions.md 的三个阶段结构（Start Stage, Planning Stage, Action Stage）
- **FR-3**: 定义每个行动记录项的格式（ACT-[序号], Thought, Target, Tool, Touches）
- **FR-4**: 更新 harness 模式执行流程，明确 Start Stage 的职责和触发条件
- **FR-5**: 按照更新后的规范完整执行本次 spec 模式任务，生成 actions.md 文档

## Non-Functional Requirements
- **NFR-1**: actions.md 格式必须简洁明了，易于阅读和理解
- **NFR-2**: 执行流程的变更必须与现有规范兼容，不破坏现有功能
- **NFR-3**: 规范文档的更新必须保持风格一致，易于维护
- **NFR-4**: actions.md 必须能够完整记录从 Start Stage 到 Action Stage 的全过程

## Constraints
- **Technical**: 
  - 仅修改 Markdown 文档，不涉及代码变更
  - 必须遵循现有 rule_harness_instructions.md 的文档风格
- **Business**: 
  - 本次更新必须在当前 spec 模式任务中验证和应用
- **Dependencies**: 
  - 依赖现有 rule_harness_instructions.md 文档结构

## Assumptions
- 用户会按照更新后的规范使用 harness 模式
- AI 代理能够正确理解和执行新的规范要求
- actions.md 的手动记录方式在当前阶段是可接受的
- 本次作为首次应用，能够验证规范的可行性

## Acceptance Criteria

### AC-1: actions.md 规范章节已添加到 rule_harness_instructions.md
- **Given**: rule_harness_instructions.md 文档已存在
- **When**: 查看文档内容
- **Then**: 文档中包含关于 actions.md 的完整规范说明，包括三个阶段的定义和行动记录格式
- **Verification**: `human-judgment`
- **Notes**: 检查新增章节是否完整、格式是否正确

### AC-2: harness 模式执行流程已更新，包含 Start Stage
- **Given**: rule_harness_instructions.md 文档已更新
- **When**: 查看执行流程相关章节
- **Then**: 文档中明确说明了 Start Stage 的触发条件、职责和与 Planning Stage 的衔接
- **Verification**: `human-judgment`
- **Notes**: 检查流程更新是否清晰、逻辑是否合理

### AC-3: actions.md 文档已按规范生成
- **Given**: 本次 spec 模式任务已执行完成
- **When**: 查看 PRD 目录中的文件
- **Then**: 目录中包含 actions.md 文档，且文档包含三个阶段，每个阶段有完整的行动记录
- **Verification**: `programmatic`
- **Notes**: 验证文件存在，且结构符合规范

### AC-4: actions.md 中的行动记录完整
- **Given**: actions.md 文档已生成
- **When**: 查看文档内容
- **Then**: 每个行动记录项都包含 Thought, Target, Tool, Touches 四个要素，且内容真实反映执行过程
- **Verification**: `human-judgment`
- **Notes**: 检查记录是否完整、准确

### AC-5: 本次任务执行符合新规范
- **Given**: 本次 spec 模式任务已完成
- **When**: 回顾整个执行过程
- **Then**: 执行流程严格按照更新后的规范，从 Start Stage 开始，建立 PRD 目录后进入 Planning Stage
- **Verification**: `human-judgment`
- **Notes**: 验证执行流程是否符合新规范

## Open Questions
- 无
