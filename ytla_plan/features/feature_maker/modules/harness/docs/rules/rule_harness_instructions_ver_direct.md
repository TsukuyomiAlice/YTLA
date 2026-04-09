# YTLA - Harness 工程规范（非IDE依赖版）

## 0. 非常重要，必须阅读

0.1 仅当你阅读到本文档时，如果本文档内容与其它文档存在冲突，**以本文档要求为准**.

0.2 **当你看到这份文档并且用户要求进行项目开发时，必须即刻开始本文档里提到的 Start Stage**

## 1. 总述

### 1.1 适用范围

- 适用核心名: 全部
- 适用栈: 包括前后端
- 适用语言类型和框架: 全部

### 1.2 设计理念

- **约定优于配置** - 通过标准化的目录结构和文件命名实现自动化
- **规划先行** - 先规划再执行，确保变更可控
- **子代理协作** - 合理使用分段对话或独立对话实现任务分解和并行处理
- **验证驱动** - 每个任务都有明确的验收标准
- **过程可追溯** - 通过 actions.md 记录完整的执行过程

### 1.3 工作环境假设

本文档适用于任意大模型对话环境，无需特定IDE。

**文件操作说明**：
- 读取文件：请明确告知需要读取的文件路径，我会描述文件内容
- 写入文件：请明确告知文件路径和内容，我会提供完整的文件内容供你保存
- 修改文件：请明确告知需要修改的文件路径和具体修改内容
- 列出目录：请明确告知目录路径，我会描述目录结构

**用户交互说明**：
- 所有交流通过自然语言对话进行
- 需要用户确认时，我会明确提出问题
- 用户可以随时提出新的需求或修改要求

**子代理协作说明**：
- 对于复杂任务，可以通过分段对话或独立对话实现
- 每个分段对话有清晰的任务描述和验收标准
- 分段对话完成后，汇总结果继续执行

## 2. Harness 模式启动引导

### 2.1 启动引导流程

在用户明确要求进行项目开发后，即刻开始 **Start Stage**：

**Start Stage（启动阶段）**：

1. **思考分析** - 理解用户需求，确定目标模组位置和任务类型
2. **探索代码库** - 请用户提供当前代码库状态，或根据已知信息分析
3. **检索已有 PRD** - 请用户检查目标模组的 docs/tasks 区域内是否已存在相关 PRD 文档
   - 检查方法：查看 PRD 目录下的 tasks.md 第一行是否包含 "本任务进度: 已完成" 或不存在该行
   - 如果显示 "已完成" 或不存在该行，则视为该 PRD 工程已完成
4. **创建 PRD 目录** - 请用户在指定位置创建目录，或提供目录路径确认
5. **进入 Planning Stage** - 建立 PRD 目录后进入规划阶段

## 3. 工作模式

### 3.1 三个阶段概述

Harness 模式包含三个连续的阶段：

1. **Start Stage（启动阶段）** - 检索已有 PRD、创建 PRD 目录
2. **Planning Stage（规划阶段）** - 生成规划文档（origin.md、spec.md、tasks.md、checklist.md、actions.md）
3. **Action Stage（执行阶段）** - 执行 tasks.md 中的任务

**重要**：每次执行新的文件操作之前，必须先完成 actions.md 的记录（更新 actions.md 本身不用记录，避免陷入自身死循环）

### 3.2 Spec Mode（规划模式）

**适用场景**：需要详细规划的任务，如新增功能、重构、文档维护等

**工作流程**（Planning Stage）：

1. 生成 Action Record (actions.md) - 行动记录
2. 生成 Original Requirement (origin.md) - 原始需求文档
3. 生成 PRD (spec.md) - 产品需求文档
4. 生成 Implementation Plan (tasks.md) - 实现计划
   - tasks.md 第一行必须包含：`本任务进度: 未完成`
5. 生成 Verification Checklist (checklist.md) - 验证清单
6. 请用户审查规划文档
7. 等待用户批准后进入 Action Stage

### 3.3 Agent Mode（执行模式）

**适用场景**：已规划好的任务，或简单的单步任务

**工作流程**（Action Stage）：

1. 从 tasks.md 选择优先级最高的待处理任务
2. 告知用户正在处理该任务
3. 如需复杂任务，建议通过分段对话或独立对话处理
4. 执行任务并进行验证
5. 告知用户任务完成情况
6. 重复直到所有任务完成，进入第7步
7. 所有任务执行完毕后，主动向用户发起提问，确认任务是否全部完成
8. 用户确认完成后，请用户更新 tasks.md 第一行为 "本任务进度: 已完成"

## 4. 规划文档规范

### 4.1 origin.md (Original Requirements Document) 规范

**必填章节**：

- 头部信息
- 多轮对话记录（每个对话使用 `# Dialogue [序号]` 作为标题）
- User Requirements - 用户需求
- Analyze - 需求分析
- Evaluation Result - 预估结果

**格式要求**：

```markdown
Harness Instructions file version: [输入的harness文件的文件名及版本]  
Harness Instructions file Author: [harness文件的作者名]

# Original Requirement - 原始需求

# Dialogue 1

## User Requirement: 
[用户输入的原始内容]

## Analyze：
[对用户输入内容的需求分析过程，包含以下内容]
**Given**： [原文中提及的资源]
**Target**： [用户提到的目标，或用户的指令要求]
**Evidence**： [用以指明用户实际需求的具体内容]

## Evaluation Result：
[用户希望获得的产物列表，包含以下内容]
### [产物名]： [产物的形式]

# Dialogue 2

## User Requirement: 
[用户追加的需求内容]

## Analyze：
[对追加需求的分析]
**Given**： [相关资源]
**Target**： [追加的目标]
**Evidence**： [追加需求的具体内容]

## Evaluation Result：
[追加需求的产物列表]
```

**多轮对话说明**：

- 原始需求作为 Dialogue 1，后续追加需求依次编号为 Dialogue 2、Dialogue 3 等
- 每个 Dialogue 都包含完整的 User Requirement、Analyze 和 Evaluation Result 章节
- 对话序号从 1 开始递增
- 更新 origin.md 时，采用追加方式在文件末尾添加新内容，不要覆盖整个文件（初始创建和完全重写除外）

### 4.2 spec.md (Product Requirements Document) 规范

**必填章节**：

- Overview - 概要
- Goals - 目标
- Non-Goals - 非目标（边界）
- Background & Context - 背景和上下文
- Functional Requirements - 功能需求
- Non-Functional Requirements - 非功能需求
- Constraints - 约束条件
- Assumptions - 假设
- Acceptance Criteria - 验收标准（Given/When/Then 格式）
- Open Questions - 待解决问题

**验收标准格式要求**：

```markdown
### AC-1: [标准名称]
- **Given**: [前置条件]
- **When**: [触发动作]
- **Then**: [可观察的结果]
- **Verification**: `programmatic` | `human-judgment`
- **Notes**: [补充说明]
```

### 4.3 tasks.md (Implementation Plan) 规范

**格式要求**：

```markdown
本任务进度: [已完成/未完成]

# [Project Title] - The Implementation Plan (Decomposed and Prioritized Task List)

## [ ] Task [序号]: [任务标题]
- **Priority**: P0 | P1 | P2
- **Depends On**: [依赖的任务 ID 或 "None"]
- **Description**: 
  - [需要实现的内容]
  - [关键实现细节]
- **Acceptance Criteria Addressed**: [AC-1, AC-2, ...]
- **Test Requirements**:
  - `programmatic` TR-[序号].1: [可测量的验证点]
  - `human-judgement` TR-[序号].2: [人工审查的要点]
- **Notes**: [边界情况、风险、实现提示]
```

**优先级定义**：

- **P0** - 关键路径，阻塞其他工作，核心功能
- **P1** - 重要但不阻塞，次要功能
- **P2** - 锦上添花，优化，完善

**进度标记说明**：

- tasks.md 第一行必须包含 "本任务进度: \[已完成/未完成]" 标记
- 新任务初始状态为 "未完成"
- 用户确认任务全部完成后，更新为 "已完成"
- Start Stage 检索时，如显示 "已完成" 或不存在该行，视为该 PRD 工程已完成

### 4.4 checklist.md (Verification Checklist) 规范

**格式要求**：

```markdown
- [ ] Checkpoint 1: [简洁具体的验证检查点描述]
- [ ] Checkpoint 2: [简洁具体的验证检查点描述]
...
```

**注意事项**：

- 每个检查点应该是可验证的
- 避免模糊的描述
- 按逻辑顺序排列

### 4.5 actions.md (Action Record) 规范

**文档用途**：用于记录执行 spec 模式的完整过程，包括思考、目标、操作和文件操作

**必填章节**：

- Start Stage（启动阶段）
- Planning Stage（规划阶段）
- Action Stage（执行阶段）

**行动记录项格式要求**：

```markdown
### ACT-[序号]:
- **Thought**: [思考内容]
- **Target**: [执行目标]
- **Action**: [具体操作描述]
- **Touches**: [读取/生成/修改/删除的文件列表，涉及的实际对象等]
```

**记录规则**：

- 每次执行新的文件操作之前，必须先完成 actions.md 的记录
- **重要**：更新 actions.md 本身的操作不需要记录，避免陷入自身死循环
- Thought 应该真实记录当时的思考过程
- Target 应该明确具体
- Action 应该描述具体的操作
- Touches 应该列出涉及的文件的完整路径
- 更新 actions.md 时，采用追加方式在文件末尾添加新内容，不要覆盖整个文件

**临时生成文本存储规范**：

- 当生成了包含大规模文本的非目标文件时，将相关内容记录在 PRD 目录下
- 临时文件命名格式为：`temp_[自行设计标题].md`
- 标题应能清晰反映文件内容
- 临时文件只记录在当前 PRD 目录下
- **重要**：分段对话生成临时文档时，必须在同目录（当前任务所在的 PRD 目录）下生成，确保文档位置不混乱

**过程文件列表规范**：

- 在 actions.md 文档标题下方，新增 "Generated Procedure Files List  过程文件列表" 章节
- 该章节用于记录生成的大规模文本内容文件的文件名（不包含路径）
- 每次新生成中途分析文档时，都更新这个章节里的内容
- 文件名列表按生成顺序排列

**用户输入记录规则**：

- 在 Planning Stage 和 Action Stage 中，用户输入使用 `### USER：Dialogue [序号]` 格式插入
- 用户输入记录后，继续记录后续操作
- 对话序号与 origin.md 中的对话序号保持一致

**Planning Stage 一次性记录规则**：

- 在 Start Stage 完成后，可以一次性记录 origin.md、spec.md、tasks.md、checklist.md 的生成操作
- 一次性记录后可以连续生成这些文件
- 一次性记录仅适用于这四个规划文档的初始生成

**Action Stage 记录规则**：

- Action Stage 通常保持分开记录，每次操作单独记录
- 相同目标的操作可以合并记录，不限阶段
- 合并记录时，Thought、Target、Action、Touches 都应该清晰地反映多个操作

**todo 列表操作记录规则**：

- Todo 列表在第一次生成时必须记录在 actions.md 里，并且带上完整的 task 内容
- 使用标准的 ACT- 记录格式
- 更新 todo 列表状态时也要记录到 actions.md

**通知用户操作记录规则**：

- 通知用户操作也需要记录到 actions.md
- 使用标准的 ACT- 记录格式

**向用户发起提问记录规则**：

- 向用户发起追问或提问的操作，必须在提问之前记录到 actions.md
- 使用标准的 ACT- 记录格式
- 记录应包含提问的目的和内容概要

**子代理/分段对话操作记录规则**：

- 分段对话的调用操作必须明确地被记录在 actions.md 里
- 使用标准的 ACT- 记录格式
- 记录应包含分段对话的任务描述和目标

**相同目标操作合并规则**：

- 如果多个操作针对相同目标，可以合并记录
- 合并记录不限阶段（Planning Stage 或 Action Stage 都可以）
- 合并记录时，Thought 应该说明多个操作的共同目标
- Action 应该列出所有使用的操作
- Touches 应该列出所有涉及的文件

**示例**：

```markdown
# Action Record - 行动记录

## Generated Procedure Files List  过程文件列表

- temp_initial_analysis.md
- temp_code_review_notes.md

---

## Start Stage (启动阶段)

### ACT-1:
- **Thought**: 用户发送了项目开发要求，需要先探索代码库了解当前状态
- **Target**: 查看目标模组的目录结构
- **Action**: 请用户提供目标模组的目录结构
- **Touches**: [目标模组路径]

---

## Planning Stage (规划阶段)

### USER：Dialogue 1
[用户原始输入内容]

### ACT-2:
- **Thought**: Start Stage 已完成，现在一次性记录并生成所有规划文档
- **Target**: 创建 PRD 目录并生成 origin.md、spec.md、tasks.md、checklist.md
- **Action**: 请用户创建 PRD 目录，然后提供所有规划文档内容
- **Touches**: [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]
             [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/origin.md
             [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/spec.md
             [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/tasks.md
             [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/checklist.md

### USER：Dialogue 2
[用户追加需求内容]

### ACT-3:
- **Thought**: 用户提出了追加需求，需要更新 origin.md 和相关文档
- **Target**: 更新 origin.md 添加 Dialogue 2，更新其他规划文档
- **Action**: 提供更新后的文档内容
- **Touches**: [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/origin.md
             [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/spec.md

### ACT-4:
- **Thought**: 规划文档已生成完毕，现在需要请用户审查
- **Target**: 请用户审查规划文档
- **Action**: 告知用户规划文档已生成，请审查
- **Touches**: []

---

## Action Stage (执行阶段)

### ACT-5:
- **Thought**: 开始执行第一个任务
- **Target**: 开始处理 Task 1
- **Action**: 告知用户正在处理 Task 1
- **Touches": []

### ACT-6:
- **Thought**: Task 1 比较复杂，建议通过分段对话处理
- **Target**: 建议通过分段对话执行 Task 1
- **Action**: 向用户建议分段对话处理，并提供分段对话的任务描述
- **Touches": []
- **Subtask**: 描述：[3-5 个词的简短描述]
任务：[详细的任务说明]
返回语言：zh-CN

### ACT-7:
- **Thought**: 执行 Task 1 的具体内容
- **Target": 完成 Task 1 的要求
- **Action**: 提供需要生成/修改的文件内容
- **Touches": [目标文件路径]

### ACT-8:
- **Thought**: Task 1 已完成，需要告知用户
- **Target": 告知用户 Task 1 已完成
- **Action": 告知用户 Task 1 完成情况
- **Touches": []

### ACT-9:
- **Thought": 需要向用户追问某些细节以便继续执行
- **Target": 向用户提问
- **Action": 记录提问操作并向用户提问
- **Touches": []

### USER：Dialogue 3
[用户在执行阶段提出的追加需求或对追问的回复]

### ACT-10:
- **Thought": 用户提出了新的需求，需要更新 origin.md 和规划文档
- **Target": 更新 origin.md 添加 Dialogue 3，更新相关规划
- **Action": 提供更新后的文档内容
- **Touches": [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/origin.md
             [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/tasks.md

### ACT-11:
- **Thought": 所有任务已执行完毕，现在需要向用户确认任务是否全部完成
- **Target": 向用户确认任务完成情况
- **Action": 记录确认操作并向用户提问
- **Touches": []

### USER：Dialogue 4
[用户确认任务已完成]

### ACT-12:
- **Thought": 用户已确认任务完成，需要请用户更新 tasks.md 第一行为"已完成"
- **Target": 请用户更新 tasks.md 进度标记
- **Action": 告知用户更新 tasks.md
- **Touches": [目标模组路径]/docs/tasks/PRD_yyyymmdd_[任务描述]/tasks.md
```

### 4.6 PRD 文档更新规则

**文档分类和更新方式**：

- **spec.md、tasks.md、checklist.md**：优先提供完整内容供用户覆盖
- **origin.md、actions.md**：由于新的内容不会对旧的内容产生影响，所以总是在文档末尾追加内容
  - 仅限于在origin.md、action.md中，为了便于定位，在每次生成追加文本时，最后添加一行
  ```markdown
  spec mode logging
  ```
  用来表示文末。在追加内容时，以此为标识。

**说明**：

- spec.md、tasks.md、checklist.md 文档内容经常需要整体修改，提供完整内容覆盖可以确保文档的一致性和完整性
- origin.md、actions.md 文档主要用于记录历史过程，通过追加方式可以保留完整的历史记录
- 唯一的例外是，如果发现文档内容出现了遗漏、乱序等严重的记录问题，那么必须提供完整内容重写

## 5. 文档维护工作流

### 5.1 完整工作流

```
1. 用户发起请求
   ↓
2. Start Stage（启动阶段）
   ├─ 理解需求，探索代码库
   ├─ 检索已有 PRD 文档（检查 tasks.md 第一行进度标记）
   ├─ 请用户创建 PRD 目录
   └─ 进入 Planning Stage
   ↓
3. Planning Stage（规划阶段）
   ├─ 生成 actions.md（记录整个过程）
   ├─ 一次性记录 origin.md、spec.md、tasks.md、checklist.md
   ├─ 提供这些规划文档内容（tasks.md 第一行添加"本任务进度: 未完成"）
   ├─ 记录用户追加需求（如有）
   ├─ 请用户审查规划文档
   └─ 等待用户批准
   ↓
4. 用户批准规划
   ↓
5. Action Stage（执行阶段）
   ├─ 选择 P0 任务
   ├─ 告知用户正在处理该任务
   ├─ 如需复杂任务，建议分段对话
   ├─ 执行任务
   ├─ 验证任务
   ├─ 告知用户任务完成
   ├─ 记录用户追加需求（如有）
   ├─ 如需向用户追问，先记录再提问
   ├─ 重复直到所有任务完成
   └─ 更新 actions.md
   ↓
6. 所有任务执行完毕
   ↓
7. 主动向用户确认任务是否全部完成
   ├─ 先记录确认操作到 actions.md
   └─ 向用户发起提问
   ↓
8. 用户确认完成
   ↓
9. 最终完成步骤
   ├─ 记录用户确认到 actions.md
   ├─ 请用户更新 tasks.md 第一行为"本任务进度: 已完成"
   └─ 完成并总结
```

### 5.2 追加需求记录流程

**适用场景**：

- Planning Stage 用户批准前提出的追加需求
- Action Stage 执行过程中提出的追加需求
- Action Stage 执行完成后提出的追加需求

**记录流程**：

```
1. 用户提出追加需求
   ↓
2. 在 actions.md 中插入用户输入记录
   ├─ 使用 `### USER：Dialogue [序号]` 格式
   ├─ 序号与 origin.md 保持一致
   └─ 插入到对应阶段（Planning Stage 或 Action Stage）
   ↓
3. 在 origin.md 中添加新的 Dialogue 章节
   ├─ 标题使用 `# Dialogue [序号]`
   ├─ 包含完整的 User Requirement、Analyze、Evaluation Result
   ├─ 序号从之前的最大值递增
   └─ 使用追加方式在 origin.md 末尾添加
   ↓
4. 更新相关规划文档（根据需要）
   ├─ 更新 spec.md（如有功能需求变更）
   ├─ 更新 tasks.md（如有任务变更）
   ├─ 更新 checklist.md（如有验证点变更）
   └─ 记录所有更新操作到 actions.md
   ↓
5. 继续执行（如需）
   ├─ 如在 Planning Stage，继续等待用户批准
   ├─ 如在 Action Stage，继续执行任务或更新任务
   └─ 记录后续操作到 actions.md
```

**注意事项**：

- 追加需求必须同时记录在 origin.md 和 actions.md 中
- actions.md 中的用户输入记录必须使用 `### USER：Dialogue [序号]` 格式
- 对话序号必须与 origin.md 中的序号保持一致
- 追加需求后的规划文档更新也必须记录到 actions.md
- 更新 origin.md 和 actions.md 时，采用追加方式在文件末尾添加新内容

### 5.3 向用户发起提问流程

**适用场景**：

- 需要向用户追问以明确需求
- 任务执行完毕需要用户确认是否完成
- 其他需要用户输入的场景

**记录流程**：

```
1. 准备向用户发起提问
   ↓
2. 在 actions.md 中记录提问操作
   ├─ 使用标准的 ACT- 记录格式
   ├─ Thought 说明提问的目的
   ├─ Target 明确提问的目标
   ├─ Action 描述提问操作
   └─ Touches 留空或列出相关文件
   ↓
3. 向用户发起实际提问
   ↓
4. 用户回复后，在 actions.md 中插入用户输入记录
   ├─ 使用 `### USER：Dialogue [序号]` 格式
   └─ 插入到对应阶段
   ↓
5. 继续后续操作
```

## 6. 分段对话协作规范

### 6.1 何时使用分段对话

**推荐使用场景**：

- 任务可以分解为多个独立的子任务
- 任务需要大量的上下文探索
- 任务可以并行处理
- 任务是黑盒验证（只需要结果，不需要过程）

**不推荐使用场景**：

- 单步简单任务
- 任务间有紧密的依赖关系
- 需要保留完整的上下文用于后续任务

### 6.2 分段对话委派规范

**委派任务时的提示词要点**：

- 清晰的任务描述
- 明确的验收标准
- 提供必要的上下文
- 指定返回格式
- 说明如何验证

**示例**：

```
请独立完成以下任务：

描述：[3-5 个词的简短描述]
任务：[详细的任务说明]
返回语言：zh-CN

请按要求完成后返回结果。
```

### 6.3 分段对话协作模式

**串行模式**：

```
主对话 → 分段对话 1 → 分段对话 2 → ... → 完成
```

适用：任务间有依赖关系

**并行模式**：

```
         ┌→ 分段对话 1 ─┐
主对话 ──┼→ 分段对话 2 ─┼→ 汇总 → 完成
         └→ 分段对话 3 ─┘
```

适用：任务间相互独立

## 7. 质量检查清单

### 7.1 规划阶段检查清单

- [ ] origin.md 包含所有必填章节
- [ ] origin.md 头部信息已添加
- [ ] origin.md 多轮对话使用 `# Dialogue [序号]` 格式
- [ ] spec.md 包含所有必填章节
- [ ] 每个目标都有对应的验收标准
- [ ] 验收标准使用 Given/When/Then 格式
- [ ] 每个验收标准都有明确的验证类型
- [ ] Non-Goals 明确说明了边界
- [ ] tasks.md 第一行已添加 "本任务进度: 未完成" 标记
- [ ] tasks.md 任务分解合理
- [ ] 任务优先级正确
- [ ] 任务依赖关系正确
- [ ] 每个任务都有测试要求
- [ ] checklist.md 检查点完整且可验证
- [ ] actions.md 已创建且包含三个阶段
- [ ] actions.md 中的行动记录项格式正确
- [ ] actions.md 中已包含 "Generated Procedure Files List  过程文件列表" 章节
- [ ] Planning Stage 使用了一次性记录方式（如适用）
- [ ] Start Stage 已完整执行并记录

### 7.2 执行阶段检查清单

- [ ] 一次只执行一个任务
- [ ] 任务状态及时告知用户
- [ ] 复杂任务建议分段对话
- [ ] 每个任务完成后进行验证
- [ ] 测试要求都已满足
- [ ] 任务完成后更新 checklist.md
- [ ] 执行过程及时记录到 actions.md
- [ ] todo 列表操作已记录
- [ ] 通知用户操作已记录
- [ ] 向用户提问前已记录到 actions.md
- [ ] 用户追加需求已记录（如有）
- [ ] actions.md 中用户输入使用 `### USER：Dialogue [序号]` 格式（如有）
- [ ] 更新 origin.md 和 actions.md 时使用追加方式
- [ ] 临时生成文本按规范存储在 PRD 目录下
- [ ] 过程文件列表已及时更新（如有临时文件生成）

### 7.3 最终验收检查清单

- [ ] 所有 P0 任务已完成
- [ ] 所有 P1 任务已完成（或已明确为后续任务）
- [ ] checklist.md 所有检查点已通过
- [ ] 验收标准都已满足
- [ ] 没有引入新的问题
- [ ] 文档已同步更新
- [ ] actions.md 完整记录了整个执行过程
- [ ] 用户追加需求已完整记录（如有）
- [ ] 已向用户确认任务是否完成
- [ ] 用户确认完成后，tasks.md 第一行已更新为 "本任务进度: 已完成"
- [ ] 用户需求已满足

## 8. 最佳实践

### 8.1 规划最佳实践

- **先探索后规划** - 充分理解当前状态再做规划
- **边界清晰** - 明确什么是 IN，什么是 OUT
- **可验证的标准** - 每个验收标准都应该是可验证的
- **合理分解** - 任务粒度要适中，既不过大也不过小
- **优先级正确** - 先做关键路径上的任务
- **一次性生成** - 修改或创建 spec.md、tasks.md、checklist.md 文档时，优先提供完整内容，不要逐行修改
- **Planning Stage 一次性记录** - 在 Start Stage 完成后，可以一次性记录 origin.md、spec.md、tasks.md、checklist.md 的生成操作
- **及时记录** - 在每次操作前(包括但不限于文件操作、用户询问操作、分段对话操作等)先更新 actions.md
- **记录追加需求** - 用户提出的追加需求必须同时记录在 origin.md（`# Dialogue [序号]`）和 actions.md（`### USER：Dialogue [序号]`）
- **tasks.md 进度标记** - 新创建的 tasks.md 第一行必须添加 "本任务进度: 未完成"
- **临时文件规范** - 生成大规模临时文本时，按规范存储在 PRD 目录下并记录到 actions.md 的过程文件列表中

### 8.2 执行最佳实践

- **一次一个** - 一次只执行一个任务，完成一个再做下一个
- **及时告知** - 任务状态要及时告知用户
- **合理分段** - 复杂任务建议分段对话
- **验证驱动** - 完成任务后立即验证
- **渐进式** - 完成一个任务再进入下一个
- **记录过程** - 执行过程及时记录到 actions.md
- **记录 todo 操作** - todo 列表操作也要记录，并且在新建 todo 列表时，列出列表内每一项 task 的内容
- **记录分段对话操作** - 发起分段对话操作也要记录
- **记录通知操作** - 通知用户操作也要记录
- **记录提问操作** - 向用户发起提问前必须先记录到 actions.md
- **相同目标合并记录** - 针对相同目标的多个操作可以合并记录
- **Action Stage 分开记录** - Action Stage 通常保持分开记录，除非目标相同
- **追加写入** - 更新 origin.md 和 actions.md 时，优先使用追加方式在文件末尾添加新内容，不要覆盖整个文件
- **任务完成确认** - 所有任务执行完毕后，必须主动向用户确认任务是否全部完成
- **更新进度标记** - 用户确认完成后，请用户更新 tasks.md 第一行为 "本任务进度: 已完成"
- **临时文件管理** - 生成临时文件后立即更新 actions.md 的过程文件列表

## 9. 常见陷阱和避免方法

### 9.1 规划阶段陷阱

❌ **陷阱**：规划过于详细，导致执行时发现不可行\
✅ **避免**：保持规划在合理的抽象层次，留出调整空间

❌ **陷阱**：没有明确 Non-Goals，导致范围蔓延\
✅ **避免**：明确说明什么不做，设定清晰的边界

❌ **陷阱**：验收标准模糊，无法验证\
✅ **避免**：使用 Given/When/Then 格式，明确验证类型

❌ **陷阱**：对 spec.md、tasks.md、checklist.md 文档逐行修改，反复提供部分内容，导致执行效率低下和文件版本混淆\
✅ **避免**：修改或创建 spec.md、tasks.md、checklist.md 文档时，优先提供完整文件内容。如果文件已存在，先请用户提供完整内容，再提供完整的更新后内容。

❌ **陷阱**：更新 origin.md 或 actions.md 时使用覆盖写入，导致历史记录丢失\
✅ **避免**：更新这两个文档时，总是使用追加方式在文件末尾添加新内容，且以"spec mode logging"作为文本末尾标记（初始创建除外）

❌ **陷阱**：忘记记录 actions.md，或记录不完整\
✅ **避免**：在每次操作前先更新 actions.md，确保记录完整

❌ **陷阱**：记录 actions.md 时也记录对 actions.md 本身的更新，导致无限循环\
✅ **避免**：更新 actions.md 本身的操作不需要记录

❌ **陷阱**：用户追加需求只记录在一个文档中，导致过程不完整\
✅ **避免**：追加需求必须同时记录在 origin.md（使用 `# Dialogue [序号]`）和 actions.md（使用 `### USER：Dialogue [序号]`）中

❌ **陷阱**：Planning Stage 每个文件生成都单独记录，效率低下\
✅ **避免**：在 Start Stage 完成后，可以一次性记录 origin.md、spec.md、tasks.md、checklist.md 的生成操作，然后连续提供这些文件

❌ **陷阱**：忘记在 tasks.md 第一行添加进度标记\
✅ **避免**：新创建的 tasks.md 第一行必须添加 "本任务进度: 未完成"

❌ **陷阱**：忘记在 actions.md 中添加 "Generated Procedure Files List  过程文件列表" 章节\
✅ **避免**：创建 actions.md 时，在文档标题下方立即添加过程文件列表章节

### 9.2 执行阶段陷阱

❌ **陷阱**：同时执行多个任务，导致混乱\
✅ **避免**：一次只执行一个任务，完成一个再做下一个

❌ **陷阱**：不使用分段对话，导致主对话上下文过大\
✅ **避免**：合理使用分段对话分解任务

❌ **陷阱**：任务完成后不验证，导致后期发现问题\
✅ **避免**：每个任务完成后立即验证

❌ **陷阱**：只记录文件操作，不记录 todo 列表和通知用户操作\
✅ **避免**：actions.md 需要记录所有操作类型，包括文件操作、todo 列表操作、通知用户操作

❌ **陷阱**：相同目标的操作分开记录，导致 actions.md 冗长\
✅ **避免**：如果多个操作针对相同目标，可以合并记录，不限阶段

❌ **陷阱**：Action Stage 也使用一次性记录，导致过程不清晰\
✅ **避免**：Action Stage 通常保持分开记录，除非目标相同的操作可以合并

❌ **陷阱**：向用户发起提问前没有记录到 actions.md\
✅ **避免**：提问操作必须在执行前记录到 actions.md，使用标准的 ACT- 格式

❌ **陷阱**：todo 列表的具体Task 没有记录到 actions.md\
✅ **避免**：todo 列表的具体Task必须在发起 todo 列表之前记录到 actions.md，使用标准的 ACT- 格式

❌ **陷阱**：更新 origin.md 或 actions.md 时使用覆盖写入，导致历史记录丢失\
✅ **避免**：更新这两个文档时，总是使用追加方式在文件末尾添加新内容，且以"spec mode logging"作为文本末尾标记（初始创建除外）

❌ **陷阱**：更新 origin.md 或 actions.md 时出现了乱序，为了节约时间不管文档问题继续直接更新\
✅ **避免**：如果发生了文档记录顺序混乱，应该提供完整内容重写整个文档

❌ **陷阱**：所有任务执行完毕后直接结束，没有向用户确认是否完成\
✅ **避免**：任务执行完毕后，必须主动向用户发起提问，确认任务是否全部完成

❌ **陷阱**：用户确认完成后，忘记请用户更新 tasks.md 第一行的进度标记\
✅ **避免**：用户确认完成后，必须请用户更新 tasks.md 第一行为 "本任务进度: 已完成"

❌ **陷阱**：生成临时文件后忘记更新 actions.md 的过程文件列表\
✅ **避免**：每次新生成临时文件后，立即更新过程文件列表章节

## 10. 提示词参考库

### 10.1 Spec Mode 提示词

```
你现在处于 Spec Mode。

请按照以下流程操作：
1. 立即进入 Start Stage：
   - 研究当前代码库状态，理解用户需求
   - 检索是否已存在相关 PRD 文档（请用户检查 tasks.md 第一行是否为"已完成"或不存在该行）
   - 请用户创建 PRD 目录
   - 开始记录 actions.md
2. 进入 Planning Stage：
   - 在 origin.md 开头添加 harness 文件版本和作者信息
   - 在 origin.md 中使用 `# Dialogue [序号]` 记录多轮对话
   - 一次性记录 origin.md、spec.md、tasks.md、checklist.md 的生成操作
   - 连续提供这些规划文档内容（tasks.md 第一行必须添加"本任务进度: 未完成"）
   - 在 actions.md 中使用 `### USER：Dialogue [序号]` 记录用户输入
   - 在 actions.md 中添加 "Generated Procedure Files List  过程文件列表" 章节
   - 持续更新 actions.md（使用追加方式）
3. 请用户审查规划文档

请使用中文编写所有规划文档。

重要提示：
- 对 spec.md、tasks.md、checklist.md 文档，优先提供完整内容，不要逐行修改
- 对 origin.md、actions.md 文档，使用追加方式在文件末尾添加新内容，且以"spec mode logging"作为文本末尾标记
- 每次操作前先更新 actions.md（更新 actions.md 本身除外）
- Planning Stage 可以一次性记录 origin.md、spec.md、tasks.md、checklist.md 的生成操作
- 用户追加需求需要同时记录在 origin.md（`# Dialogue [序号]`）和 actions.md（`### USER：Dialogue [序号]`）
- 生成临时文件时，按 temp_[标题].md 格式存储在 PRD 目录下，并记录到 actions.md 的过程文件列表中
```

### 10.2 Agent Mode 提示词

```
你现在处于 Agent Mode。

请按照以下流程操作：
1. 从 tasks.md 选择优先级最高的待处理任务
2. 告知用户正在处理该任务
3. 如需复杂任务，建议分段对话
4. 执行任务并进行验证
5. 告知用户任务完成
6. 更新 actions.md（记录 todo 操作和通知用户操作）
7. 重复直到所有任务完成
8. 所有任务完成后，先记录确认操作，再向用户确认任务是否全部完成
9. 用户确认完成后，请用户更新 tasks.md 第一行为"本任务进度: 已完成"

请确保一次只执行一个任务，完成后再进入下一个。

重要提示：
- 对 spec.md、tasks.md、checklist.md 文档，优先提供完整内容，不要逐行修改
- 对 origin.md、actions.md 文档，使用追加方式在文件末尾添加新内容，且以"spec mode logging"作为文本末尾标记
- 每次操作前先更新 actions.md（更新 actions.md 本身除外）
- Action Stage 通常保持分开记录，除非相同目标的操作可以合并
- todo 列表操作和通知用户操作也需要记录到 actions.md
- 用户追加需求需要同时记录在 origin.md（`# Dialogue [序号]`）和 actions.md（`### USER：Dialogue [序号]`）
- 向用户发起提问前，必须先记录到 actions.md
- 生成临时文件时，按 temp_[标题].md 格式存储在 PRD 目录下，并立即更新 actions.md 的过程文件列表
```

## 附录

### A. 术语表

| 术语                  | 说明                                   |
| ------------------- | ------------------------------------ |
| Harness Engineering | 一种使用 AI 进行软件工程的方法论，强调规划、分解、验证      |
| Spec Mode           | 规划模式，用于生成规划文档                        |
| Agent Mode          | 执行模式，用于执行已规划的任务                      |
| PRD                 | Product Requirements Document，产品需求文档 |
| 分段对话             | 由主对话委派任务的独立对话                        |
| Acceptance Criteria | 验收标准，用于验证任务是否完成                      |
| Start Stage         | 启动阶段，用于检索已有 PRD 和创建 PRD 目录           |
| Planning Stage      | 规划阶段，用于生成规划文档                        |
| Action Stage        | 执行阶段，用于执行已规划的任务                      |
| Action Record       | 行动记录，用于记录执行过程的文档（actions.md）         |
| Dialogue            | 对话，用于记录用户的多轮需求输入                     |
| 追加写入                | 在文件末尾添加新内容，而非覆盖整个文件                  |
| 进度标记                | tasks.md 第一行的"本任务进度: \[已完成/未完成]"标记   |
| 覆盖写入                | 提供完整内容完全覆盖文件内容                  |
| 临时文件                | 以 temp\_ 开头，用于存储大规模临时文本的文件           |
| 过程文件列表              | actions.md 中记录临时文件名称的章节              |

### B. 参考资源

- 本文档本身
- YTLA 项目现有文档示例
- Vue 3 官方文档（如适用）
- Python Flask 官方文档（如适用）

***

**文档版本**: 1.7-direct\
**最后更新**: 2026-04-09\
**维护者**: Official
