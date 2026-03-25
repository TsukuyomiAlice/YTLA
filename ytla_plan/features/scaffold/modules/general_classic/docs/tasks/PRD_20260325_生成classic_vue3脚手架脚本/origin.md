Harness Instructions file version: rule_harness_instructions.md v1.7  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md`   
 参考文档: `d:\YTLA\ytla_plan\generator\moduleGenerator.py`   
 目标: 
 1  在 `d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\script`   里生成一些自动化脚手架的脚本：  
 这些脚本适用于core为classic，前端框架为vue3的模组的初始化 
 文件名格式为 
 script_[core_name，这里为classic]_[program_language,这里为vue3]_[模组类型名，本次为sidecard和module]_[组件目录名].py  
 举例:  
 script_classic_vue3_sidecard_components.py (表示用于生成一个sidecard的component组件的vue文件)  
 script_classic_vue3_sidecard_composables.py (表示用于生成一个sidecard的composables组件的ts文件)  
 可用于参照的已有模组：  
 module类型: `d:\YTLA\ytla_plan_vue\src\features\basic\modules\definition`  sideCard类型: `d:\YTLA\ytla_plan_vue\src\features\sample\cards\sample1` 
 另外，具体的模板文档的格式标准，可以参考 `d:\YTLA\ytla_plan_vue\src\core\classic\cards\sideCard` 以及针对它的分析  
 在你正式生成之前，你需要先做2份小结：  
 针对sideCard的脚手架空模板文件包括的种类，以及可以生成的模组和规范空代码    
 针对module的脚手架空模板文件包括的种类，以及可以生成的模组和规范空代码  
 只有在这两份文档由我确认通过之后，才进行目标脚本文件的生成

## Analyze：
**Given**： rule_harness_instructions.md, moduleGenerator.py, sideCard 模组, module 模组 (definition), sample1 模组  
**Target**： 在 script 目录生成自动化脚手架脚本，用于初始化 core=classic、前端框架=vue3 的模组（sidecard 和 module 类型），先生成两份小结文档供用户确认  
**Evidence**： 用户明确要求先做两份小结文档，确认通过后再生成脚本；文件名格式为 script_classic_vue3_[模组类型]_[目录名].py

## Evaluation Result：
### temp_summary_sidecard.md： SideCard 脚手架空模板文件小结（Markdown 格式）
### temp_summary_module.md： Module 脚手架空模板文件小结（Markdown 格式）
### origin.md： 原始需求文档
### spec.md： 产品需求文档
### tasks.md： 实现计划
### checklist.md： 验证清单
### actions.md： 行动记录

# Dialogue 2

## User Requirement: 
做的不错，但是上一轮你忘记在harness模式下执行了  
把上一步的内容都补好  
然后，docs文件是不用生成的，因为在scaffold目录里，已经有docs相关的生成方法了  
另外再追加一些标准：  
你可以调查后发现，对于一个具体的feature，在cards目录和modules目录下，会有一个_type目录  
其中，在definitions目录里，也包含cardDataType.ts和cardType.ts  
再分析下

## Analyze：
**Given**： 之前的小结文档，sample/cards/_type 目录，basic/modules/_type 目录  
**Target**： 补全 harness 模式下的内容，更新小结文档（去掉 docs 相关，添加 _type 目录标准），生成完整的规划文档  
**Evidence**： 用户指出需要补全 harness 模式；docs 文件不用生成；需要添加 _type 目录的标准（包含共享的类型定义和注册表）

## Evaluation Result：
### 已更新 temp_summary_sidecard.md： 包含 _type 目录结构，去掉 docs 相关内容
### 已更新 temp_summary_module.md： 包含 _type 目录结构，去掉 docs 相关内容
### origin.md： 追加 Dialogue 2
### spec.md： 产品需求文档
### tasks.md： 实现计划
### checklist.md： 验证清单
### actions.md： 追加 ACT-3 和 Dialogue 2

# Dialogue 3

## User Requirement: 
我看到你在sideCard的主组件模板里，script部分里出现了handleEdit  
这里有一个希望追加的规范：  
对于生成的vue文件的的script部分，期望只出现： 
prop和emit的代码  
其它的函数应该通过composables等具体的函数调用获取（即只写import）

## Analyze：
**Given**： 之前的小结文档，新的Vue组件脚本规范  
**Target**： 更新小结文档，Vue文件script部分只保留 prop 和 emit 的代码，其他函数通过 composables 获取  
**Evidence**： 用户明确要求追加此规范

## Evaluation Result：
### 已更新 temp_summary_sidecard.md： 添加Vue组件脚本规范，更新组件模板和composable模板
### origin.md： 追加 Dialogue 3

spec mode logging
