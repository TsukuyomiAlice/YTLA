## User Requirement: 
/spec 
 `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md` 
 这次是要更新这个文档，并且同时按更新后的该文档来执行spec模式 
 我们要再在task文件夹里添加一个文档，叫做Action Record (actions.md) - 行动记录 
 actions.md用于记录执行spec模式的过程 
 文档分为三个部分：Start Stage(启动阶段)，Planing Stage (规划阶段) ，和Action Stage（执行阶段） 
 启动阶段用于执行检索是否已存在并生成PRD文档，然后再开始正常的规划阶段 
 
 每个阶段需要按实际行动记录以下内容： 
 ### ACT-[序号]: 
 - **Thought**: [思考内容] 
 - **Target**: [执行目标] 
 - **Tool**: [使用工具] 
 - **Touches** [读取/生成/修改/删除的文件列表] 
 
 并且，我们要改变harness模式下的执行顺序： 
 在读取到 `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md` 后，即刻开始Start Stage，在建立PRD目录后进入Planing Stage 
 新的Actions.md需要在每次执行新的文件操作之前完成记录（更新Actions.md本身不用记录，避免陷入自身死循环）

## Analyze：
**Given**： 目标文档 `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions.md` 已存在，用户要求更新该文档并按更新后的规范执行 spec 模式
**Target**： 
1. 更新 rule_harness_instructions.md 文档，添加关于 actions.md 的规范
2. 定义 actions.md 的文档结构和内容要求
3. 更新 harness 模式的执行流程，加入 Start Stage
4. 按更新后的规范执行本次 spec 模式任务
**Evidence**： 用户明确要求添加 actions.md 文档，定义三个阶段（Start Stage, Planning Stage, Action Stage），每个阶段记录 Thought, Target, Tool, Touches，并要求改变执行顺序

## Evaluation Result：
### 产物1：更新后的 rule_harness_instructions.md 文档
- 包含 actions.md 的规范说明
- 更新执行流程，加入 Start Stage
- 包含 actions.md 的格式要求
### 产物2：PRD 规划文档（按更新后的规范执行）
- origin.md（原始需求文档）
- spec.md（产品需求文档）
- tasks.md（实现计划）
- checklist.md（验证清单）
- actions.md（行动记录文档）
