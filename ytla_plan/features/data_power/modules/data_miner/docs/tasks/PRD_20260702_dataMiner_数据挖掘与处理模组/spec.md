# data\_miner 数据挖掘与处理模组 - 产品需求文档

## Overview

为 YTLA `data_power` 特性下的 `data_miner` 模块添加数据挖掘与处理功能，提供从 `data_manager` 模块读取原始数据、按数据类型进行智能分析处理、并将处理结果归档保存到结构化存储中的完整能力。

## Goals

1. 实现按 plan 维度列出 data\_manager 模块下所有原始数据文件的能力
2. 实现根据用户选择的数据文件，按文件类型采用不同分析方案进行处理
3. 实现数据拆分、清洗、重新整理、归档与保存的完整流程
4. 关系型数据保存为 sqlite 数据库文件，非关系型数据保存为 json 文件
5. 能够输出本模块下已保存的处理结果信息（数据文件、数据格式、数据来源等）

## Non-Goals

* 不涉及对 data\_miner 之外的其他模块的数据处理

* 不实现实时数据流处理（仅处理已存储的静态文件）

* 不实现数据可视化或图表展示

* 不实现数据导出到外部系统

* 不实现批量分析任务调度（一次只处理一个文件）

* 不实现用户权限校验

* 不实现数据的修改编辑功能（仅读取、清洗、保存）

## Background & Context

data\_miner 模块位于 `data_power` 特性的 modules 下，是 data\_power 特性的数据分析中枢。data\_manager 已实现了数据文件的展示、上传和删除功能，数据文件存储在 `DATA_SOURCE_PATH/plan_{plan_id}/module_{module_id}/{timestamp}/{filename}` 路径下。

data\_miner 需要从 data\_manager 的模块目录中读取原始数据，利用 pandas 进行数据处理分析，然后将分析结果保存到 data\_miner 自身的模块目录下，形成结构化的分析结果。

目前 data\_miner 仅有基础的项目骨架（`__init__.py` 桩文件），没有实际的业务功能。

## Functional Requirements

### FR-1: 列出原始数据文件列表

**描述**：用户可以通过 API 获取指定 plan 下所有 data\_manager 模块存储的原始数据文件列表，供用户选择需要处理的数据文件。

**接口规范**：

* **Method**: `GET`

* **Path**: `/data_miner/source_files`

* **Query Parameters**: `plan_id` (int, required) - 目标 plan 的 ID

* **Response**:

```json
{
  "success": true,
  "files": [
    {
      "file_name": "example.xlsx",
      "file_path": "plan_1/module_5/20260702120000/example.xlsx",
      "file_size": 1024000,
      "upload_time": "2026-07-02 12:00:00",
      "module_id": 5,
      "module_name": "my_data_manager",
      "file_type": "xlsx"
    }
  ]
}
```

**处理逻辑**：

1. 根据 `plan_id` 查询该 plan 下所有 module
2. 筛选出 `module_sub_type` 为 `data_manager` 的 module
3. 遍历每个 data\_manager module 对应的数据存储目录（`{DATA_SOURCE_PATH}/plan_{plan_id}/module_{module_id}/`）
4. 递归读取目录下的所有文件，提取文件名、上传时间、文件大小等信息
5. 将文件信息与对应的 module\_id、module\_name 组合返回

### FR-2: 分析处理指定数据文件

**描述**：用户选择指定的原始数据文件后，系统根据文件类型采用合适的分析方案进行处理，包括数据读取、粗分、拆分、清洗、整理、归档保存。

**接口规范**：

* **Method**: `POST`

* **Path**: `/data_miner/process`

* **Request Body**: `application/json`

```json
{
  "plan_id": 1,
  "source_file_path": "plan_1/module_5/20260702120000/example.xlsx",
  "module_id": 99
}
```

* **Response**:

```json
{
  "success": true,
  "result": {
    "source_file": "plan_1/module_5/20260702120000/example.xlsx",
    "source_file_type": "xlsx",
    "output_file_path": "plan_1/module_99/20260702123000/example.db",
    "output_file_type": "db",
    "output_format": "sqlite",
    "record_count": 150,
    "processed_at": "2026-07-02 12:30:00"
  }
}
```

**处理逻辑**：

1. 验证请求参数：plan\_id、source\_file\_path、module\_id
2. 验证源文件存在于正确的 data\_manager 模块目录下
3. 根据文件扩展名选择对应的分析脚本（script layer）
4. 通过 script 层读取和粗分原始数据（使用 pandas）
5. 在 process 层进行数据拆分、清洗、重新整理
6. 判断数据类型：

   * 关系型数据（结构化表格数据）→ 保存为 sqlite .db 文件

   * 非关系型数据（嵌套/非结构化数据）→ 保存为 json 文件
7. 生成输出文件到：`{DATA_SOURCE_PATH}/plan_{plan_id}/module_{module_id}/{timestamp}/{原始文件名}.db` 或 `.json`

### FR-3: 列出已处理数据文件

**描述**：用户可以获取指定 plan 下 data\_miner 模块自身已保存的处理结果文件列表。

**接口规范**：

* **Method**: `GET`

* **Path**: `/data_miner/processed_files`

* **Query Parameters**: `plan_id` (int, required) - 目标 plan 的 ID

* **Response**:

```json
{
  "success": true,
  "files": [
    {
      "file_name": "example.db",
      "file_path": "plan_1/module_99/20260702123000/example.db",
      "file_size": 204800,
      "processed_time": "2026-07-02 12:30:00",
      "source_file": "plan_1/module_5/20260702120000/example.xlsx",
      "output_format": "sqlite",
      "module_id": 99,
      "module_name": "my_data_miner"
    }
  ]
}
```

**处理逻辑**：

1. 根据 `plan_id` 查询该 plan 下所有 module
2. 筛选出 `module_sub_type` 为 `data_miner` 的 module
3. 遍历每个 data\_miner module 对应的数据存储目录
4. 递归读取目录下的 .db 和 .json 文件
5. 从目录结构中解析处理时间和关联的源文件信息
6. 返回文件列表

### FR-4: 数据文件类型与对应分析方案

**描述**：不同文件类型使用不同的分析脚本方案进行数据处理。

| 文件类型              | 读库方式               | 分析方案                      | 输出格式                         |
| ----------------- | ------------------ | ------------------------- | ---------------------------- |
| xlsx/xls          | pandas.read\_excel | 读取所有sheet，逐sheet分析结构化表格数据 | sqlite .db                   |
| csv               | pandas.read\_csv   | 读取CSV数据，分析列结构和数据类型        | sqlite .db                   |
| json              | pandas.read\_json  | 分析JSON结构，展平嵌套数据           | json（保持原格式）或 sqlite .db（展平后） |
| db/sqlite/sqlite3 | sqlite3.connect    | 连接数据库，提取所有表结构和数据          | sqlite .db                   |

**处理逻辑**（script 层）：

1. xlsx/xls：使用 `pandas.read_excel()` 读取，遍历所有 sheet，对每个 sheet 进行数据清洗
2. csv：使用 `pandas.read_csv()` 读取，自动检测分隔符，进行数据清洗
3. json：使用 `pandas.read_json()` 或 `json.load()` 读取，判断是否为表格型数据
4. db/sqlite/sqlite3：使用 `sqlite3` 模块连接，提取表结构、表名和数据

### FR-5: 数据清洗和处理规则

**描述**：对所有读取的数据执行标准化清洗流程。

**处理规则**：

1. 空值处理：去除全部为空的列/行，填充可选空值
2. 列名标准化：去除列名首尾空格，统一为英文大写（参考 investment 模组的命名风格）
3. 数据类型推断：使用 pandas 自动推断列数据类型
4. 重复数据：标记或去除完全重复的行
5. 数据统计：记录总行数、列数、每列非空值数量等基本信息

## Non-Functional Requirements

* **安全性**：文件路径必须防止路径穿越攻击，所有文件操作限定在 DATA\_SOURCE\_PATH 范围内

* **可靠性**：处理失败时应返回明确错误信息，不产生脏数据

* **可维护性**：遵循 classic 架构（routes/process/dao/script 分离），script 层按文件类型分离逻辑

* **日志记录**：使用已有的 `@router_log` 和 `@process_log` 装饰器记录操作日志

* **兼容性**：兼容 pandas 支持的各类数据结构（DataFrame、Series 等）

## Constraints

* 存储路径基础目录通过应用配置 `DATA_SOURCE_PATH` 指定

* 仅支持 data\_manager 模块已上传的原始文件格式（xlsx, xls, csv, json, db, sqlite, sqlite3）

* 使用 pandas 作为主要数据处理库

* sqlite 数据库操作使用 `core.classic.frame.database.func.sqliteConnector` 或原生 sqlite3

## Assumptions

* data\_miner 模块已正确注册到 Flask 应用

* DATA\_SOURCE\_PATH 在应用配置中已定义

* plan 和 module 数据已存在于数据库中

* 文件系统具有读写权限

* pandas 库已安装可用

* 用户传入的 module\_id 是 data\_miner 类型模块的 ID

## Acceptance Criteria

### AC-1: 列出 data\_manager 模块的原始数据文件

* **Given**: 指定 plan 下有 data\_manager 模块且已有上传的原始数据文件

* **When**: 调用 `GET /data_miner/source_files?plan_id=1`

* **Then**: 返回的 files 列表包含所有 data\_manager 模块下的文件信息（file\_name、file\_path、file\_size、file\_type、module\_id、module\_name）

* **Verification**: `programmatic`

* **Notes**: 仅返回 module\_sub\_type 为 data\_manager 的模块文件

### AC-2: 空数据文件列表

* **Given**: 指定 plan 下没有 data\_manager 模块，或 data\_manager 模块尚无上传文件

* **When**: 调用 `GET /data_miner/source_files?plan_id=1`

* **Then**: 返回 `{"success": true, "files": []}`

* **Verification**: `programmatic`

### AC-3: 成功处理 xlsx 文件并输出 sqlite

* **Given**: data\_manager 模块下有一个合法的 .xlsx 文件

* **When**: 调用 `POST /data_miner/process` 指定该文件的 source\_file\_path

* **Then**: 返回 success=true，处理后的 .db 文件保存在 data\_miner 模块目录下，文件内容包含原始数据

* **Verification**: `programmatic`

* **Notes**: 验证输出文件路径格式正确，sqlite 数据库可正常打开查询

### AC-4: 成功处理 csv 文件并输出 sqlite

* **Given**: data\_manager 模块下有一个合法的 .csv 文件

* **When**: 调用 `POST /data_miner/process` 指定该文件的 source\_file\_path

* **Then**: 返回 success=true，处理后的 .db 文件保存在 data\_miner 模块目录下

* **Verification**: `programmatic`

### AC-5: 成功处理 json 文件并输出 json 或 sqlite

* **Given**: data\_manager 模块下有一个合法的 .json 文件

* **When**: 调用 `POST /data_miner/process` 指定该文件的 source\_file\_path

* **Then**: 返回 success=true，处理后的 .json（非结构化）或 .db（表格型）文件保存在 data\_miner 模块目录下

* **Verification**: `programmatic`

### AC-6: 成功处理 sqlite/db 文件并输出 sqlite

* **Given**: data\_manager 模块下有一个合法的 .db 文件

* **When**: 调用 `POST /data_miner/process` 指定该文件的 source\_file\_path

* **Then**: 返回 success=true，处理后的 .db 文件保存在 data\_miner 模块目录下

* **Verification**: `programmatic`

### AC-7: 拒绝非法文件路径

* **Given**: 请求的 source\_file\_path 包含 `../` 等路径穿越字符

* **When**: 调用 `POST /data_miner/process`

* **Then**: 返回 `{"success": false, "error": "非法的文件路径"}`

* **Verification**: `programmatic`

### AC-8: 拒绝不存在的源文件

* **Given**: 请求的 source\_file\_path 指向一个不存在的文件

* **When**: 调用 `POST /data_miner/process`

* **Then**: 返回 `{"success": false, "error": "源文件不存在"}`

* **Verification**: `programmatic`

### AC-9: 拒绝不支持的源文件类型

* **Given**: 请求的 source\_file\_path 扩展名不在支持列表中（如 .exe、.pdf）

* **When**: 调用 `POST /data_miner/process`

* **Then**: 返回 `{"success": false, "error": "不支持的文件类型"}`

* **Verification**: `programmatic`

### AC-10: 列出 data\_miner 已处理文件

* **Given**: data\_miner 模块下已有处理完成的数据文件

* **When**: 调用 `GET /data_miner/processed_files?plan_id=1`

* **Then**: 返回的 files 列表包含所有 data\_miner 模块下的处理结果文件，包含 output\_format、source\_file 等信息

* **Verification**: `programmatic`

### AC-11: 空处理结果列表

* **Given**: 指定 plan 下 data\_miner 模块尚无处理结果文件

* **When**: 调用 `GET /data_miner/processed_files?plan_id=1`

* **Then**: 返回 `{"success": true, "files": []}`

* **Verification**: `programmatic`

### AC-12: 数据处理包含数据清洗步骤

* **Given**: 一个包含空值、重复行、不规范列名的原始数据文件

* **When**: 调用 `POST /data_miner/process` 处理该文件

* **Then**: 输出的结果数据中空值被处理、重复行被标记或去除、列名经过标准化

* **Verification**: `programmatic`

* **Notes**: 通过查询输出文件内容验证清洗效果

## Open Questions

1. data\_miner 模块的 Blueprint 注册路径（url\_prefix）应该如何设定？
2. 对于超大文件的处理是否需要分块或限制文件大小？
3. 输出 sqlite 文件的表名如何生成？使用原始文件名 sanitized 版本？
4. data\_miner 模块的 module\_sub\_type 值是否是 `data_miner`？需要确认数据库中的枚举值。
5. 是否需要在处理结果中保留原始数据文件的完整路径和上传时间？
   spec mode logging

