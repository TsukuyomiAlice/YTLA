# data_manager 数据文件管理功能 - 产品需求文档

## Overview
为 YTLA `data_power` 特性下的 `data_manager` 模块添加数据文件管理功能，提供对 plan 内数据相关模块（data_manager、data_miner、data_analyzer、data_demonstrator）的数据文件进行展示、上传和删除的操作能力。

## Goals
1. 实现按 plan 维度展示数据文件的列表视图，包含文件所在模块信息
2. 实现安全可靠的数据文件上传与持久化存储
3. 实现已上传文件的删除功能，确保仅能删除上传路径下的文件

## Non-Goals
- 不涉及文件的编辑或内容预览功能
- 不涉及文件搜索或过滤功能（文件名和模块维度）
- 不实现批量上传或批量删除
- 不涉及用户权限校验
- 不实现文件内容解析或数据导入
- 不涉及跨 plan 的文件浏览

## Background & Context
data_manager 模块位于 `data_power` 特性的 modules 下，是整个 data_power 特性的数据管理中枢。当前 data_manager 仅有基础的项目骨架（`__init__.py` 桩文件），没有实际的业务功能。

根据 `core/classic` 架构参考，YTLA 项目采用 Flask Blueprint 模式，按 routes → process → dao 三层架构组织代码。plan 和 module 通过 SQLite 数据库关联，每个 module 通过 `belong_plan_id` 关联到 plan，通过 `module_sub_type` 标识子类型（如 data_manager、data_miner 等）。

本功能将遵循 classic 的代码模式和约定，为 data_manager 模块添加完整的数据文件管理能力。

## Functional Requirements

### FR-1: 展示数据文件列表

**描述**：用户可以通过 API 获取指定 plan 下所有数据相关模块（data_manager、data_miner、data_analyzer、data_demonstrator）存储的数据文件列表。

**接口规范**：
- **Method**: `GET`
- **Path**: `/data_manager/files`
- **Query Parameters**: `plan_id` (int, required) - 目标 plan 的 ID
- **Response**:
```json
{
  "success": true,
  "files": [
    {
      "file_name": "example.xlsx",
      "file_path": "plan_1/module_5/20260702120000/example.xlsx",
      "file_size": 1024000,
      "upload_time": "20260702120000",
      "module_id": 5,
      "module_name": "my_data_manager"
    }
  ]
}
```

**处理逻辑**：
1. 根据 `plan_id` 查询该 plan 下所有 active 的 module
2. 筛选出 `module_sub_type` 为 `data_manager`、`data_miner`、`data_analyzer`、`data_demonstrator` 的 module
3. 遍历每个 module 对应的数据存储目录（`{DATA_STORAGE_PATH}/plan_{plan_id}/module_{module_id}/`）
4. 递归读取目录下的所有文件，提取文件名、上传时间、文件大小等信息
5. 将文件信息与对应的 module_id、module_name 组合返回

### FR-2: 上传数据文件

**描述**：用户可以向指定 module 上传数据文件。接受常见数据文件格式，并存储在约定的路径结构中。

**接口规范**：
- **Method**: `POST`
- **Path**: `/data_manager/upload`
- **Request Body**: `multipart/form-data`
  - `file` (file, required) - 上传的文件
  - `module_id` (int, required) - 目标 module 的 ID
- **Accepted File Types**: `.xlsx`, `.xls`, `.csv`, `.json`, `.db`, `.sqlite`, `.sqlite3`
- **Response**:
```json
{
  "success": true,
  "file_info": {
    "file_name": "data.xlsx",
    "file_path": "plan_1/module_5/20260702120000/data.xlsx",
    "module_id": 5,
    "upload_time": "20260702120000"
  }
}
```

**处理逻辑**：
1. 验证请求中包含文件和 module_id
2. 验证文件扩展名在白名单中
3. 通过 module_id 获取 module 信息，验证 module 存在且属于 data_manager/data_miner/data_analyzer/data_demonstrator 类型
4. 获取 module 的 `belong_plan_id`
5. 构造存储路径：`{DATA_STORAGE_PATH}/plan_{plan_id}/module_{module_id}/{YYYYmmDDHHMMSS}/`
6. 使用 `werkzeug.utils.secure_filename` 处理文件名安全性
7. 保存文件到目标路径
8. 返回文件信息

### FR-3: 删除已上传的数据文件

**描述**：用户可以根据文件路径删除已上传的数据文件。仅限于删除存储在 FR-2 约定路径下的文件。

**接口规范**：
- **Method**: `POST`
- **Path**: `/data_manager/files/delete`
- **Request Body**: `application/json`
```json
{
  "file_path": "plan_1/module_5/20260702120000/data.xlsx"
}
```
- **Response**:
```json
{
  "success": true,
  "message": "文件删除成功"
}
```

**处理逻辑**：
1. 验证请求中包含 file_path
2. **安全性校验**：验证 file_path 是否在允许的存储路径范围内（`{DATA_STORAGE_PATH}/plan_{plan_id}/module_{module_id}/`）
3. 验证路径不能包含 `..` 等路径穿越字符
4. 验证目标文件是否存在
5. 执行文件删除操作
6. 删除后验证文件是否已被删除
7. 返回操作结果

## Non-Functional Requirements

- **安全性**：文件上传路径必须防止路径穿越攻击；删除操作必须验证文件路径在允许范围内
- **可靠性**：文件上传失败时应返回明确错误信息，不产生脏数据
- **可维护性**：遵循 classic 架构的代码模式（routes/process/dao 分离）
- **日志记录**：使用已有 `@router_log` 和 `@process_log` 装饰器记录操作日志

## Constraints

- 存储路径基础目录通过应用配置 `DATA_STORAGE_PATH` 指定
- 文件类型白名单严格限定
- 文件大小限制遵循框架默认或可通过配置调整

## Assumptions

- data_manager 模块已正确注册到 Flask 应用
- DATA_STORAGE_PATH 在应用配置中已定义
- plan 和 module 数据已存在于数据库中
- 文件系统具有读写权限

## Acceptance Criteria

### AC-1: 获取空数据文件列表
- **Given**: 指定 plan 下没有任何数据模块，或数据模块尚无上传文件
- **When**: 调用 `GET /data_manager/files?plan_id=1`
- **Then**: 返回 `{"success": true, "files": []}`
- **Verification**: `programmatic`
- **Notes**: 空列表而非错误响应

### AC-2: 获取包含数据文件的列表
- **Given**: 指定 plan 下有 data_manager 和 data_miner 模块，且各模块已有上传文件
- **When**: 调用 `GET /data_manager/files?plan_id=1`
- **Then**: 返回的 files 列表包含所有文件，每个文件条目包含 file_name、file_path、file_size、upload_time、module_id、module_name
- **Verification**: `programmatic`

### AC-3: 不包含非数据类模块的文件
- **Given**: 指定 plan 下有 data_manager 和 其他类型（如 timer）的模块
- **When**: 调用 `GET /data_manager/files?plan_id=1`
- **Then**: 只返回 data_manager 等数据类模块的文件，不包含其他类型模块的文件
- **Verification**: `programmatic`

### AC-4: 成功上传数据文件
- **Given**: 上传一个合法的 .xlsx 文件到指定的 data_manager 模块
- **When**: 调用 `POST /data_manager/upload` 携带 file 和 module_id
- **Then**: 返回 success=true，文件存储在 `{DATA_STORAGE_PATH}/plan_{plan_id}/module_{module_id}/{timestamp}/` 路径下，文件名被安全处理
- **Verification**: `programmatic`

### AC-5: 拒绝非法文件类型
- **Given**: 上传一个 .exe 文件到 data_manager 模块
- **When**: 调用 `POST /data_manager/upload`
- **Then**: 返回 `{"success": false, "error": "不支持的文件类型"}`
- **Verification**: `programmatic`

### AC-6: 成功删除已上传文件
- **Given**: 某个文件已存在于上传路径下
- **When**: 调用 `POST /data_manager/files/delete` 携带该文件的 file_path
- **Then**: 返回 success=true，文件从文件系统中删除
- **Verification**: `programmatic`

### AC-7: 拒绝路径穿越删除请求
- **Given**: 删除请求包含 `../../` 等路径穿越字符
- **When**: 调用 `POST /data_manager/files/delete`
- **Then**: 返回 `{"success": false, "error": "非法的文件路径"}`
- **Verification**: `programmatic`

### AC-8: 拒绝删除非上传路径下的文件
- **Given**: 删除请求指向 `DATA_STORAGE_PATH` 范围之外的文件
- **When**: 调用 `POST /data_manager/files/delete`
- **Then**: 返回 `{"success": false, "error": "文件不在可删除范围内"}`
- **Verification**: `programmatic`

### AC-9: 上传文件到非数据类模块时拒绝
- **Given**: module_id 对应的模块 sub_type 不是 data_manager/data_miner/data_analyzer/data_demonstrator
- **When**: 调用 `POST /data_manager/upload`
- **Then**: 返回 `{"success": false, "error": "目标模块不是数据模块"}`
- **Verification**: `programmatic`

## Open Questions

1. 是否需要在删除空目录时清理 timestamp 目录？
2. 是否需要有文件大小的限制？若需要，限制值应为多少？
3. DATA_STORAGE_PATH 的默认值应如何配置？
4. 是否需要对上传文件进行病毒扫描或内容校验？
spec mode logging
