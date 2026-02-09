# YTLA 脚手架工具文档

## 项目简介

YTLA (Your T&L Assistant) 是一个模块化 Web 应用平台框架，用户可通过自由生成并组合模块（Modules）和卡片（Cards）快速构建个性化工作流。

## 脚手架工具概述

脚手架工具是 YTLA 平台的重要组成部分，用于生成基础框架和自动化代码，支持快速开发和扩展。

## core_classic系列

### core层

- classic：用作程序框架的运行，视作为"硬件"
    - frame：底层框架
    - cards：卡片
    - modules：模组
    - plans：计划
    - users：用户

### feature层

- planManage：用于主界面运行，视作为"OS"
- aiConnector：用于连接ai服务，ai_tools专用应用
- scaffold：用于生成基础框架
- 其它feature：用作功能

## scaffold 包定义

在scaffold下定义了三种不同的包：

- frontend_xxx：指使用某种语言的前端
- backend_xxx：指使用某种语言的后端
- general_xxx：指的是核心组件的版本名

## 脚手架类型

### 1. 前端脚手架 (frontend_vue3)

用于生成 Vue 3 前端项目结构，包含：
- 组件模板
- 布局模板
- 样式模板
- 国际化支持
- 路由配置

### 2. 后端脚手架 (backend_python)

用于生成 Python-Flask 后端项目结构，包含：
- API 路由模板
- 数据库访问模板
- 业务逻辑模板
- 定时任务模板

### 3. 核心脚手架 (core_classic)

用于生成核心框架结构，包含：
- 基础组件模板
- 模块管理模板
- 卡片管理模板
- 计划管理模板

## 脚手架使用指南

### 1. 生成前端项目

```bash
# 生成前端 Vue 3 项目结构
python -m features.scaffold.modules.frontend_vue3.process.processGenerateStructure
```

### 2. 生成后端项目

```bash
# 生成后端 Python-Flask 项目结构
python -m features.scaffold.modules.backend_python.process.processGenerateStructure
```

### 3. 生成核心框架

```bash
# 生成核心框架结构
python -m features.scaffold.modules.core_classic.process.processGenerateStructure
```

## 脚手架配置

### 1. 前端配置

- 支持自定义组件类型
- 支持自定义布局结构
- 支持自定义样式主题

### 2. 后端配置

- 支持自定义 API 路由
- 支持自定义数据库结构
- 支持自定义业务逻辑

### 3. 核心配置

- 支持自定义模块类型
- 支持自定义卡片类型
- 支持自定义计划结构

## 开发规则

1. 脚手架开发
   1. 遵循模块化设计原则
   2. 确保生成的代码符合项目规范
   3. 支持配置化生成，提高灵活性
   4. 保持与核心框架的一致性

## 当前进展

- 基础脚手架框架搭建完成
- 支持前端 Vue 3 项目生成
- 支持后端 Python-Flask 项目生成
- 支持核心框架结构生成

## 下一步计划

- 增强脚手架配置能力
- 支持更多前端框架
- 支持更多后端框架
- 集成 AI 生成能力
- 提供可视化配置界面