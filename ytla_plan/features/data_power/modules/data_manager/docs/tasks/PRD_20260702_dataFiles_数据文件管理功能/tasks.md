本任务进度: 未完成

> 2026-07-02 修正: 按 PRD 规格修正 FR-2 上传接口（移除 plan_id 参数依赖，从 module 数据派生 belong_plan_id）

# data_manager 数据文件管理功能 - 实现计划

## [x] Task 1: 创建 data_manager 模块的 Blueprint 和配置入口
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - 在 `routes/routeDataFiles.py` 中定义 `data_manager_bp` Blueprint（已创建）
  - 通过自动动态 Blueprint 扫描机制注册（`register_dynamic_blueprints` 自动发现）
- **Acceptance Criteria Addressed**: None (基础设施)
- **Test Requirements**:
  - `programmatic` TR-1.1: Blueprint 变量名符合 `*_bp` 命名约定，可被自动发现
  - `programmatic` TR-1.2: DATA_STORAGE_PATH 可配置且默认值有效
- **Notes**: ✅ 已完成，经确认自动注册机制完全正确

## [x] Task 2: 实现文件列表展示功能 (route + process)
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - `routes/routeDataFiles.py` 已实现 `GET /data_manager/files` 路由
  - `process/processDataFiles.py` 已实现文件列表查询的业务逻辑
  - 按 plan_id 查询并筛选子类型为 data_manager/data_miner/data_analyzer/data_demonstrator 的模块
  - 递归扫描模块数据目录获取文件列表
  - 返回包含 file_name、file_path、file_size、upload_time、module_id、module_name 的响应
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3
- **Test Requirements**:
  - `programmatic` TR-2.1: 空目录返回空列表
  - `programmatic` TR-2.2: 包含文件时返回正确的文件信息
  - `programmatic` TR-2.3: 只返回数据类模块的文件，过滤非数据类模块
- **Notes**: ✅ 已完成，与 PRD 规格完全一致

## [x] Task 3: 修正文件上传功能使其符合 PRD 规格 (route + process)
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - **路由修正**：`POST /data_manager/upload` 路由仅接受 `file` + `module_id` 参数，移除 `plan_id` 参数
  - **业务逻辑修正**：上传 process 函数改为从 module 数据（`belong_plan_id`）派生 `plan_id`
  - 实现方式：在 process 中查询 module 信息获取 `belong_plan_id`，替代从请求参数获取 `plan_id`
  - 文件类型白名单校验保持不变（xlsx, xls, csv, json, db, sqlite, sqlite3）
  - 存储路径格式保持不变：`{DATA_STORAGE_PATH}/plan_{plan_id}/module_{module_id}/{timestamp}/`
  - 使用 `werkzeug.utils.secure_filename` 处理文件名
- **Acceptance Criteria Addressed**: AC-4, AC-5, AC-9
- **Test Requirements**:
  - `programmatic` TR-3.1: 合法文件上传成功并存储在正确路径（plan_id 从 module 派生）
  - `programmatic` TR-3.2: 非法类型文件上传被拒绝
  - `programmatic` TR-3.3: 上传到非数据类模块被拒绝
  - `programmatic` TR-3.4: 不传递 plan_id 参数仍能正确上传
- **Notes**: 
  - 这是关键修正：现有代码要求 `plan_id` 从请求表单传入，但 PRD 规格要求从 module 的 `belong_plan_id` 派生
  - 使用 `daoModules.get_modules()` 无参数调用获取所有模块，按 module_id 查找目标模块，从中提取 `belong_plan_id`

## [x] Task 4: 实现文件删除功能 (route + process)
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - `routes/routeDataFiles.py` 已实现 `POST /data_manager/files/delete` 路由
  - `process/processDataFiles.py` 已实现删除业务逻辑
  - 路径安全性校验已实现（防穿越、范围限制）
  - 文件删除后验证结果
- **Acceptance Criteria Addressed**: AC-6, AC-7, AC-8
- **Test Requirements**:
  - `programmatic` TR-4.1: 合法文件路径成功删除
  - `programmatic` TR-4.2: 路径穿越请求被拒绝
  - `programmatic` TR-4.3: 超出存储范围的路径被拒绝
  - `programmatic` TR-4.4: 不存在的文件路径返回适当错误
- **Notes**: ✅ 已完成，与 PRD 规格完全一致

## [x] Task 5: 验证所有功能并更新文档
- **Priority**: P1
- **Depends On**: Task 3
- **Description**:
  - 验证 Task 3 修正后不影响其他功能
  - 更新 spec.md（如有必要）
  - 更新 checklist.md 标记已验证项
- **Acceptance Criteria Addressed**: AC-1 ~ AC-9
- **Test Requirements**:
  - `programmatic` TR-5.1: 所有验收标准可验证
- **Notes**: 最终验收

# Task Dependencies
- [Task 1] ✅ 已完成
- [Task 2] ✅ 已完成（依赖 Task 1）
- [Task 3] 待执行（依赖 Task 1）
- [Task 4] ✅ 已完成（依赖 Task 1）
- [Task 5] 待执行（依赖 Task 3）
spec mode logging
