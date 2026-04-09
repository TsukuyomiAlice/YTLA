# YTLA - Harness 工程规范 - 项目文件架构信息

## 0. 非常重要，必须阅读

在2.1章节同样存在以下内容

新生成的PRD文档和目录，需要放在下列指定位置：

- **对有明确类别的指定生成内容的任务**（如指定生成/更新readme.md）： **目标模组（子模组）下的** docs(documents)/tasks/PRD\_yyyymmdd\_\[文件]\_\[任务描述]/目录下
- **跨多个不同类别文件的任务(如同时涉及到process / script / ui ，而非单一概念的readme.md文档)**：在对应上位的 docs(documents)/tasks/PRD\_yyyymmdd\_\[任务描述]目录

检索是否存在已有的PRD文档时，也需要在 **目标模组（子模组）下的** docs/tasks/区域内查找

## 1. 总述

### 1.1 适用范围

- 指定规范目录：docs / documents（根据框架不同）
- 指定规范文档：harness\_instructions.md

## 2. Harness 模式启动引导

### 2.1 PRD 文档位置规定

新生成的PRD文档和目录，需要放在下列指定位置：

- **对有明确指定生成内容的任务**（如指定生成/更新readme.md）： **目标模组（子模组）下的** docs(documents)/tasks/PRD\_yyyymmdd\_\[文件]\_\[任务描述]/目录下
- **跨多个文件的任务**：在对应上位的 docs(documents)/tasks/PRD\_yyyymmdd\_\[任务描述]目录

检索是否存在已有的PRD文档时，也需要在 **目标模组（子模组）下的** docs(documents)/tasks/区域内查找

**示例**：

- 目标模组：`\[项目路径]/\[目标模组路径]`
- 任务：维护 readme.md 文档
- 正确的 PRD 目录：`\[项目路径]/\[目标模组路径]/docs(documents)/tasks/PRD_20260320_readme_维护documents模块readme文档\`

**错误示例**：

- ❌ 不要创建在项目根目录的 `./specs/` 下
- ❌ 不要创建在项目根目录的 `.trae/specs/` 下

## 3. 质量检查清单

### 3.1 规划阶段检查清单

- [ ] PRD 目录创建在目标模组的 docs/tasks 下，而非其他位置
- [ ] PRD 目录命名符合规范：PRD\_yyyymmdd\_\[文件]\_\[任务描述]

## 4. 常见陷阱和避免方法

### 4.1 规划阶段陷阱

❌ **陷阱**：PRD 目录创建在错误的位置（如 .trae/specs/ 或项目根目录）\
✅ **避免**：严格遵循 2.1 节的规定，必须创建在目标模组的 docs/tasks 下

***

**文档版本**: 1.7\
**最后更新**: 2026-03-24\
**维护者**: Official
