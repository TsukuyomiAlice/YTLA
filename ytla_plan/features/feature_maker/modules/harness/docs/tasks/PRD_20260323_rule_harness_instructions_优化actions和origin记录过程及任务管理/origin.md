Harness Instructions file version: rule_harness_instructions.md v1.4  
Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md` 
 将本次任务视作为一个全新的task，你需要直接开启一个新的PRD工程  
 我们要改进和优化对actions.md和origin.md文档的记录过程  
 1 当AI发起对用户的追问时，这一步需要在执行提问之前被记录到actions.md里  
 2 当我们追加内容到actions.md和origin.md里时，直接在文件末尾换行追加，不要重新覆盖写入  
 3 为了优化在Start stage里对PRD文档的检索过程，我们将在tasks.md的第一行添加这样一行内容：  
 ```markdown  
 本任务进度: [已完成/未完成] 
 ``` 
 这样，在以后的任务的Start stage，如果有PRD目录，就以此作为判断依据  
 如果显示已完成，或者不存在本行内容，那么都视作该PRD工程已经完成了  
 4 我们调整任务完成的依据  
 当所有任务执行的最后，以AI主动发起提问的形式判断本次任务是否全部完成  
 如果用户确认已完成，则完成最后的更新工作（包括记录用户回复已完成，tasks.md第一行更新为已完成等） 
 5 actions.md中，需要将向用户发起提问的操作记录下来，该记录应在提问之前进行

## Analyze：
**Given**： rule_harness_instructions.md 文档，当前的 harness 模块代码库
**Target**： 改进和优化对 actions.md 和 origin.md 文档的记录过程，包含5个具体改进点
**Evidence**： 用户明确列出了5个需要改进的功能点，包括：AI追问前记录、追加写入而非覆盖、tasks.md第一行添加进度标记、任务完成依据调整为用户确认、提问操作记录在 actions.md

## Evaluation Result：
### 产物1： 更新 rule_harness_instructions.md 文档，记录所有新的规范
### 产物2： 完整的 PRD 规划文档（origin.md、spec.md、tasks.md、checklist.md、actions.md）

# Dialogue 2

## User Requirement: 
确认完成了

## Analyze：
**Given**： AI 已完成所有任务并询问用户确认
**Target**： 确认本次任务全部完成
**Evidence**： 用户明确回复"确认完成了"

## Evaluation Result：
### 最终状态确认： 本次任务已全部完成，tasks.md 第一行将更新为"本任务进度: 已完成"
