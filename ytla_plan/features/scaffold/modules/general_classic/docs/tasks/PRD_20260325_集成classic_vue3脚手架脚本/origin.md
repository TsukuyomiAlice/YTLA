Harness Instructions file version: rule_harness_instructions.md v1.7  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec  注意要求： `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md`   
 继续这个task ，并且沿用当前的PRD 
 首先，生成的脚本只保留方法，不要留下执行段  
 然后，看一下现在 `d:\YTLA\ytla_plan\features\scaffold\modules\general_classic`  ，想一下，是不是做个processsGenerateFile_vue3.py，并且适当修改已经存在的 `d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\process\processGenerateStructure.py` ，这样可以一键生成？  
 另外，确认一下目前是怎么确定前后端的语言环境的，  应该是从 `d:\YTLA\ytla_plan\config.py` 里确认的  
 然后，在 `d:\YTLA\ytla_plan\features_test\scaffold\modules\general_classic` 里做一下测试

## Analyze：
**Given**： rule_harness_instructions.md, 已生成的 script_classic_vue3_*.py 脚本, processGenerateStructure.py, frontend_vue3 的实现方式 (constGenerators.py, processGenerateStructure.py), config.py, features_test 目录  
**Target**： 1) 修改已生成的脚本，只保留方法，去掉执行段；2) 创建 const 配置文件定义生成器列表；3) 创建 processGenerateFile_vue3.py 来调用这些脚本；4) 修改 processGenerateStructure.py 实现一键生成；5) 确认前后端语言环境从 config.py 读取；6) 在 features_test 目录做测试  
**Evidence**： 用户明确要求沿用当前PRD，修改脚本去掉执行段，创建 processGenerateFile_vue3.py，修改 processGenerateStructure.py 实现一键生成，从 config.py 确认语言环境，在 features_test 做测试

## Evaluation Result：
### origin.md： 原始需求文档
### spec.md： 产品需求文档
### tasks.md： 实现计划
### checklist.md： 验证清单
### 已修改的 script_classic_vue3_*.py： 只保留方法，去掉执行段
### constGenerators_vue3.py： 定义 classic_vue3 的生成器列表
### processGenerateFile_vue3.py： 调用脚本的 process 文件
### 已修改的 processGenerateStructure.py： 集成 processGenerateFile_vue3.py，实现一键生成
### processGenerateStructureTest.py： 测试用例

spec mode logging
