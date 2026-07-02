本任务进度: 未完成

# Data Manager Frontend - The Implementation Plan (Decomposed and Prioritized Task List)

## [ ] Task 0: 在 _type/ 下创建 ReturnToPlanDashboardButton 组件
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - 在 `data_power/modules/_type/ui/` 下创建 `ReturnToPlanDashboardButton.vue`
  - 在 `data_power/modules/_type/styles/` 下创建 `data-power-manage-button.scss`
  - 参照 investment 模块的实现（`ReturnToPlanDashboardButton.vue` + `investment-manage-button.scss`）
  - 更新 `data_power/modules/_type/locales/zh.json` 和 `en.json` 添加按钮文本
  - 组件功能：点击后调用 panelStore 和 moduleProcessStore 返回 dashboard
- **Acceptance Criteria Addressed**: AC-4
- **Test Requirements**:
  - `human-judgement` TR-0.1: 按钮样式与 data_power 模块风格一致
  - `human-judgement` TR-0.2: 按钮功能与 investment 版本一致
- **Notes**: 文件路径为 `d:\YTLA\ytla_plan_vue\src\features\data_power\modules\_type\ui\ReturnToPlanDashboardButton.vue`

## [ ] Task 1: 创建 dataManagerService.ts API 服务
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - 在 `services/` 目录下创建 `dataManagerService.ts`
  - 参照 `fundInfoService.ts` 的代码格式和风格
  - 实现三个方法：
    - `getFiles(planId: number)` — 调用 `GET /data_manager/files?plan_id=X`
    - `uploadFile(moduleId: number, file: File)` — 调用 `POST /data_manager/upload`（form-data）
    - `deleteFile(filePath: string)` — 调用 `POST /data_manager/files/delete`（JSON body）
  - 每个方法返回 `{ success, data, message }` 结构
  - 使用 `import.meta.env.VITE_API_BASE` 作为 API 基础路径
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3
- **Test Requirements**:
  - `human-judgement` TR-1.1: 代码结构、命名规范与 fundInfoService.ts 一致
  - `human-judgement` TR-1.2: 三个方法的 URL 路径和参数与后端 API 定义匹配
- **Notes**: 文件存放路径为 `d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager\services\dataManagerService.ts`

## [ ] Task 2: 创建 dataManagerStore.ts Pinia Store
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - 在 `stores/` 目录下创建 `dataManagerStore.ts`
  - 参照 `fundInfoStore.ts` 的代码格式和风格
  - State:
    - `files: FileInfo[]` — 文件列表
    - `isLoading: boolean` — 加载状态
    - `error: string | null` — 错误信息
  - Actions:
    - `fetchFiles(planId: number)` — 获取文件列表
    - `uploadFile(moduleId: number, file: File)` — 上传文件并刷新列表
    - `deleteFile(filePath: string)` — 删除文件并刷新列表
    - `clear()` — 清除状态
  - FileInfo 类型定义：fileName, filePath, fileSize, uploadTime, moduleId, moduleName
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3
- **Test Requirements**:
  - `human-judgement` TR-2.1: Store 的 action 调用正确的 service 方法
  - `human-judgement` TR-2.2: 错误处理逻辑完整（try/catch → set error）
- **Notes**: 文件存放路径为 `d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager\stores\dataManagerStore.ts`

## [ ] Task 3: 实现 Data_managerMain_00.vue 主区域组件
- **Priority**: P0
- **Depends On**: Task 2
- **Description**:
  - 实现 main 区域组件，展示所有数据文件
  - 使用 `dataManagerStore` 管理状态
  - 显示字段：文件名、文件大小（格式化显示）、上传时间、所属模块
  - 对每个文件提供删除按钮
  - 包含 loading 状态、空数据状态、错误状态的 UI 处理
  - 文件名格式化为人类可读（使用原始文件名）
  - 文件大小格式化为 KB/MB 单位
  - 上传时间格式化为可读日期
  - 删除按钮点击时调用 store.deleteFile()
  - 组件挂载时自动调用 fetchFiles
  - 参照 Fund_infoMain_00.vue 的代码格式和风格
- **Acceptance Criteria Addressed**: AC-1, AC-2
- **Test Requirements**:
  - `human-judgement` TR-3.1: 组件结构与 Fund_infoMain_00.vue 一致
  - `human-judgement` TR-3.2: 文件列表展示完整（文件名、大小、时间、模块）
  - `human-judgement` TR-3.3: 删除按钮可见且可用
  - `human-judgement` TR-3.4: loading 和 error 状态正确处理
- **Notes**: 
  - 文件存放路径为 `d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager\components\Data_managerMain_00.vue`
  - plan_id 通过 panelStore 获取
  - 样式使用 scoped SCSS，参照 investment 风格

## [ ] Task 4: 实现 Data_managerSub_00.vue 子区域组件
- **Priority**: P0
- **Depends On**: Task 2
- **Description**:
  - 实现 sub 区域组件，包含：
    1. 返回 dashboard 按钮（复用 ReturnToPlanDashboardButton 组件）
    2. 文件上传功能（文件选择 + 上传按钮）
  - 上传功能：
    - 文件选择 input（accept=".xlsx,.xls,.csv,.json,.db,.sqlite"）
    - 上传按钮，调用 store.uploadFile()
    - 上传状态反馈
    - module_id 从当前模块上下文获取
  - 参照 Fund_infoSub_00.vue 的代码格式和风格
- **Acceptance Criteria Addressed**: AC-3, AC-4
- **Test Requirements**:
  - `human-judgement` TR-4.1: 组件结构与 Fund_infoSub_00.vue 一致
  - `human-judgement` TR-4.2: 返回 dashboard 按钮可见并可点击
  - `human-judgement` TR-4.3: 文件上传功能可用
- **Notes**: 
  - 文件存放路径为 `d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager\components\Data_managerSub_00.vue`
  - ReturnToPlanDashboardButton 路径: `@/features/data_power/modules/_type/ui/ReturnToPlanDashboardButton.vue`
  - 上传成功后需要刷新 main 区域的列表（可通过 store 共享状态）

## [ ] Task 5: 更新多语言配置文件
- **Priority**: P1
- **Depends On**: None
- **Description**:
  - 更新 `locales/zh.json`：添加文件管理相关的中文 UI 标签
  - 更新 `locales/en.json`：添加文件管理相关的英文 UI 标签
  - 需要添加的标签：
    - `file_list_title` — 文件列表标题
    - `file_name` — 文件名
    - `file_size` — 文件大小
    - `upload_time` — 上传时间
    - `module_name` — 所属模块
    - `btn_upload` — 上传按钮
    - `btn_delete` — 删除按钮
    - `btn_upload_file` — 选择文件
    - `status_loading` — 加载中
    - `status_no_files` — 暂无文件
    - `status_error` — 加载失败
    - `confirm_delete` — 删除确认提示
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3
- **Test Requirements**:
  - `human-judgement` TR-5.1: 所有新增标签在 zh.json 和 en.json 中对应
  - `human-judgement` TR-5.2: 组件中使用 `$t()` 引用这些标签
- **Notes**: 文件存放路径为 `d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager\locales\zh.json` 和 `en.json`

# Task Dependencies
- Task 2 (Store) 依赖 Task 1 (Service)
- Task 3 (Main 组件) 依赖 Task 2 (Store)
- Task 4 (Sub 组件) 依赖 Task 2 (Store)
- Task 5 (多语言) 没有依赖，可与 Task 1 并行
- Task 3 和 Task 4 可并行执行（均依赖 Task 2）
spec mode logging
