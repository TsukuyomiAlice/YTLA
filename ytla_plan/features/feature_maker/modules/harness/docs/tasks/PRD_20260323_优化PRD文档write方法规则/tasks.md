本任务进度: 已完成

# PRD 文档 Write 方法规则优化 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 更新 rule_harness_instructions.md - 添加 PRD 文档 write 方法规则定义
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中添加明确的 PRD 文档 write 方法规则定义
  - 说明 spec.md、tasks.md、checklist.md 使用 write 覆盖方式更新
  - 说明 origin.md、actions.md 使用末尾换行追加方式更新
  - 将规则添加到文档的适当章节（如规划文档规范或最佳实践章节）
- **Acceptance Criteria Addressed**: [AC-1, AC-2]
- **Test Requirements**:
  - `human-judgement` TR-1.1: 检查文档中明确说明了不同文档类型的 write 方法规则
  - `human-judgement` TR-1.2: 检查规则定义清晰无歧义
- **Notes**: 需要确定规则添加的具体章节位置，确保与现有文档结构协调

## [x] Task 2: 更新 rule_harness_instructions.md - 修订“常见陷阱和避免方法”章节
- **Priority**: P0
- **Depends On**: [Task 1]
- **Description**: 
  - 梳理和修订“常见陷阱和避免方法”章节
  - 添加与 write 方法规则相关的陷阱描述和避免方法
  - 确保陷阱描述针对 write 覆盖和末尾追加的不同场景提供具体指导
  - 更新现有陷阱描述，确保与新的 write 方法规则一致
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `human-judgement` TR-2.1: 检查“常见陷阱和避免方法”章节包含 write 方法相关的陷阱
  - `human-judgement` TR-2.2: 检查陷阱描述和避免方法与新的 write 方法规则一致
- **Notes**: 需要仔细审查现有陷阱，确保更新后不会引入矛盾

## [x] Task 3: 验证规则文档更新后的兼容性
- **Priority**: P1
- **Depends On**: [Task 1, Task 2]
- **Description**: 
  - 验证更新后的 rule_harness_instructions.md 文档与现有 Harness 工程规范保持兼容
  - 检查规则是否与现有 PRD 文档生成和更新流程协调一致
  - 确保文档整体结构和风格保持连贯
- **Acceptance Criteria Addressed**: [AC-4]
- **Test Requirements**:
  - `human-judgement` TR-3.1: 检查更新后的文档没有破坏现有规范的其他部分
  - `human-judgement` TR-3.2: 检查规则与现有工作流程协调一致
- **Notes**: 需要通读整个文档，确保更新部分与上下文衔接自然

## [x] Task 4: 更新本 PRD 的 tasks.md 进度标记
- **Priority**: P1
- **Depends On**: [Task 3]
- **Description**: 
  - 所有任务执行完毕后，更新本 tasks.md 第一行进度标记为“已完成”
  - 验证格式符合规范要求
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `programmatic` TR-4.1: 验证 tasks.md 第一行准确包含 "本任务进度: 已完成"
- **Notes**: 本任务用于验证新规则的实际应用