Harness Instructions file version: rule_harness_instructions_ver_ide.md v1.7, rule_harness_instructions_for_ytla.md v1.7
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement:
为 data_power 特性下的 data_miner 模块设计数据挖掘与处理功能。该模组包含以下功能：

1）列出在该 Plan 对应的 data_source 下所有储存在属于 data_manager module 里的原始数据
2）用户选择数据，模组使用合适的方式读取，粗分原始数据，并对数据进行合适地拆分、清洗、重新整理与归档、保存
3）能够输出在本 module 下保存的数据文件、数据格式、数据来源等信息

具体思路：
1. 可输入的数据类型需要参考 data_manager（xlsx, xls, csv, json, db, sqlite, sqlite3）
2. 针对文件类型的不同，选择使用不同的粗分方案并整理数据
3. 可以使用的三方库为 pandas（已安装）
4. 关系型数据库最终使用 sqlite 储存最后的整理结果，非关系型用 json 文件
5. 分析后的文件保存在：/plan_id / module_id / yyyymmddHHMMSS（时间戳） / 原始文件名.db（sqlite 数据库的保存结果） or 原始文件名.json（非关系型数据库的保存结果），文件类型取决于原始数据的文件类型

产物应该包括：
- routes 文件——api 定义
- process 文件——数据处理的主流程
- dao——用于生成 sqlite db 文件
- script——针对不同的文件原始格式进行的分析用脚本

## Analyze:
**Given**：
- 目标模组：features/data_power/modules/data_miner
- 参考模组：features/data_power/modules/data_manager（数据文件管理功能已实现）
- 参考模组：features/investment（完整的三层架构示例：routes/process/dao/script）
- 数据存储路径：DATA_SOURCE_PATH 配置指向的基础目录
- 数据文件存储在：DATA_SOURCE_PATH/plan_{plan_id}/module_{module_id}/{timestamp}/{filename}
- data_manager 已实现的模块子类型：data_manager, data_miner, data_analyzer, data_demonstrator
- 核心架构：Flask Blueprint + routes/process/dao 三层架构
- 已安装三方库：pandas

**Target**：
- 为 data_miner 模块设计完整的数据挖掘与处理功能
- 实现从 data_manager 模块读取原始数据、分析处理、归档保存的完整流程
- 产物包括 routes、process、dao、script 四个层面的文件

**Evidence**：
- data_manager 的 processDataFiles.py 提供了文件列表查询和上传功能，data_miner 需要基于此读取原始数据
- investment 模组展示了 routes/process/dao/script 的完整代码模式
- daoFundInfo.py 展示了 sqlite 数据库操作模式（create_table、drop_table、CRUD）
- 用户明确要求使用 pandas 进行数据处理
- 用户明确要求区分关系型（sqlite）和非关系型（json）数据存储

## Evaluation Result：
### 规划文档：
- origin.md：原始需求记录
- spec.md：产品需求文档
- tasks.md：实现计划
- checklist.md：验证清单
- actions.md：行动记录

### 执行产物：
- routes/routeDataMiner.py：API 路由定义
- process/processDataMiner.py：数据处理主流程
- dao/daoDataMiner.py：sqlite 数据库操作
- script/scriptDataMiner.py：不同文件格式的分析脚本

# Dialogue 2

## User Requirement:
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md` `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md`  `d:\YTLA\ytla_plan\features\data_power\modules\data_miner\docs\tasks\PRD_20260702_dataMiner_数据挖掘与处理模组`
规则文档和prd文档在这里，不要再另外创建了，继续做

## Analyze:
**Given**：
- PRD 文档已存在于指定路径（spec.md、tasks.md、checklist.md、actions.md、origin.md）
- 用户明确要求不要再创建新文档，直接继续执行

**Target**：
- 直接进入 Action Stage，按照 tasks.md 的计划执行代码实现
- 创建 routes/dao/script/process 四个层面的代码文件

**Evidence**：
- spec.md 中定义了 FR-1~FR-5 五个功能需求和 AC-1~AC-12 十二个验收标准
- tasks.md 列出了 5 个实现任务（Task 1~Task 5）
- checklist.md 列出了 14 个验证检查点
- 用户强调"继续做"，表明规划阶段已认可，直接进入执行

## Evaluation Result：
### 执行产物（按 tasks.md 执行）：
- Task 1: routes/routeDataMiner.py - Blueprint 和三條 API 路由
- Task 2: dao/daoDataMiner.py - sqlite 数据库操作方法
- Task 3: script/scriptDataMiner.py - 四种文件类型的读取和粗分
- Task 4: process/processDataMiner.py - 数据处理主流程（安全验证→读取→清洗→转换→保存）
- Task 5: 验证修复 - 补充 file_type 和 source_file 字段缺失

### 最终状态：
- 所有 5 个任务已完成
- 14 个检查点全部通过
spec mode logging
