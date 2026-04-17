# UI组件AI生成规范文档 - 代码示例 (rule_ui_standards.md)

## 概述

本文档专注于提供 Vue3/TS/SCSS 规范文档的示例，展示怎么具体编写代码。

### UI 组件使用场景

UI 组件存在两种使用场景：

**场景一：UI 作为主组件的子组件**
- UI 作为 component 或 layout 下的子组件存在
- 主组件已有完整的 prop 和 emit 设计
- UI 直接通过 props 接收主组件的数据和方法
- 不需要自己的 composable（除非有纯视图级别的逻辑）
- 示例：sideCard 模块中的 ButtonPin.vue

**场景二：UI 作为独立组件**
- UI 先于主组件设计，需要自己提供定义接口
- 有完整的 props 和 emits 定义
- 使用自己的 composable 处理逻辑
- 可以独立使用和测试
- 示例：sideCardController 模块中的 ButtonAdd.vue

**判断指南**
- 是否专门为某个特定主组件设计？是→场景一，否→场景二
- 主组件是否已有完整的状态管理和逻辑？是→场景一，否→场景二
- 是否需要在多个上下文中独立使用？是→场景二，否→场景一

两种场景都是规范允许的，选择哪种取决于具体的设计需求。

## 代码模板与示例

### .vue组件模板

对于 ui 目录下的组件，有两种不同的 Props 处理模式：

#### 模式一：直接定义 Props 模式

适用于独立的 UI 组件，特点是：

- Props 直接在 defineProps 中定义，不从 definitions 导入
- 通过 Props 接收来自父组件的数据和方法
- 样式导入可以使用相对路径或绝对路径

```vue
<template>
  <!-- 1. 使用语义化HTML标签 -->
  <!-- 2. 使用v-if/v-show控制显示 -->
  <!-- 3. 使用v-bind绑定属性和类 -->
  <!-- 4. 使用@事件监听器 -->
  <!-- 5. 使用ref进行DOM引用 -->
  <!-- 6. 使用插槽slot进行内容分发 -->
</template>

<script setup lang="ts">
// 直接在 defineProps 中定义接口，不从 definitions 导入
defineProps<{
  // 定义 Props 接口
}>()
</script>

<style scoped lang="scss">
// 导入样式文件，使用同级目录的相对路径
@use './styles/component';
</style>
```

#### 模式二：从 definitions 导入类型模式

适用于需要使用 definitions 中类型定义的 UI 组件，特点是：

- Props 和 Emits 从 definitions 目录导入
- 使用 withDefaults 提供默认值
- 导入并使用组合式函数处理逻辑

```vue
<template>
  <!-- 1. 使用语义化HTML标签 -->
  <!-- 2. 使用v-if/v-show控制显示 -->
  <!-- 3. 使用v-bind绑定属性和类 -->
  <!-- 4. 使用@事件监听器 -->
  <!-- 5. 使用ref进行DOM引用 -->
  <!-- 6. 使用插槽slot进行内容分发 -->
</template>

<script setup lang="ts">
// ============================================================================
// 关注点分离说明（非常重要！）
// ============================================================================
//
// 【核心原则】Vue文件仅负责视图，逻辑必须在TS文件中实现
//
// .vue 文件职责（仅包含以下内容）：
//   - 仅包含 HTML 模板（template 部分）
//   - 仅包含导入语句（script 部分）
//   - 仅包含样式导入（style 部分）
//
// 不应该在 .vue 文件中：
//   - 直接编写业务逻辑（必须在 composables 的 .ts 文件中）
//   - 直接编写样式代码（必须在 styles 的 .scss 文件中）
//   - 定义响应式数据（必须在 composables 中）
//   - 定义计算属性（必须在 composables 中）
//   - 定义方法（必须在 composables 中）
//
// 重构目标：让代码的格式与结构完全符合本文档设计的规范
// ============================================================================

// ============================================================================
// 导入规范说明
// ============================================================================
// 1. 第三方库导入（第一组）
//    import { ref, computed } from 'vue'
//    import { useRouter } from 'vue-router'
//
// 2. 相对路径导入 - 类型定义（第二组）
//    import type { ComponentProps, ComponentEmits } from '../definitions/[组件名]Type'
//
// 3. 相对路径导入 - 本模块（第三组）
//    import { useComponentLogic } from '../composables/useComponentLogic'
//
// 组之间空一行，组内按字母顺序排序
// ============================================================================

// 导入 Props 和 Emits 类型（从外部 definitions 文件）
import type { ComponentProps, ComponentEmits } from '../definitions/[组件名]Type'

// 导入组合式函数（从外部 composables 文件）
import { useComponentLogic } from '../composables/useComponentLogic'

// 定义 Props 和 Emits，使用 withDefaults 提供默认值
const props = withDefaults(defineProps<ComponentProps>(), {
  // 提供默认值
})
const emit = defineEmits<ComponentEmits>()

// 使用组合式函数获取所有逻辑
const { /* 解构需要的数据和方法 */ } = useComponentLogic(props, emit)
</script>

<style scoped lang="scss">
// 仅导入样式文件，不编写具体样式代码
@use '../styles/component';
</style>
```

#### 实际示例：ButtonSubmit.vue

```vue
<template>
  <button
    class="action-button"
    @click.stop="handleSubmit"
    :aria-label="isLoading ? '正在提交...' : '提交表单'"
    :title="isLoading ? '正在提交，请稍候' : '点击提交表单'"
    :class="{ '--loading': isLoading, '--disabled': isDisabled }"
    :disabled="isDisabled || isLoading"
  >
    <span class="button-label">{{ label }}</span>
    <span v-if="isLoading" class="loading-spinner"></span>
  </button>
</template>

<script setup lang="ts">
// ============================================================================
// 关注点分离示例
// ============================================================================
// 本文件仅包含：
// 1. 导入语句（类型定义 + 组合式函数）
// 2. defineProps 和 defineEmits 定义
// 3. 从组合式函数解构数据和方法
//
// 所有逻辑都在 useButtonSubmit.ts 中实现
// ============================================================================

// 导入 Props 和 Emits 类型（从外部 definitions 文件）
import type { ButtonSubmitProps, ButtonSubmitEmits } from '../definitions/ButtonSubmitType'

// 导入组合式函数（从外部 composables 文件）
import { useButtonSubmit } from '../composables/useButtonSubmit'

// 定义 Props 和 Emits
const props = defineProps<ButtonSubmitProps>()
const emit = defineEmits<ButtonSubmitEmits>()

// 使用组合式函数获取所有逻辑
const { isLoading, isDisabled, label, handleSubmit } = useButtonSubmit(props, { emit })
</script>

<style scoped lang="scss">
// 仅导入样式文件，具体样式在 styles 目录中
@use '../styles/ui-button';
@use '../styles/button-submit';
</style>
```

#### 配套的 ButtonSubmitType.ts 文件示例

```typescript
// definitions/ButtonSubmitType.ts
export interface ButtonSubmitProps {
  isLoading: boolean
  isDisabled: boolean
  label: string
}

export type ButtonSubmitEmits = {
  submit: []
}
```

#### 配套的 useButtonSubmit.ts 文件示例

```typescript
// composables/useButtonSubmit.ts
import { computed } from 'vue'
import type { ButtonSubmitProps, ButtonSubmitEmits } from '../definitions/ButtonSubmitType'


// ============================================================================
// 逻辑实现说明
// ============================================================================
// 所有业务逻辑都在这里实现：
// - 响应式数据定义
// - 计算属性定义
// - 方法定义
// - 副作用处理
// ============================================================================

export const useButtonSubmit = (props: ButtonSubmitProps, options: UseButtonSubmitOptions) => {
  const { emit } = options

  const handleSubmit = () => {
    if (props.isDisabled || props.isLoading) return
    emit('submit')
  }

  return {
    isLoading: computed(() => props.isLoading),
    isDisabled: computed(() => props.isDisabled),
    label: computed(() => props.label),
    handleSubmit
  }
}
```

### .ts composable模板

#### 模板结构说明

```typescript
// composables/use[ComponentName].ts 模板

// ============================================================================
// 导入规范说明
// ============================================================================
// 1. 第三方库导入（第一组）
//    import { ref, computed } from 'vue'
//
// 2. 相对路径导入 - 本模块（第三组）
//    import type { LocalType } from '../definitions/[组件名]Type'
//
// 组之间空一行，组内按字母顺序排序
// ============================================================================

// ============================================================================
// 职责说明
// ============================================================================
// 本文件负责实现所有业务逻辑：
// 1. 导入类型定义
// 2. 导入工具函数
// 3. 定义composable参数接口
// 4. 定义返回值接口
// 5. 实现主函数逻辑
// 6. 定义内部响应式数据
// 7. 定义计算属性
// 8. 定义操作方法
// 9. 定义副作用监听
// 10. 返回公共接口
// ============================================================================

// 1. 导入类型定义
// 2. 导入工具函数
// 3. 定义composable参数接口
// 4. 定义返回值接口
// 5. 实现主函数逻辑
// 6. 定义内部响应式数据
// 7. 定义计算属性
// 8. 定义操作方法
// 9. 定义副作用监听
// 10. 返回公共接口
```

#### 实际示例：useButtonSubmit.ts

```typescript
// 第三方库导入
import { ref, computed, watch } from 'vue'

// 相对路径导入 - 本模块类型
import type { ButtonSubmitProps } from '../definitions/ButtonSubmitType'

export const useButtonSubmit = (props: ButtonSubmitProps = {}) => {
  const isLoading = ref(props.initialLoading || false)
  const isDisabled = ref(props.initialDisabled || false)

  const handleSubmit = async () => {
    if (isDisabled.value || isLoading.value) return
    
    isLoading.value = true
    try {
      // 执行提交逻辑，例如调用API
      // await submitForm()
    } catch (error) {
      console.error('提交失败:', error)
    } finally {
      isLoading.value = false
    }
  }

  return { 
    isLoading, 
    isDisabled, 
    handleSubmit 
  }
}
```

### .scss样式模板

#### 模板结构说明

```scss
// styles/[component-name].scss 模板

// ============================================================================
// SCSS导入规范说明
// ============================================================================
// 1. 第三方库导入（第一组）
//    @use 'normalize.css';
//
// 2. 绝对路径导入 - 公共样式（第二组）
//    @use '@/styles/variables' as *;
//    @use '@/styles/mixins';
//
// 3. 相对路径导入 - 本模块样式（第三组）
//    @use '../variables';
//    @use '../styles/shared';
//
// 注意：使用 @use 而不是 @import，优先使用别名导入
// ============================================================================

// 1. 定义CSS自定义属性
// 2. 定义基础样式类
// 3. 定义状态修饰类
// 4. 定义动画效果
// 5. 定义响应式设计
// 6. 定义工具类
```

#### 实际示例：button-submit.scss

```scss
.submit-button {
  transition: all 0.3s ease;

  &.--loading {
    opacity: 0.7;
    cursor: wait;
  }

  &.--disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .loading-spinner {
    display: inline-block;
    width: 1rem;
    height: 1rem;
    border: 2px solid #fff;
    border-top-color: transparent;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

#### 实际示例：ui-button.scss（片段）

```scss
.action-button {
  @include button-reset;

  padding: 0.5rem 1rem;
  background: #42b983;
  color: white;
  border-radius: 4px;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid transparent;

  // 激活状态
  &.--active {
    background: #3aa876;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  // 禁用状态
  &.--disabled {
    background: #cccccc;
    color: #888888;
    cursor: not-allowed;
  }
}
```

### 类型导入规范（摘要）

类型导入规范已在前面的代码模板部分详细说明，这里仅提供快速参考：

**核心规则**：

1. **类型优先**：使用 `import type` 导入纯类型
2. **绝对导入**：跨模块使用 `@/` 前缀（`@/definitions/xxx`）
3. **相对导入**：同模块优先使用同级目录 `./` 前缀
4. **路径限制**：相对路径不超过两层，ui目录下组件只能在该组件目录下调用

**路径别名定义（在 tsconfig.json 中）**:

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

## 重构前后对比示例

### 场景：关注点分离重构

**重构前（不推荐）- 逻辑在Vue文件中**：

```vue
<template>
  <button @click="handleClick" :disabled="isDisabled">
    {{ buttonText }}
  </button>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const props = defineProps<{
  label: string
  disabled?: boolean
}>()

const emit = defineEmits<{
  click: []
}>()

// ❌ 不应该在Vue文件中定义响应式数据
const isLoading = ref(false)

// ❌ 不应该在Vue文件中定义计算属性
const buttonText = computed(() => {
  return isLoading.value ? '加载中...' : props.label
})

// ❌ 不应该在Vue文件中定义方法
const isDisabled = computed(() => props.disabled || isLoading.value)

const handleClick = () => {
  if (isDisabled.value) return
  isLoading.value = true
  setTimeout(() => {
    emit('click')
    isLoading.value = false
  }, 1000)
}
</script>

<style scoped>
/* ❌ 不应该在Vue文件中编写样式代码 */
button {
  padding: 8px 16px;
  background: blue;
  color: white;
}
</style>
```

**重构后（推荐）- 逻辑在TS文件中**：

```vue
<template>
  <button @click="handleClick" :disabled="isDisabled">
    {{ buttonText }}
  </button>
</template>

<script setup lang="ts">
// ✅ 仅导入类型
import type { ButtonDemoProps, ButtonDemoEmits } from './definitions/ButtonDemoType'

// ✅ 仅导入组合式函数
import { useButtonDemo } from './composables/useButtonDemo'

// ✅ 仅定义Props和Emits
const props = defineProps<ButtonDemoProps>()
const emit = defineEmits<ButtonDemoEmits>()

// ✅ 从组合式函数获取所有逻辑
const { isDisabled, buttonText, handleClick } = useButtonDemo(props, { emit })
</script>

<style scoped lang="scss">
// ✅ 仅导入样式文件
@use '../styles/button-demo';
</style>
```

**配套的 useButtonDemo.ts**：

```typescript
import { ref, computed } from 'vue'
import type { ButtonDemoProps, ButtonDemoEmits } from './definitions/ButtonDemoType'

interface UseButtonDemoOptions {
  emit: (event: keyof ButtonDemoEmits, ...args: any[]) => void
}

// ✅ 所有逻辑在TS文件中实现
export const useButtonDemo = (props: ButtonDemoProps, options: UseButtonDemoOptions) => {
  const { emit } = options

  const isLoading = ref(false)

  const buttonText = computed(() => {
    return isLoading.value ? '加载中...' : props.label
  })

  const isDisabled = computed(() => props.disabled || isLoading.value)

  const handleClick = () => {
    if (isDisabled.value) return
    isLoading.value = true
    setTimeout(() => {
      emit('click')
      isLoading.value = false
    }, 1000)
  }

  return {
    isDisabled,
    buttonText,
    handleClick
  }
}
```

## 重构场景示例

### 场景1：组件重命名与目录调整

**目标**：将 `SubmitButton` 重命名为 `ButtonSubmit`，并调整目录结构

**执行步骤**：

1. 使用 `git mv` 重命名文件：
   ```bash
   git mv submit-button/ui/SubmitButton.vue button-submit/ui/ButtonSubmit.vue
   git mv submit-button/composables/useSubmitButton.ts button-submit/composables/useButtonSubmit.ts
   git mv submit-button/styles/submit-button.scss button-submit/styles/button-submit.scss
   ```
2. 更新组件内部的所有引用
3. 搜索并更新所有调用方的导入语句
4. 更新相关文档和注释
5. 运行测试确保一切正常

**注意事项**：

- 使用 git mv 保持版本历史
- 逐步更新，每步验证可编译
- 考虑提供短暂的兼容层

### 场景2：组件接口变更（Props/Emits重构）

**目标**：优化 ButtonSubmit 组件的 Props 接口设计

**执行步骤**：

1. 分析现有接口的使用情况
2. 设计新的接口，保持向后兼容
3. 标记旧接口为 deprecated
4. 更新组件实现支持新旧接口
5. 逐步迁移调用方到新接口
6. 移除 deprecated 接口（如需要）

**兼容性策略**：

```typescript
// ✅ 推荐：保持向后兼容
interface ButtonSubmitProps {
  // 旧接口保留，标记为deprecated
  /** @deprecated 使用 loading 代替 */
  isLoading?: boolean
  /** @deprecated 使用 disabled 代替 */
  isDisabled?: boolean
  
  // 新接口
  loading?: boolean
  disabled?: boolean
}

// 在组合式函数中处理兼容逻辑
export const useButtonSubmit = (props: ButtonSubmitProps = {}) => {
  const loading = ref(props.loading ?? props.isLoading ?? false)
  const disabled = ref(props.disabled ?? props.isDisabled ?? false)
  // ...
}
```

## AI提示词模板

### 组件生成提示词模板

```markdown
# 生成 [元件类型][组件名称] UI组件

## 项目上下文
- **项目**：YTLA Vue 3 项目
- **技术栈**：Vue 3 + TypeScript + SCSS + Composition API
- **命名规范**：遵循 `元件类型 + 功能描述` 命名规则
- **文件位置**：`ui/[完整组件名].vue`

## 组件基本信息
- **元件类型**：[Container | Bar | Button | Panel | Layer | Card]
- **组件名称**：[具体名称，如Submit, Title, Close等]
- **完整组件名**：[元件类型][组件名称]，如ButtonSubmit, BarTitle

## 组件功能描述
[详细描述组件的功能、用途和使用场景]

## Props定义要求
提供以下props定义：
1. **控制类Props**：控制组件显示/隐藏、状态等
2. **数据类Props**：传入组件的数据
3. **事件类Props**：处理函数和回调
4. **配置类Props**：样式、尺寸等配置

## Emits定义要求
定义组件发出的事件，每个事件应包含：
- 事件名称（使用kebab-case）
- 事件参数类型
- 事件描述

## Slots定义要求
定义组件插槽，每个插槽应包含：
- 插槽名称
- 插槽作用域参数（如有）
- 插槽描述

## 模板结构要求
1. 使用语义化HTML标签
2. 包含必要的aria标签支持无障碍访问
3. 使用v-if/v-show控制显示
4. 使用事件修饰符（如.stop, .prevent）
5. 使用ref进行DOM引用
6. 遵循BEM命名约定

## 脚本部分要求
1. 使用 `<script setup lang="ts">` 语法
2. 导入必要的类型定义（使用 `import type`）
3. 使用defineProps定义props
4. 使用defineEmits定义事件
5. 使用组合式函数处理逻辑
6. 提供明确的类型注解
7. 遵循导入规范：第三方库 → 绝对路径 → 相对路径
8. **重要**：Vue文件仅负责视图，所有逻辑必须在composables的TS文件中实现

## 样式部分要求
1. 使用 `<style scoped lang="scss">` 语法
2. 导入必要的样式文件
3. 使用CSS自定义属性
4. 包含响应式设计
5. 提供状态样式（active, disabled, hover等）

## 输出格式
生成完整的`.vue`文件，包含：
1. 模板部分（template）
2. 脚本部分（script setup）
3. 样式部分（style scoped）
```

### Composables生成提示词模板

```markdown
# 生成 use[完整组件名] 组合式函数

## 项目上下文
- **对应组件**: [完整组件名].vue
- **文件位置**: `composables/use[完整组件名].ts`
- **命名规范**: `use` + PascalCase组件名

## 功能描述
[描述组合式函数的核心功能，如状态管理、事件处理、副作用等]

## 输入参数
定义函数的输入参数接口

## 返回值要求
返回包含以下内容的响应式接口：
1. **状态变量**：ref或reactive定义的状态
2. **计算属性**：基于状态的派生值
3. **操作方法**：处理用户交互的函数
4. **生命周期方法**：清理或初始化函数

## 内部逻辑要求
1. 使用ref/reactive定义响应式状态
2. 使用computed定义计算属性
3. 使用watch/watchEffect处理副作用
4. 使用onMounted/onBeforeUnmount处理生命周期
5. 使用项目现有的工具函数（如usePersistence）
6. 遵循导入规范：第三方库 → 绝对路径 → 相对路径
7. **重要**：所有业务逻辑都在这里实现，Vue文件仅负责视图

## 错误处理
1. 包含错误状态管理
2. 提供错误处理机制
3. 添加必要的日志记录

## 输出格式
生成完整的`.ts`文件，包含：
1. 导入语句
2. 类型定义
3. 主函数实现
4. 导出语句
```

### 样式生成提示词模板

```markdown
# 生成 [完整组件名] 样式文件

## 项目上下文
- **对应组件**: [完整组件名].vue
- **文件位置**: `styles/[组件名-kebab-case].scss`
- **命名规范**: kebab-case

## 样式结构要求
1. **CSS自定义属性**：定义颜色、间距、圆角等变量
2. **基础样式类**：主组件样式，使用BEM命名
3. **修饰符样式**：状态类（--active, --disabled, --hover等）
4. **子元素样式**：组件内部元素的样式
5. **动画效果**：过渡和动画定义
6. **响应式设计**：移动端和桌面端适配
7. **深色模式**：prefers-color-scheme适配

## BEM命名约定
- 块（Block）：`.component`
- 元素（Element）：`.component__element`
- 修饰符（Modifier）：`.component--modifier`

## 状态样式要求
为以下状态提供样式：
1. 默认状态
2. 悬停状态（:hover）
3. 激活状态（--active）
4. 禁用状态（--disabled）
5. 焦点状态（:focus-visible）
6. 错误状态（--error）

## 输出格式
生成完整的`.scss`文件，包含：
1. CSS自定义属性定义
2. 基础样式类
3. 状态修饰符
4. 动画效果
5. 响应式设计
```

### 组件重构提示词模板

```markdown
# 重构 [现有组件名] UI组件

## 项目上下文
- **项目**：YTLA Vue 3 项目
- **技术栈**：Vue 3 + TypeScript + SCSS + Composition API
- **重构目标**：让代码的格式与结构符合文档设计的规范，实现关注点分离，Vue文件仅负责视图

## 现有组件信息
- **现有组件名**：[现有组件名，如SubmitButton]
- **现有文件位置**：[现有文件路径]
- **目标组件名**：[目标组件名，如ButtonSubmit]
- **目标文件位置**：[目标文件路径]

## 重构要求
1. **向后兼容性**：[是否需要保持向后兼容]
2. **影响范围**：[已知的影响范围和调用方]
3. **特殊约束**：[任何特殊的重构约束]
4. **核心要求**：
   - Vue文件仅负责视图（HTML模板、导入语句、样式导入）
   - 所有逻辑必须移动到composables的TS文件中
   - 样式代码必须在styles的SCSS文件中

## 重构内容
[详细描述需要重构的具体内容]

## 输出格式
1. 重构步骤说明
2. 新的组件文件
3. 更新建议（针对调用方）
4. 验证清单
```

## 验证清单

### AI 代理验证清单

当您（AI代理）完成UI组件生成或重构后，请使用以下验证清单检查生成的组件是否符合所有规范：

#### 1. 命名验证

1. ✅ **元件命名规范验证**：验证是否符合"元件类型+功能描述"的命名模式
   - **标准**：元件类型（Button/Bar/Container）+ 功能描述（Submit/Title/Icon）
   - **示例**：`ButtonSubmit`（元件类型Button + 功能Submit），`BarTitle`，`ContainerIcon`
   - **验证方法**：检查组件名称是否匹配 `^[A-Z][a-z]+[A-Z][a-z]+$` 模式
2. ✅ **文件命名规范验证**：验证不同文件类型的命名约定
   - **标准**：
     - Vue组件：`PascalCase.vue`（如 `ButtonSubmit.vue`）
     - 组合式函数：`useCamelCase.ts`（如 `useButtonSubmit.ts`）
     - 样式文件：`kebab-case.scss`（如 `button-submit.scss`）
   - **验证方法**：检查文件命名是否符合各自类型的命名规则
3. ✅ **类型导入命名规范验证**：验证导入语句的命名是否符合规范
   - **标准**：
     - 类型导入使用 `import type` 语法
     - 从 `definitions` 导入使用 `@/definitions/*` 绝对路径
     - 相对路径不超过两层（`../..`）
   - **示例**：`import type { ButtonProps } from '@/definitions/ui/components'`
   - **验证方法**：检查所有导入语句是否符合规范

#### 2. 文件结构验证

1. ✅ **目录结构位置验证**：验证文件是否在正确的目录中
   - **标准**：
     - UI组件：`ui/` 目录（如 `ui/ButtonSubmit.vue`）
     - 组合式函数：`composables/` 目录（如 `composables/useButtonSubmit.ts`）
     - 样式文件：`styles/` 目录（如 `styles/button-submit.scss`）
   - **验证方法**：检查文件路径是否匹配预期目录结构
2. ✅ **文件配套完整性验证**：验证每个UI组件是否有完整的配套文件
   - **标准**：每个UI组件应有对应的Vue文件、组合式函数、样式文件
   - **示例**：`ButtonSubmit.vue` → `useButtonSubmit.ts` + `button-submit.scss`
   - **验证方法**：检查相关配套文件是否存在且正确关联
3. ✅ **重构兼容性验证**：验证重构是否保持向后兼容
   - **标准**：重构后：
     - Props/Emits/Slots接口保持兼容（或有明确的迁移路径）
     - 导入路径有过渡期兼容方案
     - 有完整的调用方更新计划
   - **示例**：保留旧接口并标记为 deprecated
   - **验证方法**：对比重构前后的接口定义，检查兼容性处理

#### 3. 代码风格验证

1. ✅ **TypeScript类型安全验证**：验证是否全面使用TypeScript类型定义
   - **标准**：所有Props、Emits、数据接口都有完整的TypeScript类型定义
   - **示例**：组件应定义完整的Props和Emits接口，例如使用`interface`定义Props类型
   - **验证方法**：检查是否使用 `interface` 和 `type` 定义，避免使用 `any` 类型
2. ✅ **组合式API规范验证**：验证是否遵循Vue3组合式API最佳实践
   - **标准**：使用 `<script setup lang="ts">`，逻辑封装在组合式函数中
   - **示例**：组合式函数应封装特定逻辑，例如`useButtonSubmit`封装提交按钮的逻辑
   - **验证方法**：检查是否使用组合式函数，避免在组件中直接编写复杂逻辑
3. ✅ **模块导入导出规范验证**：验证导入导出是否正确
   - **标准**：
     - Vue组件：默认导出
     - 组合式函数：命名导出
   - **示例**：`ButtonSubmit.vue` 默认导出，`useButtonSubmit.ts` 使用 `export const useButtonSubmit`
   - **验证方法**：检查导出方式是否符合约定
4. ✅ **导入语句组织验证**：验证导入语句的分组和排序是否规范
   - **标准**：导入语句按 第三方库 → 绝对路径 → 相对路径 的顺序分组，组间空行，组内按字母顺序
   - **示例**：
     ```typescript
     // 1. 第三方库
     import { ref } from 'vue'
     // 2. 相对路径
     import type { ButtonProps } from '../definitions/uiComponentName'
     // 3. 相对路径
     import { useButtonSubmit } from '../composables/useButtonSubmit'
     ```
   - **验证方法**：检查导入语句的顺序和分组

#### 4. 关注点分离验证（最重要！）

1. ✅ **Vue文件职责验证**：验证Vue文件是否仅负责视图
   - **标准**：Vue文件应仅包含：
     - HTML模板（template部分）
     - 导入语句（script部分）
     - 样式导入（style部分）
   - **验证方法**：检查Vue文件中是否包含业务逻辑、响应式数据定义、计算属性定义、方法定义等
2. ✅ **逻辑实现位置验证**：验证逻辑是否在TS文件中实现
   - **标准**：所有业务逻辑、响应式数据、计算属性、方法都应在composables的TS文件中实现
   - **验证方法**：检查composables文件中是否包含所有逻辑实现
3. ✅ **样式实现位置验证**：验证样式是否在SCSS文件中实现
   - **标准**：所有样式代码都应在styles的SCSS文件中实现，Vue文件仅导入样式文件
   - **验证方法**：检查Vue文件的style部分是否仅包含导入语句

#### 5. 功能验证

1. ✅ **Props接口定义验证**：验证Props是否有完整的TypeScript接口定义
   - **标准**：使用 `interface` 定义Props，提供默认值
   - **示例**：组件应使用`interface`定义Props接口，例如`ButtonSubmitProps`定义提交按钮的属性
   - **验证方法**：检查 `defineProps` 是否有对应的接口类型
2. ✅ **Emits类型定义验证**：验证Emits是否有完整的类型定义
   - **标准**：使用 `type` 定义Emits类型
   - **示例**：组件应使用`type`定义Emits类型，例如`ButtonSubmitEmits`定义提交按钮的事件
   - **验证方法**：检查 `defineEmits` 是否有对应的类型定义
3. ✅ **Slots插槽定义验证**：验证是否提供必要的插槽
   - **标准**：为可定制内容提供具名插槽
   - **示例**：UI组件应提供必要的插槽用于内容定制，如 `#default` 插槽用于默认内容，`#actions` 插槽用于操作按钮等
   - **验证方法**：检查组件是否提供必要的插槽接口
4. ✅ **重构影响范围验证**：验证重构是否只影响预期的组件
   - **标准**：重构：
     - 有明确的影响范围分析
     - 所有调用方都已识别并有更新计划
     - 无意外的副作用
   - **示例**：搜索代码库确认所有引用该组件的文件都已处理
   - **验证方法**：检查重构影响分析文档和调用方更新记录

#### 6. 样式验证

1. ✅ **SCSS样式规范验证**：验证是否使用SCSS并遵循规范
   - **标准**：使用 `<style scoped lang="scss">`，导入相关样式文件
   - **示例**：组件应导入相关样式文件，如`ui-button`和`button-submit`样式
   - **验证方法**：检查样式部分是否使用SCSS语法和正确导入
2. ✅ **BEM命名与响应式设计验证**：验证是否使用BEM命名和响应式设计
   - **标准**：
     - BEM命名：使用 `.block__element--modifier` 模式
     - 响应式设计：使用媒体查询或混合宏
   - **示例**：样式文件应使用BEM命名，如`&.--loading`修饰符表示加载状态
   - **验证方法**：检查样式是否使用BEM命名和响应式技术

#### 7. 重构专项验证

1. ✅ **组件接口兼容性验证**：验证重构后组件的公共接口是否保持向后兼容
   - **标准**：重构后组件的Props、Emits、Slots接口应保持向后兼容，避免破坏性变更
   - **验证方法**：对比重构前后的接口定义，使用 TypeScript 类型检查验证兼容性
2. ✅ **现有调用关系完整性验证**：验证重构后组件是否仍被所有现有调用方正确引用
   - **标准**：确保所有现有调用该组件的文件都能正常工作，包括导入路径、组件名称、Props传递、Emits监听
   - **验证方法**：搜索代码库中所有引用该组件的文件，逐一检查调用关系
3. ✅ **样式类名一致性验证**：验证重构后样式类名是否保持一致
   - **标准**：确保重构后CSS类名遵循BEM规范，不随意更改现有类名，确保父组件的样式选择器仍能正常工作
   - **验证方法**：对比重构前后的样式文件，检查类名变更情况
4. ✅ **组合式函数引用完整性验证**：验证重构后组合式函数的引用是否完整
   - **标准**：确保重构后组合式函数的导出名称保持一致，返回的接口保持兼容，所有使用该组合式函数的组件都能正常导入和使用
   - **验证方法**：搜索代码库中所有引用该组合式函数的文件，检查导入和使用情况
5. ✅ **测试覆盖完整性验证**：验证重构后组件的测试覆盖是否完整
   - **标准**：确保重构后现有的单元测试、集成测试都能通过，新增的功能有对应的测试覆盖
   - **验证方法**：运行项目测试套件，检查重构相关的测试用例通过率

## 附录

### 术语表

| 术语        | 定义                                       |
| --------- | ---------------------------------------- |
| **元件类型**  | UI组件的分类，如Button, Bar, Container等         |
| **组合式函数** | Vue 3的组合式API函数，用于封装可复用逻辑                 |
| **BEM命名** | CSS命名方法论：Block-Element-Modifier          |
| **Props** | 组件接收的属性，用于配置组件行为                         |
| **Emits** | 组件发出的事件，用于向上通信                           |
| **Slots** | 组件的内容插槽，用于内容分发                           |
| **类型导入**  | 使用 `import type` 语法导入纯类型                 |
| **绝对导入**  | 使用路径别名的导入方式                              |
| **相对导入**  | 使用 `./` 或 `../` 的导入方式                    |
| **路径别名**  | `tsconfig.json` 中配置的导入路径简写               |
| **关注点分离** | 视图、逻辑、样式分离明确，Vue文件仅负责视图，逻辑在TS文件中，不处理i18n |

### 外部资源

- [Vue 3官方文档](https://vuejs.org/guide)
- [TypeScript手册](https://www.typescriptlang.org/docs)
- [SCSS文档](https://sass-lang.com/documentation)
- [TypeScript 3.8+ 类型导入语法](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export)

***

**文档信息**

- 生成时间：2026年4月9日
- 基于版本：项目UI组件规范（20260409）
- 适用场景：YTLA项目UI组件AI生成与重构 - 代码示例
- 文件位置：rule\_ui\_standards.md
- 规范范围：Vue3/TS/SCSS代码示例

