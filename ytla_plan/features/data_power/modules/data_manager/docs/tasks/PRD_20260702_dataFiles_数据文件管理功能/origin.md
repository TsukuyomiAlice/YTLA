Harness Instructions file version: rule_harness_instructions_ver_ide.md v1.7, rule_harness_instructions_for_ytla.md v1.7
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement:
为 data_power 特性下的 data_manager 模块添加数据文件管理功能。包含三个功能：
1. 展示在指定的 plan - module 下存储的各类和数据相关的文件
   - 展示该 data_manager 对应的 module 所在的 plan 内，所有隶属于 data_manager、data_miner、data_analyzer、data_demonstrator 模组对应的 module 文件夹
   - 展示文件名和对应所在的 module_id、module name
2. 上传并妥善储存初始数据文件
   - 接收文件类型：office excel系列（xlsx, xls）、csv、json、sqlite db 文件（db, sqlite, sqlite3）
   - 上传文件储存位置：该 Module 对应的数据文件储存路径（plan_x / module_x / 上传时间戳YYYYmmDDHHMMSS / 该原始文件）
3. 提供删除已上传的文件的功能
   - 仅限在路径2下的文件，提供删除功能

需要设计完整的 router 和 process 文件。

同时要求：按照 rule_harness_instructions_ver_ide.md 和 rule_harness_instructions_for_ytla.md 的规则执行，不要按照 .trae/specs/add-data-manager-files 的内容执行。

## Analyze:
**Given**： 
- data_manager 模块路径：features/data_power/modules/data_manager
- 参考架构：core/classic（Flask Blueprint + routes/process/dao 三层架构）
- 已有 PRD 文档：PRD_20260702_dataFiles_数据文件管理功能（已标记为完成）
- 已有代码文件：routes/routeDataFiles.py、process/processDataFiles.py
- plan 和 module 规则：通过 SQLite 数据库关联，module 通过 belong_plan_id 关联到 plan，通过 module_sub_type 标识子类型

**Target**：
- 按照 PRD_20260702_dataFiles_数据文件管理功能 中的设计执行代码实现
- 确保实现与 PRD 规格一致

**Evidence**：
- 用户明确要求"按照 PRD_20260702_dataFiles_数据文件管理功能 下的设计执行"
- 用户明确要求"不要按照 .trae/specs/add-data-manager-files 的内容执行"
- 已有代码可能来自其他规格，需要对比 PRD 修正

## Evaluation Result：
### 代码文件修正/重写：
- routes/routeDataFiles.py：路由文件
- process/processDataFiles.py：业务逻辑文件
- 需确保与 PRD 规格完全一致

### 验证清单：
- checklist.md 中的检查点代码实现验证

# Dialogue 2

## User Requirement:
按照 `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_ver_ide.md` `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_for_ytla.md` 的规则，重新执行 spec 模式流程。

## Analyze:
**Given**：
- 已有的 PRD 文档已标记为"已完成"
- 用户要求重新按照 harness 规则执行
- 需要在 harness 规则框架下重新审查和调整现有代码

**Target**：
- 遵循 Harness 规则（Start Stage → Planning Stage → Action Stage）
- 审查现有代码与 PRD 的一致性
- 如有差异，修正代码使其符合 PRD

**Evidence**：
- rule_harness_instructions_ver_ide.md 0.2 节要求进入 Start Stage
- rule_harness_instructions_for_ytla.md 2.1 节规定 PRD 文档位置

## Evaluation Result：
### 规划文档：
- origin.md：原始需求记录
- spec.md：产品需求文档（复用已有或更新）
- tasks.md：实现计划（复用已有或更新）
- checklist.md：验证清单（复用已有或更新）
- actions.md：行动记录

### 执行产物：
- routes/routeDataFiles.py（按 PRD 修正）
- process/processDataFiles.py（按 PRD 修正）
spec mode logging
