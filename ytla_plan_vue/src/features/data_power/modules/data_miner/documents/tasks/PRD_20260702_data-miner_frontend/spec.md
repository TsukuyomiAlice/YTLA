# data_miner 前端页面 Spec

## Why
为 data_miner 模块提供可视化页面，使用户能在同一界面中查看 data_manager 原始数据文件和 data_miner 已处理数据文件，并执行分析、查看、删除等操作。

## What Changes

### 前端（Vue）
- **新增** service 层：`data_minerService.ts` — 封装后端 API 调用
- **新增** store 层：`data_minerStore.ts` — Pinia 状态管理
- **重写** Main 组件：`Data_minerMain_00.vue` — 统一的文件列表表格
- **重写** Sub 组件：`Data_minerSub_00.vue` — 已处理文件的详情展示
- **重写** `Data_minerMain.vue` — 调用 FlowManager 的调度容器
- **重写** `Data_minerSub.vue` — 调用 FlowManager 的调度容器
- **更新** `locales/zh.json` 和 `en.json` — 国际化文本
- **更新** `registries.ts` — 注册 Sub 组件路由
- **更新** `data_minerFlowManager.ts` — 管理 Main/Sub 状态

### 后端（Flask）
- **新增** `GET /data_miner/view` — 查看已处理文件的详细内容
- **新增** `DELETE /data_miner/delete` — 删除已处理文件
- **修改** `GET /data_miner/source_files` — 返回数据增加文件大小字段
- **修改** `GET /data_miner/processed_files` — 返回数据增加加工时间、数据来源等前端需要的字段

## Impact
- 前端 data_miner 模组的所有 Vue 文件将获得实质性内容
- 后端 data_miner 模组需新增 2 个路由和对应 process/dao 方法
- 与 data_manager 前端模式保持一致的架构

## Requirements

### FR-1: 文件列表展示
系统 SHALL 在 main 区域展示两类文件：同一 plan 下 data_manager 模组的原始数据文件，以及 data_miner 自身已处理的数据文件。

#### Scenario: 正常加载
- **WHEN** 用户进入 data_miner 页面
- **THEN** 系统同时请求 source_files 和 processed_files 接口
- **AND** 将两类文件合并展示在统一表格中
- **AND** 每行包含：文件名、模组ID、数据来源、大小、生成时间、操作按钮

### FR-2: 操作区分
系统 SHALL 根据文件来源显示不同的操作按钮。

#### Scenario: 原始文件操作
- **WHEN** 文件来源为 data_manager（原始数据）
- **THEN** 操作列显示"分析"按钮

#### Scenario: 已处理文件操作
- **WHEN** 文件来源为 data_miner（已处理数据）
- **THEN** 操作列显示"查看"和"删除"两个按钮

### FR-3: 分析功能
系统 SHALL 支持对原始数据文件触发行分析处理。

#### Scenario: 点击分析
- **WHEN** 用户点击原始文件的"分析"按钮
- **THEN** 系统调用 `POST /data_miner/process` 接口
- **AND** 处理完成后刷新文件列表
- **AND** 新生成的分析文件出现在已处理文件列表

### FR-4: 查看功能
系统 SHALL 在 sub 区域展示已处理文件的详细内容。

#### Scenario: 点击查看
- **WHEN** 用户点击已处理文件的"查看"按钮
- **THEN** 系统调用 `GET /data_miner/view` 接口
- **AND** 在 sub 区域展示文件内容详情
- **AND** sub 区域最上方显示 return to dashboard 按钮

### FR-5: 删除功能
系统 SHALL 支持删除已处理的数据文件。

#### Scenario: 点击删除
- **WHEN** 用户点击已处理文件的"删除"按钮
- **THEN** 系统调用 `DELETE /data_miner/delete` 接口
- **AND** 删除成功后刷新文件列表

### FR-6: 后端新增接口
系统 SHALL 在现有后端基础上新增 view 和 delete 接口。

#### Scenario: View 接口
- **WHEN** 前端请求 `GET /data_miner/view?plan_id=X&file_path=Y`
- **THEN** 后端读取对应文件内容并返回
- **AND** 对于 .db 文件，读取并返回表中数据
- **AND** 对于 .json 文件，读取并返回 JSON 内容

#### Scenario: Delete 接口
- **WHEN** 前端请求 `DELETE /data_miner/delete` 携带 `plan_id` 和 `file_path`
- **THEN** 后端删除对应文件及同目录下的 `.meta.json` 文件
- **AND** 返回操作结果

### FR-7: Sub 区域
系统 SHALL 在 sub 区域展示被查看文件的详细内容。

#### Scenario: Sub 区域显示
- **WHEN** sub 区域激活
- **THEN** 显示被查看文件的完整数据内容
- **AND** 顶部有 return to dashboard 按钮
- **AND** 点击 return 按钮后关闭 sub 区域，返回 main 区域
spec mode logging
