# 类型定义导入规范

## 概述与适用范围

### 文档概述
本文档定义了YTLA项目中类型定义文件的导入规范，确保类型导入的一致性、可维护性和IDE支持。本规范适用于所有TypeScript文件中的类型导入，包括UI组件、组合式函数、服务、存储等所有模块。

### 规范范围限制
**本规范适用于以下范围**：
1. **类型文件导入**：从 `definitions` 目录导入的类型定义
2. **相对路径导入**：同一模块内的类型导入
3. **绝对路径导入**：跨模块的类型导入
4. **类型与值的混合导入**：同时导入类型和值的场景

**明确排除以下内容**：
- 第三方库类型导入（从 `node_modules` 导入）
- 全局类型声明（在 `*.d.ts` 文件中）
- 运行时值的导入规范（由其他规范覆盖）

### 核心原则
- **一致性**：遵循统一的导入路径格式和风格
- **可读性**：导入路径清晰表达模块关系
- **可维护性**：便于重构和文件移动
- **IDE友好**：确保IDE能够正确解析和跳转
- **性能优化**：避免不必要的类型导入

## 导入路径规范

### 类型定义文件位置约定
项目中的类型定义统一存放在 `definitions` 目录下，结构如下：

```
definitions/
├── core/                    # 核心类型定义
│   ├── base.ts            # 基础类型
│   ├── errors.ts          # 错误类型
│   └── events.ts          # 事件类型
├── ui/                      # UI组件类型
│   ├── components.ts      # 组件Props/Emits类型
│   └── forms.ts           # 表单类型
└── domain/                  # 领域模型类型
    ├── user.ts            # 用户领域类型
    └── plan.ts            # 计划领域类型
```

### 绝对导入路径规范
对于跨模块的类型导入，使用绝对路径（基于项目根目录的别名）。

#### 路径别名定义
项目配置了以下路径别名（在 `tsconfig.json` 中）：
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@definitions/*": ["src/definitions/*"],
      "@ui/*": ["src/ui/*"],
      "@composables/*": ["src/composables/*"],
      "@stores/*": ["src/stores/*"],
      "@services/*": ["src/services/*"]
    }
  }
}
```

#### 绝对导入规则
1. **跨模块导入**：使用 `@definitions/*` 别名导入类型定义
2. **同模块导入**：优先使用相对路径
3. **深度限制**：相对路径超过 `../..` 时改用绝对路径
4. **类型优先**：类型导入使用 `type` 关键字明确标识

#### 绝对导入示例
```typescript
// ✅ 推荐：使用类型导入
import type { User, UserProfile } from '@definitions/domain/user'
import type { ButtonProps, ButtonEmits } from '@definitions/ui/components'

// ✅ 推荐：同时导入类型和值
import { useUserStore } from '@stores/user'
import type { UserState } from '@stores/user'

// ❌ 不推荐：不使用类型关键字
import { User, UserProfile } from '@definitions/domain/user'
```

### 相对导入路径规范
对于同一模块内的类型导入，使用相对路径。

#### 相对导入规则
1. **同级目录**：使用 `./` 前缀
2. **父级目录**：使用 `../` 前缀，最多不超过两层
3. **类型优先**：同样使用 `type` 关键字
4. **文件扩展名**：省略 `.ts`、`.vue` 等扩展名

#### 相对导入示例
```typescript
// ✅ 同级文件导入
import type { LocalConfig } from './config'
import type { FormValidation } from './validation'

// ✅ 父级目录导入（一层）
import type { BaseProps } from '../base'
import type { ComponentState } from '../state'

// ✅ 混合导入（类型和值）
import { validateForm } from './validation'
import type { ValidationResult } from './validation'

// ❌ 不推荐：过深的相对路径（改用绝对路径）
import type { CoreType } from '../../../definitions/core/base'
```

### 导入语句格式规范

#### 导入语句排序
导入语句按以下顺序分组，组之间空一行：
1. 第三方库导入
2. 绝对路径导入（别名）
3. 相对路径导入

每组内部按字母顺序排序。

#### 导入格式示例
```typescript
// 1. 第三方库
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

// 2. 绝对路径导入
import type { User, UserProfile } from '@definitions/domain/user'
import type { ButtonProps } from '@definitions/ui/components'
import { useUserStore } from '@stores/user'

// 3. 相对路径导入
import type { LocalState } from './state'
import { formatDate } from './utils'
```

## 具体导入代码示例

### 示例1：UI组件中的类型导入
**文件位置**：`components/button-submit/ui/ButtonSubmit.vue`

```vue
<script setup lang="ts">
// 第三方库导入
import { computed } from 'vue'

// 绝对路径导入 - 类型定义
import type { ButtonProps, ButtonEmits } from '@definitions/ui/components'
import type { ThemeMode } from '@definitions/core/base'

// 绝对路径导入 - 组合式函数
import { useTheme } from '@composables/useTheme'

// 相对路径导入 - 本模块的组合式函数
import { useButtonSubmit } from '../composables/useButtonSubmit'
import type { ButtonSubmitState } from '../composables/useButtonSubmit'

// Props定义
const props = defineProps<ButtonProps>()

// Emits定义
const emit = defineEmits<ButtonEmits>()

// 业务逻辑
const { isDarkMode } = useTheme()
const { isLoading, isDisabled, handleSubmit } = useButtonSubmit(props)

// 计算属性
const buttonClass = computed(() => ({
  'button-submit': true,
  '--dark': isDarkMode.value,
  '--loading': isLoading.value,
  '--disabled': isDisabled.value
}))
</script>
```

### 示例2：组合式函数中的类型导入
**文件位置**：`components/button-submit/composables/useButtonSubmit.ts`

```typescript
// 第三方库导入
import { ref, computed, watch } from 'vue'

// 绝对路径导入 - 核心类型
import type { AsyncFunction, VoidFunction } from '@definitions/core/base'
import type { ErrorHandler } from '@definitions/core/errors'

// 绝对路径导入 - 服务
import { useNotificationService } from '@services/notification'
import type { NotificationOptions } from '@services/notification'

// 相对路径导入 - 本模块类型
import type { ButtonSubmitProps } from './types'

// 导出接口定义
export interface ButtonSubmitState {
  isLoading: boolean
  isDisabled: boolean
  error: string | null
}

// 导出组合式函数
export const useButtonSubmit = (props: ButtonSubmitProps = {}) => {
  // 响应式状态
  const isLoading = ref(props.initialLoading || false)
  const isDisabled = ref(props.initialDisabled || false)
  const error = ref<string | null>(null)

  // 服务
  const { showError } = useNotificationService()

  // 计算属性
  const canSubmit = computed(() => !isLoading.value && !isDisabled.value)

  // 方法
  const handleSubmit = async (action: AsyncFunction) => {
    if (!canSubmit.value) return

    isLoading.value = true
    error.value = null

    try {
      await action()
    } catch (err) {
      error.value = err instanceof Error ? err.message : '提交失败'
      showError({
        title: '操作失败',
        message: error.value
      } as NotificationOptions)
    } finally {
      isLoading.value = false
    }
  }

  // 监听器
  watch(() => props.initialDisabled, (newVal) => {
    isDisabled.value = newVal
  })

  // 返回公共接口
  return {
    isLoading,
    isDisabled,
    error,
    canSubmit,
    handleSubmit
  }
}
```

### 示例3：类型定义文件中的类型导入
**文件位置**：`definitions/ui/components.ts`

```typescript
// 从同目录的其他类型文件导入
import type { ThemeColor, ThemeSize } from './theme'
import type { IconName } from './icons'

// 从核心类型导入
import type { Nullable, Optional } from '../core/base'
import type { EventEmitter } from '../core/events'

// 按钮基础属性
export interface ButtonBaseProps {
  variant?: ThemeColor
  size?: ThemeSize
  disabled?: boolean
  loading?: boolean
  icon?: IconName
  iconPosition?: 'left' | 'right'
}

// 按钮Props
export interface ButtonProps extends ButtonBaseProps {
  type?: 'button' | 'submit' | 'reset'
  label?: string
  ariaLabel?: string
}

// 按钮Emits
export interface ButtonEmits {
  (e: 'click', event: MouseEvent): void
  (e: 'focus', event: FocusEvent): void
  (e: 'blur', event: FocusEvent): void
}

// 按钮状态
export interface ButtonState {
  isHovered: boolean
  isFocused: boolean
  isPressed: boolean
}

// 表单按钮Props（扩展基础按钮）
export interface FormButtonProps extends ButtonProps {
  formId?: string
  validateBeforeSubmit?: boolean
}

// 导出工具类型
export type ButtonVariant = ThemeColor
export type ButtonSize = ThemeSize
export type ButtonEvent = keyof ButtonEmits
```

## 相对导入与绝对导入使用场景说明

### 相对导入使用场景

#### 适用场景
1. **同一模块内**：同一功能模块下的文件互相导入
   - 例如：`components/foo/ui/Foo.vue` 导入 `components/foo/composables/useFoo.ts`
   
2. **紧密耦合的文件**：逻辑上紧密相关、总是一起移动的文件
   - 例如：测试文件导入被测试文件
   - 例如：样式工具导入同目录的变量定义

3. **子模块内部**：在一个较大模块内部的子目录间导入
   - 例如：`utils/format/date.ts` 导入 `utils/format/shared.ts`

#### 优势
- **路径短**：导入语句更简洁
- **显式关系**：清晰表达文件间的相对位置
- **重构友好**：整个目录移动时，相对路径无需修改

#### 劣势
- **深度问题**：过深的相对路径（如 `../../../..`）难以阅读
- **文件移动**：单个文件移动时需要更新所有引用

### 绝对导入使用场景

#### 适用场景
1. **跨模块导入**：从其他功能模块导入类型或值
   - 例如：任何模块导入 `@definitions/*` 中的类型
   - 例如：组件导入 `@stores/*` 中的状态管理

2. **深度超过两层**：相对路径超过 `../..` 时使用绝对路径
   - 例如：`components/deep/nested/file.ts` 导入 `definitions/core/base.ts`

3. **公共模块导入**：导入项目公共的工具、服务、存储等
   - 例如：导入 `@composables/*`、`@services/*`、`@utils/*`

4. **类型定义导入**：所有 `definitions` 目录下的类型定义统一使用绝对路径

#### 优势
- **清晰明了**：一眼看出导入来源
- **稳定不变**：文件移动时，绝对路径无需修改
- **搜索友好**：便于全局搜索和替换
- **IDE支持**：更好的自动补全和跳转体验

#### 劣势
- **路径较长**：导入语句可能较长
- **配置依赖**：需要配置 `tsconfig.json` 的路径别名

### 决策矩阵

| 场景 | 推荐方式 | 示例 |
|------|---------|------|
| 同一目录 | 相对导入（`./`） | `import type { T } from './types'` |
| 父级一层 | 相对导入（`../`） | `import type { T } from '../base'` |
| 父级两层及以上 | 绝对导入 | `import type { T } from '@definitions/core/base'` |
| 导入类型定义 | 绝对导入 | `import type { T } from '@definitions/domain/user'` |
| 导入公共服务 | 绝对导入 | `import { S } from '@services/api'` |
| 导入公共组合式函数 | 绝对导入 | `import { useX } from '@composables/useX'` |
| 导入同模块组合式函数 | 相对导入 | `import { useX } from '../composables/useX'` |

## 代码模板中的导入说明补充

### .vue组件模板导入补充

#### 模板导入说明
```vue
<script setup lang="ts">
// ============================================================================
// 导入规范说明
// ============================================================================
// 1. 第三方库导入（第一组）
//    import { ref, computed } from 'vue'
//    import { useRouter } from 'vue-router'
//
// 2. 绝对路径导入 - 类型定义（第二组）
//    import type { SomeType } from '@definitions/xxx'
//
// 3. 绝对路径导入 - 公共模块（第二组）
//    import { useXxx } from '@composables/useXxx'
//    import { useXxxStore } from '@stores/xxx'
//
// 4. 相对路径导入 - 本模块（第三组）
//    import type { LocalType } from './types'
//    import { useLocal } from '../composables/useLocal'
//
// 组之间空一行，组内按字母顺序排序
// ============================================================================

// 1. 第三方库导入
import { ref, computed, watch } from 'vue'

// 2. 绝对路径导入
import type { ComponentProps, ComponentEmits } from '@definitions/ui/components'
import type { ThemeMode } from '@definitions/core/base'
import { useTheme } from '@composables/useTheme'
import { useAppStore } from '@stores/app'

// 3. 相对路径导入
import type { LocalState } from './types'
import { useComponentLogic } from '../composables/useComponentLogic'
import type { ComponentLogicReturn } from '../composables/useComponentLogic'

// Props定义
const props = defineProps<ComponentProps>()

// Emits定义
const emit = defineEmits<ComponentEmits>()

// 业务逻辑实现...
</script>
```

### .ts composable模板导入补充

#### 模板导入说明
```typescript
// ============================================================================
// 导入规范说明
// ============================================================================
// 1. 第三方库导入（第一组）
//    import { ref, computed } from 'vue'
//
// 2. 绝对路径导入 - 类型定义（第二组）
//    import type { SomeType } from '@definitions/xxx'
//
// 3. 绝对路径导入 - 公共模块（第二组）
//    import { useXxx } from '@composables/useXxx'
//    import { XxxService } from '@services/xxx'
//
// 4. 相对路径导入 - 本模块（第三组）
//    import type { LocalType } from './types'
//
// 组之间空一行，组内按字母顺序排序
// ============================================================================

// 1. 第三方库导入
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'

// 2. 绝对路径导入
import type { AsyncFunction, VoidFunction } from '@definitions/core/base'
import type { ErrorHandler } from '@definitions/core/errors'
import type { User } from '@definitions/domain/user'
import { useUserStore } from '@stores/user'
import { ApiService } from '@services/api'

// 3. 相对路径导入
import type { ComposableProps, ComposableReturn } from './types'
import { formatLocalDate } from './utils'

// 接口定义
export interface UseXxxProps {
  initialValue?: string
  autoSave?: boolean
}

export interface UseXxxReturn {
  value: string
  isLoading: boolean
  error: string | null
  setValue: (value: string) => void
  save: () => Promise<void>
}

// 组合式函数实现
export const useXxx = (props: UseXxxProps = {}): UseXxxReturn => {
  // 实现逻辑...
}
```

### .scss样式文件导入补充

#### 样式导入说明
```scss
// ============================================================================
// SCSS导入规范说明
// ============================================================================
// 1. 第三方库导入（第一组）
//    @use 'normalize.css';
//
// 2. 绝对路径导入 - 公共样式（第二组）
//    @use '@styles/variables' as *;
//    @use '@styles/mixins';
//
// 3. 相对路径导入 - 本模块样式（第三组）
//    @use './variables';
//    @use '../styles/shared';
//
// 注意：使用 @use 而不是 @import，优先使用别名导入
// ============================================================================

// 1. 第三方库导入
@use 'normalize.css';

// 2. 绝对路径导入
@use '@styles/variables' as *;
@use '@styles/mixins' as *;
@use '@styles/reset';

// 3. 相对路径导入
@use './variables' as local-vars;
@use '../styles/component-shared';

// 样式定义
.component {
  // 使用公共变量
  color: $text-primary;
  padding: $spacing-md;
  
  // 使用公共混入
  @include flex-center;
  
  // 使用本地变量
  border-radius: local-vars.$border-radius;
}
```

## 验证清单

### 类型导入验证清单

完成类型导入后，请使用以下验证清单检查是否符合规范：

#### 1. 导入路径验证
1. ✅ **类型定义导入**：所有从 `definitions` 导入的类型都使用 `@definitions/*` 绝对路径
2. ✅ **相对路径深度**：相对路径不超过两层（`../..`），超过时使用绝对路径
3. ✅ **路径别名**：正确使用配置的路径别名（`@/`、`@definitions/`、`@composables/` 等）
4. ✅ **文件扩展名**：省略 `.ts`、`.vue`、`.scss` 等文件扩展名

#### 2. 类型关键字验证
5. ✅ **类型导入**：纯类型导入使用 `import type` 语法
6. ✅ **混合导入**：同时导入类型和值时，分别使用类型导入和值导入
7. ✅ **导出类型**：类型导出时是否需要 `export type` 取决于TS版本和配置

#### 3. 导入顺序验证
8. ✅ **分组顺序**：按 第三方库 → 绝对路径 → 相对路径 的顺序分组
9. ✅ **组间空行**：不同组之间有一个空行分隔
10. ✅ **组内排序**：每组内部按字母顺序排序

#### 4. 导入内容验证
11. ✅ **未使用导入**：移除所有未使用的导入
12. ✅ **导入数量**：避免单个导入语句过长，考虑拆分或使用命名空间
13. ✅ **循环依赖**：检查并避免循环导入依赖

#### 5. 代码模板验证
14. ✅ **Vue组件**：组件中的导入符合模板规范
15. ✅ **Composable**：组合式函数中的导入符合模板规范
16. ✅ **样式文件**：SCSS文件中的导入使用 `@use` 和正确的别名

## 附录

### 术语表
| 术语 | 定义 |
|------|------|
| **类型导入** | 使用 `import type` 语法导入纯类型 |
| **绝对导入** | 使用路径别名的导入方式 |
| **相对导入** | 使用 `./` 或 `../` 的导入方式 |
| **路径别名** | `tsconfig.json` 中配置的导入路径简写 |
| **混合导入** | 同一文件中同时导入类型和值 |

### 外部资源
- [TypeScript 模块导入文档](https://www.typescriptlang.org/docs/handbook/modules.html)
- [TypeScript 3.8+ 类型导入语法](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export)
- [Vue 3 组合式API导入规范](https://vuejs.org/guide/typescript/composition-api.html)

---
**文档信息**
- 生成时间：2026年4月2日
- 基于版本：项目类型导入规范（20260402）
- 适用场景：YTLA项目所有TypeScript文件
- 文件位置：temp_import_section.md
- 关联文档：rule_ui_instructions.md
