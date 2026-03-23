Harness Instructions file version: rule_harness_instructions.md  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec   `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md` 
 以我提供给你的这本文档作为参考标准 
 忘记.trae/spec目录，这里被禁用了 
 这次我们要厘清关于对PRD文档使用write方法的规则   
 我们规定：  
 对spec, tasks, checklist文档，遵循旧规则，依然优先使用write覆盖的方式更新  
 对origin, actions文档，由于新的内容不会对旧的内容产生影响，所以总是在文档末尾换行添加  
 在完成规则修改的基础上，特别需要对“常见陷阱和避免方法”章节进行梳理和修订

## Analyze：
**Given**： rule_harness_instructions.md 文档作为参考标准，.trae/spec 目录被禁用  
**Target**： 厘清关于对 PRD 文档使用 write 方法的规则，规定 spec/tasks/checklist 文档使用 write 覆盖更新，origin/actions 文档使用末尾追加更新，并对“常见陷阱和避免方法”章节进行梳理和修订  
**Evidence**： 用户明确规定了不同文档类型的更新方式：spec、tasks、checklist 文档优先使用 write 覆盖方式更新；origin、actions 文档总是在文档末尾换行添加。同时要求对“常见陷阱和避免方法”章节进行梳理和修订。

## Evaluation Result：
### 规则文档更新： 更新 rule_harness_instructions.md 中关于 PRD 文档 write 方法的规定
### 陷阱章节修订： 梳理和修订“常见陷阱和避免方法”章节，确保与新的 write 方法规则一致