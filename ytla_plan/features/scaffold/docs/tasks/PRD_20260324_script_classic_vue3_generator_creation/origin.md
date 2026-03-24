Harness Instructions file version: rule_harness_instructions.md  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec  `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md` 
 这个分析可以接受  
 现在需要你生成一些代码了  
 你应该注意到了， `d:\YTLA\ytla_plan\generator\moduleGenerator.py` 里包含了一些前端相关的生成内容  
 但是这些代码已经过时了  
 你能根据我们分析的结果制作一些生成器吗？ 
 你现在只需要制作生成器，不用立刻在相关文件内集成调用  
 生成器的路径和文件名规则如下：  
 生成到 `d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\script` 目录内 
 文件名规则： 
 script_classic_vue3_[vue3内的模组名]_sidecard_generator.py  
 script_classic_vue3_[vue3内的模组名]_module_generator.py

## Analyze：
**Given**： 之前的分析报告显示 scaffold 模块结构，frontend_vue3 模块包含 15 种生成器，general_classic 模块是协调器。早期脚本 moduleGenerator.py 已过时。
**Target**： 基于分析结果制作新的生成器脚本，放置在 general_classic/script 目录内，文件名符合特定规则。
**Evidence**： 用户明确要求制作生成器，提供了文件名规则和放置目录，并说明不用立即集成调用。

## Evaluation Result：
### 生成器脚本： 为 classic vue3 制作 sidecard_generator 和 module_generator 脚本，放置在 general_classic/script 目录内，文件名符合 script_classic_vue3_[vue3内的模组名]_sidecard_generator.py 和 script_classic_vue3_[vue3内的模组名]_module_generator.py 规则。

# Dialogue 2

## User Requirement: 
先纠正一下，不是模组(agile, timer这类）  
 而是组件类型（指components, composables这些）  
 并且文件名也应该更改： 
 script_classic(版本名)_vue3(程序语言/框架名)_sidecard_[components(前端组件名)]_generator.py 
 script_classic(版本名)_vue3(程序语言/框架名)_modules_[components(前端组件名)]_generator.py

## Analyze：
**Given**： 用户澄清之前的误解，不是针对模组（agile, timer 等），而是针对组件类型（components, composables 等）。文件名规则也更新了。
**Target**： 更新生成器设计，针对组件类型（如 components、composables、stores 等）而不是模组。更新文件名规则。
**Evidence**： 用户明确澄清了组件类型和文件名规则的变化。

## Evaluation Result：
### 更新后的生成器脚本： 为 classic 版本的 vue3 框架制作 sidecard 和 modules 结构的生成器脚本，针对前端组件类型（如 components、composables 等），文件名符合 script_classic_vue3_sidecard_[components]_generator.py 和 script_classic_vue3_modules_[components]_generator.py 规则。

spec mode logging