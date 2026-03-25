# 生成 Classic Vue3 脚手架脚本 - Product Requirement Document

## Overview
- **Summary**: 本项目旨在为 YTLA 项目生成一套自动化脚手架脚本，用于快速初始化 core=classic、前端框架=vue3 的模组，包括 sidecard 和 module 两种类型。脚本将遵循项目现有规范，生成标准化的目录结构和空模板代码。
- **Purpose**: 解决手动创建模组时容易出错、不符合规范的问题，提高开发效率，确保所有新生成的模组都遵循项目的统一标准。
- **Target Users**: YTLA 项目的前端开发人员

## Goals
- 生成适用于 sidecard 类型的自动化脚手架脚本
- 生成适用于 module 类型的自动化脚手架脚本
- 脚本文件命名符合规范：script_classic_vue3_[模组类型]_[目录名].py
- 生成的空模板代码符合项目现有规范
- 支持 _type 共享目录的生成
- docs 文件不生成（scaffold 已有相关方法）

## Non-Goals (Out of Scope)
- 不生成 docs 相关文件（scaffold 目录已有相关生成方法）
- 不修改现有模组的代码
- 不生成后端相关的脚手架脚本
- 不处理除 classic 核心外的其他核心类型
- 不处理除 Vue3 外的其他前端框架

## Background & Context
- YTLA 项目已有成熟的模组结构规范，参考 sideCard 和 definition 模组
- 已有 moduleGenerator.py 作为参考，但需要扩展和完善
- 发现存在 _type 共享目录，用于存放共享的类型定义和注册表
- scaffold 目录已有 docs 相关的生成方法

## Functional Requirements
- **FR-1**: 生成 sidecard 类型的脚手架脚本，包括 _type 目录和具体功能实现目录
- **FR-2**: 生成 module 类型的脚手架脚本，包括 _type 目录和具体功能实现目录
- **FR-3**: 每个目录类型（如 components、composables、definitions 等）对应一个独立的脚本文件
- **FR-4**: 脚本生成的空模板代码符合项目规范
- **FR-5**: 脚本支持参数化配置（如 module_type、module_sub_type 等）
- **FR-6**: 脚本输出使用提示信息

## Non-Functional Requirements
- **NFR-1**: 脚本代码清晰易读，有适当的注释
- **NFR-2**: 脚本遵循 Python 编码规范
- **NFR-3**: 脚本执行速度快，无明显延迟
- **NFR-4**: 生成的文件编码为 UTF-8

## Constraints
- **Technical**: 
  - 编程语言：Python
  - 前端框架：Vue 3 + TypeScript
  - 核心类型：classic
- **Business**: 
  - 时间约束：按用户要求先确认小结文档再生成脚本
- **Dependencies**: 
  - 参考现有模组：sideCard、definition、sample1
  - 参考 moduleGenerator.py

## Assumptions
- 假设项目目录结构不会发生重大变化
- 假设用户会确认小结文档后再继续生成脚本
- 假设 scaffold 目录的 docs 生成方法可用
- 假设生成的脚本会在正确的目录下执行

## Acceptance Criteria

### AC-1: SideCard 小结文档完整准确
- **Given**: 已探索 sideCard 和 sample1 模组结构
- **When**: 用户审查 temp_summary_sidecard.md
- **Then**: 文档应包含：1) _type 目录结构说明；2) 具体功能实现目录结构说明；3) 所有文件类型的空模板代码；4) 不含 docs 相关内容
- **Verification**: `human-judgment`
- **Notes**: 用户需确认此文档

### AC-2: Module 小结文档完整准确
- **Given**: 已探索 definition 模组结构
- **When**: 用户审查 temp_summary_module.md
- **Then**: 文档应包含：1) _type 目录结构说明；2) 具体功能实现目录结构说明；3) 所有文件类型的空模板代码；4) 不含 docs 相关内容
- **Verification**: `human-judgment`
- **Notes**: 用户需确认此文档

### AC-3: SideCard 脚手架脚本生成成功
- **Given**: 小结文档已通过用户确认
- **When**: 执行 sidecard 相关脚本
- **Then**: 应生成符合命名规范的脚本文件：script_classic_vue3_sidecard_[目录名].py
- **Verification**: `programmatic`

### AC-4: Module 脚手架脚本生成成功
- **Given**: 小结文档已通过用户确认
- **When**: 执行 module 相关脚本
- **Then**: 应生成符合命名规范的脚本文件：script_classic_vue3_module_[目录名].py
- **Verification**: `programmatic`

### AC-5: 脚本生成的空模板符合规范
- **Given**: 脚手架脚本已生成
- **When**: 使用脚本生成模组文件
- **Then**: 生成的空模板代码应与小结文档中的示例一致
- **Verification**: `human-judgment`

## Open Questions
- [ ] 除了已分析的目录类型外，是否还需要其他目录类型的脚本？
- [ ] 脚本是否需要集成到现有的 scaffold 系统中？
- [ ] 是否需要一个统一的入口脚本来调用所有子脚本？
