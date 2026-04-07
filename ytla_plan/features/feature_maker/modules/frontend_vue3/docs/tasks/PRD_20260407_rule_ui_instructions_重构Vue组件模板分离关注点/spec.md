# Vue组件模板目录结构规范重构 - Product Requirement Document

## Overview
- **Summary**: 修改 rule_ui_instructions.md 文档，明确目录结构规范，确保导入路径正确：types 目录改为 definitions 目录，明确 composables、services、store、utils 等目录的用途
- **Purpose**: 确保文档中的示例使用正确的目录结构和导入路径，符合项目实际架构
- **Target Users": AI代理、前端开发人员、项目维护人员

## Goals
- 修改文件结构说明，使用正确的目录名（definitions 而非 types）
- 明确 definitions 目录用于存放 Props 和 Emits 定义
- 明确 composables 目录用于存放组合式函数
- 明确 services 目录用于存放 API 服务
- 明确 store 目录用于存放存储
- 明确 utils 目录用于存放配置文件
- 明确 styles 目录用于存放样式文件
- 更新所有示例以使用正确的目录结构和导入路径

## Non-Goals (Out of Scope)
- 不修改文档的其他章节内容
- 不改变现有的命名规则
- 不修改重构已存在UI元件的章节

## Background & Context
用户指出当前文档中的目录结构存在问题：
1. 使用了 "types" 目录，但应该使用 "definitions" 目录
2. 需要明确各个目录的具体用途
3. Props 和 Emits 定义应该在 definitions 目录下
4. 需要考虑 UI 是作为主组件还是布局组件的场景

## Functional Requirements
- **FR-1**: 修改文件结构说明，使用正确的目录名
- **FR-2**: 更新目录说明，明确各个目录的用途
- **FR-3**: 修改所有示例代码，使用正确的导入路径
- **FR-4**: 添加主组件和布局组件的场景说明
- **FR-5**: 更新文件关联示例以反映正确的目录结构

## Non-Functional Requirements
- **NFR-1": 保持文档格式和风格的一致性
- **NFR-2": 所有示例代码应语法正确
- **NFR-3": 修改应清晰易懂
- **NFR-4": 修改应可通过人工审查验证

## Constraints
- **Technical": 必须保持与 Vue 3 + TypeScript + SCSS 技术栈的兼容性
- **Business": 不能破坏现有文档的可用性
- **Dependencies": 依赖项目现有的目录结构和命名约定

## Assumptions
- 假设 definitions 目录用于存放类型定义（Props、Emits）
- 假设 composables 目录用于存放组合式函数
- 假设 services 目录用于存放 API 服务
- 假设 store 目录用于存放存储
- 假设 utils 目录用于存放工具和配置文件
- 假设 styles 目录用于存放样式文件

## Acceptance Criteria

### AC-1: 目录结构说明已更新
- **Given": 打开 rule_ui_instructions.md 文档
- **When": 查看文件结构说明
- **Then": 应该看到使用 "definitions" 而非 "types"
- **Verification": `human-judgment`

### AC-2: 目录用途说明明确
- **Given": 查看目录说明
- **When": 检查各个目录的用途描述
- **Then": 应该看到明确的 definitions、composables、services、store、utils、styles 目录用途说明
- **Verification": `human-judgment`

### AC-3: 示例使用正确的导入路径
- **Given": 查看所有代码示例
- **When": 检查导入路径
- **Then": 应该看到所有示例都使用正确的目录名和导入路径
- **Verification": `human-judgment`

### AC-4: 主组件和布局场景说明
- **Given": 查看相关内容
- **When": 查找主组件和布局组件的说明
- **Then": 应该看到关于 UI 作为主组件或布局组件的场景说明
- **Verification": `human-judgment`

### AC-5: 文档可正常读取
- **Given": 修改完成后的文档
- **When": 使用 Markdown 阅读器打开
- **Then": 文档格式正确，无语法错误，内容完整
- **Verification": `human-judgment`

## Open Questions
- 无
