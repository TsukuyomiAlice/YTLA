# 更新 Harness 工程规范添加 actions.md - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 更新 rule_harness_instructions.md，添加 actions.md 规范章节
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_harness_instructions.md 中新增 actions.md 的规范章节
  - 定义 actions.md 的三个阶段结构（Start Stage, Planning Stage, Action Stage）
  - 定义每个行动记录项的格式（ACT-[序号], Thought, Target, Tool, Touches）
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `human-judgement` TR-1.1: 检查新增章节位置合理，与现有文档风格一致 ✓
  - `human-judgement` TR-1.2: 检查三个阶段的定义清晰完整 ✓
  - `human-judgement` TR-1.3: 检查行动记录格式定义正确 ✓
- **Notes**: 在 4.4 章节之后新增了 4.5 章节

## [x] Task 2: 更新 harness 模式执行流程，添加 Start Stage
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 更新 harness 模式执行流程相关章节
  - 明确 Start Stage 的触发条件（读取 rule_harness_instructions.md 后即刻开始）
  - 明确 Start Stage 的职责（检索已有 PRD 文档、创建 PRD 目录）
  - 明确 Start Stage 与 Planning Stage 的衔接（建立 PRD 目录后进入 Planning Stage）
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `human-judgement` TR-2.1: 检查执行流程图或文字说明已更新 ✓
  - `human-judgement` TR-2.2: 检查 Start Stage 触发条件明确 ✓
  - `human-judgement` TR-2.3: 检查各阶段职责清晰，衔接合理 ✓
- **Notes**: 更新了第 2、3、5、7、8、9、10 章的相关内容

## [x] Task 3: 生成本次任务的 actions.md 文档
- **Priority**: P0
- **Depends On**: [Task 1, Task 2]
- **Description**: 
  - 按照新定义的规范生成本次任务的 actions.md 文档
  - 包含 Start Stage、Planning Stage、Action Stage 三个阶段
  - 每个阶段记录真实的行动过程（Thought, Target, Tool, Touches）
  - 确保在每次文件操作前完成记录（更新 actions.md 本身除外）
- **Acceptance Criteria Addressed**: [AC-3, AC-4, AC-5]
- **Test Requirements**:
  - `programmatic` TR-3.1: 验证 actions.md 文件存在于 PRD 目录中 ✓
  - `human-judgement` TR-3.2: 检查文档包含三个完整的阶段 ✓
  - `human-judgement` TR-3.3: 检查每个行动记录项包含四个要素 ✓
  - `human-judgement` TR-3.4: 检查记录内容真实反映本次执行过程 ✓
- **Notes**: 已完整记录从 Start Stage 到 Planning Stage 的全过程

## [x] Task 4: 验证所有规划文档完整且符合规范
- **Priority**: P1
- **Depends On**: [Task 3]
- **Description**: 
  - 验证 origin.md 符合 4.1 章节规范
  - 验证 spec.md 符合 4.2 章节规范
  - 验证 tasks.md 符合 4.3 章节规范
  - 验证 checklist.md 符合 4.4 章节规范
  - 验证 actions.md 符合新定义的规范
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3, AC-4, AC-5]
- **Test Requirements**:
  - `human-judgement` TR-4.1: 检查所有规划文档的必填章节完整 ✓
  - `human-judgement` TR-4.2: 检查文档格式符合规范要求 ✓
- **Notes**: 使用 7.1 章节的规划阶段检查清单进行验证，所有检查点已通过
