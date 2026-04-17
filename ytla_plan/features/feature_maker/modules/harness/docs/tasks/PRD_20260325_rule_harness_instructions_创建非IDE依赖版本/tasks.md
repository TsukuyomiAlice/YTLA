本任务进度: 未完成

# 创建 rule_harness_instructions.md 的非IDE依赖版本 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 将临时分析文件移入 PRD 目录
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 将 `temp_analysis_non_ide_dependencies.md` 从 `docs/rules/` 目录移动到 PRD 目录
  - 更新 actions.md 的过程文件列表
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `programmatic` TR-1.1: 临时分析文件成功移动到 PRD 目录
  - `human-judgement` TR-1.2: actions.md 中的过程文件列表已更新
- **Notes**: 确保文件移动后原始位置不再有该文件

## [x] Task 2: 创建 actions.md 文档
- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 创建 actions.md 文档
  - 记录 Start Stage 和 Planning Stage 的操作
  - 添加过程文件列表章节
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `programmatic` TR-2.1: actions.md 成功创建
  - `human-judgement` TR-2.2: actions.md 包含必要的章节和内容
  - `human-judgement` TR-2.3: 过程文件列表已正确记录

## [x] Task 3: 创建 checklist.md 文档
- **Priority**: P0
- **Depends On**: Task 2
- **Description**: 
  - 创建 checklist.md 文档
  - 列出所有验证检查点
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3, AC-4, AC-5, AC-6, AC-7]
- **Test Requirements**:
  - `programmatic` TR-3.1: checklist.md 成功创建
  - `human-judgement` TR-3.2: 检查点完整且可验证

## [x] Task 4: 创建非IDE依赖版本文档主体
- **Priority**: P0
- **Depends On**: Task 3
- **Description**: 
  - 基于原始文档创建 `rule_harness_instructions_ver_direct.md`
  - 移除所有对IDE特定命令和工具的引用
  - 补充系统级上下文和指令
  - 提供工具替代方案
  - 调整工作流程的启动和切换方式
  - 明确文件操作和用户交互的方法
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3, AC-4, AC-5, AC-6]
- **Test Requirements**:
  - `programmatic` TR-4.1: 新文档成功创建在正确位置
  - `programmatic` TR-4.2: 文档中不包含任何IDE特定命令和工具的引用
  - `human-judgement` TR-4.3: 系统级上下文和指令已补充
  - `human-judgement` TR-4.4: 工具替代方案已提供
  - `human-judgement` TR-4.5: 工作流程已调整
  - `human-judgement` TR-4.6: 核心内容已保留

## [x] Task 5: 验证新文档的可用性
- **Priority**: P1
- **Depends On**: Task 4
- **Description**: 
  - 通读新文档，确保逻辑连贯
  - 验证所有内容完整且正确
  - 确保文档可以在非IDE环境中使用
- **Acceptance Criteria Addressed**: [AC-7]
- **Test Requirements**:
  - `human-judgement` TR-5.1: 文档逻辑连贯，内容完整
  - `human-judgement` TR-5.2: 文档可以在非IDE环境中使用
