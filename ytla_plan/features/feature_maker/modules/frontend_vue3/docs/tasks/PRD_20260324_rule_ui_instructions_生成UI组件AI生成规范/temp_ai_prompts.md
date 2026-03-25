# AI 提示词模板 - UI 组件生成规范

基于 sideCard 组件分析结果和已创建的代码模板，本文档提供完整的 AI 提示词模板，用于生成符合 YTLA 项目规范的 UI 组件。

## 概述

本规范定义了生成 Vue 3 + TypeScript UI 组件的完整 AI 提示词模板体系，包括：
1. **组件生成提示词模板** - 生成 `.vue` 组件文件
2. **配套文件生成提示词模板** - 生成组合式函数、样式、类型定义等配套文件
3. **验证和测试提示词模板** - 确保代码质量和规范符合性
4. **完整提示词示例** - 提供可直接使用的示例

## 1. 组件生成提示词模板

### 模板结构

```markdown
# 生成 [组件类型][组件名称] UI 组件

## 项目上下文
- **项目**：YTLA Vue 3 项目
- **技术栈**：Vue 3 + TypeScript + SCSS + Composition API
- **命名规范**：遵循 `元件类型 + 功能描述` 命名规则
- **文件结构**：遵循标准 UI 组件目录结构

## 组件基本信息
- **组件类型**：[Container | Bar | Button | Panel | Layer | Card]
- **组件名称**：[具体名称，如 Pin, Title, Close 等]
- **完整组件名**：[元件类型][组件名称]，如 ButtonPin, BarTitle
- **文件位置**：`ui/[完整组件名].vue`

## 组件功能描述
[详细描述组件的功能、用途和使用场景]

## Props 定义要求
提供以下 props 定义：
1. **控制类 Props**：控制组件显示/隐藏、状态等
2. **数据类 Props**：传入组件的数据
3. **事件类 Props**：处理函数和回调
4. **配置类 Props**：样式、尺寸等配置

每个 props 应包含：
- 名称（使用 camelCase）
- 类型（TypeScript 类型）
- 默认值（如有）
- 描述（功能说明）

## Emits 定义要求
定义组件发出的事件，每个事件应包含：
- 事件名称（使用 kebab-case）
- 事件参数类型
- 事件描述

## Slots 定义要求
定义组件插槽，每个插槽应包含：
- 插槽名称
- 插槽作用域参数（如有）
- 插槽描述

## 模板结构要求
1. 使用语义化 HTML 标签
2. 包含必要的 aria 标签支持无障碍访问
3. 使用 v-if/v-show 控制显示
4. 使用事件修饰符（如 .stop, .prevent）
5. 使用 ref 进行 DOM 引用
6. 遵循 BEM 命名约定

## 脚本部分要求
1. 使用 `<script setup lang="ts">` 语法
2. 导入必要的类型定义
3. 使用 defineProps 定义 props
4. 使用 defineEmits 定义事件
5. 使用组合式函数处理逻辑
6. 提供明确的类型注解

## 样式部分要求
1. 使用 `<style scoped lang="scss">` 语法
2. 导入必要的样式文件
3. 使用 CSS 自定义属性
4. 包含响应式设计
5. 提供状态样式（active, disabled, hover 等）

## 输出格式
生成完整的 `.vue` 文件，包含：
1. 模板部分（template）
2. 脚本部分（script setup）
3. 样式部分（style scoped）

## 代码规范
1. 使用 TypeScript 严格类型
2. 避免使用 any 类型
3. 使用组合式 API
4. 遵循项目现有的代码风格
5. 添加必要的注释说明复杂逻辑
```

### 模板变量说明
- `[组件类型]`: 从预定义列表选择（Container, Bar, Button, Panel, Layer, Card）
- `[组件名称]`: 描述组件功能的名词或动词
- `[完整组件名]`: 自动组合为 `[组件类型][组件名称]`

## 2. 配套文件生成提示词模板

### 2.1 组合式函数生成模板

```markdown
# 生成 use[完整组件名] 组合式函数

## 项目上下文
- **对应组件**: [完整组件名].vue
- **文件位置**: `composables/use[完整组件名].ts`
- **命名规范**: `use` + PascalCase 组件名

## 功能描述
[描述组合式函数的核心功能，如状态管理、事件处理、副作用等]

## 输入参数
定义函数的输入参数接口：
```typescript
interface Use[完整组件名]Params {
  // props 参数
  prop1?: type1
  prop2?: type2
  
  // 配置参数
  configOption1?: type3
  configOption2?: type4
}
```

## 返回值要求
返回包含以下内容的响应式接口：
1. **状态变量**：ref 或 reactive 定义的状态
2. **计算属性**：基于状态的派生值
3. **操作方法**：处理用户交互的函数
4. **生命周期方法**：清理或初始化函数

## 内部逻辑要求
1. 使用 ref/reactive 定义响应式状态
2. 使用 computed 定义计算属性
3. 使用 watch/watchEffect 处理副作用
4. 使用 onMounted/onBeforeUnmount 处理生命周期
5. 使用项目现有的工具函数（如 usePersistence）

## 错误处理
1. 包含错误状态管理
2. 提供错误处理机制
3. 添加必要的日志记录

## 输出格式
生成完整的 `.ts` 文件，包含：
1. 导入语句
2. 类型定义
3. 主函数实现
4. 导出语句
```

### 2.2 样式文件生成模板

```markdown
# 生成 [完整组件名] 样式文件

## 项目上下文
- **对应组件**: [完整组件名].vue
- **文件位置**: `styles/[组件名-kebab-case].scss`
- **命名规范**: kebab-case

## 样式结构要求
1. **CSS 自定义属性**：定义颜色、间距、圆角等变量
2. **基础样式类**：主组件样式，使用 BEM 命名
3. **修饰符样式**：状态类（--active, --disabled, --hover 等）
4. **子元素样式**：组件内部元素的样式
5. **动画效果**：过渡和动画定义
6. **响应式设计**：移动端和桌面端适配
7. **深色模式**：prefers-color-scheme 适配

## BEM 命名约定
- 块（Block）：`.component`
- 元素（Element）：`.component__element`
- 修饰符（Modifier）：`.component--modifier`

## 样式变量要求
定义以下 CSS 自定义属性：
```scss
:root {
  // 颜色变量
  --component-primary: #42b983;
  --component-secondary: #35495e;
  
  // 间距变量
  --component-spacing-xs: 0.25rem;
  --component-spacing-sm: 0.5rem;
  
  // 其他变量...
}
```

## 状态样式要求
为以下状态提供样式：
1. 默认状态
2. 悬停状态 (:hover)
3. 激活状态 (--active)
4. 禁用状态 (--disabled)
5. 焦点状态 (:focus-visible)
6. 错误状态 (--error)

## 输出格式
生成完整的 `.scss` 文件，包含：
1. CSS 自定义属性定义
2. 基础样式类
3. 状态修饰符
4. 动画效果
5. 响应式设计
```

### 2.3 类型定义生成模板

```markdown
# 生成 [完整组件名] 类型定义

## 项目上下文
- **对应组件**: [完整组件名].vue
- **文件位置**: `definitions/[组件名-camelCase]Type.ts`
- **命名规范**: camelCase + Type 后缀

## 类型定义要求
定义以下类型：

### 1. Props 接口
```typescript
export interface [完整组件名]Props {
  // 基础 props
  id?: string
  class?: string
  style?: Record<string, string | number>
  
  // 功能相关 props
  [prop1]?: type1
  [prop2]?: type2
  
  // 配置相关 props
  [config1]?: type3
  [config2]?: type4
  
  // 事件处理 props
  onEvent1?: (payload: EventPayload) => void
  onEvent2?: () => void
}
```

### 2. Emits 类型
```typescript
export type [完整组件名]Emits = {
  (e: '[event-name-1]', payload: EventPayload1): void
  (e: '[event-name-2]'): void
  // 更多事件...
}
```

### 3. 数据类型
```typescript
export interface [完整组件名]Data {
  id: number | string
  // 其他数据字段...
}

export type [完整组件名]State = 'default' | 'loading' | 'error' | 'success'
```

### 4. 配置类型
```typescript
export interface [完整组件名]Config {
  // 配置选项...
}
```

## 类型复用要求
1. 尽可能复用现有类型
2. 使用联合类型和交叉类型
3. 为复杂类型提供详细的注释
4. 导出所有必要的类型

## 输出格式
生成完整的 `.ts` 文件，包含：
1. 导入语句（如有）
2. 所有类型定义
3. 导出语句
```

## 3. 验证和测试提示词模板

### 3.1 代码验证提示词

```markdown
# 验证 [完整组件名] 组件代码质量

## 验证标准
基于以下标准验证生成的代码：

### 1. 命名规范验证
- [ ] 组件文件名使用 PascalCase：[完整组件名].vue
- [ ] 组合式函数使用 use 前缀：use[完整组件名].ts
- [ ] 样式文件使用 kebab-case：[组件名-kebab-case].scss
- [ ] 类型定义文件使用 Type 后缀：[组件名-camelCase]Type.ts
- [ ] 组件内类名使用 BEM 约定

### 2. 类型安全验证
- [ ] 所有 props 有明确的 TypeScript 类型
- [ ] 避免使用 any 类型
- [ ] 事件参数有正确的类型定义
- [ ] 函数返回值有类型注解

### 3. Vue 3 最佳实践验证
- [ ] 使用 `<script setup>` 语法
- [ ] 使用组合式 API
- [ ] 正确使用 ref 和 reactive
- [ ] 使用 computed 和 watch
- [ ] 样式使用 scoped 属性

### 4. 可访问性验证
- [ ] 包含必要的 aria 标签
- [ ] 支持键盘导航
- [ ] 有足够的颜色对比度
- [ ] 提供有意义的 alt 文本

### 5. 性能验证
- [ ] 避免不必要的重新渲染
- [ ] 使用适当的生命周期钩子
- [ ] 合理使用计算属性和侦听器
- [ ] 样式使用 CSS 自定义属性

## 验证步骤
1. 检查命名规范符合性
2. 验证类型安全
3. 检查 Vue 3 最佳实践
4. 评估可访问性
5. 分析性能影响
6. 生成验证报告

## 输出格式
提供详细的验证报告，包含：
1. 通过的项目
2. 未通过的项目及原因
3. 改进建议
4. 整体质量评分
```

### 3.2 测试生成提示词

```markdown
# 为 [完整组件名] 组件生成测试

## 测试范围
为以下内容生成测试：

### 1. 组件渲染测试
- 组件正确渲染
- props 正确传递
- 插槽正确显示

### 2. 用户交互测试
- 点击事件触发
- 表单输入处理
- 状态变化响应

### 3. 状态管理测试
- 响应式状态更新
- 计算属性正确性
- 副作用处理

### 4. 边界条件测试
- 空状态处理
- 错误状态处理
- 极端值处理

## 测试工具要求
- 使用 Vitest 或 Jest
- 使用 Vue Test Utils
- 使用 Testing Library（可选）

## 测试结构
```typescript
describe('[完整组件名]', () => {
  // 渲染测试
  describe('渲染', () => {
    it('应该正确渲染', () => {})
    it('应该根据 props 显示不同内容', () => {})
  })
  
  // 交互测试
  describe('交互', () => {
    it('应该处理点击事件', () => {})
    it('应该触发 emits', () => {})
  })
  
  // 状态测试
  describe('状态', () => {
    it('应该正确更新响应式状态', () => {})
    it('应该计算属性返回正确值', () => {})
  })
})
```

## 输出格式
生成完整的测试文件，包含：
1. 导入语句
2. 测试套件描述
3. 测试用例
4. 断言语句
5. 清理代码
```

## 4. 完整提示词示例

### 示例 1: Button 类型组件 - ButtonSave

```markdown
# 生成 ButtonSave UI 组件

## 项目上下文
- **项目**：YTLA Vue 3 项目
- **技术栈**：Vue 3 + TypeScript + SCSS + Composition API
- **命名规范**：遵循 `元件类型 + 功能描述` 命名规则
- **文件位置**：`ui/ButtonSave.vue`

## 组件基本信息
- **组件类型**：Button
- **组件名称**：Save
- **完整组件名**：ButtonSave

## 组件功能描述
保存按钮组件，用于提交表单或保存数据。具有以下特性：
1. 显示"保存"文本或自定义文本
2. 支持加载状态显示
3. 支持成功/失败状态反馈
4. 支持禁用状态
5. 支持不同尺寸变体

## Props 定义要求
提供以下 props 定义：

1. **控制类 Props**：
   - `loading`?: boolean - 是否处于加载状态，默认 false
   - `disabled`?: boolean - 是否禁用按钮，默认 false
   - `success`?: boolean - 是否显示成功状态，默认 false
   - `error`?: boolean - 是否显示错误状态，默认 false

2. **配置类 Props**：
   - `size`?: 'small' | 'medium' | 'large' - 按钮尺寸，默认 'medium'
   - `variant`?: 'primary' | 'secondary' | 'outline' - 按钮变体，默认 'primary'
   - `text`?: string - 按钮文本，默认 '保存'
   - `icon`?: string - 图标名称（可选）

3. **事件类 Props**：
   - `onClick`?: (event: MouseEvent) => void - 点击事件处理函数

## Emits 定义要求
定义以下事件：
- `click`: (event: MouseEvent) => void - 点击按钮时触发
- `save-success`: () => void - 保存成功时触发（如果内部处理保存逻辑）

## Slots 定义要求
定义以下插槽：
- `default`: 按钮内容插槽，默认显示 props.text
- `loading`: 加载状态内容，默认显示加载图标
- `icon`: 图标插槽，用于自定义图标

## 模板结构要求
1. 使用 `<button>` 元素
2. 包含必要的 aria 属性：aria-label, aria-busy (当 loading 时)
3. 根据 loading 状态显示加载指示器
4. 根据 success/error 状态显示相应图标
5. 支持键盘交互（Enter, Space）

## 脚本部分要求
1. 使用 defineProps 定义所有 props
2. 使用 defineEmits 定义事件
3. 导入必要的图标组件
4. 使用组合式函数处理点击逻辑

## 样式部分要求
1. 导入 `ui-button.scss` 基础样式
2. 创建 `button-save.scss` 特定样式
3. 为不同状态提供样式：loading, success, error, disabled
4. 包含过渡动画效果

## 输出格式
生成完整的 `ButtonSave.vue` 文件，包含 template, script setup, style scoped 三部分。
```

### 示例 2: Bar 类型组件 - BarStatus

```markdown
# 生成 BarStatus UI 组件

## 项目上下文
- **项目**：YTLA Vue 3 项目
- **技术栈**：Vue 3 + TypeScript + SCSS + Composition API
- **命名规范**：遵循 `元件类型 + 功能描述` 命名规则
- **文件位置**：`ui/BarStatus.vue`

## 组件基本信息
- **组件类型**：Bar
- **组件名称**：Status
- **完整组件名**：BarStatus

## 组件功能描述
状态栏组件，用于显示系统或项目的状态信息。具有以下特性：
1. 显示状态文本和图标
2. 支持多种状态类型：info, success, warning, error
3. 支持进度显示
4. 支持关闭操作
5. 支持自动消失（toast 风格）

## Props 定义要求
提供以下 props 定义：

1. **控制类 Props**：
   - `visible`?: boolean - 是否显示状态栏，默认 true
   - `closable`?: boolean - 是否显示关闭按钮，默认 true
   - `autoClose`?: boolean - 是否自动关闭，默认 false
   - `autoCloseDelay`?: number - 自动关闭延迟（毫秒），默认 3000

2. **数据类 Props**：
   - `type`?: 'info' | 'success' | 'warning' | 'error' - 状态类型，默认 'info'
   - `message`?: string - 状态消息文本
   - `description`?: string - 详细描述（可选）
   - `progress`?: number - 进度值（0-100，可选）
   - `icon`?: string - 自定义图标名称（可选）

3. **事件类 Props**：
   - `onClose`?: () => void - 关闭事件处理函数

## Emits 定义要求
定义以下事件：
- `close`: () => void - 关闭状态栏时触发
- `click`: (event: MouseEvent) => void - 点击状态栏时触发
- `progress-complete`: () => void - 进度完成时触发（当 progress=100）

## Slots 定义要求
定义以下插槽：
- `default`: 主内容插槽，默认显示 props.message
- `icon`: 图标插槽，用于自定义图标
- `action`: 操作区域插槽，用于添加额外操作按钮
- `description`: 描述内容插槽，默认显示 props.description

## 模板结构要求
1. 使用 `<div>` 元素作为容器
2. 包含状态图标区域
3. 包含消息文本区域
4. 包含进度条区域（当有 progress 时）
5. 包含关闭按钮区域（当 closable 时）
6. 根据 type 应用不同的 CSS 类

## 脚本部分要求
1. 使用 defineProps 定义所有 props
2. 使用 defineEmits 定义事件
3. 使用 watch 监听 autoClose 和 progress 变化
4. 实现自动关闭逻辑
5. 使用 computed 根据 type 计算图标和颜色

## 样式部分要求
1. 导入 `ui-text.scss` 基础样式
2. 创建 `bar-status.scss` 特定样式
3. 为不同类型提供颜色方案：info, success, warning, error
4. 包含进入和退出动画
5. 支持响应式设计

## 输出格式
生成完整的 `BarStatus.vue` 文件，包含 template, script setup, style scoped 三部分。
```

## 5. 使用指南

### 5.1 如何选择元件类型

| 元件类型 | 适用场景 | 示例 |
|---------|---------|------|
| **Button** | 用户交互操作，点击触发动作 | ButtonSave, ButtonClose, ButtonEdit |
| **Bar** | 显示单行文本内容或状态信息 | BarTitle, BarStatus, BarProgress |
| **Container** | 包裹和组织其他 UI 元素 | ContainerIcon, ContainerTags, ContainerForm |
| **Panel** | 承载多个相关组件的区域 | PanelSettings, PanelSidebar, PanelDashboard |
| **Layer** | 整体页面布局容器 | LayerMain, LayerOverlay, LayerModal |
| **Card** | 展示独立信息单元 | CardProduct, CardUser, CardNotification |

### 5.2 命名决策流程

1. **确定组件功能**：明确组件的主要用途
2. **选择元件类型**：根据上表选择合适的类型
3. **定义功能名称**：使用动词或名词描述具体功能
4. **组合完整名称**：按照 `元件类型 + 功能名称` 格式组合
5. **验证命名**：确保名称清晰、无歧义、符合惯例

### 5.3 文件生成顺序建议

1. **首先生成类型定义**：`definitions/[组件名]Type.ts`
2. **然后生成组合式函数**：`composables/use[组件名].ts`
3. **接着生成样式文件**：`styles/[组件名-kebab-case].scss`
4. **最后生成组件文件**：`ui/[组件名].vue`
5. **可选生成测试文件**：`__tests__/[组件名].spec.ts`

## 6. 最佳实践建议

### 6.1 组件设计原则

1. **单一职责**：每个组件只负责一个明确的功能
2. **可组合性**：组件可以相互组合形成更复杂的界面
3. **可复用性**：组件设计应考虑在不同场景下的复用
4. **可维护性**：代码结构清晰，易于理解和修改
5. **可测试性**：组件逻辑应易于测试

### 6.2 代码质量要求

1. **类型安全**：全面使用 TypeScript 类型
2. **错误处理**：考虑边界情况和错误状态
3. **性能优化**：避免不必要的渲染和计算
4. **可访问性**：支持屏幕阅读器和键盘导航
5. **国际化**：支持多语言文本

### 6.3 与现有代码集成

1. **遵循现有规范**：参考 sideCard 组件的实现方式
2. **复用现有工具**：使用项目已提供的工具函数
3. **保持一致性**：代码风格和模式与现有代码一致
4. **文档完整性**：为生成的组件提供必要的文档

## 7. 附录

### 7.1 术语表

| 术语 | 定义 |
|------|------|
| **元件类型** | UI 组件的分类，如 Button, Bar, Container 等 |
| **组合式函数** | Vue 3 的组合式 API 函数，用于封装可复用逻辑 |
| **BEM 命名** | CSS 命名方法论：Block-Element-Modifier |
| **Props** | 组件接收的属性，用于配置组件行为 |
| **Emits** | 组件发出的事件，用于向上通信 |
| **Slots** | 组件的内容插槽，用于内容分发 |

### 7.2 参考资源

1. **项目规范文档**：
   - [temp_naming_rules.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/tasks/PRD_20260324_rule_ui_instructions_生成UI组件AI生成规范/temp_naming_rules.md)
   - [temp_file_structure.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/tasks/PRD_20260324_rule_ui_instructions_生成UI组件AI生成规范/temp_file_structure.md)
   - [temp_code_templates.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/tasks/PRD_20260324_rule_ui_instructions_生成UI组件AI生成规范/temp_code_templates.md)

2. **实际组件示例**：
   - [ButtonPin.vue](file:///d:/YTLA/ytla_plan_vue/src/core/classic/cards/sideCard/ui/ButtonPin.vue)
   - [BarTitle.vue](file:///d:/YTLA/ytla_plan_vue/src/core/classic/cards/sideCard/ui/BarTitle.vue)
   - [useButtonPin.ts](file:///d:/YTLA/ytla_plan_vue/src/core/classic/cards/sideCard/composables/useButtonPin.ts)

3. **外部资源**：
   - [Vue 3 官方文档](https://vuejs.org/guide)
   - [TypeScript 手册](https://www.typescriptlang.org/docs)
   - [SCSS 文档](https://sass-lang.com/documentation)

---

**文档信息**
- 生成时间：2026年3月24日
- 基于版本：sideCard 组件分析结果（20260324）
- 适用场景：YTLA 项目 UI 组件 AI 生成
- 文件位置：[temp_ai_prompts.md](file:///d:/YTLA/ytla_plan/features/feature_maker/modules/frontend_vue3/docs/tasks/PRD_20260324_rule_ui_instructions_生成UI组件AI生成规范/temp_ai_prompts.md)