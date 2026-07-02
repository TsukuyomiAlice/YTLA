# Data Manager 前端模块 - Product Requirements Document (PRD)

## Overview
为 data_power/data_manager 模块创建完整的前端界面，实现数据文件的可视化管理和上传功能。前端页面分为 main 区域（文件列表展示与删除）和 sub 区域（返回 dashboard 按钮 + 文件上传）。

## Goals
- 实现对后端 API 的封装（文件列表获取、上传、删除）
- 在 main 区域展示所有数据文件，并提供删除功能
- 在 sub 区域提供文件上传功能和返回 dashboard 的导航
- 遵循 investment 模块的代码架构和格式规范

## Non-Goals
- 不涉及文件预览功能
- 不涉及批量文件操作（如批量删除、批量下载）
- 不涉及文件内容编辑
- 不涉及用户权限管理
- 不涉及文件的排序、筛选、搜索功能
- 不修改已有的骨架文件（Main.vue、Sub.vue、FlowManager、ModuleConfig、registries.ts）

## Background & Context
- 后端已提供三个 API 端点用于文件管理（list/upload/delete）
- 前端 data_manager 模块已有骨架文件，但业务组件为空
- investment/fund_info 模块提供了可复用的架构模式（Service → Store → Component）
- 项目中已有通用的 ReturnToPlanDashboardButton 组件可直接使用

## Functional Requirements

### FR-1: 文件列表展示
- **描述**: 在 main 区域加载并展示当前 plan 下的所有数据文件
- **数据来源**: `GET /data_manager/files?plan_id=X`
- **展示字段**: 文件名、文件大小、上传时间、所属模块
- **状态**: 加载中状态、空数据状态、错误状态

### FR-2: 文件删除
- **描述**: 对允许删除的文件提供删除按钮，点击确认后删除
- **数据来源**: `POST /data_manager/files/delete`
- **交互**: 点击删除按钮 → 确认提示 → 执行删除 → 刷新列表

### FR-3: 文件上传
- **描述**: 在 sub 区域提供文件上传功能
- **数据来源**: `POST /data_manager/upload`
- **交互**: 选择文件 → 点击上传 → 显示上传进度/结果 → 刷新列表
- **约束**: 需提供 module_id 参数

### FR-4: 返回 Dashboard
- **描述**: sub 区域包含回到 dashboard 的按钮
- **实现**: 在 `_type/ui/` 下创建本模块专属的 ReturnToPlanDashboardButton 组件，参照 investment 的实现方式

## Non-Functional Requirements
- 代码格式参照 investment/fund_info 模块
- 使用 TypeScript + `<script setup lang="ts">` 语法
- 使用 scoped SCSS 样式
- 组件的 plan_id 通过 `useRoute` 或 `usePanelStore` 获取
- 使用 Pinia store 管理状态
- 错误处理遵循 catch → set error → display 模式

## Constraints
- 目标路径：`d:\YTLA\ytla_plan_vue\src\features\data_power\modules\data_manager\`
- 必须遵守 Vue 3 + TypeScript + Pinia 技术栈
- 后端 API 路径前缀需使用 `import.meta.env.VITE_API_BASE`

## Assumptions
- plan_id 可从当前 panel 状态中获取（通过 usePanelStore）
- module_id 可在文件列表中附带，上传时需要用户选择或从上下文中获取
- 允许删除的文件判断依据：后端返回的文件列表中有删除权限标识，或所有文件都允许删除

## Acceptance Criteria

### AC-1: 文件列表正常展示
- **Given**: 用户进入 data_manager 模块，当前 plan 下存在数据文件
- **When**: main 区域加载完成
- **Then**: 显示文件列表，包含文件名、大小、上传时间和所属模块
- **Verification**: `human-judgment`
- **Notes**: 应包含 loading 状态和空数据状态的正确处理

### AC-2: 文件删除成功
- **Given**: 文件列表中存在可删除的文件
- **When**: 用户点击删除按钮并确认
- **Then**: 文件被删除，列表刷新，文件不再显示
- **Verification**: `programmatic`
- **Notes**: 删除失败时应显示错误信息

### AC-3: 文件上传成功
- **Given**: 用户在 sub 区域选择了有效文件并点击上传
- **When**: 文件上传请求完成
- **Then**: 文件上传成功，main 区域的列表刷新，显示新上传的文件
- **Verification**: `programmatic`
- **Notes**: 上传失败时应显示错误信息

### AC-4: 返回 Dashboard 按钮
- **Given**: 用户在 data_manager sub 区域
- **When**: 点击"回到 dashboard"按钮
- **Then**: 页面导航到 plan dashboard
- **Verification**: `human-judgment`
- **Notes**: 在 `_type/ui/` 下创建本模块专属的 ReturnToPlanDashboardButton 组件

## Open Questions
- 上传文件时，module_id 的来源？是否需要让用户选择所属模块，还是自动使用当前模块的 ID？
- 文件删除是否需要二次确认（弹窗提示）？
- 是否需要显示上传进度条？
spec mode logging
