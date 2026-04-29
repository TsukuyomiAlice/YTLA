Harness Instructions file version: rule_harness_instructions_ver_ide.md
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
为 `d:\YTLA\ytla_plan\features\scaffold` 创建对应的前端功能 `d:\YTLA\ytla_plan_vue\src\features\scaffold` ，包含两个子模组 `d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card` 和 `d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module`   
前端页面的页面创建方式可参考其它已有的页面，例如 `d:\YTLA\ytla_plan_vue\src\features\language` `d:\YTLA\ytla_plan_vue\src\features\mathematics`   
create_card和create_module的功能相似，要求用户选择生成的模组隶属于core还是feature，选择ytla的版本（当前默认为classic），并在页面上输入类别名type_name和子类别名sub_type_name，最后选择是否生成前端/后端  
并且，需要集成到后端，通过调用后端的 `d:\YTLA\ytla_plan\features\scaffold\modules\general_classic\process\processGenerateStructure.py` 完成实际的脚手架生成  
 
在这段对话内容下，你的目标是生成一份完整的项目设计文档prj_checklist.md，放在PRD目录内，其中应详细记载每一个需要新生成的文件的名称，生成位置，用途，包含的函数，用途  
你并不在这次对话内容下实际生成相关代码  
你需要实际生成两个PRD，分别对应前端和后端的相关内容

## Analyze:
**Given**: 
- 前端已有基础文件结构（create_card和create_module模块已存在部分空文件）
- 已有language和mathematics模块作为完整参考实现
- 需要实现两个功能相似的模块：create_card和create_module
- 需要与后端API集成
- 参考模块包含完整的components、flows、registries、stores、services、locales、avatar等结构

**Target**: 
- 完善create_card和create_module两个模块的所有文件
- 实现用户界面：选择core/feature、输入type_name、sub_type_name、选择前后端生成
- 集成后端API调用
- 遵循现有模块的架构模式

**Evidence**: 
- 参考language模块的dictionary子模块实现
- 现有文件大多为空，需要完整实现
- create_card和create_module功能相似，可以共享部分逻辑

## Evaluation Result:
### create_card模块需要完善的文件:
- components/Create_cardMain_00.vue - 主界面组件
- components/Create_cardSub_00.vue - 子界面组件
- services/scaffoldCardService.ts - API服务
- stores/scaffoldCardStore.ts - 状态管理
- flows/create_cardFlowManager.ts - 流程管理
- registries/create_cardModuleConfig.ts - 模块配置
- registries/registries.ts - 注册配置
- locales/zh.json - 中文语言包
- locales/en.json - 英文语言包
- avatar/Avatar.vue - 头像组件

### create_module模块需要完善的文件:
- components/Create_moduleMain_00.vue - 主界面组件
- components/Create_moduleSub_00.vue - 子界面组件
- services/scaffoldModuleService.ts - API服务
- stores/scaffoldModuleStore.ts - 状态管理
- flows/create_moduleFlowManager.ts - 流程管理
- registries/create_moduleModuleConfig.ts - 模块配置
- registries/registries.ts - 注册配置
- locales/zh.json - 中文语言包
- locales/en.json - 英文语言包
- avatar/Avatar.vue - 头像组件

---

spec mode logging
