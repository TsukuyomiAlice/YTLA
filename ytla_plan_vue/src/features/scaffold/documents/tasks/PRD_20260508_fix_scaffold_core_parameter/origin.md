Harness Instructions file version: rule_harness_instructions_ver_ide.md
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
目标： `d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card` `d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module` 
现在的脚手架在前端向后端发送请求时有一个对请求内容的误解（参考 `d:\YTLA\ytla_plan_vue\src\features\scaffold\documents\tasks\PRD_20260428_scaffold_frontend_creation` ）： 
正确的理解应该如下 
参数type和subtype在is_core的取值不同时，代表的含义不同  
当is_core为True时，type_name代表版本名（当前恒为"classic"），sub_type_name代表在core下的类型名  
所以，对应在前端： 
如果is_core为False，没有问题； 
如果is_core为True，则应该把type_name设定为version_name(classic)，structure设定为用户在页面上的"类型名称"处输入的内容，sub_type_name则不变 

现在的改动需求如下： 
修改上面描述的问题，并且： 
    当用户选择Core模块的情况下，"类型名称"改变为"模块名称"；Feature模块的情况下则保持"类型名称" 
并且需要同步修改参数传递逻辑 
整个修改不改动后端

## Analyze:
**Given**: 
- 现有 create_card 和 create_module 两个模块
- 现有实现中，当 is_core 为 true 时，参数传递逻辑错误
- 需要修改 store 中的 submitForm 方法
- 需要修改 UI 组件，根据 isCore 动态显示标签
- 需要更新国际化文件

**Target**: 
- 修复参数传递逻辑：当 isCore 为 true 时，type_name='classic'，structure=用户输入值
- 动态修改 UI 标签：Core模块显示"模块名称"，Feature模块显示"类型名称"
- 更新两个模块的国际化文件

**Evidence**: 
- 查看 scaffoldCardStore.ts 和 scaffoldModuleStore.ts，当前 structure 固定为 'cards' 或 'modules'
- 查看 Create_cardMain_00.vue 和 Create_moduleMain_00.vue，当前标签是硬编码的
- 查看国际化文件，缺少"模块名称"的翻译

---

spec mode logging
