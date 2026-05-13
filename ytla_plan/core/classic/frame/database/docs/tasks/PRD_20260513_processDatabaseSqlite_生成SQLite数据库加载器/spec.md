# SQLite 数据库加载器 - Product Requirement Document

## Overview
- **Summary**: 仿照 processRouter.py 的方式，创建一个针对 SQLite 的数据库配置加载器，用于在服务启动时加载所有模块的数据库配置，并合并为一个统一的 db_files 字典。同时修改 sqliteConnector.py 使用新的加载器。
- **Purpose**: 解耦数据库配置管理，允许各个模块独立定义自己的数据库配置，通过统一的加载器进行整合。
- **Target Users**: 后端开发者、模块维护者

## Goals
- 创建 processDatabaseSqlite.py，提供统一的数据库配置加载功能
- 从 utilConfigs.py 复制相关数据库配置代码，但不修改原文件
- 扫描后端区域内所有 config_database_sqlite.py 文件，收集所有 db_files
- 在 app.py 中添加加载 db_files 的调用
- 修改 sqliteConnector.py，使其从 processDatabaseSqlite.py 读取 db_files
- processDatabaseSqlite.py 维护全局的 db_files 变量供其他模块导入

## Non-Goals (Out of Scope)
- 不修改 utilConfigs.py 文件
- 不实现数据库连接逻辑（仅加载配置）
- 不涉及数据库操作的 DAO 层
- app.py 不负责传递 db_files 给其他模块

## Background & Context
- 现有系统中，数据库配置集中在 utilConfigs.py 的 db_files 字段
- 需要将配置分散到各个模块的 config_database_sqlite.py 中
- processRouter.py 提供了类似的动态加载和扫描模式，可以作为参考
- sqliteConnector.py 当前从 utilConfigs 读取 db_files，需要改为从 processDatabaseSqlite 读取
- app.py 只负责启动时加载，不传递给其他模块

## Functional Requirements
- **FR-1**: 提供扫描后端区域内 config_database_sqlite.py 文件的功能
- **FR-2**: 从所有找到的配置文件中收集 db_files 并合并
- **FR-3**: 保留 utilConfigs.py 中的默认数据库配置
- **FR-4**: 在 app.py 中添加加载 db_files 的调用
- **FR-5**: processDatabaseSqlite.py 提供全局的 db_files 变量供导入
- **FR-6**: 修改 sqliteConnector.py 从 processDatabaseSqlite.py 读取 db_files

## Non-Functional Requirements
- **NFR-1**: 加载过程高效，不影响服务启动性能
- **NFR-2**: 代码结构清晰，易于维护和扩展
- **NFR-3**: 遵循现有项目的代码风格和架构模式

## Constraints
- **Technical**: Python, Flask
- **Business**: 保持向后兼容，不影响现有功能
- **Dependencies**: 依赖 config.py 获取后端目录路径

## Assumptions
- 所有 config_database_sqlite.py 文件都位于各自模块的 utils 目录下
- 所有 config_database_sqlite.py 文件都定义了 db_files 字典
- 配置文件命名统一为 config_database_sqlite.py
- processDatabaseSqlite.py 的 db_files 会在 app.py 启动时初始化完成加载

## Acceptance Criteria

### AC-1: 数据库配置加载器创建完成
- **Given**: 目标目录 d:\YTLA\ytla_plan\core\classic\frame\database\process\ 已存在
- **When**: processDatabaseSqlite.py 文件创建并实现完整功能
- **Then**: 文件包含扫描、收集、合并 db_files 的所有必要函数，并提供全局的 db_files 变量
- **Verification**: programmatic

### AC-2: 正确扫描并收集所有配置文件
- **Given**: 项目中存在多个 config_database_sqlite.py 文件
- **When**: 调用加载器的扫描和收集功能
- **Then**: 所有模块的 db_files 都被正确收集
- **Verification**: programmatic

### AC-3: utilConfigs.py 中的配置被正确复制和保留
- **Given**: utilConfigs.py 中存在数据库配置代码
- **When**: processDatabaseSqlite.py 实现完成
- **Then**: utilConfigs.py 中的数据库配置代码被复制到新文件中，且原文件未被修改
- **Verification**: human-judgment

### AC-4: app.py 中添加加载 db_files 的调用
- **Given**: app.py 已存在
- **When**: 在 app.py 中添加相应的导入和调用
- **Then**: app.py 在启动时调用加载函数完成 db_files 的加载
- **Verification**: programmatic

### AC-5: sqliteConnector.py 从 processDatabaseSqlite.py 读取 db_files
- **Given**: sqliteConnector.py 已存在
- **When**: 修改 sqliteConnector.py 的导入
- **Then**: sqliteConnector.py 从 processDatabaseSqlite.db_files 读取数据库配置
- **Verification**: programmatic

## Open Questions
- 无
