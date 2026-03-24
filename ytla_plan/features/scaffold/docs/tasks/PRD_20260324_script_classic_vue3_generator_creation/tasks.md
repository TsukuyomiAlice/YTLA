本任务进度: 已完成

# Classic Vue3 生成器脚本创建 - 实现计划

## [x] Task 1: 确定生成器设计和组件类型选择
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 分析早期 script moduleGenerator.py 的生成逻辑和代码结构
  - 确定需要创建的前端组件类型（基于 frontend_vue3 模块的生成器类型，建议选择 components、composables、stores 作为示例）
  - 设计生成器参数接口（模组名、子类型名、是否核心模块、结构类型等）
  - 确定生成器与现有 scaffold 架构的集成方式
  - 区分 sidecard（cards 结构）和 modules（modules 结构）生成器的具体差异
  - 创建临时设计文档记录设计决策
- **Acceptance Criteria Addressed**: AC-2, AC-3, AC-5
- **Test Requirements**:
  - `human-judgement` TR-1.1: 能够清晰说明生成器设计思路和参数设计
  - `human-judgement` TR-1.2: 能够解释选择的组件类型及其理由
  - `human-judgement` TR-1.3: 能够说明 sidecard 和 modules 生成器的区别
- **Notes**: 基于之前的分析结果和 frontend_vue3 模块的生成器类型进行设计

## [ ] Task 2: 创建 sidecard_generator 脚本（针对 cards 结构）
- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 创建 script_classic_vue3_sidecard_[前端组件名]_generator.py 脚本
  - 实现 cards 结构的前端目录生成逻辑
  - 包含必要的参数验证和错误处理
  - 生成指定组件类型的基础 Vue 框架文件（参考早期脚本但不复制过时代码）
  - 确保生成的路径符合现有 scaffold 架构（使用 config.FRONTEND_FOLDER）
  - 为每个选择的组件类型（components、composables、stores）创建对应的 sidecard_generator
  - 实现针对不同组件类型的特定生成逻辑
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3, AC-4, AC-5
- **Test Requirements**:
  - `programmatic` TR-2.1: 脚本文件在 general_classic/script 目录中正确创建，文件名符合规范
  - `human-judgement` TR-2.2: 代码包含清晰的文档字符串和错误处理
  - `human-judgement` TR-2.3: 生成的目录路径逻辑与现有架构一致
  - `human-judgement` TR-2.4: 生成器针对特定组件类型实现相应的生成逻辑
- **Notes**: sidecard 对应 cards 结构，生成器应专注于创建 cards 结构下特定组件类型的文件和目录

## [ ] Task 3: 创建 modules_generator 脚本（针对 modules 结构）
- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 创建 script_classic_vue3_modules_[前端组件名]_generator.py 脚本
  - 实现 modules 结构的前端目录生成逻辑
  - 包含必要的参数验证和错误处理
  - 生成指定组件类型的基础 Vue 框架文件（参考早期脚本但不复制过时代码）
  - 确保生成的路径符合现有 scaffold 架构（使用 config.FRONTEND_FOLDER）
  - 为每个选择的组件类型（components、composables、stores）创建对应的 modules_generator
  - 实现针对不同组件类型的特定生成逻辑
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3, AC-4, AC-5
- **Test Requirements**:
  - `programmatic` TR-3.1: 脚本文件在 general_classic/script 目录中正确创建，文件名符合规范
  - `human-judgement` TR-3.2: 代码包含清晰的文档字符串和错误处理
  - `human-judgement` TR-3.3: 生成的目录路径逻辑与现有架构一致
  - `human-judgement` TR-3.4: 生成器针对特定组件类型实现相应的生成逻辑
- **Notes**: modules 对应 modules 结构，生成器应专注于创建 modules 结构下特定组件类型的文件和目录

## [ ] Task 4: 验证和文档完善
- **Priority**: P1
- **Depends On**: Task 2, Task 3
- **Description**: 
  - 验证所有生成的脚本文件语法正确性
  - 检查文件名是否符合规范
  - 创建使用说明文档或代码注释
  - 更新 actions.md 记录生成过程
  - 确保所有验收标准得到满足
  - 验证组件类型针对性（AC-5）
- **Acceptance Criteria Addressed**: AC-1, AC-4, AC-5
- **Test Requirements**:
  - `programmatic` TR-4.1: 所有脚本文件可通过 Python 语法检查
  - `human-judgement` TR-4.2: 文件名规范得到遵守
  - `human-judgement` TR-4.3: 代码文档完整清晰
  - `human-judgement` TR-4.4: 生成器确实针对特定组件类型而非通用生成器
- **Notes**: 此任务确保生成器质量并完成最终交付

# Task Dependencies
- Task 2 和 Task 3 依赖于 Task 1 的设计决策
- Task 4 依赖于 Task 2 和 Task 3 的完成
- Task 2 和 Task 3 可以并行执行

spec mode logging