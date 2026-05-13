# 基金交易模块 - 后端API开发

## 概述
- **摘要**: 为基金交易模块开发后端API，支持前端展示交易记录和即时分析结果
- **目的**: 提供RESTful API接口，支持前端获取交易数据和即时分析结果，展示分组统计策略
- **目标用户**: 前端开发人员

## 目标
- [G1] 提供交易记录管理API（兼容旧API）
- [G2] 提供即时交易分析API，接受基金代码返回结构化分析结果
- [G3] 提供自动化任务执行API
- [G4] 遵循现有项目架构规范
- [G5] 调整 processTransactionMatchGroup 返回结构化数据而非写入文件

## 非目标
- 不修改现有DAO层代码
- 不修改数据库结构
- 不重新设计分析算法核心逻辑

## 背景与上下文
- 现有系统已有完善的交易分析逻辑 processTransactionMatchGroup
- 有实际分析结果文档作为参考
- 前端需要API来获取交易数据和即时分析结果
- 参考linguisticEnglish模块的架构
- 旧API在 `app_old.py` 中，需要兼容

## 功能需求
- **FR-1**: 交易记录CRUD API（兼容旧的 transactionLogOn 接口）
- **FR-2**: 即时交易分析API：传入基金代码，返回完整的分组交易分析结果（包含基金概况、分组明细、利润统计等）
- **FR-3**: 自动化清算任务API（兼容旧的 auto 接口）

## 验收标准
### AC-1: 交易记录管理API
- **Given**: 请求操作交易记录
- **When**: 传入交易数据
- **Then**: 交易记录被正确创建、更新或删除
- **Verification**: `programmatic`

### AC-2: 即时交易分析API
- **Given**: 请求获取交易分析
- **When**: 传入基金代码
- **Then**: 即时调用 processTransactionMatchGroup 进行分析，返回结构化的分析结果，包含基金概况、连续涨跌统计、分组交易明细等
- **Verification**: `programmatic`

### AC-3: 自动化任务API
- **Given**: 请求执行自动化任务
- **When**: 用户触发任务
- **Then**: 任务执行并返回结果
- **Verification**: `programmatic`
