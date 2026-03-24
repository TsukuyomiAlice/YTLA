本任务进度: 未完成

# Vue3 UI 组件 AI 生成规范 - 实现计划 (分解和优先级任务列表)

## [x] Task 1: 深入分析 sideCard 组件结构
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 全面分析 `d:\YTLA\ytla_plan_vue\src\core\classic\cards\sideCard` 目录结构，特别是 `ui` 文件夹下的组件
  - 提取 UI 组件的命名模式、文件组织方式和配套文件关系
  - 分析现有 `archi_analyze_20260323.md` 报告，识别最佳实践和改进点
- **Acceptance Criteria Addressed**: AC-6
- **Test Requirements**:
  - `programmatic` TR-1.1: 提取至少 10 个 UI 组件文件的名称和路径
  - `human-judgement` TR-1.2: 识别出命名规则中的模式和异常
- **Notes**: 需要生成临时分析文档存储在 PRD 目录下

## [x] Task 2: 研究现有 rule.md 规范
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 详细阅读 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule.md` 文件
  - 提取与 UI 组件相关的现有规范（命名规则、文件结构等）
  - 识别规范中的空白点和可扩展方向
- **Acceptance Criteria Addressed**: AC-5
- **Test Requirements**:
  - `human-judgement` TR-2.1: 总结现有规范中与 UI 组件相关的内容
  - `human-judgement` TR-2.2: 识别至少 3 个需要专门为 UI 组件扩展的规范点
- **Notes**: 需要制作规范对比表格

## [x] Task 3: 定义 UI 组件命名规则
- **Priority**: P0
- **Depends On**: Task 1, Task 2
- **Description**: 
  - 基于分析结果，制定详细的 UI 组件命名规则
  - 创建元件类型列表（Bar、Button、Container 等）及其使用场景
  - 提供复合组合词命名示例和反例
  - 定义文件命名约定（.vue、.ts、.scss 文件）
- **Acceptance Criteria Addressed**: AC-2, AC-5
- **Test Requirements**:
  - `human-judgement` TR-3.1: 命名规则至少包含 5 个正例和 2 个反例
  - `programmatic` TR-3.2: 元件类型列表至少包含 5 种类型
- **Notes**: 示例必须基于 sideCard 实际组件

## [x] Task 4: 设计文件结构与配套规范
- **Priority**: P0
- **Depends On**: Task 1, Task 3
- **Description**: 
  - 定义 UI 组件的标准文件结构
  - 详细说明 .vue 组件文件的结构（模板、脚本、样式）
  - 定义配套文件（composables、styles、definitions）的组织方式
  - 提供文件关系图和目录结构示例
- **Acceptance Criteria Addressed**: AC-3
- **Test Requirements**:
  - `human-judgement` TR-4.1: 文件结构描述清晰，包含至少 3 个配套文件类型
  - `programmatic` TR-4.2: 提供至少 2 个完整的文件结构示例
- **Notes**: 基于 sideCard 的实际文件组织

## [x] Task 5: 创建代码模板与示例
- **Priority**: P1
- **Depends On**: Task 3, Task 4
- **Description**: 
  - 基于 sideCard 组件创建可复用的代码模板
  - 提供 .vue 组件模板（包含 props、emits、setup 等）
  - 提供 .ts composable 模板（与 UI 组件相关）
  - 提供 .scss 样式模板（与 UI 组件相关）
- **Acceptance Criteria Addressed**: AC-1, AC-6
- **Test Requirements**:
  - `human-judgement` TR-5.1: 每个模板至少包含 1 个完整示例
  - `programmatic` TR-5.2: 模板代码语法正确，符合 Vue 3 和 TypeScript 规范
- **Notes**: 模板应包含注释说明各部分作用

## [x] Task 6: 制定 AI 提示词模板
- **Priority**: P1
- **Depends On**: Task 3, Task 4, Task 5
- **Description**: 
  - 创建完整的 AI 提示词模板用于生成 UI 组件
  - 包括组件生成提示词（功能描述、props、事件等）
  - 包括配套文件生成提示词（composable、样式）
  - 包括验证和测试提示词
  - 提供至少 2 个不同元件类型的完整提示词示例
- **Acceptance Criteria Addressed**: AC-4
- **Test Requirements**:
  - `human-judgement` TR-6.1: 提示词模板清晰、具体、可操作
  - `programmatic` TR-6.2: 至少 2 个完整提示词示例
- **Notes**: 提示词应遵循最佳实践，包含明确的输入输出格式

## [x] Task 7: 编写规范文档主体
- **Priority**: P1
- **Depends On**: Task 3, Task 4, Task 5, Task 6
- **Description**: 
  - 整合所有分析结果和模板，编写完整的 `rule_ui_instructions.md` 文档
  - 规范范围仅限于：`uis`目录下的vue文件、相关的`composables`文件、相关的`styles`文件
  - 包含所有必需章节：概述、命名规则、文件结构、代码模板、生成流程、AI 提示词、验证清单、附录
  - 确保文档结构清晰、内容完整、示例丰富
  - 保持与现有 rule.md 规范的一致性
  - 注意：不包含类型定义文件（definitions）和其他配套文件
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6
- **Test Requirements**:
  - `human-judgement` TR-7.1: 文档包含所有必需章节
  - `programmatic` TR-7.2: 文档中的示例至少 70% 来自 sideCard 组件
- **Notes**: 这是核心交付物，需要多次迭代完善

## [x] Task 8: 创建验证清单
- **Priority**: P2
- **Depends On**: Task 7
- **Description**: 
  - 为生成的 UI 组件创建验证清单
  - 包括命名验证、文件结构验证、代码风格验证、功能验证等
  - 提供验证工具或脚本建议
- **Acceptance Criteria Addressed**: AC-1
- **Test Requirements**:
  - `human-judgement` TR-8.1: 验证清单至少包含 10 个检查点
  - `programmatic` TR-8.2: 检查点具体、可验证
- **Notes**: 验证清单应实用，便于 AI 或开发人员使用

## [x] Task 9: 最终审查与集成
- **Priority**: P2
- **Depends On**: Task 7, Task 8
- **Description**: 
  - 对生成的规范文档进行最终审查
  - 确保文档格式正确、无拼写错误
  - 将文档保存到目标位置：`d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md`
  - 更新 actions.md 记录最终交付
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3, AC-4, AC-5, AC-6
- **Test Requirements**:
  - `human-judgement` TR-9.1: 文档通过人工审查，质量达标
  - `programmatic` TR-9.2: 文档成功保存到目标路径
- **Notes**: 最终交付前需要用户确认

# Task Dependencies
- Task 3 依赖于 Task 1 和 Task 2
- Task 4 依赖于 Task 1 和 Task 3
- Task 5 依赖于 Task 3 和 Task 4
- Task 6 依赖于 Task 3、Task 4 和 Task 5
- Task 7 依赖于 Task 3、Task 4、Task 5 和 Task 6
- Task 8 依赖于 Task 7
- Task 9 依赖于 Task 7 和 Task 8