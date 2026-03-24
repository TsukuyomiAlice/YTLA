# Classic Vue3 生成器脚本创建 Spec

## Overview
基于之前的 scaffold 模块结构分析结果，为 classic 核心类型的 Vue3 前端页面创建生成器脚本。这些脚本将放置在 general_classic/script 目录内，遵循特定的文件名规则。

## Goals
1. 创建 sidecard_generator 和 modules_generator 两种类型的生成器脚本
2. 脚本文件名遵循规则：script_classic_vue3_sidecard\_[前端组件名]\_generator.py 和 script_classic_vue3_modules\_[前端组件名]\_generator.py
3. 生成器基于早期 moduleGenerator.py 的参考，但采用当前 scaffold 架构
4. 生成器能够创建前端项目目录结构和基础 Vue 框架文件
5. 针对不同的前端组件类型（如 components、composables、stores 等）创建对应的生成器

## Non-Goals
- 不立即集成到现有调用流程中
- 不修改现有的 frontend_vue3 生成器
- 不处理后端生成逻辑
- 不为所有可能的前端组件类型创建生成器（先创建示例生成器）

## Background & Context
之前的分析显示：
- scaffold 模块包含 frontend_vue3 模块（15种生成器）和 general_classic 模块（协调器）
- 生成的文件放置在前端项目目录中，而非 scaffold 内部
- 早期脚本 moduleGenerator.py 已过时，但提供了生成逻辑参考
- frontend_vue3 模块包含多种前端组件生成器：components、composables、stores、styles、services 等

用户需要基于分析结果制作新的生成器脚本，放置在 general_classic/script 目录内。用户澄清了需求是针对组件类型而非模组，并更新了文件名规则。

## Functional Requirements
### FR-1: 生成器脚本创建
系统应创建两种类型的生成器脚本：
- sidecard_generator: 用于生成 cards 结构的文件
- modules_generator: 用于生成 modules 结构的文件

### FR-2: 文件名规范
生成器脚本文件名应遵循：
- script_classic_vue3_sidecard_[前端组件名]_generator.py
- script_classic_vue3_modules_[前端组件名]_generator.py
其中 [前端组件名] 来自前端组件类型，如 components、composables、stores、services 等。

### FR-3: 生成器功能
生成器应能够：
- 接收必要的参数（如模组名、子类型名、是否核心等）
- 创建前端项目目录结构（对应 cards 或 modules 结构）
- 生成指定组件类型的基础 Vue 框架文件
- 遵循现有的 scaffold 架构和路径生成逻辑
- 针对不同的前端组件类型实现特定的生成逻辑

### FR-4: 代码质量
生成器脚本应：
- 包含适当的错误处理
- 有清晰的文档字符串
- 使用一致的代码风格
- 参考早期脚本但不复制过时代码
- 易于扩展以支持更多组件类型

## Non-Functional Requirements
### NFR-1: 可维护性
生成器代码应易于理解和修改，结构清晰。

### NFR-2: 一致性
生成器应遵循项目现有的代码风格和架构模式。

### NFR-3: 可扩展性
生成器设计应允许未来添加新的前端组件类型或修改生成逻辑。

## Constraints
- 脚本必须放置在 general_classic/script 目录内
- 文件名必须符合指定规则
- 不能破坏现有的 scaffold 模块功能
- 必须基于之前的分析结果
- 生成器应针对组件类型而非模组

## Assumptions
- 前端项目结构保持稳定
- scaffold 模块架构不变
- 用户会手动调用生成器或未来集成到流程中
- 前端组件类型列表基于 frontend_vue3 模块的生成器类型

## Acceptance Criteria
### AC-1: 生成器脚本文件创建
- **Given**: general_classic/script 目录
- **When**: 创建生成器脚本
- **Then**: 脚本文件被创建在正确目录，文件名符合规范
- **Verification**: `programmatic`
- **Notes**: 检查文件是否存在且命名正确

### AC-2: 生成器功能完整性
- **Given**: 生成器脚本
- **When**: 分析脚本代码
- **Then**: 脚本包含必要的参数处理、目录创建和文件生成逻辑
- **Verification**: `human-judgment`
- **Notes**: 检查代码是否实现了基本生成功能

### AC-3: 与现有架构兼容性
- **Given**: 生成器脚本和 scaffold 模块
- **When**: 检查生成器代码
- **Then**: 生成器遵循现有的路径生成逻辑和架构模式
- **Verification**: `human-judgment`
- **Notes**: 确保不违反现有的设计原则

### AC-4: 代码质量
- **Given**: 生成器脚本
- **When**: 检查代码质量
- **Then**: 代码有清晰的文档、错误处理和一致的风格
- **Verification**: `human-judgment`
- **Notes**: 评估代码的可读性和可维护性

### AC-5: 组件类型针对性
- **Given**: 生成器脚本
- **When**: 检查生成器逻辑
- **Then**: 生成器针对特定的前端组件类型（如 components、composables 等）实现相应的生成逻辑
- **Verification**: `human-judgment`
- **Notes**: 确保生成器不是通用生成器，而是针对特定组件类型

## Open Questions
1. 需要为哪些具体的前端组件类型创建生成器？（建议：components、composables、stores 作为示例）
2. 生成器是否应该与现有的 frontend_vue3 生成器交互，还是独立工作？
3. 生成器参数应该如何设计？（建议：模组名、子类型名、是否核心、目标路径等）
4. sidecard 和 modules 生成器的具体区别是什么？（cards 结构与 modules 结构的差异）
5. 是否需要为所有 15 种前端组件类型创建生成器，还是选择性创建？

spec mode logging