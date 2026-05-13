Harness Instructions file version: rule_harness_instructions_for_ytla.md (1.7)
Harness Instructions file Author: Official

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement:
/spec `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\rule_harness_instructions_for_ytla.md` `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_project_definition.md` `d:\YTLA\ytla_plan\features\feature_maker\modules\frontend_vue3\docs\rules\rule_ui_instructions.md`
 你读懂了
 现在要你帮它实现一些全新的前端页面。
 这里会给你它原本的旧前端
 `d:\YTLA\ytla_plan\features\investment\temp`
 非常地简单，现在你要为它制作新的前端页面
 目标位置在 `d:\YTLA\ytla_plan_vue\src\features\investment\modules`
 你需要补齐一些后端的文件比如routes
 提供一个这个架构里的已实现应用的架构参考：
 `d:\YTLA\ytla_plan\features\linguisticEnglish` `d:\YTLA\ytla_plan_vue\src\features\language`
 要求：
 1 复原原本提供的api
 2 在此基础之上做改善
 核心要求：
 在画面上能显示出基金净值的折线图
 在画面上能比较好地表现出分组统计策略
 你可以自行决定需要分出多少个子页面，并且设计其中的切换按钮
 创建代码的范围：
 前端
 后端 routes，可以补充添加新的process用以支持新的功能（比如调取基金净值相关的内容，调取交易记录相关的内容）

## Analyze：
**Given**:
- 现有旧前端代码位于 `d:\YTLA\ytla_plan\features\investment\temp`
- 参考架构为 `linguisticEnglish`（后端）和 `language`（前端）
- 目标位置：后端在 `fund_info` 和 `fund_transaction` 模块，前端在对应的 Vue 模块
- 需要支持基金净值折线图和分组交易分析展示
- 可以创建新的 process 层处理新的业务逻辑
- 可以创建新的 routes 提供 API

**Target**:
- 复原旧 API 功能（基金信息查询、交易记录添加、自动清算执行）
- 创建新的 API 支持获取基金历史净值数据、获取交易分组分析结果
- 创建前端页面展示基金信息和净值折线图
- 创建前端页面展示交易记录和分组分析结果
- 添加页面导航功能

**Evidence**:
- 旧代码 `app_old.py` 包含三个主要接口：基金信息查询、交易记录添加、自动清算执行
- `processTransactionMatchGroup.py` 提供了完整的交易分组分析逻辑
- `daoFundHistory.py` 提供了基金历史数据访问
- `daoFundInfo.py` 提供了基金信息访问
- `daoTransactionHistory.py` 提供了交易记录访问
- 参考 `language` 模块的 Vue3 架构组织前端代码

## Evaluation Result：
### 后端：
- fund_info: 创建 routes 和 process 提供基金信息和历史数据 API
- fund_transaction: 创建 routes 和 process 提供交易记录和分析 API
### 前端：
- fund_info: 创建基金信息页面，包含净值折线图
- fund_transaction: 创建交易记录和分析页面，展示分组统计策略
### 通用：
- 页面导航组件

# Dialogue 2

## User Requirement:
关于基金交易分析的部分
 我添加了一个由那套算法实际生成出来的文档 `d:\YTLA\ytla_plan\features\investment\temp\027_161725_招商中证白酒指数(LOF)A.txt` 以供参考
 因为现在转换到网页上显示了，所以需要你做一点适当调整，以便可以在网页上更好地浏览原本生成的文档
 有一个明显的差别：
 原本是通过按钮自动生成全部分析文档的，现在不再需要使用这个按钮了
 改为：
 选择某个基金，对该基金做即时的分析，将分析结果传到前端后，在前端展示
 另外，添加origin.md和actions.md，你看情况补

## Analyze：
**Given**:
- 有实际的分析结果文档作为参考
- 需要从"按钮生成文档"改为"选择基金即时分析并在前端展示"
- 需要创建 origin.md 和 actions.md 文档

**Target**:
- 更新需求，分析改为即时计算并返回 JSON 格式数据
- 设计前端展示分析结果的组件
- 补充创建 origin.md 和 actions.md

**Evidence**:
- 分析文档包含基金概况、连续涨跌统计、分组交易明细等内容
- 分析结果需要结构化以便前端展示
- 需要调整 processTransactionMatchGroup 的返回格式

## Evaluation Result：
### 后端：
- processTransactionMatchGroup 需要返回结构化数据而非写入文件
- API 接口设计为接受基金代码，返回分析结果
### 前端：
- 展示分析结果的各个部分，包括分组交易详情
### 文档：
- 补充创建 origin.md 和 actions.md

spec mode logging
