Harness Instructions file version: rule_harness_instructions_ver_ide.md v1.7, rule_harness_instructions_for_ytla.md v1.7
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement:
用户要求为 `data_manager` 模块创建前端(Vue)界面。目标位置为 `d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager`。需要参考 `d:\YTLA\ytla_plan\features\data_power\modules\data_manager` 的后端代码，并参照前端已有架构模式 `d:\YTLA\ytla_plan_vue\src\features\investment`。

具体要求：
1. 前端页面分 main 区域和 sub 区域。在 main 区域上显示所有的文档，并对允许删除的文件提供删除按钮
2. sub 区域需要包含一个回到 dashboard 的按钮（实现方式参照 investment），并另外把上传文件的功能放在 sub 区域里
3. 代码格式参照 investment 模块

## Analyze:
**Given**：
- 后端代码路径：`d:\YTLA\ytla_plan\features\data_power\modules\data_manager`
- 前端目标路径：`d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager`
- 参考架构：`d:\YTLA\ytla_plan_vue\src\features\investment\modules\fund_info`
- Harness 规则文件：`rule_harness_instructions_ver_ide.md` 和 `rule_harness_instructions_for_ytla.md`

**Target**：
- 为 data_manager 模块创建完整的前端代码，包括 Service、Store、Main 组件、Sub 组件，以及更新多语言配置

**Evidence**：
- 后端 API 定义（来自 routeDataFiles.py）：
  - `GET /data_manager/files?plan_id=X` — 返回文件列表（含 file_name, file_path, file_size, upload_time, module_id, module_name）
  - `POST /data_manager/upload` — 上传文件（form-data: file + module_id）
  - `POST /data_manager/files/delete` — 删除文件（JSON: {"file_path": "..."}）
- 前端已有骨架文件：Data_managerMain.vue、Data_managerMain_00.vue、Data_managerSub.vue、Data_managerSub_00.vue（均为空）、data_managerFlowManager.ts、data_managerModuleConfig.ts、registries.ts
- Investment 参考模式：Service → Store → Component（Main_00 + Sub_00）
- 已有字体图标（locales/zh.json、en.json）包含 subtype_name 和 subtype_description

## Evaluation Result：
### 产物 1：dataManagerService.ts
- 形式：API 服务类，位于 `services/` 目录下
- 包含 getFiles、uploadFile、deleteFile 三个方法
- 参照 fundInfoService.ts 的代码格式

### 产物 2：dataManagerStore.ts
- 形式：Pinia store，位于 `stores/` 目录下
- 包含文件列表状态、loading 状态、error 状态
- 包含 fetchFiles、uploadFile、deleteFile 等 actions
- 参照 fundInfoStore.ts 的代码格式

### 产物 3：Data_managerMain_00.vue
- 形式：Main 区域组件
- 功能：显示所有数据文件的列表，对允许删除的文件提供删除按钮
- 参照 Fund_infoMain_00.vue 的代码格式

### 产物 4：Data_managerSub_00.vue
- 形式：Sub 区域组件
- 功能：包含回到 dashboard 的按钮 + 文件上传功能
- 参照 Fund_infoSub_00.vue 和 ReturnToPlanDashboardButton.vue 的代码格式

### 产物 5：locales/zh.json 和 locales/en.json 更新
- 形式：JSON 文件更新
- 内容：添加文件管理相关的 UI 文本标签（如文件列表标题、上传按钮、删除按钮、文件大小等）
spec mode logging
