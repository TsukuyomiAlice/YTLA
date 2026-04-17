Harness Instructions file version: rule_harness_instructions_ver_ide.md
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md` 依然在 `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md` 规则下，继续与这两个文档有关的内容 
 第二个需求是 
 在 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md` 被读取之后，调整实际的ai代理工作流程 
 具体而言，如果读到了 `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md` ，那么会在planning阶段中，结合现有的目录情况，分析用户对ui内容的实际需求 
 在进入Action阶段之前，额外生成一份分析文件，这份文件一并保存在PRD目录下，名字叫ui_checklist.md 
 里面应该记录下列信息 
 本次的ui生成形式：新建(根据用户需求新建ui)/重构(将已有的ui文件进行重构)/提取(指从components或layouts中提取出ui元素) 
 拟生成的ui列表（包括ui文件名，生成原因，用途，包含的派生文件） 
 需要重构的ui列表（包含ui文件名，重构原因，现有的派生文件，重构后的派生文件和变动简述） 
 在进入Action阶段之后，应当将ui_checklist.md作为核对清单

## Analyze：
**Given**： 
- harness 规则文档：d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md
- UI 规则文档：d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md
- UI 标准文档：d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_standards.md

**Target**： 
在 rule_ui_instructions.md 文档中添加关于 AI 代理工作流程调整的规范，包括：
1. 当读取到 rule_ui_instructions.md 时的特殊处理流程
2. Planning Stage 中的 UI 需求分析步骤
3. ui_checklist.md 的生成要求和格式规范
4. Action Stage 中使用 ui_checklist.md 作为核对清单的要求

**Evidence**： 
用户明确要求调整 AI 代理工作流程，当读取到 rule_ui_instructions.md 时：
- 在 Planning Stage 结合目录分析用户 UI 实际需求
- 在进入 Action Stage 前生成 ui_checklist.md
- ui_checklist.md 包含：UI 生成形式、拟生成 UI 列表、需要重构的 UI 列表
- 在 Action Stage 将 ui_checklist.md 作为核对清单

## Evaluation Result：
### rule_ui_instructions.md 更新：在文档中添加 UI 工作流程调整规范
### ui_checklist.md 格式模板：定义 ui_checklist.md 的标准格式和内容要求

spec mode logging
