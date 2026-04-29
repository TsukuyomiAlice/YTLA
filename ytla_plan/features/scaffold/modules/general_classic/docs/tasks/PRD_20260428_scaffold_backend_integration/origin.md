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
- 后端已有 `processGenerateStructure.py` 函数可以生成脚手架
- 已有多个现有模块的实现可作为参考（language、mathematics等）
- 前端已有基础文件结构（create_card和create_module模块已存在基础文件）
- 已有路由实现示例（llm_caller）
- 需要创建两个PRD（后端和前端）

**Target**: 
- 创建后端PRD：包含后端API接口、数据类型、路由等
- 创建前端PRD：包含前端组件、服务、存储等
- 生成详细的prj_checklist.md，列出所有需要生成的文件

**Evidence**: 
- 后端已有的 `processGenerateStructure.py` 函数需要API包装
- 前端现有文件大多为空，需要完整实现
- 参考模块的结构清晰，可遵循相同模式

## Evaluation Result:
### 后端PRD: 
- origin.md - 原始需求文档
- spec.md - 产品需求文档
- tasks.md - 实现计划
- checklist.md - 验证清单
- actions.md - 行动记录
- prj_checklist.md - 项目设计文档

### 前端PRD:
- origin.md - 原始需求文档
- spec.md - 产品需求文档
- tasks.md - 实现计划
- checklist.md - 验证清单
- actions.md - 行动记录
- prj_checklist.md - 项目设计文档

---

# Dialogue 2

## User Requirement: 
我看过你的文档了  
前端的部分没有问题  
后端的部分你做复杂了，按以下要求去改：  
你只需要实际生成两个文件即可  
在process下生成一个processGenerator，用来调用processGenerateStructure  
在routes下生成一份blueprint，只用来负责调用processGenerator  
所有的业务处理全部在processGeneerator内实现

## Analyze:
**Given**: 
- 已有的后端PRD文档过于复杂
- 用户要求简化设计
- 已有processGenerateStructure.py可直接调用

**Target**: 
- 简化后端PRD设计
- 只需要两个文件：processGenerateScaffold.py和routeScaffold.py
- 所有业务处理在processGenerateScaffold内实现

**Evidence**: 
- 用户明确要求简化
- 只需要process下一个文件，routes下一个文件

## Evaluation Result:
### 后端PRD（简化后）: 
- origin.md - 原始需求文档（已更新）
- spec.md - 产品需求文档（已简化）
- tasks.md - 实现计划（已简化）
- checklist.md - 验证清单（已简化）
- actions.md - 行动记录（已更新）
- prj_checklist.md - 项目设计文档（已简化，只列出两个文件）

---

spec mode logging
