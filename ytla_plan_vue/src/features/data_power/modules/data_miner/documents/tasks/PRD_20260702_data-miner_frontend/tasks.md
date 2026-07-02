# Tasks
- [ ] Task 1: 创建前端 Service 层 — 封装所有后端 API 调用
  - [ ] SubTask 1.1: 创建 `data_minerService.ts`，包含 `getSourceFiles`/`getProcessedFiles`/`processFile`/`viewProcessedFile`/`deleteProcessedFile` 方法
- [ ] Task 2: 创建前端 Store 层 — Pinia 状态管理
  - [ ] SubTask 2.1: 创建 `data_minerStore.ts`，管理文件列表、当前查看文件、sub 激活状态
- [ ] Task 3: 实现 Main 区域组件 — 文件列表表格
  - [ ] SubTask 3.1: 重写 `Data_minerMain_00.vue`，实现统一的文件列表表格
  - [ ] SubTask 3.2: 分别对原始文件显示"分析"按钮，对已处理文件显示"查看"和"删除"按钮
  - [ ] SubTask 3.3: 重写 `Data_minerMain.vue` 作为调度容器
- [ ] Task 4: 实现 Sub 区域组件 — 文件详情展示
  - [ ] SubTask 4.1: 重写 `Data_minerSub_00.vue`，展示文件内容并包含 return 按钮
  - [ ] SubTask 4.2: 重写 `Data_minerSub.vue` 作为调度容器
- [ ] Task 5: 更新 FlowManager / Locales / Registries
  - [ ] SubTask 5.1: 重写 `data_minerFlowManager.ts`，管理 Main/Sub 切换和当前查看文件状态
  - [ ] SubTask 5.2: 更新 `locales/zh.json` 和 `en.json`
  - [ ] SubTask 5.3: 更新 `registries.ts` 注册 Sub_00 组件
- [ ] Task 6: 修改后端 — 新增 view 和 delete 接口
  - [ ] SubTask 6.1: 在 `routeDataMiner.py` 新增 `/data_miner/view` 和 `/data_miner/delete` 路由
  - [ ] SubTask 6.2: 在 `processDataMiner.py` 新增 `view_processed_file` 和 `delete_processed_file` 方法
  - [ ] SubTask 6.3: 在 `daoDataMiner.py` 新增 `query_table_data` 方法（读取 db 表数据）
- [ ] Task 7: 验证所有功能

# Task Dependencies
- [Task 3] depends on [Task 1, Task 2, Task 5]
- [Task 4] depends on [Task 1, Task 2, Task 5]
- [Task 6] 可与 Task 1-5 并行执行
- [Task 7] depends on [Task 3, Task 4, Task 5, Task 6]
