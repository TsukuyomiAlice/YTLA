Harness Instructions file version: rule_harness_instructions.md v1.7  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec 按 `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md` 规范执行  
分析对象 `d:\YTLA\ytla_plan_vue\src\core\classic\cards\sideCard` （包含已做分析 `d:\YTLA\ytla_plan_vue\src\core\classic\cards\sideCard\documents\design\archi_analyze_20260323.md` ）  
需求：生成 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md` 内容，为vue3的ui组件提供ai生成规范  
注意：这里特指生成于uis文件夹下的vue组件，以及相关的配套文件的生成规范，不包含其它组件  
生成参考文档 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule.md`   
可以向我发起追问确认文档的生成具体细节  
可以在本地存储你生成的临时内容

## Analyze：
**Given**： 
- harness 规范文件：`d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md`
- 分析对象：`d:\YTLA\ytla_plan_vue\src\core\classic\cards\sideCard` 目录及其现有分析文档 `archi_analyze_20260323.md`
- 参考文档：`d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule.md`（Vue3 工程与文件规范）
- 目标文件：`d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md`

**Target**： 
生成一个专门针对 Vue3 UI 组件（位于 `uis` 文件夹下的 `.vue` 组件）的 AI 生成规范文档，涵盖组件本身及其配套文件（composables、styles、definitions 等）的生成规则。

**Evidence**：
- 用户明确要求“特指生成于uis文件夹下的vue组件，以及相关的配套文件的生成规范，不包含其它组件”
- 需要基于现有 sideCard 组件的实际结构和现有规范 rule.md 进行分析
- 用户允许追问细节和本地存储临时内容

## Evaluation Result：
### rule_ui_instructions.md：Vue3 UI 组件 AI 生成规范文档
- 形式：Markdown 文档，包含完整的规范结构
- 内容：专注于 uis 文件夹下的 Vue 组件及其配套文件的生成规则
- 依据：基于 sideCard 组件实例和现有 rule.md 规范

# Dialogue 2

## User Requirement: 
您希望生成的 rule_ui_instructions.md 文档包含哪些主要章节？=完整规范结构
UI 组件命名规则需要详细到哪种程度？=详细规则 + 示例
配套文件规范需要覆盖哪些文件类型？=完整配套
是否需要包含 AI 生成的具体提示词示例？=包含完整提示词
附加信息：如果有问题可以随时向我提问

## Analyze：
**Given**：用户对四个关键问题的选择结果
**Target**：根据用户的选择细化规范文档的具体要求
**Evidence**：
- 文档结构：完整规范结构（概述、命名规则、文件结构、代码模板、生成流程、验证清单等）
- 命名规则：详细规则 + 示例（包括元件类型列表、命名示例、常见错误示例）
- 配套文件：完整配套（.vue 组件、.ts composable、.scss 样式文件、类型定义等所有配套文件）
- AI 提示词：包含完整提示词（提供用于生成 UI 组件的完整 AI 提示词模板和示例）

## Evaluation Result：
### 细化后的规范要求：
- **文档结构**：完整规范结构，包含多个章节
- **命名规则**：详细规则加丰富示例
- **配套文件**：覆盖所有配套文件类型
- **AI 提示词**：包含完整提示词模板

# Dialogue 3

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md`    
我把任务临时中断了，因为我发现了你在sub-agent过程中没有把temp文件生成在主任务指定的PRD目录下   
之前你的子进程生成的全部文件，我已经都保存在 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\tasks\PRD_20260324_rule_ui_instructions_生成UI组件AI生成规范` 下了  
现在你需要注意，在启动sub-agents时，子进程生成的temp文档都需要存放在这个目录下  
现在你可以继续你的工作了

## Analyze：
**Given**：用户指出了temp文件存储位置问题
**Target**：确保后续子代理生成的临时文件存储在正确的PRD目录下
**Evidence**：
- 用户发现子代理生成的temp文件没有放在指定的PRD目录下
- 用户已将现有temp文件移动到正确的PRD目录
- 用户要求后续子代理生成temp文件时必须存放在PRD目录下

## Evaluation Result：
### 修正后的临时文件存储规范：
- 所有子代理生成的临时文件必须存放在 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\tasks\PRD_20260324_rule_ui_instructions_生成UI组件AI生成规范` 目录下
- 临时文件命名格式：`temp_[描述].md`
- 需要在actions.md的Generated Procedure Files List中记录所有临时文件

# Dialogue 4

## User Requirement: 
在你开始最终任务之前，我需要打断你  
这份 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md` 的规范目标，仅限于对vue前端项目的/uis目录下的vue文件，以及这些文件会涉及到的/composables下的文件和/styles下的文件

## Analyze：
**Given**：用户澄清了规范文档的范围限制
**Target**：根据新的范围限制更新规范文档
**Evidence**：
- 规范目标仅限于：`/uis`目录下的vue文件
- 仅限于这些UI组件会涉及到的：`/composables`下的文件
- 仅限于这些UI组件会涉及到的：`/styles`下的文件
- 不包含其他文件如类型定义文件（definitions）、布局文件（layouts）等

## Evaluation Result：
### 修正后的规范范围：
- **核心文件**：`uis`目录下的`.vue`组件文件
- **配套文件**：与UI组件相关的`composables`目录下的`.ts`文件
- **配套文件**：与UI组件相关的`styles`目录下的`.scss`文件
- **排除文件**：类型定义文件（definitions）、布局文件（layouts）、服务文件（services）、存储文件（stores）等

需要更新以下文档：
1. spec.md：更新FR-3和FR-4，移除类型定义和其他配套文件
2. tasks.md：更新Task 5、Task 6、Task 7描述，明确范围限制
3. 最终规范文档：仅包含限定范围内的内容

spec mode logging