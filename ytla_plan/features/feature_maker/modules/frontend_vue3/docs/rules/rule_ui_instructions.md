# UI组件AI生成规范文档 (rule_ui_instructions.md)

## 概述与适用范围

### 文档概述
本文档定义了YTLA项目中UI组件的AI生成规范，基于项目现有架构最佳实践和通用组件设计模式。本规范提供了完整的组件生成流程、代码模板、命名规则和AI提示词模板，旨在确保新生成的UI组件符合项目统一架构和编码规范。

### 规范范围限制
**本规范仅限于以下范围**：

1. **UI组件文件**：`uis`目录下的Vue文件（`.vue`）
2. **组合式函数文件**：与这些UI组件相关的`composables`目录下的文件（`.ts`）
3. **样式文件**：与这些UI组件相关的`styles`目录下的文件（`.scss`）

**明确排除以下内容**：
- 类型定义文件（definitions）
- 布局文件（layouts）
- 服务文件（services）
- 存储文件（stores）
- 工厂文件（factories）
- 流程文件（flows）
- 注册表文件（registries）

### 核心原则
- **一致性**：遵循项目统一的组件设计模式和编码风格
- **可复用性**：组件设计支持跨功能模块复用
- **类型安全**：全面使用TypeScript类型注解
- **关注点分离**：视图、逻辑、样式分离明确
- **可访问性**：支持ARIA标签和键盘导航

## 命名规则

基于项目规范和实践经验，制定以下命名规则：

### 元件类型列表
| 元件类型 | 使用场景 | 示例 |
|---------|---------|-------------|
| **Container**（容器） | 包裹和组织其他UI元素的布局容器 | ContainerLayout、ContainerForm、ContainerList |
| **Bar**（条形/行） | 显示单行文本内容的水平区域 | BarTitle、BarDescription、BarStatus |
| **Button**（按钮） | 用户交互的点击操作元素 | ButtonSubmit、ButtonCancel、ButtonDelete |
| **Panel**（面板） | 承载多个相关组件或功能的区域 | ContentPanel、SidePanel、ModalPanel |
| **Layer**（层/布局） | 整体页面布局容器 | MainLayer、OverlayLayer、BackgroundLayer |
| **Card**（卡片） | 展示独立信息单元的自包含组件 | InfoCard、ProductCard、UserCard |

### 复合组合词命名规则

#### 命名结构
```
元件类型名 + 元件名 + 元件功能名
```

#### 命名规范
1. **各部分首字母大写**（PascalCase）
2. **元件类型名**：从预定义列表中选择（Container、Bar、Button、Panel、Layer、Card）
3. **元件名**：描述组件所属的主要领域或功能模块（如Layout、Form、List）
4. **元件功能名**：描述组件的具体功能（如Pin、Edit、Title、Description）
5. **组合词应使用明确的业务术语**，避免通用名称
6. **确保名称清晰反映组件职责**，避免歧义

#### 命名示例
- **ButtonSubmit** - 提交按钮
- **ContainerLayout** - 布局容器
- **BarTitle** - 标题栏
- **ContentPanel** - 内容面板
- **MainLayer** - 主布局层

#### 错误命名示例
- **SubmitButton** - 类型顺序错误（应为ButtonSubmit）
- **LayoutSubmitButton** - 缺少类型前缀，缺少功能描述
- **GenericButton** - 过于通用，未描述具体功能

### 文件命名约定

#### Vue组件文件
- **命名规则**: PascalCase
- **示例**: 
  - `ButtonSubmit.vue` (UI组件)
  - `BarTitle.vue` (UI组件)
  - `ContainerLayout.vue` (布局组件)

#### TypeScript组合式函数文件
- **命名规则**: camelCase，前缀为 `use`
- **示例**: 
  - `useFormLogic.ts` (表单逻辑组合式函数)
  - `useButtonSubmit.ts` (提交按钮交互逻辑)
  - `useBarTitle.ts` (标题栏逻辑)

#### SCSS样式文件
- **命名规则**: kebab-case
- **示例**: 
  - `component.scss` (主样式)
  - `button-submit.scss` (按钮样式)
  - `container-layout.scss` (容器样式)

## 文件结构与组织

### UI组件标准目录结构

每个UI组件应遵循以下标准目录结构（仅限规范范围）：

```
组件名称/
├── ui/                      # UI组件目录（规范范围）
│   ├── [类型][名称].vue     # UI组件文件（遵循命名规则）
│   └── *.vue                # 其他UI组件
├── composables/             # 组合式函数目录（规范范围）
│   ├── use[组件名称].ts     # 主组合式函数
│   └── use*.ts             # 子功能组合式函数
└── styles/                  # 样式文件目录（规范范围）
    ├── [组件名称].scss      # 主样式文件
    └── *-component.scss     # 组件样式文件
```

### 核心目录说明
| 目录名 | 用途 | 必需性 | 示例 |
|--------|------|--------|-------------|
| ui | UI子组件 | 必需 | ButtonSubmit.vue, BarTitle.vue |
| composables | 组合式函数逻辑 | 必需 | useFormLogic.ts, useButtonSubmit.ts |
| styles | SCSS样式文件 | 必需 | component.scss, button-submit.scss |

### 文件关联示例

#### ButtonSubmit组件配套文件
```
button-submit/
├── ui/
│   └── ButtonSubmit.vue      # UI组件
├── composables/
│   └── useButtonSubmit.ts    # 组合式函数
└── styles/
    ├── ui-button.scss       # 通用按钮样式
    └── button-submit.scss   # 特定按钮样式
```

#### BarTitle组件配套文件
```
bar-title/
├── ui/
│   └── BarTitle.vue         # UI组件
├── composables/
│   └── useBarTitle.ts       # 组合式函数
└── styles/
    ├── ui-text.scss         # 通用文本样式
    └── component.scss       # 主样式文件
```

## 代码模板与示例

### .vue组件模板

#### 模板结构说明
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
// 1. 导入依赖
// 2. 定义组件props接口
// 3. 定义组件emits类型
// 4. 使用defineProps定义props
// 5. 使用defineEmits定义事件
// 6. 使用组合式函数
// 7. 定义响应式数据
// 8. 定义计算属性
// 9. 定义生命周期钩子
</script>

<style scoped lang="scss">
// 1. 使用@use导入样式依赖
// 2. 使用scoped限定样式作用域
// 3. 使用BEM命名约定
// 4. 使用CSS自定义属性
// 5. 使用响应式设计
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
defineProps<{
  isLoading: boolean
  isDisabled: boolean
  label: string
  handleSubmit: () => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/ui-button';
@use '../styles/button-submit';
</style>
```

#### 实际示例：BarTitle.vue
```vue
<template>
  <div
    v-if="showTitle"
    :ref="
      function () {
        return titleRef
      }
    "
    class="editable-title"
    :contenteditable="isTitleEditable"
    @click="startEditTitle"
    @blur="handleTitleBlur"
    @keydown.enter="handleTitleBlur($event)"
    @keydown.esc="cancelEditTitle"
    :data-placeholder="!name ? '...' : ''"
  >
    {{ name }}
  </div>
</template>

<script setup lang="ts">
defineProps<{
  showTitle: boolean
  name: string | undefined
  titleRef: HTMLElement | null
  isTitleEditable: boolean
  startEditTitle: () => void
  handleTitleBlur: (e: Event) => void
  cancelEditTitle: () => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/component';
@use '../styles/ui-text';
</style>
```

### .ts composable模板

#### 模板结构说明
```typescript
// composables/use[ComponentName].ts 模板

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
import { ref } from 'vue'

interface ButtonSubmitProps {
  initialLoading?: boolean
  initialDisabled?: boolean
}

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

// 1. 定义CSS自定义属性
// 2. 定义基础样式类
// 3. 定义状态修饰类
// 4. 定义动画效果
// 5. 定义响应式样式
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

## 生成流程与步骤

### 步骤1：确定组件需求
1. **明确功能**：确定组件的主要用途和功能
2. **识别类型**：根据元件类型列表选择合适的类型
3. **规划交互**：定义用户交互方式和状态变化
4. **评估复杂度**：判断是否需要子组件和组合式函数

### 步骤2：设计组件接口
1. **定义Props**：列出组件接收的所有属性
2. **定义Emits**：定义组件发出的所有事件
3. **定义Slots**：规划组件的内容插槽
4. **类型设计**：为所有接口设计TypeScript类型

### 步骤3：创建文件结构
1. **创建目录**：按照标准目录结构创建文件
2. **命名文件**：遵循命名规则为文件命名
3. **建立关联**：确保组件文件、组合式函数和样式文件正确关联

### 步骤4：实现组件逻辑
1. **编写模板**：实现组件的HTML结构
2. **实现脚本**：使用组合式API实现逻辑
3. **添加样式**：使用SCSS编写组件样式
4. **集成资源**：导入必要的依赖和工具

### 步骤5：验证与测试
1. **规范检查**：验证是否符合所有命名和结构规范
2. **功能测试**：确保组件按预期工作
3. **类型检查**：验证TypeScript类型安全
4. **样式审查**：检查样式的一致性和响应式设计

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
2. 导入必要的类型定义
3. 使用defineProps定义props
4. 使用defineEmits定义事件
5. 使用组合式函数处理逻辑
6. 提供明确的类型注解

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

## 验证清单

### AI 代理验证清单

当您（AI代理）完成UI组件生成后，请使用以下验证清单检查生成的组件是否符合所有规范：

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

#### 2. 文件结构验证
3. ✅ **目录结构位置验证**：验证文件是否在正确的目录中
   - **标准**：
     - UI组件：`ui/` 目录（如 `ui/ButtonSubmit.vue`）
     - 组合式函数：`composables/` 目录（如 `composables/useButtonSubmit.ts`）
     - 样式文件：`styles/` 目录（如 `styles/button-submit.scss`）
   - **验证方法**：检查文件路径是否匹配预期目录结构

4. ✅ **文件配套完整性验证**：验证每个UI组件是否有完整的配套文件
   - **标准**：每个UI组件应有对应的Vue文件、组合式函数、样式文件
   - **示例**：`ButtonSubmit.vue` → `useButtonSubmit.ts` + `button-submit.scss`
   - **验证方法**：检查相关配套文件是否存在且正确关联

#### 3. 代码风格验证
5. ✅ **TypeScript类型安全验证**：验证是否全面使用TypeScript类型定义
   - **标准**：所有Props、Emits、数据接口都有完整的TypeScript类型定义
   - **示例**：组件应定义完整的Props和Emits接口，例如使用`interface`定义Props类型
   - **验证方法**：检查是否使用 `interface` 和 `type` 定义，避免使用 `any` 类型

6. ✅ **组合式API规范验证**：验证是否遵循Vue3组合式API最佳实践
   - **标准**：使用 `<script setup lang="ts">`，逻辑封装在组合式函数中
   - **示例**：组合式函数应封装特定逻辑，例如`useButtonSubmit`封装提交按钮的逻辑
   - **验证方法**：检查是否使用组合式函数，避免在组件中直接编写复杂逻辑

7. ✅ **模块导入导出规范验证**：验证导入导出是否正确
   - **标准**：
     - Vue组件：默认导出
     - 组合式函数：命名导出
   - **示例**：`ButtonSubmit.vue` 默认导出，`useButtonSubmit.ts` 使用 `export const useButtonSubmit`
   - **验证方法**：检查导出方式是否符合约定

#### 4. 功能验证
8. ✅ **Props接口定义验证**：验证Props是否有完整的TypeScript接口定义
   - **标准**：使用 `interface` 定义Props，提供默认值
   - **示例**：组件应使用`interface`定义Props接口，例如`ButtonSubmitProps`定义提交按钮的属性
   - **验证方法**：检查 `defineProps` 是否有对应的接口类型

9. ✅ **Emits类型定义验证**：验证Emits是否有完整的类型定义
   - **标准**：使用 `type` 定义Emits类型
   - **示例**：组件应使用`type`定义Emits类型，例如`ButtonSubmitEmits`定义提交按钮的事件
   - **验证方法**：检查 `defineEmits` 是否有对应的类型定义

10. ✅ **Slots插槽定义验证**：验证是否提供必要的插槽
    - **标准**：为可定制内容提供具名插槽
    - **示例**：UI组件应提供必要的插槽用于内容定制，如 `#default` 插槽用于默认内容，`#actions` 插槽用于操作按钮等
    - **验证方法**：检查组件是否提供必要的插槽接口

#### 5. 样式验证
11. ✅ **SCSS样式规范验证**：验证是否使用SCSS并遵循规范
    - **标准**：使用 `<style scoped lang="scss">`，导入相关样式文件
    - **示例**：组件应导入相关样式文件，如`ui-button`和`button-submit`样式
    - **验证方法**：检查样式部分是否使用SCSS语法和正确导入

12. ✅ **BEM命名与响应式设计验证**：验证是否使用BEM命名和响应式设计
    - **标准**：
      - BEM命名：使用 `.block__element--modifier` 模式
      - 响应式设计：使用媒体查询或混合宏
    - **示例**：样式文件应使用BEM命名，如`&.--loading`修饰符表示加载状态
    - **验证方法**：检查样式是否使用BEM命名和响应式技术

## 附录

### 术语表
| 术语 | 定义 |
|------|------|
| **元件类型** | UI组件的分类，如Button, Bar, Container等 |
| **组合式函数** | Vue 3的组合式API函数，用于封装可复用逻辑 |
| **BEM命名** | CSS命名方法论：Block-Element-Modifier |
| **Props** | 组件接收的属性，用于配置组件行为 |
| **Emits** | 组件发出的事件，用于向上通信 |
| **Slots** | 组件的内容插槽，用于内容分发 |

### 外部资源
- [Vue 3官方文档](https://vuejs.org/guide)
- [TypeScript手册](https://www.typescriptlang.org/docs)
- [SCSS文档](https://sass-lang.com/documentation)

---
**文档信息**
- 生成时间：2026年3月24日
- 基于版本：项目UI组件规范（20260324）
- 适用场景：YTLA项目UI组件AI生成
- 文件位置：rule_ui_instructions.md
- 规范范围：仅限uis目录下的vue文件、相关的composables和styles文件