# Scaffold Backend Integration - Product Requirement Document

## Overview
- **Summary**: 为scaffold模块创建后端API接口，提供脚手架生成功能的RESTful API
- **Purpose**: 提供后端API接口，让前端可以调用processGenerateStructure来生成项目脚手架
- **Target Users**: 前端开发者、项目创建者

## Goals
- 创建process下的processGenerator，用来调用processGenerateStructure
- 创建routes下的blueprint，只用来负责调用processGenerator
- 所有的业务处理全部在processGenerator内实现

## Non-Goals (Out of Scope)
- 不创建额外的instance目录和文件
- 不创建额外的api目录和文件
- 不修改现有的processGenerateStructure.py

## Background & Context
- 后端已有processGenerateStructure.py函数，可以生成Python和Vue3的脚手架结构
- 现有多个模块的路由实现作为参考（如llm_caller）
- 需要遵循现有项目的代码规范和架构模式

## Functional Requirements
- **FR-1**: 创建processGenerateScaffold.py
  - 负责调用processGenerateStructure
  - 包含所有业务处理逻辑
  - 参数验证
  - 错误处理

- **FR-2**: 创建routeScaffold.py
  - Flask Blueprint实现
  - /health端点 - 健康检查
  - /generate端点 - 脚手架生成
  - 只负责调用processGenerateScaffold

## Non-Functional Requirements
- **NFR-1**: 遵循Flask REST API规范
- **NFR-2**: 完善的错误处理

## Constraints
- **Technical**: 必须使用Flask框架，遵循现有代码结构
- **Business**: 保持与现有processGenerateStructure.py函数的兼容性
- **Dependencies**: 依赖现有的processGenerateStructure.py函数

## Assumptions
- 前端会提供所有必要的参数
- processGenerateStructure.py函数已经稳定可用
- 后端环境已经配置好

## Acceptance Criteria

### AC-1: processGenerateScaffold.py实现完成
- **Given**: processGenerateScaffold.py文件已创建
- **When**: 调用该函数并传入正确参数
- **Then**: 函数正确调用processGenerateStructure并返回结果
- **Verification**: programmatic
- **Notes**: 所有业务处理在processGenerator内实现

### AC-2: routeScaffold.py实现完成
- **Given**: routeScaffold.py文件已创建
- **When**: 发送HTTP请求到/generate端点
- **Then**: 路由正确调用processGenerateScaffold并返回JSON响应
- **Verification**: programmatic
- **Notes**: Blueprint只负责调用processGenerator

### AC-3: 健康检查接口正常
- **Given**: 后端服务正在运行
- **When**: 发送GET请求到/health端点
- **Then**: 返回200状态和ok状态
- **Verification**: programmatic
- **Notes**: 验证健康检查功能

### AC-4: 错误处理正常
- **Given**: 发送无效参数的请求
- **When**: 后端处理请求
- **Then**: 返回400错误和清晰的错误信息
- **Verification**: programmatic
- **Notes**: 验证参数验证和错误处理

## Open Questions
- [ ] 是否需要添加额外的验证逻辑（如type_name格式验证）？
- [ ] 是否需要添加权限验证？
