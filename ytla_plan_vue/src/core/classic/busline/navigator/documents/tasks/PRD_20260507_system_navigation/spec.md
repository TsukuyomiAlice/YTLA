# System Navigation - Product Requirement Document

## Overview

* **Summary**: 实现一个基于配置的系统导航系统，支持在 System Root (planManager)、Plan Desktop (planDashboard) 以及具体模块之间的灵活跳转。

* **Purpose**: 解决现有系统中导航按钮分散、难以统一管理的问题，通过配置化的方式实现导航层级的抽象，便于未来扩展其他 System。

* **Target Users**: 应用开发者和用户，需要在不同层级间导航的用户。

## Goals

1. 创建 System Config 配置文件，定义 System Root 和 Plan Desktop
2. 创建 System Navigator Registry，用于注册导航按钮
3. 创建 System Navigator Store，管理导航按钮的激活状态
4. 创建 System Navigation Bar 组件，用于展示导航按钮
5. 实现基于配置的可见性控制

## Non-Goals (Out of Scope)

1. 不实现除 planManage 外的其他 System（留待未来扩展）
2. 不修改现有的 ReturnToPlanButton 和 ReturnToPlanDashboardButton 的功能逻辑
3. 不实现复杂的导航历史记录功能

## Background & Context

现有系统已经有以下组件：

* `ReturnToPlanButton.vue`: 跳转到 planManager（System Root）

* `ReturnToPlanDashboardButton.vue`: 跳转到 planDashboard（Plan Desktop）

* `moduleRegistry.ts`: 模块注册机制

* `panelStore.ts`: 面板状态管理

* `systemRegistry.ts`: 系统注册表

现有问题：

1. 按钮的使用是硬编码在各个模块中的
2. 没有统一的导航管理机制
3. 难以扩展其他 System

## Functional Requirements

* **FR-1**: System Config 配置

  * 支持配置 System ID

  * 支持配置 System Root Module（如 planManager）

  * 支持配置 Plan Desktop Module（如 planDashboard）

  * 支持配置 System Root Panel（如 plan\_manage）

* **FR-2**: Navigation Button 注册

  * 支持注册导航按钮，包含按钮 ID、目标层级、组件路径

  * 支持配置按钮的可见性条件

  * 支持配置按钮的排序权重

* **FR-3**: Navigator Store

  * 支持激活/停用导航按钮

  * 支持获取当前可见的按钮

  * 支持按层级管理按钮

* **FR-4**: Navigation Bar 组件

  * 展示当前激活的可见导航按钮

  * 自动适配上下文显示/隐藏按钮

## Non-Functional Requirements

* **NFR-1**: 性能 - 组件加载应该是异步的，不阻塞主应用启动

* **NFR-2**: 可扩展性 - 应该支持未来添加其他 System，无需修改核心代码

* **NFR-3**: 类型安全 - 完整的 TypeScript 类型定义

## Constraints

* **Technical**: 必须使用现有的 Pinia Store、Vue 3 Composition API、项目已有的代码风格

* **Business**: 必须保持与现有按钮的兼容性

* **Dependencies**: 依赖现有 panelStore、moduleRegistry 等

## Assumptions

1. 未来可能有其他 System（除 planManage 外）
2. 按钮的可见性判断主要基于当前 Panel 和 Module 信息
3. 用户希望有一个统一的导航机制

## Acceptance Criteria

### AC-1: System Config 初始化

* **Given**: 应用启动时

* **When**: 加载 System Config

* **Then**: SystemConfig 应该正确设置，包括 systemModule = 'planManage', rootModule = 'planManager', desktopModule = 'planDashboard', rootPanel = 'plan\_manage'

* **Verification**: `programmatic`

* **Notes**: 可以通过 Store 的 getter 验证

### AC-2: Navigation Button 注册

* **Given**: System 已初始化

* **When**: 注册 ReturnToSystemRoot 和 ReturnToPlanDesktop 按钮

* **Then**: 按钮应该被正确注册到 Registry 中

* **Verification**: `programmatic`

* **Notes**: 可以通过 getAllSystemButtons() 验证

### AC-3: 按钮可见性判断

* **Given**: 当前在某个 Plan 下的具体模块中

* **When**: 检查按钮可见性

* **Then**: ReturnToSystemRoot 和 ReturnToPlanDesktop 都应该可见

* **Verification**: `programmatic`

### AC-4: Navigation Bar 渲染

* **Given**: 已激活导航按钮

* **When**: 在模块中使用 SystemNavigationBar

* **Then**: 应该正确渲染可见的按钮

* **Verification**: `human-judgment`

### AC-5: 导航功能正常

* **Given**: 在某个 Plan 的具体模块中

* **When**: 点击 ReturnToSystemRoot

* **Then**: 应该跳转到 planManager

* **Verification**: `programmatic`

### AC-6: 在 System Root 时按钮隐藏

* **Given**: 当前在 plan\_manage 面板中

* **When**: 检查按钮可见性

* **Then**: ReturnToSystemRoot 应该不可见

* **Verification**: `programmatic`

## Open Questions

* [ ] 是否需要支持多个 System 同时存在？

* [ ] 按钮的国际化文本应该放在哪里？

