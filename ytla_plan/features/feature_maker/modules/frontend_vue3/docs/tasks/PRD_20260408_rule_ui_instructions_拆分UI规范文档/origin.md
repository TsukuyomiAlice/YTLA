Harness Instructions file version: rule_harness_instructions_ver_ide.md  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md` 
 目标: `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md` 
 一共有两个任务，现在是第一个 
 在保持原文档内容没有丢失，理解不受到影响的前提下，将rule_ui_instructions.md拆分为两个文档: 
 新的文档 rule_ui_standards.md专注于提供vue3 / ts / scss规范文档的示例 
 原文档则保留具体的规则和关注点

## Analyze：
**Given**： 
- 现有文档：rule_ui_instructions.md
- 目标：拆分文档为两个部分
- 约束：保持原文档内容不丢失，理解不受影响

**Target**： 
- 创建新文档 rule_ui_standards.md，专注于 Vue3/TS/SCSS 规范示例
- 保留原文档 rule_ui_instructions.md，专注于具体规则和关注点

**Evidence**： 
- 用户明确要求拆分文档
- 具体说明了两个新文档的职责分工

## Evaluation Result：
### 新文档 rule_ui_standards.md： 专注于提供 Vue3/TS/SCSS 规范文档的示例
### 原文档 rule_ui_instructions.md： 保留具体的规则和关注点



# Dialogue 2

## User Requirement: 
我希望的是，这两个文档之间并没有交叉引用的内容 
换而言之，拆分后的两个文档，新的standard专注于怎么具体写代码，instructions则专注于怎么设计代码

## Analyze：
**Given**： 
- 已有的拆分计划
- 用户追加的新要求：两个文档之间没有交叉引用

**Target**： 
- rule_ui_standards.md 专注于怎么具体写代码（代码示例）
- rule_ui_instructions.md 专注于怎么设计代码（规则和关注点）
- 两个文档之间没有交叉引用

**Evidence**： 
- 用户明确说明两个文档之间不应该有交叉引用
- 明确了两个文档的职责：standard 是代码示例，instructions 是设计规则

## Evaluation Result：
### rule_ui_standards.md： 专注于怎么具体写代码（代码示例）
### rule_ui_instructions.md： 专注于怎么设计代码（规则和关注点）
### 补充要求： 两个文档之间没有交叉引用




# Dialogue 3

## User Requirement: 
好，安全起见，拆分的两个文件用temp_做前缀，保留原始文件，然后就可以执行了

## Analyze：
**Given**： 
- 已有的拆分计划
- 用户追加的安全要求：拆分的文件用 temp_ 做前缀，保留原始文件

**Target**： 
- 创建 temp_rule_ui_standards.md（专注于怎么具体写代码）
- 创建 temp_rule_ui_instructions.md（专注于怎么设计代码）
- 保留原始的 rule_ui_instructions.md 不变
- 两个 temp_ 文档之间没有交叉引用

**Evidence**： 
- 用户明确要求使用 temp_ 前缀
- 用户要求保留原始文件
- 用户同意执行

## Evaluation Result：
### temp_rule_ui_standards.md： 专注于怎么具体写代码（代码示例）
### temp_rule_ui_instructions.md： 专注于怎么设计代码（规则和关注点）
### 原始 rule_ui_instructions.md： 保持不变
### 补充要求： 两个 temp_ 文档之间没有交叉引用

spec mode logging
