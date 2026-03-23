# PRD 文档 Write 方法规则优化 Spec

## Overview - 概要
当前 rule_harness_instructions.md 文档中关于 PRD 文档的 write 方法规则需要进一步明确和优化。用户规定：对 spec、tasks、checklist 文档，遵循旧规则，依然优先使用 write 覆盖的方式更新；对 origin、actions 文档，由于新的内容不会对旧的内容产生影响，所以总是在文档末尾换行添加。同时需要对“常见陷阱和避免方法”章节进行梳理和修订，确保与新的 write 方法规则一致。

## Goals - 目标
1. 明确 PRD 文档 write 方法规则：spec/tasks/checklist 使用 write 覆盖更新，origin/actions 使用末尾追加更新
2. 更新 rule_harness_instructions.md 文档，反映上述规则
3. 梳理和修订“常见陷阱和避免方法”章节，确保与新的 write 方法规则一致
4. 确保规则与现有 Harness 工程规范保持兼容

## Non-Goals - 非目标（边界）
1. 不改变现有 PRD 文档的格式规范（如 origin.md 的 Dialogue 格式、spec.md 的章节结构等）
2. 不修改除 rule_harness_instructions.md 之外的其他文档
3. 不改变 .trae/specs 目录的使用规则（该目录已被禁用）

## Background & Context - 背景和上下文
在 Harness 工程规范中，PRD 文档包括 origin.md、spec.md、tasks.md、checklist.md、actions.md 五种类型。目前文档中关于如何更新这些文档的规则不够明确，导致在实际操作中可能存在混淆。用户明确规定了不同文档类型的更新方式，需要将此规则正式纳入规范文档。

## Functional Requirements - 功能需求
1. **FR-1：Write 方法规则定义**
   - 系统应明确规定 spec.md、tasks.md、checklist.md 文档使用 write 覆盖方式更新
   - 系统应明确规定 origin.md、actions.md 文档使用末尾换行追加方式更新
   - 规则应在 rule_harness_instructions.md 文档中明确说明

2. **FR-2：规则文档更新**
   - 更新 rule_harness_instructions.md 文档，在适当章节添加 write 方法规则说明
   - 确保规则说明清晰、无歧义

3. **FR-3：陷阱章节修订**
   - 梳理和修订“常见陷阱和避免方法”章节，确保与新的 write 方法规则一致
   - 更新相关陷阱描述和避免方法

## Non-Functional Requirements - 非功能需求
1. **NFR-1：兼容性**
   - 规则更新应与现有 Harness 工程规范保持向后兼容
   - 不应破坏现有 PRD 文档的工作流程

2. **NFR-2：可读性**
   - 规则说明应清晰易懂，便于后续维护者理解

## Constraints - 约束条件
1. 必须遵循现有的 PRD 文档格式规范
2. 不能使用 .trae/specs 目录（已被禁用）

## Assumptions - 假设
1. 用户了解 write 覆盖和末尾追加的区别
2. 现有 Harness 工程规范的其他部分保持不变

## Acceptance Criteria - 验收标准（Given/When/Then 格式）

### AC-1: Write 方法规则定义
- **Given**: rule_harness_instructions.md 文档
- **When**: 查阅文档中关于 PRD 文档 write 方法的说明
- **Then**: 应明确说明 spec.md、tasks.md、checklist.md 使用 write 覆盖更新，origin.md、actions.md 使用末尾追加更新
- **Verification**: `human-judgement`
- **Notes**: 规则应在文档的适当章节（如规划文档规范或最佳实践章节）中明确说明

### AC-2: 规则文档更新完成
- **Given**: 更新后的 rule_harness_instructions.md 文档
- **When**: 检查文档的 write 方法规则说明
- **Then**: 应包含清晰的规则定义和示例（如适用）
- **Verification**: `human-judgement`
- **Notes**: 更新后的文档应保持整体结构和风格的连贯性

### AC-3: 陷阱章节修订完成
- **Given**: 更新后的 rule_harness_instructions.md 文档
- **When**: 检查“常见陷阱和避免方法”章节
- **Then**: 应包含与 write 方法规则相关的陷阱描述和避免方法
- **Verification**: `human-judgement`
- **Notes**: 陷阱描述应针对 write 方法的不同更新方式提供具体指导

### AC-4: 向后兼容性
- **Given**: 更新后的 rule_harness_instructions.md 文档
- **When**: 应用新的 write 方法规则到现有 PRD 工作流
- **Then**: 不应破坏现有的 PRD 文档生成和更新流程
- **Verification**: `human-judgement`
- **Notes**: 确保规则与现有规范的其他部分协调一致

## Open Questions - 待解决问题
1. 是否需要为 write 覆盖和末尾追加提供具体的工具使用示例？
2. 是否需要在最佳实践章节添加关于 write 方法选择的指导？