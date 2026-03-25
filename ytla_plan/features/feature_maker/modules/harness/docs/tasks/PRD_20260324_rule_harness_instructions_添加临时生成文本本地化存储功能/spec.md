# Harness 临时文本存储优化 - Product Requirement Document

## Overview
- **Summary**: 为 Harness 工程规范添加临时生成文本的本地化存储功能，包括规范临时文件命名、在 actions.md 中添加过程文件列表章节、以及更新相关操作指南
- **Purpose**: 解决 AI 生成大规模临时文本的存储和管理问题，通过标准化的存储方式和记录机制，保持对话上下文的整洁，同时保留过程文件的可追溯性
- **Target Users**: 使用 Harness 模式的 AI 代理

## Goals
- 定义临时生成文本的存储位置和命名规范
- 在 actions.md 中新增过程文件列表章节
- 明确过程文件列表的更新规则
- 更新文档版本信息

## Non-Goals (Out of Scope)
- 修改现有的 PRD 目录结构规范
- 修改 origin.md、spec.md、tasks.md、checklist.md 的现有规范
- 添加文件管理和清理功能

## Background & Context
- 当前 Harness 模式已经有完善的规划文档管理规范，但缺少对临时生成文本的管理机制
- AI 在执行任务过程中可能会生成大规模的分析文本、中间结果等，这些内容不属于最终目标文件，但可能有保存价值
- 需要一个标准化的机制来存储这些临时文件，并在 actions.md 中进行记录

## Functional Requirements
- **FR-1**: 定义临时生成文本文件的存储位置和命名规范
- **FR-2**: 在 actions.md 中新增 "Generated Procedure Files List  过程文件列表" 章节
- **FR-3**: 明确过程文件列表的更新方法和时机
- **FR-4**: 更新文档版本号和最后更新日期

## Non-Functional Requirements
- **NFR-1**: 规范应与现有文档风格保持一致
- **NFR-2**: 临时文件命名应清晰可识别
- **NFR-3**: 过程文件列表应便于维护和更新

## Constraints
- **Technical**: 仅修改 rule_harness_instructions.md 文档
- **Business**: 保持与现有规范的向后兼容性
- **Dependencies**: 依赖现有的 actions.md 规范和 PRD 目录结构

## Assumptions
- 临时文件只存储在 PRD 目录下
- 临时文件以 temp_ 开头，AI 可以自行设计合适的标题
- 过程文件列表只记录文件名，不包含路径
- 每次新生成临时文件时都需要更新过程文件列表

## Acceptance Criteria

### AC-1: 临时文件存储和命名规范
- **Given**: AI 需要生成大规模临时文本
- **When**: AI 创建临时文本文件
- **Then**: 文件存储在 PRD 目录下，命名格式为 temp_[AI自行设计标题].md
- **Verification**: `human-judgment`
- **Notes**: 标题应能反映文件内容

### AC-2: actions.md 新增过程文件列表章节
- **Given**: actions.md 文档结构
- **When**: 更新 rule_harness_instructions.md 规范
- **Then**: 规范中明确要求在 actions.md 中新增 "Generated Procedure Files List  过程文件列表" 章节
- **Verification**: `human-judgment`

### AC-3: 过程文件列表更新规则
- **Given**: 新生成的临时文件
- **When**: AI 生成新的临时文件
- **Then**: 使用 SearchReplace 更新 actions.md 中的过程文件列表，添加新文件名（不包含路径）
- **Verification**: `human-judgment`

### AC-4: 文档版本更新
- **Given**: 所有规范更新完成
- **When**: 任务完成时
- **Then**: 更新 rule_harness_instructions.md 的版本号和最后更新日期
- **Verification**: `programmatic`

## Open Questions
- [ ] 无
