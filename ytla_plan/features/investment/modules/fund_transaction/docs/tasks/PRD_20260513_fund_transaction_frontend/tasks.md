# 基金交易模块 - 后端API开发实施计划

## [ ] Task 1: 创建路由文件和基础结构
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 在routes目录下创建新的路由文件 `routeFundTransaction.py`
  - 参考linguisticEnglish模块的路由结构，使用 Blueprint 方式
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3]
- **Test Requirements**:
  - `programmatic` TR-1.1: 路由文件可以被正确导入

## [ ] Task 2: 调整 processTransactionMatchGroup 返回结构化数据
- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 调整现有 processTransactionMatchGroup 的返回格式
  - 从写入文件改为返回结构化数据（dict 或 对象）
  - 保持现有逻辑不变，仅调整输出方式
  - 返回数据包含：基金概况、连续涨跌统计、分组交易明细、每日利润等
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `programmatic` TR-2.1: process 函数可以正确返回结构化数据
  - `programmatic` TR-2.2: 数据格式化为JSON格式

## [ ] Task 3: 创建process层来处理API逻辑
- **Priority**: P0
- **Depends On**: Task 2
- **Description**: 
  - 在process目录下创建处理API请求的逻辑 `processFundTransaction.py`
  - 调用 daoTransactionHistory 和调整后的 processTransactionMatchGroup
  - 格式化返回数据
- **Acceptance Criteria Addressed**: [AC-1, AC-2]
- **Test Requirements**:
  - `programmatic` TR-3.1: process层可以正确调用现有分析逻辑
  - `programmatic` TR-3.2: 数据格式化为JSON格式

## [ ] Task 4: 实现交易记录管理API
- **Priority**: P0
- **Depends On**: Task 3
- **Description**: 
  - 实现创建交易记录的接口
  - 实现获取交易记录列表的接口
  - 兼容旧的 transactionLogOn API（保持相同参数和返回格式）
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `programmatic` TR-4.1: 可以创建和获取交易记录

## [ ] Task 5: 实现即时交易分析API
- **Priority**: P0
- **Depends On**: Task 3
- **Description**: 
  - 实现即时交易分析接口，接受基金代码
  - 返回完整的结构化分析结果，包含基金概况、分组明细、利润统计等
  - 数据结构便于前端展示分组统计策略
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `programmatic` TR-5.1: 返回正确的分析结果，包含所有必要信息

## [ ] Task 6: 实现自动化任务API
- **Priority**: P1
- **Depends On**: Task 3
- **Description**: 
  - 实现执行自动化清算任务的接口
  - 兼容旧的 auto API（保持相同参数和返回格式）
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `programmatic` TR-6.1: 可以正确触发和返回任务结果
