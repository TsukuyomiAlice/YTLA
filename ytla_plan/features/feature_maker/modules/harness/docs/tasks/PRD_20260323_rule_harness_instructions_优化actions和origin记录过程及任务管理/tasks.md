本任务进度: 已完成

# Harness 工程规范优化 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 更新 rule_harness_instructions.md - 添加 AI 追问记录规范
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中添加关于 AI 发起用户追问前必须记录到 actions.md 的规范
  - 更新 actions.md 记录规则章节，明确提问操作的记录要求
  - 该记录必须在提问之前进行
- **Acceptance Criteria Addressed**: [AC-1, AC-5]
- **Test Requirements**:
  - `human-judgement` TR-1.1: 文档中明确说明 AI 追问前必须记录到 actions.md
  - `human-judgement` TR-1.2: 文档中提供了追问记录的格式示例
- **Notes**: 需要在 4.5 actions.md 规范章节和 8.2 执行最佳实践章节中添加相关内容

## [x] Task 2: 更新 rule_harness_instructions.md - 文档追加写入规范
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中明确规定更新 actions.md 和 origin.md 时采用追加写入方式
  - 说明例外情况（如初始创建或完全重写规划文档时仍可使用覆盖写入）
  - 更新最佳实践和常见陷阱章节
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `human-judgement` TR-2.1: 文档明确说明 actions.md 和 origin.md 更新采用追加方式
  - `human-judgement` TR-2.2: 文档说明了例外情况
- **Notes**: 需要更新 8.1 规划最佳实践和 9.1 规划阶段陷阱章节

## [x] Task 3: 更新 rule_harness_instructions.md - tasks.md 进度标记规范
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中添加 tasks.md 第一行必须包含任务进度标记的规范
  - 说明进度标记的格式："本任务进度: [已完成/未完成]"
  - 更新 Start Stage 检索流程，说明如何使用该标记判断 PRD 工程状态
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `human-judgement` TR-3.1: 文档明确说明 tasks.md 第一行必须包含进度标记
  - `human-judgement` TR-3.2: 文档说明了进度标记的判断逻辑
- **Notes**: 需要更新 2.1 Start Stage、4.3 tasks.md 规范章节，以及添加新任务的示例

## [x] Task 4: 更新 rule_harness_instructions.md - 任务完成确认流程规范
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中调整任务完成依据的说明
  - 添加 AI 主动询问用户确认完成的流程
  - 说明用户确认后需要执行的最终步骤
- **Acceptance Criteria Addressed**: [AC-4, AC-5]
- **Test Requirements**:
  - `human-judgement` TR-4.1: 文档明确说明任务完成需要用户确认
  - `human-judgement` TR-4.2: 文档说明了用户确认后的完整流程
- **Notes**: 需要更新 5.1 完整工作流章节，以及添加新的最佳实践

## [x] Task 5: 验证并更新本 PRD 的 tasks.md 第一行
- **Priority**: P1
- **Depends On**: [Task 3]
- **Description**: 
  - 确保本 PRD 的 tasks.md 第一行已正确添加进度标记
  - 验证格式符合新规范要求
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `programmatic` TR-5.1: tasks.md 第一行准确包含 "本任务进度: 未完成"
- **Notes**: 本任务用于验证新规范的实际应用
