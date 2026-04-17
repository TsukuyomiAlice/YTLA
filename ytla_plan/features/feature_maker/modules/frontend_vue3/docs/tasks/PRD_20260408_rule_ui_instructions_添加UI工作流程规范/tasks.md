本任务进度: 已完成

# UI工作流程规范添加 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 在 rule_ui_instructions.md 中添加 UI 工作流程调整章节
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在 rule_ui_instructions.md 文档开头添加新的章节
  - 章节标题为 "AI 代理工作流程调整"
  - 包含所有工作流程规范内容
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `programmatic` TR-1.1: rule_ui_instructions.md 中新增章节存在
  - `human-judgement` TR-1.2: 新增章节位置正确（在文档开头）
- **Notes**: 保持与现有文档风格一致

## [x] Task 2: 定义读取 rule_ui_instructions.md 时的特殊处理流程
- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 在新增章节中说明当读取到 rule_ui_instructions.md 时的特殊处理
  - 明确说明本文档作为附加规则，在其他AI代理规则之后用于调整
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `human-judgement` TR-2.1: 特殊处理流程说明清晰
  - `human-judgement` TR-2.2: 触发条件明确

## [x] Task 3: 规范 Planning Stage 中的 UI 需求分析步骤
- **Priority**: P0
- **Depends On**: Task 2
- **Description**: 
  - 说明在 Planning Stage 中结合现有目录情况分析用户对 UI 内容的实际需求
  - 列出具体的分析步骤
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `human-judgement` TR-3.1: UI 需求分析步骤完整
  - `human-judgement` TR-3.2: 分析步骤可执行

## [x] Task 4: 定义 ui_checklist.md 的标准格式和内容要求
- **Priority**: P0
- **Depends On**: Task 3
- **Description**: 
  - 说明在进入 Action Stage 之前额外生成 ui_checklist.md
  - 定义 ui_checklist.md 的标准格式
  - 明确应包含的信息：
    - 本次的 UI 生成形式（新建/重构/提取）
    - 拟生成的 UI 列表（ui 文件名、生成原因、用途、包含的派生文件）
    - 需要重构的 UI 列表（ui 文件名、重构原因、现有的派生文件、重构后的派生文件和变动简述）
- **Acceptance Criteria Addressed**: [AC-4]
- **Test Requirements**:
  - `human-judgement` TR-4.1: ui_checklist.md 格式定义清晰
  - `human-judgement` TR-4.2: 所有必需的信息项都已定义
  - `human-judgement` TR-4.3: 提供了格式示例

## [x] Task 5: 规范 Action Stage 中使用 ui_checklist.md 作为核对清单的要求
- **Priority**: P0
- **Depends On**: Task 4
- **Description**: 
  - 说明在进入 Action Stage 之后，应当将 ui_checklist.md 作为核对清单
  - 明确如何使用这个核对清单
- **Acceptance Criteria Addressed**: [AC-5]
- **Test Requirements**:
  - `human-judgement` TR-5.1: 核对清单使用要求明确
  - `human-judgement` TR-5.2: 使用方法说明清晰

## [x] Task 6: 验证所有更新正确
- **Priority**: P1
- **Depends On**: Task 5
- **Description**: 
  - 验证 rule_ui_instructions.md 的所有更新正确
  - 确保文档格式和风格一致
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3, AC-4, AC-5]
- **Test Requirements**:
  - `human-judgement` TR-6.1: 所有更新内容正确
  - `human-judgement` TR-6.2: 文档格式和风格一致
- **Notes**: 进行全面的文档审查
