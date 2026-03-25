# Scaffold 模块结构分析

## 1. 模块概述

scaffold 模块是 YTLA 项目的代码生成框架，用于自动化生成前端和后端代码文件。包含以下子模块：

### 1.1 `_type` 模块
- **职责**: 公共配置模块，提供类型定义和共享配置。
- **位置**: `modules/_type`
- **关键文件**: `const/constLangs.py`, `func/string.py`, `script/scriptCreateFile.py`

### 1.2 `backend_python_flask` 模块
- **职责**: 后端 Python Flask 代码生成器，生成后端 API、DAO、服务等。
- **位置**: `modules/backend_python_flask`
- **关键流程**: `processGenerateApi.py`, `processGenerateDao.py`, `processGenerateStructure.py` 等

### 1.3 `frontend_vue3` 模块
- **职责**: 前端 Vue3 代码生成器，生成 Vue 组件、组合式函数、存储、样式等。
- **位置**: `modules/frontend_vue3`
- **关键流程**: `processGenerateComponents.py`, `processGenerateComposables.py`, `processGenerateStores.py`, `processGenerateStructure.py` 等
- **生成器列表**: 包含 15 种生成器（参见 `constGenerators.generators`）

### 1.4 `general_classic` 模块
- **职责**: classic 核心类型的协调生成器，调用后端和前端生成器。
- **位置**: `modules/general_classic`
- **关键流程**: `processGenerateStructure.py`（协调器）

## 2. 模块关系

- `general_classic` 依赖 `frontend_vue3` 和 `backend_python_flask`。
- `frontend_vue3` 和 `backend_python_flask` 是独立的生成器集合。
- `_type` 可能被其他模块引用，提供公共类型和函数。

## 3. 文件生成流程

### 3.1 前端生成流程
调用 `generate_vue3_structure(is_core, structure, type_name, sub_type_name)` 函数：
- `is_core`: 是否为核心模块（true → 'core'，false → 'features'）
- `structure`: 结构类型（'cards', 'modules', 'plans', 'frame', 'users' 等）
- `type_name`: 类型类别/核心版本（如 'classic'）
- `sub_type_name`: 子类型类别（默认 '_type'）

**生成路径**: `frontend_project_path / prefix / type_name / structure / sub_type_name`
- `frontend_project_path`: 来自 `config.FRONTEND_FOLDER`，指向前端项目目录
- `prefix`: 'core' 或 'features'
- 示例：`src/core/classic/cards/_type`

### 3.2 协调生成流程
`general_classic` 中的 `process_generate_structure` 函数接收参数并决定是否生成前端和后端结构。

## 4. 关键发现

1. **生成的文件位置**: 生成的文件放置在前端项目目录（`ytla_plan_vue/src/...`），而非 scaffold 模块内部。
2. **生成器类型**: 包含组件、组合式函数、存储、样式、流程管理器等 15 种生成器。
3. **结构类型影响**: `structure` 参数影响生成路径的中间目录（cards/modules/plans/frame/users）。
4. **子类型默认值**: `sub_type_name` 默认为 '_type'，表示通用类型。

## 5. 问题初步回答

### 5.1 生成的基础 Vue 框架文件包含哪些类型？
包含组件、组合式函数、存储、样式、流程管理器、注册表、服务、工具等 15 种类型。

### 5.2 结构类型对目录位置的影响？
`structure` 参数直接影响生成路径的中间目录名，例如：
- `cards` → `.../cards/_type/`
- `modules` → `.../modules/_type/`
- `plans` → `.../plans/_type/`（仅核心模块可用）

### 5.3 生成的文件放在 scaffold 内部还是前端项目目录？
生成的文件放置在前端项目目录中，具体路径由 `config.FRONTEND_FOLDER` 配置决定。

## 6. 待深入分析点

1. `config.FRONTEND_FOLDER` 的具体值是什么？
2. 后端生成路径的类似逻辑。
3. 如何触发生成流程（用户调用入口）。

---
*分析时间: 2026-03-24*