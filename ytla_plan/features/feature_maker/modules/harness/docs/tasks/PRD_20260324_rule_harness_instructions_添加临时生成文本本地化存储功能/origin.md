Harness Instructions file version: 1.63  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md`   
 注意：本次执行标准与优化对象都是这本markdown文件  
 我们这次继续优化这本harness模式指引  
 这次是为临时生成文本提供本地化存储  
 当ai生成了包含大规模文本的非目标文件时，允许ai将相关内容存储在PRD目录下，以temp_[ai自行设计标题].md的方式储存，并且将生成的文件名记录在actions.md的标题下方  
 在actions.md中新增一个章节，叫做"Generated Procedure Files List  过程文件列表"，该章节记录ai生成的大规模文本内容文件的文件名（不包含路径）  
 每次新生成中途分析文档时，都用SearchReplace更新这个章节里的内容

## Analyze：
**Given**： rule_harness_instructions.md 文档  
**Target**： 为harness模式指引添加临时生成文本的本地化存储功能，包括temp文件命名规范、在actions.md中添加过程文件列表章节  
**Evidence**： 当ai生成了包含大规模文本的非目标文件时，允许ai将相关内容存储在PRD目录下，以temp_[ai自行设计标题].md的方式储存；在actions.md中新增"Generated Procedure Files List  过程文件列表"章节，记录文件名；每次新生成中途分析文档时，用SearchReplace更新这个章节

## Evaluation Result：
### rule_harness_instructions.md： 更新文档，添加临时生成文本本地化存储功能规范


# Dialogue 2

## User Requirement: 
顺带再强化一下actions.md的记录要求，可能有的已经出现在rule文档里了  
 1 Todo列表 也应该在第一次生成时被记录在actions.md里，并且带上完整的task内容 
 2 sub-agent的调用操作也应明确地被记录在actions.md里

## Analyze：
**Given**： rule_harness_instructions.md 文档
**Target**： 强化 actions.md 的记录要求，包括：1) Todo列表第一次生成时记录完整 task 内容；2) sub-agent 调用操作明确记录
**Evidence**： 用户明确要求强化这两个方面的记录要求

## Evaluation Result：
### rule_harness_instructions.md： 更新文档，强化 actions.md 的记录要求

spec mode logging

