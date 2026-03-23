# Harness Mode 文档记录优化 - Product Requirement Document

## Overview
- **Summary**: 优化 harness mode 的文档记录过程，支持记录用户在规划阶段和执行阶段提出的追加需求，更新 origin.md 和 actions.md 的格式规范，优化 Planning Stage 的记录方式，并扩展 actions.md 的记录范围
- **Purpose**: 解决在用户批准执行前或执行完成后，追加需求无法被完整记录的问题，同时优化 Planning Stage 的记录效率，扩展 actions.md 的记录范围，确保整个开发过程的可追溯性
- **Target Users**: 使用 harness mode 进行开发的 AI 代理和开发团队

## Goals
- 在 origin.md 中支持记录多轮用户对话，使用 `# Dialogue [序号]` 作为标题
- 在 origin.md 开头（仅限 spec 模式）添加 harness 文件版本和作者信息
- 在 actions.md 的 Planning Stage 和 Action Stage 中支持插入用户输入记录，使用 `### USER：Dialogue [序号]` 格式
- 优化 Planning Stage 中 actions.md 的记录方式，支持一次性记录多个文件生成操作
- 扩展 actions.md 的记录范围，包含 todo 列表操作和通知用户操作
- 支持相同目标的操作合并记录，不限阶段
- 更新 rule_harness_instructions.md 文档，添加新的规范说明
- 确保文档记录的完整性和可追溯性

## Non-Goals (Out of Scope)
- 不修改其他规划文档（spec.md、tasks.md、checklist.md）的现有格式
- 不改变 harness mode 的核心执行流程
- 不添加自动化对话分析功能
- 不在 Action Stage 中使用一次性记录方式（除非目标相同）

## Background & Context
- 现有 harness mode 已具备完整的规划和执行流程
- 在实际使用中，用户经常会在规划阶段和执行阶段提出追加需求
- 目前的规范没有明确如何记录这些追加需求，导致过程不可追溯
- Planning Stage 中每个文件生成都单独记录，效率较低
- actions.md 目前只记录文件操作，缺少 todo 列表和通知用户操作的记录
- 需要通过更新 origin.md 和 actions.md 的规范来解决这些问题

## Functional Requirements
- **FR-1**: origin.md 支持多轮对话记录，使用 `# Dialogue [序号]` 标题格式
- **FR-2**: origin.md 在开头（仅限 spec 模式）添加 harness 文件版本和作者信息
- **FR-3**: actions.md 支持在 Planning Stage 和 Action Stage 中插入用户输入记录
- **FR-4**: actions.md 中用户输入使用 `### USER：Dialogue [序号]` 格式
- **FR-5**: Planning Stage 中 actions.md 支持一次性记录 origin.md、spec.md、tasks.md、checklist.md 的生成操作
- **FR-6**: Action Stage 保持原有的分开记录方式（除非目标相同）
- **FR-7**: actions.md 支持记录 todo 列表操作
- **FR-8**: actions.md 支持记录通知用户操作
- **FR-9**: actions.md 支持相同目标的操作合并记录，不限阶段
- **FR-10**: 更新 rule_harness_instructions.md 文档，添加新规范的说明和示例
- **FR-11**: 在规则文档中明确追加需求的记录流程
- **FR-12**: 在规则文档中明确 Planning Stage 和 Action Stage 不同的记录方式
- **FR-13**: 在规则文档中明确 actions.md 的扩展记录范围

## Non-Functional Requirements
- **NFR-1**: 文档格式保持清晰易读
- **NFR-2**: 规范说明应包含具体的示例
- **NFR-3**: 向后兼容，不影响现有文档的读取
- **NFR-4**: 区分 Planning Stage 和 Action Stage 的记录方式，避免混淆
- **NFR-5**: 相同目标的操作合并记录时，应保持清晰的逻辑

## Constraints
- **Technical**: 仅修改 markdown 文档，不涉及代码变更
- **Business**: 需遵循现有 harness mode 的整体框架
- **Dependencies**: 依赖现有的 rule_harness_instructions.md 文档结构

## Assumptions
- 用户追加需求主要出现在 Planning Stage（批准前）和 Action Stage（执行中/后）
- 追加需求需要同时记录在 origin.md（需求变更）和 actions.md（执行过程）中
- 对话序号从 1 开始递增
- Planning Stage 一次性记录仅适用于 origin.md、spec.md、tasks.md、checklist.md 这四个规划文档的初始生成
- Action Stage 通常保持分开记录，但相同目标的操作可以合并
- origin.md 开头的版本和作者信息仅在确认是 spec 模式时添加

## Acceptance Criteria

### AC-1: origin.md 支持多轮对话记录
- **Given**: 用户在规划或执行过程中提出追加需求
- **When**: 记录追加需求到 origin.md
- **Then**: 使用 `# Dialogue [序号]` 作为对话标题，序号从 1 开始递增
- **Verification**: `human-judgment`
- **Notes**: 原始需求可以作为 Dialogue 1，后续追加需求依次编号

### AC-2: origin.md 包含文件版本和作者信息
- **Given**: 确认是 spec 模式
- **When**: 生成 origin.md
- **Then**: 在 origin.md 最开始添加 harness 文件版本和作者信息
- **Verification**: `human-judgment`

### AC-3: actions.md 支持插入用户输入记录
- **Given**: 用户在 Planning Stage 或 Action Stage 中提出输入
- **When**: 记录到 actions.md
- **Then**: 在对应阶段中插入 `### USER：Dialogue [序号]` 标记，然后记录用户输入和后续操作
- **Verification**: `human-judgment`

### AC-4: Planning Stage 支持一次性记录
- **Given**: 在 Start Stage 完成后，需要生成 origin.md、spec.md、tasks.md、checklist.md
- **When**: 在 actions.md 中记录这些文件的生成
- **Then**: 可以一次性记录这四个文件的生成操作，然后连续生成这些文件
- **Verification**: `human-judgment`

### AC-5: Action Stage 保持分开记录（除非目标相同）
- **Given**: 在 Action Stage 执行任务
- **When**: 在 actions.md 中记录操作
- **Then**: 通常保持每个任务或文件操作分开记录，但相同目标的操作可以合并
- **Verification**: `human-judgment`

### AC-6: actions.md 记录 todo 列表操作
- **Given**: 执行 todo 列表操作（更新任务状态等）
- **When**: 在 actions.md 中记录
- **Then**: 记录 todo 列表操作，包括使用的工具和目标
- **Verification**: `human-judgment`

### AC-7: actions.md 记录通知用户操作
- **Given**: 执行通知用户操作
- **When**: 在 actions.md 中记录
- **Then**: 记录通知用户操作，包括使用的工具和目标
- **Verification**: `human-judgment`

### AC-8: 相同目标的操作可以合并记录
- **Given**: 有多个操作针对相同目标
- **When**: 在 actions.md 中记录
- **Then**: 可以合并记录这些操作，不限阶段
- **Verification**: `human-judgment`

### AC-9: rule_harness_instructions.md 包含新规范
- **Given**: 规则文档需要更新
- **When**: 修改 rule_harness_instructions.md
- **Then**: 文档中包含所有新规范的说明，并有具体示例
- **Verification**: `programmatic`（检查文档内容是否包含新规范）

### AC-10: 规范包含完整示例
- **Given**: 规则文档已更新
- **When**: 查看新规范章节
- **Then**: 包含所有新功能的完整示例
- **Verification**: `human-judgment`

## Open Questions
- [ ] 对话序号是否需要跨多个 PRD 文档连续？
