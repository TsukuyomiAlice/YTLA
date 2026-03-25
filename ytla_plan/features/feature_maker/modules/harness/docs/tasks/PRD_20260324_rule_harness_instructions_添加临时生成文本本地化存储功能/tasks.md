本任务进度: 已完成

# Harness 临时文本存储优化 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 添加临时文件存储和命名规范
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中添加关于临时生成文本的存储位置规范
  - 明确临时文件命名格式为 temp_[AI自行设计标题].md
  - 说明临时文件应存储在 PRD 目录下
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `human-judgement` TR-1.1: 文档中明确说明了临时文件的存储位置
  - `human-judgement` TR-1.2: 文档中明确说明了临时文件的命名格式
- **Notes**: 可以在 4.5 actions.md 规范章节或新增章节中添加

## [x] Task 2: 添加 actions.md 过程文件列表规范
- **Priority**: P0
- **Depends On**: [Task 1]
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 actions.md 规范
  - 明确要求在 actions.md 中新增 "Generated Procedure Files List  过程文件列表" 章节
  - 说明该章节的位置（在文档标题下方）
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `human-judgement` TR-2.1: 文档中明确说明了过程文件列表章节的名称
  - `human-judgement` TR-2.2: 文档中明确说明了章节的位置
- **Notes**: 更新 4.5 actions.md 规范章节

## [x] Task 3: 添加过程文件列表更新规则
- **Priority**: P0
- **Depends On**: [Task 2]
- **Description**: 
  - 在 rule_harness_instructions.md 中明确过程文件列表的更新规则
  - 说明每次新生成临时文件时使用 SearchReplace 更新该章节
  - 说明只记录文件名，不包含路径
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `human-judgement` TR-3.1: 文档中明确说明了更新方法（SearchReplace）
  - `human-judgement` TR-3.2: 文档中明确说明了记录内容（仅文件名）
- **Notes**: 与现有 SearchReplace 使用规范保持一致

## [x] Task 4: 更新 actions.md 示例
- **Priority**: P1
- **Depends On**: [Task 2, Task 3]
- **Description**: 
  - 在 rule_harness_instructions.md 中更新 actions.md 的示例
  - 在示例中加入过程文件列表章节
  - 展示完整的 actions.md 结构
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `human-judgement` TR-4.1: 示例中包含过程文件列表章节
  - `human-judgement` TR-4.2: 示例展示了正确的章节位置
- **Notes**: 更新 4.5 节中的 actions.md 示例

## [x] Task 5: 更新文档版本信息
- **Priority**: P2
- **Depends On**: [Task 1, Task 2, Task 3, Task 4]
- **Description**: 
  - 更新 rule_harness_instructions.md 的文档版本号
  - 更新最后更新日期
- **Acceptance Criteria Addressed**: [AC-4]
- **Test Requirements**:
  - `programmatic` TR-5.1: 文档版本号已更新
  - `programmatic` TR-5.2: 最后更新日期已更新
- **Notes": 版本号建议从 1.63 更新到 1.64

## [x] Task 6: 强化 todo 列表记录要求
- **Priority": P0
- **Depends On": [Task 5]
- **Description": 
  - 强化 todo 列表在第一次生成时记录在 actions.md 里
  - 明确要求带上完整的 task 内容
  - 更新 actions.md 示例，添加 todo 列表记录示例
- **Acceptance Criteria Addressed": [追加需求]
- **Test Requirements":
  - `human-judgement` TR-6.1: 文档明确要求 todo 列表第一次生成时记录完整 task 内容
  - `human-judgement` TR-6.2: actions.md 示例包含 todo 列表记录示例
- **Notes": 与现有 todo 列表记录规范保持一致

## [x] Task 7: 强化 sub-agent 调用记录要求
- **Priority": P0
- **Depends On": [Task 6]
- **Description": 
  - 强化 sub-agent 的调用操作必须明确地被记录在 actions.md 里
  - 明确要求记录子代理任务描述和目标
  - 更新 actions.md 示例，添加 sub-agent 调用记录示例
  - 更新文档版本号
- **Acceptance Criteria Addressed": [追加需求]
- **Test Requirements":
  - `human-judgement` TR-7.1: 文档明确要求 sub-agent 调用操作必须明确记录
  - `human-judgement` TR-7.2: actions.md 示例包含 sub-agent 调用记录示例
  - `programmatic` TR-7.3: 文档版本号已更新
- **Notes": 与现有子代理记录规范保持一致
