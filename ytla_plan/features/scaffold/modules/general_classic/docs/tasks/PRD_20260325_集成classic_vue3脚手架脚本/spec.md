# 集成 Classic Vue3 脚手架脚本 - Product Requirement Document

## Overview
- **Summary**: 本项目旨在将之前生成的 classic_vue3 脚手架脚本集成到现有的 scaffold 系统中，实现一键生成模组结构的功能。包括修改脚本去掉执行段、创建配置文件、创建调用模块、修改现有 process 文件、以及添加测试用例。
- **Purpose**: 将零散的脚本整合成统一的系统，使其能够与现有的 scaffold 架构无缝集成，提高开发效率。
- **Target Users**: YTLA 项目的开发人员

## Goals
- 修改已生成的 script_classic_vue3_*.py 脚本，只保留方法，去掉执行段（if __name__ == "__main__"）
- 创建 const 配置文件，定义 classic_vue3 的生成器列表
- 创建 processGenerateFile_vue3.py，用于调用这些脚本方法
- 修改已有的 processGenerateStructure.py，集成 processGenerateFile_vue3.py，实现一键生成
- 确认前后端语言环境从 config.py 读取
- 在 features_test 目录添加测试用例

## Non-Goals (Out of Scope)
- 不修改现有的 backend_python_flask 和 frontend_vue3 模块
- 不重构整个 scaffold 系统
- 不添加新的脚本类型（只整合已有的）

## Background & Context
- 之前已生成了 22 个 script_classic_vue3_*.py 脚本，位于 general_classic/script/ 目录
- 现有的 processGenerateStructure.py 调用 backend_python_flask 和 frontend_vue3 的生成器
- frontend_vue3 使用 constGenerators.py 定义生成器列表，通过动态导入调用
- config.py 定义了 CORE_VERSION、BACKEND_VERSION、FRONTEND_VERSION
- features_test 目录已有测试用例

## Functional Requirements
- **FR-1**: 修改所有已生成的 script_classic_vue3_*.py 脚本，去掉执行段，只保留方法定义
- **FR-2**: 在 general_classic/const/ 目录创建 constGenerators_vue3.py，定义 sidecard 和 module 类型的生成器列表
- **FR-3**: 在 general_classic/process/ 目录创建 processGenerateFile_vue3.py，根据参数调用相应的脚本方法
- **FR-4**: 修改 processGenerateStructure.py，在 gen_frontend 为 True 时调用 processGenerateFile_vue3.py
- **FR-5**: 确保系统从 config.py 读取前后端语言环境配置
- **FR-6**: 在 features_test 目录添加针对 classic_vue3 的测试用例

## Non-Functional Requirements
- **NFR-1**: 保持与现有 frontend_vue3 架构的一致性
- **NFR-2**: 脚本方法命名清晰，易于维护
- **NFR-3**: 向后兼容，不影响现有功能

## Constraints
- **Technical**: 
  - 编程语言：Python
  - 核心类型：classic
  - 前端框架：Vue 3
- **Business**: 
  - 沿用之前的PRD
- **Dependencies**: 
  - config.py 的配置
  - 已生成的 script_classic_vue3_*.py 脚本
  - frontend_vue3 的架构作为参考

## Assumptions
- 假设已生成的脚本方法都可以通过参数正确调用
- 假设 _type 和具体功能实现目录的区分可以通过 sub_type_name 参数判断
- 假设 config.py 的配置不会变更
- 假设 features_test 目录的测试架构不变

## Acceptance Criteria

### AC-1: 所有脚本已修改，只保留方法
- **Given**: 已生成的 22 个 script_classic_vue3_*.py 脚本
- **When**: 检查每个脚本文件
- **Then**: 脚本中不包含 if __name__ == "__main__" 执行段，只包含方法定义
- **Verification**: `programmatic`
- **Notes**: 检查所有脚本文件

### AC-2: constGenerators_vue3.py 已创建
- **Given**: 需要创建配置文件
- **When**: 检查 general_classic/const/ 目录
- **Then**: constGenerators_vue3.py 存在，且定义了 sidecard 和 module 类型的生成器列表
- **Verification**: `programmatic`
- **Notes**: 生成器列表格式参考 frontend_vue3/const/constGenerators.py

### AC-3: processGenerateFile_vue3.py 已创建
- **Given**: 需要创建调用模块
- **When**: 检查 general_classic/process/ 目录
- **Then**: processGenerateFile_vue3.py 存在，且能根据 structure（cards/modules）和 sub_type_name（_type或具体名称）调用相应的生成器
- **Verification**: `programmatic`
- **Notes**: 参考 frontend_vue3/process/processGenerateStructure.py 的实现方式

### AC-4: processGenerateStructure.py 已修改
- **Given**: 需要修改现有文件
- **When**: 检查 processGenerateStructure.py
- **Then**: 当 gen_frontend 为 True 时，会调用 processGenerateFile_vue3.py，且能正确根据 config.py 的配置判断
- **Verification**: `programmatic`
- **Notes**: 保持与 backend_python_flask 和 frontend_vue3 的集成方式一致

### AC-5: 测试用例已添加
- **Given**: 需要添加测试
- **When**: 检查 features_test/scaffold/modules/general_classic/process/ 目录
- **Then**: processGenerateStructureTest.py 包含针对 classic_vue3 的测试用例
- **Verification**: `programmatic`
- **Notes**: 测试 sidecard 和 module 类型，_type 和具体功能实现

## Open Questions
- [ ] sidecard 和 module 的生成器列表是否需要分开定义？
- [ ] 是否需要根据 config.py 的 CORE_VERSION、FRONTEND_VERSION 动态判断调用哪个生成器？
