# 创建 rule_harness_instructions.md 的非IDE依赖版本 - Product Requirement Document

## Overview
- **Summary**: 基于现有的 `rule_harness_instructions.md` 文档，创建一个不依赖特定IDE功能的版本 `rule_harness_instructions_ver_direct.md`，使用户可以直接用这份文档向大模型发出项目开发要求。
- **Purpose**: 解决原始文档对特定IDE内置工具和命令的依赖问题，使Harness工程方法论可以在任意大模型对话环境中使用。
- **Target Users**: 需要使用大模型进行软件工程但不使用特定IDE的用户。

## Goals
- 创建 `rule_harness_instructions_ver_direct.md` 文档
- 移除所有对IDE特定工具和命令的引用
- 补充必要的系统级上下文和指令
- 保留原始文档的核心工作理念和文档规范
- 确保新文档可以在任意大模型对话环境中使用

## Non-Goals (Out of Scope)
- 不修改原始文档 `rule_harness_instructions.md`
- 不改变Harness工程方法论的核心理念
- 不添加新的功能或流程
- 不为特定大模型平台做优化（保持通用性）

## Background & Context
- 现有文档 `rule_harness_instructions.md` 是一份针对特定IDE的提示词文档
- 该文档依赖IDE内置的命令（如 /spec、/plan）和工具（如 TodoWrite、Read、Write 等）
- 用户希望能够在不使用该IDE的情况下，直接向大模型发出项目开发要求
- 核心工作理念（规划先行、子代理协作、验证驱动等）需要保留

## Functional Requirements
- **FR-1**: 新文档必须包含原始文档的所有核心内容
- **FR-2**: 新文档必须移除所有对IDE特定命令的引用
- **FR-3**: 新文档必须移除所有对IDE特定工具的引用
- **FR-4**: 新文档必须补充系统级上下文和指令
- **FR-5**: 新文档必须提供工具替代方案
- **FR-6**: 新文档必须调整工作流程的启动和切换方式
- **FR-7**: 新文档必须明确文件操作和用户交互的方法
- **FR-8**: 新文档必须可以在任意大模型对话环境中使用

## Non-Functional Requirements
- **NFR-1**: 新文档必须与原始文档保持相同的语言风格和结构
- **NFR-2**: 新文档必须易于理解和使用
- **NFR-3**: 新文档必须保持与原始文档相同的文档质量
- **NFR-4**: 新文档生成后，必须能够立即投入使用

## Constraints
- **Technical**: 必须基于现有文档 v1.7 版本进行修改
- **Business**: 必须在本次任务中完成，无明确时间限制但需尽快完成
- **Dependencies**: 依赖现有 `rule_harness_instructions.md` 文档

## Assumptions
- 大模型具有基本的对话能力和文本生成能力
- 用户可以手动执行文件操作（或通过其他工具）
- 用户可以通过自然语言与大模型进行交互
- 子代理协作可以通过分段对话或独立对话实现

## Acceptance Criteria

### AC-1: 新文档成功创建
- **Given**: 原始文档 `rule_harness_instructions.md` 存在
- **When**: 执行创建任务
- **Then**: 新文档 `rule_harness_instructions_ver_direct.md` 成功创建在 `d:\YTLA\ytla_plan\features\feature_maker\modules\harness\docs\rules\` 目录下
- **Verification**: `programmatic`

### AC-2: 所有IDE特定内容已移除
- **Given**: 新文档已创建
- **When**: 检查新文档内容
- **Then**: 新文档中不包含任何对IDE特定命令（如 /spec、/plan）和工具（如 TodoWrite、Read、Write、Edit、AskUserQuestion、NotifyUser、subagent 等）的引用
- **Verification**: `programmatic`

### AC-3: 系统级上下文和指令已补充
- **Given**: 新文档已创建
- **When**: 检查新文档内容
- **Then**: 新文档开头包含必要的系统级上下文和指令，说明工作环境假设
- **Verification**: `human-judgment`

### AC-4: 工具替代方案已提供
- **Given**: 新文档已创建
- **When**: 检查新文档内容
- **Then**: 新文档提供了不依赖IDE工具的替代方法，包括文件操作、用户交互、子代理协作等
- **Verification**: `human-judgment`

### AC-5: 工作流程已调整
- **Given**: 新文档已创建
- **When**: 检查新文档内容
- **Then**: 新文档调整了工作流程的启动和切换方式，从命令触发改为用户明确要求
- **Verification**: `human-judgment`

### AC-6: 核心内容已保留
- **Given**: 新文档已创建
- **When**: 对比新旧文档
- **Then**: 新文档保留了原始文档的核心工作理念、文档规范、质量检查清单、最佳实践、常见陷阱和术语表
- **Verification**: `human-judgment`

### AC-7: 文档可在非IDE环境使用
- **Given**: 新文档已创建
- **When**: 尝试在任意大模型对话环境中使用
- **Then**: 新文档可以正常引导大模型完成项目开发任务
- **Verification**: `human-judgment`

## Open Questions
- [ ] 用户是否需要在新文档中提供具体的文件操作工具推荐？
- [ ] 子代理协作在非IDE环境中是否有特定的实现要求？
- [ ] 是否需要为不同类型的大模型平台提供变体版本？
