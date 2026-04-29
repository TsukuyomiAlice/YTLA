# Scaffold Frontend Creation - Product Requirement Document

## Overview
- **Summary**: 为scaffold模块创建前端界面，包含create_card和create_module两个子模块，提供脚手架生成的用户界面
- **Purpose**: 提供用户友好的界面，让用户可以通过表单输入参数并生成项目脚手架
- **Target Users**: 项目开发者、模块创建者

## Goals
- 完善create_card模块的所有文件
- 完善create_module模块的所有文件
- 实现用户表单界面，包含所有必要输入字段
- 集成后端API调用
- 实现状态管理和错误处理
- 提供国际化支持（中英文）

## Non-Goals (Out of Scope)
- 不修改后端API（后端在单独PRD中）
- 不实现除card和module之外的其他结构类型
- 不实现复杂的预览功能

## Background & Context
- 前端已有基础文件结构，大多为空
- 已有language和mathematics模块作为完整参考实现
- 后端将提供REST API供前端调用
- 需要遵循项目现有的Vue 3 + TypeScript + Pinia架构

## Functional Requirements
- **FR-1**: create_card模块实现
  - 主界面组件（Create_cardMain_00.vue）
  - 子界面组件（Create_cardSub_00.vue）
  - API服务（scaffoldCardService.ts）
  - 状态管理（scaffoldCardStore.ts）
  - 流程管理（create_cardFlowManager.ts）
  - 模块配置（create_cardModuleConfig.ts, registries.ts）
  - 国际化（locales/zh.json, locales/en.json）
  - 头像组件（avatar/Avatar.vue）

- **FR-2**: create_module模块实现
  - 主界面组件（Create_moduleMain_00.vue）
  - 子界面组件（Create_moduleSub_00.vue）
  - API服务（scaffoldModuleService.ts）
  - 状态管理（scaffoldModuleStore.ts）
  - 流程管理（create_moduleFlowManager.ts）
  - 模块配置（create_moduleModuleConfig.ts, registries.ts）
  - 国际化（locales/zh.json, locales/en.json）
  - 头像组件（avatar/Avatar.vue）

- **FR-3**: 表单功能实现
  - 选择core/feature（单选框/下拉框）
  - 选择版本（默认classic，下拉框）
  - 输入type_name（文本输入框）
  - 输入sub_type_name（文本输入框）
  - 选择是否生成后端（复选框）
  - 选择是否生成前端（复选框）
  - 提交按钮
  - 表单验证

- **FR-4**: API集成
  - 调用后端 /scaffold/generate 接口
  - 处理加载状态
  - 处理成功响应
  - 处理错误响应
  - 显示生成结果信息

## Non-Functional Requirements
- **NFR-1**: 响应式设计，适配不同屏幕尺寸
- **NFR-2**: 良好的用户体验，加载状态和错误提示清晰
- **NFR-3**: 遵循项目代码规范和架构模式
- **NFR-4**: TypeScript类型安全

## Constraints
- **Technical**: 必须使用Vue 3 + TypeScript + Pinia
- **Business**: 必须与后端API保持兼容
- **Dependencies**: 依赖后端API接口

## Assumptions
- 后端API按预期实现
- 项目环境配置正确
- 用户有基本的计算机操作能力

## Acceptance Criteria

### AC-1: create_card模块界面完整
- **Given**: 用户访问create_card模块
- **When**: 查看界面
- **Then**: 可以看到完整的表单界面，包含所有输入字段
- **Verification**: human-judgment
- **Notes**: 验证界面元素完整性

### AC-2: create_module模块界面完整
- **Given**: 用户访问create_module模块
- **When**: 查看界面
- **Then**: 可以看到完整的表单界面，包含所有输入字段
- **Verification**: human-judgment
- **Notes**: 验证界面元素完整性

### AC-3: 表单验证正常工作
- **Given**: 用户在表单中输入无效数据
- **When**: 点击提交按钮
- **Then**: 显示验证错误信息
- **Verification**: human-judgment
- **Notes**: 验证表单验证功能

### AC-4: API调用成功
- **Given**: 用户输入有效数据并提交
- **When**: 后端API正常响应
- **Then**: 显示成功消息和生成结果
- **Verification**: programmatic
- **Notes**: 验证API集成

### AC-5: 错误处理正常
- **Given**: 用户提交表单
- **When**: 后端API返回错误
- **Then**: 显示友好的错误消息
- **Verification**: human-judgment
- **Notes**: 验证错误处理

### AC-6: 模块注册正确
- **Given**: 项目已构建
- **When**: 查看模块注册表
- **Then**: create_card和create_module模块已正确注册
- **Verification**: human-judgment
- **Notes**: 验证模块配置

## Open Questions
- [ ] 是否需要在成功后提供跳转到生成的模块的链接？
- [ ] 是否需要添加历史记录功能？
