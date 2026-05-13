本任务进度: 已完成

# SQLite 数据库加载器 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 实现 processDatabaseSqlite.py 的核心功能
- **Priority**: P0
- **Depends On**: None
- **Description": 
  - 仿照 processRouter.py 的结构，创建扫描 config_database_sqlite.py 文件的函数
  - 实现从配置文件中收集 db_files 的函数
  - 将 utilConfigs.py 中的数据库配置代码复制过来
  - 实现合并所有 db_files 的功能
  - 提供全局的 db_files 变量供导入
- **Acceptance Criteria Addressed": [AC-1, AC-2, AC-3]
- **Test Requirements":
  - programmatic TR-1.1: 能够正确扫描并找到所有 config_database_sqlite.py 文件
  - programmatic TR-1.2: 能够正确从每个文件中导入并收集 db_files
  - programmatic TR-1.3: 能够正确合并所有 db_files 为一个统一的字典
  - human-judgment TR-1.4: utilConfigs.py 中的数据库配置代码被正确复制，且原文件未被修改
  - programmatic TR-1.5: 提供全局的 db_files 变量供其他模块导入
- **Notes": 参考 processRouter.py 的代码结构和风格

## [x] Task 2: 更新 app.py 添加加载 db_files 的调用
- **Priority": P0
- **Depends On": [Task 1]
- **Description": 
  - 在 app.py 中导入 processDatabaseSqlite 模块
  - 添加调用加载器的代码
  - 确保在服务启动时正确加载
- **Acceptance Criteria Addressed": [AC-4]
- **Test Requirements":
  - programmatic TR-2.1: app.py 能够正确导入并调用加载器
  - programmatic TR-2.2: 服务启动时能够正确加载 db_files
- **Notes": app.py 只负责调用加载函数，不传递 db_files 给其他模块

## [x] Task 3: 修改 sqliteConnector.py 从 processDatabaseSqlite.py 读取 db_files
- **Priority": P0
- **Depends On": [Task 1]
- **Description": 
  - 修改 sqliteConnector.py 的导入
  - 从 processDatabaseSqlite.db_files 读取配置
- **Acceptance Criteria Addressed": [AC-5]
- **Test Requirements":
  - programmatic TR-3.1: sqliteConnector.py 能够正确从 processDatabaseSqlite 导入并使用 db_files
  - programmatic TR-3.2: 数据库连接功能正常工作
- **Notes": 保持向后兼容
