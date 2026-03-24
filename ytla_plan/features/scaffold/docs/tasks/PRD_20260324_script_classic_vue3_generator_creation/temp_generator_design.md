# Classic Vue3 生成器设计文档

## 1. 分析结果

### 1.1 参考样本分析

#### sidecard 样本（sample 目录）
- **路径**: `d:\YTLA\ytla_plan_vue\src\features\sample`
- **结构**:
  - `cards/_type/`: 通用类型目录
    - `components/`: 通用组件（如 SampleCardSelector.vue）
    - `definitions/`: 类型定义
    - `flows/`: 流程管理器
    - `locales/`: 国际化配置
    - `registries/`: 注册表
  - `cards/sample1/`, `sample2/`, `sample3/`: 子类型目录
    - 每个子类型有相同的子目录结构
- **组件示例**: SampleCardSelector.vue（简单组件）、Sample1Card.vue（完整卡片组件）

#### module 样本（basic/definition 目录）
- **路径**: `d:\YTLA\ytla_plan_vue\src\features\basic\modules\definition`
- **结构**:
  - `components/`: 组件文件（Main、Sub、Step 组件）
  - `flows/`: 流程管理器（definitionFlowManager.ts）
  - `locales/`: 国际化配置
  - `registries/`: 模块配置（definitionModuleConfig.ts）
  - `avatar/`: 头像组件
- **文件示例**: DefinitionMain.vue（简单入口）、definitionFlowManager.ts（流程管理）、definitionModuleConfig.ts（模块配置）

### 1.2 早期脚本分析（moduleGenerator.py）

- **功能**: 生成 Vue 模块化开发所需的完整目录结构和基础代码文件
- **参数**: `module_type`（模组大类）、`module_sub_type`（模块子类型）
- **生成内容**:
  1. 标准化的目录结构（components、composables、flows、layouts、locales、registries、services、stores、styles、types、utils）
  2. 基础组件模板文件（Main/Sub 组件对模式）
  3. 模块流程管理器（Flow Manager）
  4. 模块注册表（Module Config）
- **输出**: 生成文件到前端项目目录，并提供需要在 main.ts 和 locale 中添加的代码提示

### 1.3 frontend_vue3 生成器类型

基于 `constGenerators.generators`，支持15种生成器：
1. `processGenerateAvatar` - 头像相关
2. `processGenerateComponents` - 组件目录
3. `processGenerateComposables` - 组合式函数
4. `processGenerateDefinitions` - 类型定义
5. `processGenerateFactories` - 工厂模式
6. `processGenerateLayouts` - 布局文件
7. `processGenerateLocales` - 国际化配置
8. `processGenerateServices` - 服务定义
9. `processGenerateStores` - 状态存储
10. `processGenerateStyles` - 样式文件
11. `processGenerateUi` - UI组件
12. `processGenerateDocuments` - 文档文件
13. `processGenerateRegistries` - 注册表
14. `processGenerateFlows` - 流程管理器
15. `processGenerateUtils` - 工具函数

## 2. 生成器设计

### 2.1 生成器类型

根据需求，创建两种类型的生成器：
1. **sidecard_generator**: 针对 cards 结构的生成器
2. **modules_generator**: 针对 modules 结构的生成器

### 2.2 文件名规范

- `script_classic_vue3_sidecard_[前端组件名]_generator.py`
- `script_classic_vue3_modules_[前端组件名]_generator.py`

其中 `[前端组件名]` 为小写，如：components、composables、stores 等。

### 2.3 生成器参数设计

**基础参数**:
- `module_type`: 模组大类（如 'sample', 'basic'）
- `module_sub_type`: 模块子类型（如 'sample1', 'definition'）
- `is_core`: 是否核心模块（True/False，默认 False）
- `structure_type`: 结构类型（'cards' 或 'modules'，由生成器类型隐含）

**组件相关参数**:
- `component_type`: 组件类型（如 'components', 'composables', 'stores' 等）
- `component_name`: 组件名称（可选，如 'SampleCard', 'DefinitionMain'）

### 2.4 生成器功能设计

#### sidecard_generator（cards 结构）
- **目标路径**: `{frontend_project}/{prefix}/{module_type}/cards/{module_sub_type}/{component_type}/`
- **生成内容**:
  - 创建目录结构
  - 生成基础 Vue 组件文件（根据组件类型不同）
  - 对于 components 类型：生成类似 SampleCardSelector.vue 或 Sample1Card.vue 的组件
  - 对于其他组件类型：生成相应的基础文件

#### modules_generator（modules 结构）
- **目标路径**: `{frontend_project}/{prefix}/{module_type}/modules/{module_sub_type}/{component_type}/`
- **生成内容**:
  - 创建目录结构
  - 生成基础 Vue 组件文件（根据组件类型不同）
  - 对于 components 类型：生成类似 DefinitionMain.vue 的组件
  - 对于 flows 类型：生成类似 definitionFlowManager.ts 的流程管理器
  - 对于 registries 类型：生成类似 definitionModuleConfig.ts 的模块配置

### 2.5 组件类型生成逻辑差异

1. **components**:
   - 生成 `.vue` 单文件组件
   - 模板结构根据 structure_type 不同而变化（cards 或 modules）

2. **composables**:
   - 生成 `.ts` 组合式函数文件
   - 包含基本的 TypeScript 类型定义

3. **stores**:
   - 生成 `.ts` 存储文件
   - 使用 Pinia 或类似的存储模式

4. **flows**:
   - 仅适用于 modules 结构
   - 生成 `.ts` 流程管理器文件

5. **registries**:
   - 仅适用于 modules 结构
   - 生成 `.ts` 模块配置文件

### 2.6 与现有架构集成

- **路径生成**: 使用 `config.FRONTEND_FOLDER` 获取前端项目路径
- **前缀确定**: 根据 `is_core` 参数决定 'core' 或 'features'
- **结构类型**: sidecard → 'cards'，modules → 'modules'

## 3. 实现计划

### 3.1 选择的前端组件类型

基于 `constGenerators.generators` 和用户要求，选择以下组件类型作为示例：
1. **components** - 组件目录（最常用）
2. **composables** - 组合式函数（现代 Vue 3 特性）
3. **stores** - 状态存储（状态管理）

### 3.2 需要创建的生成器脚本

需要创建6个生成器脚本：

**sidecard_generator**:
1. `script_classic_vue3_sidecard_components_generator.py`
2. `script_classic_vue3_sidecard_composables_generator.py`
3. `script_classic_vue3_sidecard_stores_generator.py`

**modules_generator**:
1. `script_classic_vue3_modules_components_generator.py`
2. `script_classic_vue3_modules_composables_generator.py`
3. `script_classic_vue3_modules_stores_generator.py`

### 3.3 代码结构模板

每个生成器脚本应包含：

1. **导入模块**: 必要的 Python 模块
2. **参数处理**: 命令行参数或函数参数
3. **路径构建**: 基于参数构建目标路径
4. **目录创建**: 创建必要的目录结构
5. **文件生成**: 生成对应组件类型的文件
6. **错误处理**: 适当的异常处理
7. **日志输出**: 生成过程日志

## 4. 开放性问题决策

基于分析，做出以下设计决策：

1. **组件类型选择**: components、composables、stores 作为示例
2. **生成器交互方式**: 独立工作，不直接与现有 frontend_vue3 生成器交互
3. **参数设计**: 采用函数参数方式，便于未来集成
4. **结构差异**: sidecard 生成器专注于 cards 结构，modules 生成器专注于 modules 结构
5. **创建范围**: 先创建6个示例生成器，未来可根据需要扩展

## 5. 下一步行动

1. 基于此设计文档开始实现 Task 2 和 Task 3
2. 首先实现 `script_classic_vue3_sidecard_components_generator.py` 作为原型
3. 验证原型后，批量创建其他生成器
4. 完成所有生成器后执行 Task 4 进行验证

---
*设计时间: 2026-03-24*  
*基于分析结果和用户需求*