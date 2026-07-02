本任务进度: 已完成

# data_miner 数据挖掘与处理模组 - 实现计划

## [x] Task 1: 创建 data_miner 模块的 Blueprint 和路由配置
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - 在 `routes/routeDataMiner.py` 中定义 `data_miner_bp` Blueprint
  - 定义三个 API 路由：
    - `GET /data_miner/source_files` - 列出原始数据文件（FR-1）
    - `POST /data_miner/process` - 分析处理指定数据文件（FR-2）
    - `GET /data_miner/processed_files` - 列出已处理数据文件（FR-3）
  - 使用 `@router_log` 装饰器记录操作日志
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-10, AC-11
- **Test Requirements**:
  - `programmatic` TR-1.1: Blueprint 变量名符合 `*_bp` 命名约定，可被自动发现注册
  - `programmatic` TR-1.2: 三条路由的 URL 映射正确可用
- **Notes**: 参考 `routeDataFiles.py` 和 `routeModuleFundInfo.py` 的代码模式

## [x] Task 2: 实现 DAO 层 - sqlite 数据库操作
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - 在 `dao/daoDataMiner.py` 中实现通用的 sqlite 数据库操作方法
  - 方法包括：
    - `create_table_from_dataframe(db_path, df, table_name)` - 从 pandas DataFrame 创建表并写入数据
    - `execute_cursor(db_name, sql, params)` - 通用参数化查询执行
    - `drop_table(db_path, table_name)` - 删除表
    - `get_table_info(db_path, table_name)` - 获取表结构信息
  - 使用 `core.classic.frame.database.func.sqliteConnector` 或原生 sqlite3
- **Acceptance Criteria Addressed**: AC-3, AC-4, AC-5, AC-6
- **Test Requirements**:
  - `programmatic` TR-2.1: 能从 DataFrame 正确创建 sqlite 表并写入数据
  - `programmatic` TR-2.2: 表字段类型和名称与 DataFrame 列信息一致
- **Notes**: 参考 `daoFundInfo.py` 的代码模式

## [x] Task 3: 实现 Script 层 - 不同文件格式的分析脚本
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - 在 `script/scriptDataMiner.py` 中实现按文件类型区分的分析功能
  - 支持的文件类型和方法：
    - `read_xlsx(file_path)` - 使用 `pandas.read_excel()` 读取 xlsx/xls 文件，返回按 sheet 组织的 DataFrame 字典
    - `read_csv(file_path)` - 使用 `pandas.read_csv()` 读取 csv 文件，返回 DataFrame
    - `read_json(file_path)` - 使用 `pandas.read_json()` 或 `json.load()` 读取 json 文件，判断是否可展平为表格
    - `read_db(file_path)` - 使用 `sqlite3.connect()` 连接 db 文件，提取所有表名和数据
  - 每个方法返回统一结构：`{"success": bool, "data": {...}, "format_type": "relational" | "non_relational", "metadata": {...}}`
  - 包含数据粗分逻辑：分析数据是关系型表格还是非关系型结构
- **Acceptance Criteria Addressed**: AC-3, AC-4, AC-5, AC-6, AC-9
- **Test Requirements**:
  - `programmatic` TR-3.1: 每种文件类型都能正确读取
  - `programmatic` TR-3.2: 不支持的扩展名返回错误
- **Notes**: 参考 `scriptFundInfo.py` 和 `scriptFundHistory.py` 的代码模式

## [x] Task 4: 实现 Process 层 - 数据处理主流程
- **Priority**: P0
- **Depends On**: Task 1, Task 2, Task 3
- **Description**:
  - 在 `process/processDataMiner.py` 中实现核心业务逻辑
  - 功能方法：
    - `get_source_files(plan_id)` - 获取原始数据文件列表（FR-1），参考 `processDataFiles.get_data_files()`
    - `process_data_file(plan_id, source_file_path, module_id)` - 处理数据文件主流程（FR-2）
    - `get_processed_files(plan_id)` - 获取已处理文件列表（FR-3）
  - `process_data_file` 的核心流程：
    1. 验证源文件路径合法性（防穿越、存在性校验）
    2. 根据文件扩展名调用对应的 script 方法读取数据
    3. 执行数据清洗（空值处理、列名标准化、重复行处理）
    4. 判断输出格式：关系型→sqlite .db，非关系型→.json
    5. 生成输出文件路径并保存
    6. 返回处理结果信息
  - 数据清洗规则（FR-5）：
    - 去除完全为空的列和行
    - 列名去除首尾空格，转为英文大写
    - 去除完全重复的行
    - 统计并返回数据基本信息
  - 使用 `@process_log` 装饰器
- **Acceptance Criteria Addressed**: AC-1~AC-12
- **Test Requirements**:
  - `programmatic` TR-4.1: 正确处理四种文件类型并保存结果
  - `programmatic` TR-4.2: 路径穿越请求被拒绝
  - `programmatic` TR-4.3: 不存在源文件返回错误
  - `programmatic` TR-4.4: 数据清洗逻辑正确执行
- **Notes**: 
  - 参考 `processDataFiles.py` 和 `processModuleFundInfo.py` 的代码模式
  - 输出文件路径格式：`{DATA_SOURCE_PATH}/plan_{plan_id}/module_{module_id}/{timestamp}/{sanitized_filename}.db|.json`
  - 数据清洗在 process 层统一执行，script 层只负责读取和粗分

## [x] Task 5: 验证所有功能并更新文档
- **Priority**: P1
- **Depends On**: Task 4
- **Description**:
  - 验证所有 API 路由可正确响应
  - 验证四种文件类型的处理流程完整可用
  - 验证数据清洗逻辑正确执行
  - 验证安全性校验（路径穿越、不支持文件类型）正常工作
  - 验证空数据场景的返回符合预期
  - 更新 checklist.md 标记已验证项
- **Acceptance Criteria Addressed**: AC-1 ~ AC-12
- **Test Requirements**:
  - `programmatic` TR-5.1: 所有验收标准可验证
- **Notes**: 最终验收

# Task Dependencies
- [Task 1] P0 - 无依赖
- [Task 2] P0 - 无依赖（可并行执行）
- [Task 3] P0 - 无依赖（可并行执行）
- [Task 4] P0 - 依赖 Task 1, Task 2, Task 3
- [Task 5] P1 - 依赖 Task 4

# 并行执行说明
- Task 1、Task 2、Task 3 相互独立，可并行执行
- Task 4 需在 Task 1/2/3 完成后执行
- Task 5 需在 Task 4 完成后执行
spec mode logging
