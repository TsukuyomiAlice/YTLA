- [x] Checkpoint 1: Task 1 - Blueprint 注册和配置入口已创建
  - [x] Blueprint 变量 `data_manager_bp` 已定义（变量名以 `_bp` 结尾）
  - [x] 动态 Blueprint 扫描机制可自动发现并注册
  - [x] DATA_STORAGE_PATH 配置可获取 (通过 current_app.config)

- [x] Checkpoint 2: Task 2 - 文件列表展示功能
  - [x] `routes/routeDataFiles.py` 包含 `GET /data_manager/files` 路由
  - [x] `process/processDataFiles.py` 包含文件列表查询逻辑
  - [x] 按 plan_id 查询并筛选数据类模块的逻辑正确
  - [x] 文件扫描包含完整文件信息（file_name, file_path, file_size, upload_time, module_id, module_name）
  - [x] 空目录返回空列表

- [x] Checkpoint 3: Task 3 - 文件上传功能（按 PRD 规格修正）
  - [x] `POST /data_manager/upload` 路由仅接受 `file` + `module_id` 参数（无 `plan_id`）
  - [x] `plan_id` 从 module 的 `belong_plan_id` 派生（非请求参数）
  - [x] 文件类型白名单已实现 (xlsx/xls/csv/json/db/sqlite/sqlite3)
  - [x] 存储路径格式正确：`{DATA_STORAGE_PATH}/plan_{plan_id}/module_{module_id}/{timestamp}/`
  - [x] 文件名使用 secure_filename 处理
  - [x] 非法文件类型上传被拒绝
  - [x] 上传到非数据类模块被拒绝

- [x] Checkpoint 4: Task 4 - 文件删除功能
  - [x] `POST /data_manager/files/delete` 路由已创建
  - [x] 路径安全性校验已实现（防穿越）
  - [x] 路径范围校验已实现（限制在存储路径内）
  - [x] 文件删除后验证结果
  - [x] 不存在的文件路径返回正确错误信息

- [x] Checkpoint 5: 日志和错误处理
  - [x] 路由函数使用 `@router_log` 装饰器
  - [x] process 函数使用 `@process_log` 装饰器
  - [x] 所有异常情况有明确的错误返回

- [x] Checkpoint 6: 代码风格一致性
  - [x] 路由遵循 Flask Blueprint 模式
  - [x] process 函数遵循 `process_log` 装饰器模式
  - [x] 代码注释风格与 classic 一致
spec mode logging
