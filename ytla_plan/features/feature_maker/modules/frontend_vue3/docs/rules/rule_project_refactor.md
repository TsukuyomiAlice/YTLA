# YTLA - Vue3 项目重构规范

## 1. 概述

### 1.1 目的
本规范确保代码按 [rule_project_definition.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_project_definition.md) 定义的目录结构拆分，形成稳定调用关系。

### 1.2 核心原则
- **单一职责**：每个文件只负责一个功能
- **关注点分离**：类型→`definitions`，API→`services`，状态→`stores`，逻辑→`composables`，UI→`components/layouts/ui`
- **依赖倒置**：高层模块不依赖低层模块，两者依赖抽象
- **禁止循环依赖**：建立明确的调用层次

---

## 2. 调用关系规范

### 2.1 允许的调用关系

| 调用方 | 被调用方 | 说明 |
|-------|---------|------|
| `components` | `composables`、`services`、`definitions` | 组件通过组合式函数获取逻辑 |
| `composables` | `services`、`stores`、`definitions` | 组合式函数可访问服务和状态 |
| `stores` | `services`、`definitions` | stores 调用服务获取数据 |
| `services` | `definitions` | 服务只依赖类型定义 |
| `layouts` | `components`、`composables` | 布局包含组件和逻辑 |
| `ui` | `composables`、`definitions` | UI 元件使用组合式函数 |

### 2.2 禁止的调用关系
- `components` → `stores`（禁止直接访问）
- `services` → `stores`（禁止反向依赖）
- 任何形式的循环依赖

---

## 3. 目录级重构规则

### 3.1 definitions - 类型定义层
- **职责**：定义 TypeScript 类型、接口、数据结构
- **规则**：接口以 `I` 前缀，类型命名 PascalCase，文件 kebab-case
- **示例**：`IUser`, `UserStatus`, `IUserCardProps`, `IUserCardEmits`
- **参考规范**：[rule_definitions_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_definitions_standards.md)

### 3.2 services - 服务层
- **职责**：封装后端 API、统一错误处理、数据转换
- **规则**：文件以 `-service` 后缀，类以 `Service` 后缀，返回 Promise
- **依赖限制**：仅依赖 `definitions`
- **参考规范**：[rule_services_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_services_standards.md)

### 3.3 stores - 状态管理层
- **职责**：管理应用级共享状态
- **规则**：使用 Pinia 的 `defineStore`，包含 state/getters/actions，文件以 `-store` 后缀
- **异步规范**：包含 loading/error/data 三元组
- **参考规范**：[rule_stores_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_stores_standards.md)

### 3.4 composables - 组合式函数层
- **职责**：封装可复用逻辑
- **规则**：文件以 `use-` 前缀，函数以 `use` 前缀，返回响应式对象
- **依赖限制**：可依赖 `definitions`、`services`、`stores`
- **参考规范**：[rule_composables_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_composables_standards.md)

### 3.5 components - 业务组件层
- **职责**：UI 展示和用户交互
- **规则**：Props/Emits 类型必须放在 `definitions`，使用 `<script setup>`，样式用 `<style scoped>`
- **依赖限制**：禁止直接访问 `stores`
- **参考规范**：[rule_components_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_components_standards.md)

### 3.6 layouts - 布局组件层
- **职责**：定义页面布局结构
- **规则**：文件以 `Layout` 后缀，使用 slots 提供内容插入点
- **参考规范**：[rule_layouts_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_layouts_standards.md)

### 3.7 ui - UI 元件层
- **职责**：提供基础 UI 元件
- **规则**：与业务无关，可复用，使用 props 定制外观
- **参考规范**：[rule_ui_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_ui_standards.md)

### 3.8 styles - 样式层
- **职责**：定义组件样式规则、主题变量、混合宏
- **规则**：Vue 文件中不应包含任何样式代码，所有样式必须提取到 `styles` 目录
- **参考规范**：[rule_styles_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_styles_standards.md)

### 3.9 utils - 工具函数层
- **职责**：提供通用工具函数、封装常用算法
- **规则**：无副作用、单一职责、与业务无关
- **参考规范**：[rule_utils_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_utils_standards.md)

### 3.10 registries - 注册机制层
- **职责**：提供模块、组件的注册和加载机制
- **规则**：使用类封装，提供 register/unregister 方法
- **参考规范**：[rule_registries_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_registries_standards.md)

### 3.11 factories - 工厂模式层
- **职责**：实现工厂模式创建对象
- **规则**：文件以 `-factory` 后缀，提供 `create` 方法
- **参考规范**：[rule_factories_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_factories_standards.md)

### 3.12 flows - 流程管理层
- **职责**：管理页面流程和状态转换
- **规则**：文件以 `-flow` 后缀，使用状态机管理
- **参考规范**：[rule_flows_standards.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/rules/rule_flows_standards.md)

---

## 4. AI 执行流程指引

### 4.1 状态机
```json
{
  "states": {
    "INIT": "检查环境和工具依赖",
    "ANALYZE": "扫描代码和依赖分析",
    "SPLIT": "按优先级提取代码",
    "VERIFY": "验证重构质量",
    "DONE": "生成报告完成"
  },
  "transitions": {
    "INIT→ANALYZE": "环境就绪",
    "ANALYZE→SPLIT": "分析完成",
    "SPLIT→VERIFY": "拆分完成",
    "VERIFY→DONE": "检查通过"
  }
}
```

### 4.2 执行步骤

**步骤 4.2.1: 初始化**
```json
{
  "action": "检查项目结构",
  "target": ["src/core", "src/features"],
  "expected": ["definitions", "services", "stores", "composables", "components", "layouts", "ui"],
  "onFail": "创建缺失目录"
}
```

**步骤 4.2.2: 分析**
```json
{
  "action": "扫描代码",
  "patterns": ["src/**/*.vue", "src/**/*.ts"],
  "rules": [
    {"name": "内联类型", "pattern": "interface\\s+\\w+\\s*\\{", "location": "*.vue"},
    {"name": "API调用", "pattern": "fetch\\(|axios\\.", "location": "*.vue"},
    {"name": "状态访问", "pattern": "useStore\\(|store\\.", "location": "*.vue"}
  ]
}
```

**步骤 4.2.3: 生成依赖图**
```json
{
  "action": "检测循环依赖",
  "command": "npx madge --circular src/",
  "onWarning": "记录并继续"
}
```

**步骤 4.2.4: 拆分 - 优先级高**
```json
{
  "action": "提取类型定义",
  "source": ["*.vue", "*.ts"],
  "target": "src/**/definitions/",
  "rules": [
    {"pattern": "interface\\s+(\\w+)", "rename": "I$1"},
    {"pattern": "defineProps<(\\{[^}]+\\})>", "extract": true}
  ],
  "fileNaming": "{componentName}-props.ts"
}
```

```json
{
  "action": "提取服务层",
  "source": ["*.vue", "*.ts"],
  "target": "src/**/services/",
  "fileNaming": "{resource}-service.ts",
  "classNaming": "{Resource}Service"
}
```

**步骤 4.2.5: 拆分 - 优先级中**
```json
{
  "action": "提取状态管理",
  "source": ["*.vue", "*.ts"],
  "target": "src/**/stores/",
  "fileNaming": "{feature}-store.ts",
  "storeNaming": "use{Feature}Store"
}
```

**步骤 4.2.6: 拆分 - 优先级低**
```json
{
  "action": "提取组合式函数",
  "source": ["*.vue", "*.ts"],
  "target": "src/**/composables/",
  "fileNaming": "use-{feature}.ts",
  "functionNaming": "use{Feature}"
}
```

**步骤 4.2.7: 更新组件引用**
```json
{
  "action": "更新导入路径",
  "rules": [
    {"old": "defineProps<\\{[^}]+\\}>", "new": "defineProps<I{Component}Props>"},
    {"old": "useStore\\(", "replaceWith": "use{Feature}() via composable"}
  ]
}
```

**步骤 4.2.8: 验证**
```json
{
  "action": "TypeScript 检查",
  "command": "npx tsc --noEmit",
  "onFail": {"action": "修复类型错误", "retry": 3}
}
```

```json
{
  "action": "ESLint 检查",
  "command": "npx eslint src/",
  "onFail": {"command": "npx eslint src/ --fix", "retry": 1}
}
```

```json
{
  "action": "单元测试",
  "command": "npm run test",
  "threshold": {"coverage": 80, "passRate": 100}
}
```

**步骤 4.2.9: 生成报告**
```json
{
  "action": "生成重构报告",
  "output": "refactor_report.md",
  "content": {
    "summary": {"filesProcessed": 0, "typesExtracted": 0, "servicesExtracted": 0, "storesExtracted": 0, "composablesExtracted": 0},
    "changes": [], "issues": [], "suggestions": []
  }
}
```

---

## 5. 代码质量标准

### 5.1 可测试性
- 函数单一职责
- 使用依赖注入
- 避免全局状态

### 5.2 可读性
- 函数 ≤ 50 行
- 文件 ≤ 200 行
- 清晰命名

### 5.3 可维护性
- 遵循 DRY 原则
- 代码风格一致
- 使用 ESLint

---

## 6. 工具支持

### 6.1 ESLint 规则
```json
{
  "rules": {
    "import/order": ["error", {"groups": ["builtin", "external", "internal"]}],
    "import/no-cycle": ["error", {"maxDepth": 10}],
    "vue/no-unused-properties": "error"
  }
}
```

### 6.2 TypeScript 配置
```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "baseUrl": ".",
    "paths": {"@/*": ["src/*"]}
  }
}
```

### 6.3 依赖分析
```bash
npx madge --circular src/
npx madge --image dep-graph.svg src/
```

---

## 7. 常见反模式

### 7.1 组件直接访问 stores
**错误**：`import { useUserStore } from '../stores/user-store'`  
**正确**：通过 composables 访问

### 7.2 Props/Emits 内联定义
**错误**：组件内直接定义类型  
**正确**：提取到 `definitions`

### 7.3 服务层访问 stores
**错误**：服务层依赖状态管理  
**正确**：服务只负责数据获取

### 7.4 循环依赖
**错误**：模块相互依赖  
**正确**：重新设计结构或引入中间层

---

## 9. 重构检查清单

### 9.1 分析阶段
- [ ] 识别职责混杂的文件
- [ ] 生成依赖图
- [ ] 识别内联类型定义
- [ ] 识别内联样式代码

### 9.2 拆分阶段
- [ ] 提取类型定义到 `definitions`
- [ ] 提取 API 调用到 `services`
- [ ] 提取状态到 `stores`
- [ ] 提取逻辑到 `composables`
- [ ] 提取 Props/Emits 到 `definitions`
- [ ] 提取样式到 `styles`
- [ ] 提取工具函数到 `utils`

### 9.3 验证阶段
- [ ] TypeScript 类型检查通过
- [ ] 消除循环依赖
- [ ] ESLint 检查通过
- [ ] 单元测试通过
- [ ] 代码覆盖率达标

### 9.4 规范文档引用检查
- [ ] 代码符合 `rule_definitions_standards.md`
- [ ] 代码符合 `rule_services_standards.md`
- [ ] 代码符合 `rule_stores_standards.md`
- [ ] 代码符合 `rule_composables_standards.md`
- [ ] 代码符合 `rule_components_standards.md`
- [ ] 代码符合 `rule_layouts_standards.md`
- [ ] 代码符合 `rule_ui_standards.md`
- [ ] 代码符合 `rule_styles_standards.md`
- [ ] 代码符合 `rule_utils_standards.md`
- [ ] 代码符合 `rule_registries_standards.md`
- [ ] 代码符合 `rule_factories_standards.md`
- [ ] 代码符合 `rule_flows_standards.md`

---

**文档版本**: 1.0  
**最后更新**: 2026-05-18  
**维护者**: Official