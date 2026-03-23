# Harness Mode 文档记录优化 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 更新 origin.md 规范说明 - 多轮对话
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 origin.md 的规范章节
  - 添加多轮对话记录的说明
  - 添加 `# Dialogue [序号]` 格式的示例
- **Acceptance Criteria Addressed**: [AC-1, AC-9, AC-10]
- **Test Requirements**:
  - `programmatic` TR-1.1: 检查规则文档中 origin.md 规范包含 `# Dialogue [序号]` 说明
  - `human-judgement` TR-1.2: 检查示例是否完整清晰
- **Notes**: 保持与现有 origin.md 规范的向后兼容性

## [x] Task 2: 更新 origin.md 规范说明 - 头部信息
- **Priority**: P0
- **Depends On**: [Task 1]
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 origin.md 的规范章节
  - 添加在开头（仅限 spec 模式）添加 harness 文件版本和作者信息的说明
  - 添加头部信息格式的示例
- **Acceptance Criteria Addressed**: [AC-2, AC-9, AC-10]
- **Test Requirements**:
  - `programmatic` TR-2.1: 检查规则文档中包含 origin.md 头部信息说明
  - `human-judgement` TR-2.2: 检查头部信息示例是否完整清晰
- **Notes**: 明确说明仅限 spec 模式时添加头部信息

## [x] Task 3: 更新 actions.md 规范说明 - 用户输入记录
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 actions.md 的规范章节
  - 添加在 Planning Stage 和 Action Stage 中插入用户输入记录的说明
  - 添加 `### USER：Dialogue [序号]` 格式的示例
- **Acceptance Criteria Addressed**: [AC-3, AC-9, AC-10]
- **Test Requirements**:
  - `programmatic` TR-3.1: 检查规则文档中 actions.md 规范包含 `### USER：Dialogue [序号]` 说明
  - `human-judgement` TR-3.2: 检查示例是否完整清晰，包含 Planning Stage 和 Action Stage 两个场景
- **Notes**: 保持与现有 actions.md 规范的向后兼容性

## [x] Task 4: 添加 Planning Stage 一次性记录规范
- **Priority**: P0
- **Depends On**: [Task 3]
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 actions.md 规范章节
  - 添加 Planning Stage 一次性记录 origin.md、spec.md、tasks.md、checklist.md 的说明
  - 添加 Planning Stage 一次性记录的示例
- **Acceptance Criteria Addressed**: [AC-4, AC-9, AC-10]
- **Test Requirements**:
  - `programmatic` TR-4.1: 检查规则文档中包含 Planning Stage 一次性记录说明
  - `human-judgement` TR-4.2: 检查一次性记录示例是否完整清晰
- **Notes**: 明确说明一次性记录仅适用于 Planning Stage 的四个规划文档初始生成

## [x] Task 5: 添加 Action Stage 记录规范
- **Priority**: P0
- **Depends On**: [Task 3, Task 4]
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 actions.md 规范章节
  - 明确说明 Action Stage 通常保持分开记录，但相同目标的操作可以合并
  - 添加 Action Stage 分开记录和合并记录的示例
- **Acceptance Criteria Addressed**: [AC-5, AC-8, AC-9, AC-10]
- **Test Requirements**:
  - `programmatic` TR-5.1: 检查规则文档中包含 Action Stage 记录说明
  - `human-judgement` TR-5.2: 检查示例是否完整清晰，包含分开记录和合并记录两种场景
- **Notes**: 强调 Action Stage 通常分开记录，但相同目标的可以合并

## [x] Task 6: 添加 todo 列表操作记录规范
- **Priority**: P0
- **Depends On**: [Task 3]
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 actions.md 规范章节
  - 添加记录 todo 列表操作的说明
  - 添加 todo 列表操作记录的示例
- **Acceptance Criteria Addressed**: [AC-6, AC-9, AC-10]
- **Test Requirements**:
  - `programmatic` TR-6.1: 检查规则文档中包含 todo 列表操作记录说明
  - `human-judgement` TR-6.2: 检查 todo 列表操作记录示例是否完整清晰
- **Notes**: 明确说明 todo 列表操作也需要记录到 actions.md

## [x] Task 7: 添加通知用户操作记录规范
- **Priority**: P0
- **Depends On**: [Task 3, Task 6]
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 actions.md 规范章节
  - 添加记录通知用户操作的说明
  - 添加通知用户操作记录的示例
- **Acceptance Criteria Addressed**: [AC-7, AC-9, AC-10]
- **Test Requirements**:
  - `programmatic` TR-7.1: 检查规则文档中包含通知用户操作记录说明
  - `human-judgement` TR-7.2: 检查通知用户操作记录示例是否完整清晰
- **Notes**: 明确说明通知用户操作也需要记录到 actions.md

## [x] Task 8: 添加追加需求记录流程说明
- **Priority**: P1
- **Depends On**: [Task 1, Task 2, Task 3]
- **Description**: 
  - 在 rule_harness_instructions.md 中添加新章节，专门说明追加需求的记录流程
  - 说明何时需要记录追加需求（规划阶段批准前、执行中、执行后）
  - 说明如何在 origin.md 和 actions.md 中同步记录
- **Acceptance Criteria Addressed**: [AC-9, AC-10]
- **Test Requirements**:
  - `human-judgement` TR-8.1: 检查追加需求记录流程说明是否完整清晰
- **Notes**: 可以添加在文档的最佳实践或常见陷阱部分

## [x] Task 9: 更新文档版本信息
- **Priority**: P2
- **Depends On**: [Task 1, Task 2, Task 3, Task 4, Task 5, Task 6, Task 7, Task 8]
- **Description**: 
  - 更新 rule_harness_instructions.md 的文档版本号和最后更新日期
  - 在附录或变更记录中说明本次更新的内容
- **Acceptance Criteria Addressed**: [AC-9]
- **Test Requirements**:
  - `programmatic` TR-9.1: 检查文档版本号和更新日期已更新
- **Notes**: 版本号建议从 1.3 更新到 1.4
