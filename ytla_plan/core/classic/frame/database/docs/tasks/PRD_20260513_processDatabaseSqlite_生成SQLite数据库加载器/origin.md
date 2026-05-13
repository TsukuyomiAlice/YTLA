Harness Instructions file version: rule_harness_instructions_ver_ide.md (1.7)  
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md` `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_for_ytla.md`   
 目标: 生成 `d:\YTLA\ytla_plan\core\classic\frame\database\process\processDatabaseSqlite.py`   
 需求:  
 1 仿照 `d:\YTLA\ytla_plan\core\classic\frame\router\process\processRouter.py` 的方式，做一个针对于sqlite的指定db数据库的加载器  
 启动服务时加载，加载后得到一个dict类型的字段  
 这个字段原先是在 `d:\YTLA\ytla_plan\core\classic\frame\_type\func\utilConfigs.py` 里的db_files  
 2 将 `d:\YTLA\ytla_plan\core\classic\frame\_type\func\utilConfigs.py` 里关于sqlite database的代码复制到这里，但是不要对源文件做改动   
 3 关于读取配置的方法，在后端区域内的utils目录下扫描config_database_sqlite.py文件，将其中的db_files内容全部收集到一起  
 4 在 `d:\YTLA\ytla_plan\app.py` 里对应地添加上能够获取db_files的方法

## Analyze：
**Given**: 
- 现有代码库中有 processRouter.py 作为参考示例
- utilConfigs.py 中包含 db_files 配置和数据库路径相关函数
- 项目中已存在多个 config_database_sqlite.py 文件
- app.py 是应用入口文件
- sqliteConnector.py 是数据库连接工具

**Target**: 
- 创建 processDatabaseSqlite.py，仿照 processRouter.py 的方式
- 实现启动时加载所有数据库配置的功能
- 不修改 utilConfigs.py 原文件
- 更新 app.py 添加加载调用
- 更新 sqliteConnector.py 使用新的加载器

**Evidence**: 
- processRouter.py 展示了如何扫描和动态加载模块
- utilConfigs.py 中有 get_db_folder_path() 和 db_files 配置
- 项目中已有三个 config_database_sqlite.py 作为示例
- sqliteConnector.py 当前从 utilConfigs 获取 db_files

## Evaluation Result：
### processDatabaseSqlite.py: 实现数据库配置扫描和加载功能
### app.py: 添加数据库配置加载调用
### sqliteConnector.py: 修改为从 processDatabaseSqlite.py 获取 db_files

# Dialogue 2

## User Requirement: 
你忘记记录action和origin了  
另外我有补充的内容  
把 `d:\YTLA\ytla_plan\core\classic\frame\_type\func\sqliteConnector.py` 中读取db_files的方式改成在 `d:\YTLA\ytla_plan\core\classic\frame\database\process\processDatabaseSqlite.py` 里读取已经收集到的db_files  
这意味着 `d:\YTLA\ytla_plan\core\classic\frame\_type\func\sqliteConnector.py` 中不是从app.py获取db_files的信息，app.py只负责在启动时完成读取db_files信息的过程

## Analyze：
**Given**: 
- 需要创建完整的规划文档（origin.md、actions.md 等）
- sqliteConnector.py 当前从 utilConfigs 获取 db_files
- app.py 只负责启动时加载，不负责传递给其他模块

**Target**: 
- 补充完整的 harness 规范文档
- 更新需求，明确 sqliteConnector.py 的修改方式
- processDatabaseSqlite.py 应该维护一个全局的 db_files，供 sqliteConnector.py 直接导入使用

**Evidence**: 
- sqliteConnector.py 的 database_root 函数从 utilConfigs.db_files 获取配置
- 需要改为从 processDatabaseSqlite.db_files 获取
- app.py 只调用加载函数，不负责传递配置

## Evaluation Result：
### sqliteConnector.py: 修改导入源从 processDatabaseSqlite 获取 db_files
### processDatabaseSqlite.py: 提供全局的 db_files 变量供导入

spec mode logging
