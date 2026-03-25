# Vue 3 + TypeScript 可复用代码模板

基于 sideCard 组件分析结果和文件结构规范，提供以下可复用代码模板与完整示例。

## 目录
1. [.vue 组件模板](#1-vue-组件模板)
2. [.ts composable 模板](#2-ts-composable-模板)  
3. [.scss 样式模板](#3-scss-样式模板)
4. [类型定义模板](#4-类型定义模板)
5. [基于 sideCard 的完整示例](#5-基于-sidecard-的完整示例)

---

## 1. .vue 组件模板

### 模板结构说明
```vue
<template>
  <!-- 模板部分 -->
  <!-- 1. 使用语义化HTML标签 -->
  <!-- 2. 使用v-if/v-show控制显示 -->
  <!-- 3. 使用v-bind绑定属性和类 -->
  <!-- 4. 使用@事件监听器 -->
  <!-- 5. 使用ref进行DOM引用 -->
  <!-- 6. 使用插槽slot进行内容分发 -->
</template>

<script setup lang="ts">
// 脚本部分
// 1. 导入依赖
// 2. 定义组件props接口
// 3. 定义组件emits类型
// 4. 使用defineProps定义props
// 5. 使用defineEmits定义事件
// 6. 定义响应式数据
// 7. 定义计算属性
// 8. 定义方法函数
// 9. 定义生命周期钩子
// 10. 暴露组件接口
</script>

<style scoped lang="scss">
// 样式部分
// 1. 使用@use导入样式依赖
// 2. 使用scoped限定样式作用域
// 3. 使用BEM命名约定
// 4. 使用CSS自定义属性
// 5. 使用响应式设计
</style>
```

### 完整模板示例
```vue
<template>
  <!-- 主容器 -->
  <div 
    v-if="showComponent"
    ref="componentRef"
    class="component-wrapper"
    :class="{
      '--active': isActive,
      '--disabled': isDisabled
    }"
    :data-testid="componentId"
  >
    <!-- 内容区域 -->
    <div class="component-content">
      <!-- 默认插槽 -->
      <slot></slot>
      
      <!-- 命名插槽 -->
      <slot name="header"></slot>
      <slot name="footer"></slot>
    </div>
    
    <!-- 事件触发元素 -->
    <button
      v-if="showButton"
      class="action-button"
      @click="handleClick"
      @keydown.enter="handleClick"
      @keydown.esc="handleCancel"
      :disabled="isDisabled"
      :aria-label="buttonLabel"
      :title="buttonTitle"
    >
      <slot name="button-content">
        {{ buttonText }}
      </slot>
    </button>
  </div>
</template>

<script setup lang="ts">
// 导入类型定义
import type { ComponentProps, ComponentEmits } from './componentTypes.ts'

// 导入组合式函数
import { useComponentLogic } from './composables/useComponentLogic.ts'

// 定义组件props接口
interface Props extends ComponentProps {
  /** 组件是否显示 */
  showComponent?: boolean
  /** 按钮是否显示 */
  showButton?: boolean
  /** 按钮文本 */
  buttonText?: string
  /** 按钮标签（无障碍访问） */
  buttonLabel?: string
  /** 按钮提示文本 */
  buttonTitle?: string
  /** 组件唯一标识 */
  componentId?: string
  /** 组件是否激活 */
  isActive?: boolean
  /** 组件是否禁用 */
  isDisabled?: boolean
}

// 定义组件emits类型
interface Emits extends ComponentEmits {
  /** 点击事件 */
  (e: 'click', payload: { id?: string; event: MouseEvent }): void
  /** 取消事件 */
  (e: 'cancel'): void
  /** 状态变化事件 */
  (e: 'change', newState: boolean): void
}

// 定义props
const props = withDefaults(defineProps<Props>(), {
  showComponent: true,
  showButton: true,
  buttonText: '操作',
  buttonLabel: '操作按钮',
  buttonTitle: '点击执行操作',
  componentId: '',
  isActive: false,
  isDisabled: false
})

// 定义emits
const emit = defineEmits<Emits>()

// DOM引用
const componentRef = ref<HTMLElement | null>(null)

// 使用组合式函数
const { 
  localState, 
  computedValue, 
  handleAction 
} = useComponentLogic(props)

// 响应式数据
const internalState = ref<boolean>(false)

// 计算属性
const buttonClasses = computed(() => ({
  'action-button': true,
  '--active': internalState.value,
  '--disabled': props.isDisabled
}))

// 事件处理函数
const handleClick = (event: MouseEvent) => {
  if (props.isDisabled) return
  
  internalState.value = !internalState.value
  emit('click', { id: props.componentId, event })
  emit('change', internalState.value)
  
  handleAction(event)
}

const handleCancel = () => {
  internalState.value = false
  emit('cancel')
}

// 生命周期钩子
onMounted(() => {
  console.log(`组件 ${props.componentId} 已挂载`)
})

onBeforeUnmount(() => {
  console.log(`组件 ${props.componentId} 即将卸载`)
})

// 暴露给父组件的接口
defineExpose({
  componentRef,
  internalState,
  toggleState: () => { internalState.value = !internalState.value },
  resetState: () => { internalState.value = false }
})
</script>

<style scoped lang="scss">
// 导入基础样式
@use '../styles/ui-base';
@use '../styles/ui-interaction';

// 组件容器
.component-wrapper {
  position: relative;
  display: inline-block;
  font-family: inherit;
  transition: all 0.3s ease;
  
  // 激活状态
  &.--active {
    opacity: 1;
    transform: scale(1.05);
  }
  
  // 禁用状态
  &.--disabled {
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
  }
}

// 内容区域
.component-content {
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
  
  &:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  }
}

// 操作按钮
.action-button {
  @include ui-base.button-reset;
  
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
  
  // 悬停状态
  &:hover:not(.--disabled) {
    background: #3aa876;
    transform: translateY(-1px);
  }
  
  // 聚焦状态
  &:focus-visible {
    outline: 2px solid #42b983;
    outline-offset: 2px;
  }
}
</style>
```

---

## 2. .ts composable 模板

### 模板结构说明
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

### 完整模板示例
```typescript
/**
 * 组件逻辑组合式函数
 * 封装组件的业务逻辑、状态管理和副作用处理
 * 
 * @param props - 组件props
 * @returns 组件逻辑的响应式接口
 */
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue'
import type { Ref } from 'vue'

// 导入类型定义
import type { ComponentProps } from '../definitions/componentTypes.ts'

// 导入工具函数
import { usePersistence } from '@/core/classic/frame/main/composables/usePersistence.ts'
import { useLogger } from '@/core/classic/utils/composables/useLogger.ts'

// 定义composable参数接口
export interface UseComponentParams extends ComponentProps {
  /** 组件初始状态 */
  initialState?: boolean
  /** 是否启用持久化 */
  enablePersistence?: boolean
  /** 日志级别 */
  logLevel?: 'debug' | 'info' | 'warn' | 'error'
}

// 定义返回值接口
export interface UseComponentReturn {
  /** 组件状态 */
  state: Ref<boolean>
  /** 计算属性值 */
  computedValue: Ref<string>
  /** 是否处于加载状态 */
  isLoading: Ref<boolean>
  /** 错误信息 */
  error: Ref<string | null>
  
  /** 切换状态 */
  toggle: () => void
  /** 设置状态 */
  setState: (newState: boolean) => void
  /** 重置状态 */
  reset: () => void
  /** 执行操作 */
  execute: (payload?: unknown) => Promise<void>
  /** 清理资源 */
  cleanup: () => void
}

/**
 * 组件逻辑组合式函数
 * 
 * @param params - 组件参数
 * @returns 组件逻辑接口
 */
export const useComponentLogic = (params: UseComponentParams): UseComponentReturn => {
  const { 
    initialState = false, 
    enablePersistence = true,
    logLevel = 'info'
  } = params

  // ========== 响应式状态 ==========
  
  /** 组件主状态 */
  const state = ref<boolean>(initialState)
  
  /** 加载状态 */
  const isLoading = ref<boolean>(false)
  
  /** 错误信息 */
  const error = ref<string | null>(null)
  
  /** 内部计数器 */
  const counter = ref<number>(0)
  
  // ========== 工具函数 ==========
  
  /** 持久化工具 */
  const { getPersistence, setPersistence } = usePersistence()
  
  /** 日志工具 */
  const logger = useLogger('ComponentLogic', logLevel)
  
  // ========== 计算属性 ==========
  
  /** 基于状态的计算值 */
  const computedValue = computed<string>(() => {
    return state.value ? '激活状态' : '未激活状态'
  })
  
  /** 状态描述 */
  const stateDescription = computed<string>(() => {
    if (isLoading.value) return '加载中...'
    if (error.value) return `错误: ${error.value}`
    return computedValue.value
  })
  
  // ========== 操作方法 ==========
  
  /**
   * 切换组件状态
   */
  const toggle = (): void => {
    if (isLoading.value) {
      logger.warn('组件正在加载中，无法切换状态')
      return
    }
    
    state.value = !state.value
    counter.value += 1
    
    logger.info(`状态已切换: ${state.value}`, { 
      counter: counter.value,
      componentId: params.componentId 
    })
    
    // 持久化状态
    if (enablePersistence && params.componentId) {
      setPersistence('components', {
        [params.componentId]: state.value
      })
    }
  }
  
  /**
   * 设置组件状态
   * 
   * @param newState - 新状态值
   */
  const setState = (newState: boolean): void => {
    state.value = newState
    logger.debug(`状态已设置为: ${newState}`)
  }
  
  /**
   * 重置组件状态
   */
  const reset = (): void => {
    state.value = initialState
    counter.value = 0
    error.value = null
    logger.info('状态已重置')
  }
  
  /**
   * 执行异步操作
   * 
   * @param payload - 操作参数
   */
  const execute = async (payload?: unknown): Promise<void> => {
    if (isLoading.value) {
      logger.warn('操作已在执行中')
      return
    }
    
    isLoading.value = true
    error.value = null
    
    try {
      logger.info('开始执行操作', { payload })
      
      // 模拟异步操作
      await new Promise(resolve => setTimeout(resolve, 500))
      
      // 操作成功
      state.value = true
      logger.info('操作执行成功')
      
    } catch (err) {
      // 操作失败
      error.value = err instanceof Error ? err.message : '未知错误'
      logger.error('操作执行失败', err)
      
    } finally {
      isLoading.value = false
    }
  }
  
  /**
   * 清理资源
   */
  const cleanup = (): void => {
    logger.debug('清理组件资源')
    reset()
    // 清理其他资源...
  }
  
  // ========== 副作用监听 ==========
  
  // 监听状态变化
  watch(state, (newValue, oldValue) => {
    logger.debug(`状态变化: ${oldValue} → ${newValue}`)
  })
  
  // 监听错误状态
  watch(error, (newError) => {
    if (newError) {
      logger.error('组件发生错误', { error: newError })
    }
  })
  
  // 监听组件ID变化
  watch(() => params.componentId, (newId, oldId) => {
    if (enablePersistence && newId && newId !== oldId) {
      const persistedState = getPersistence('components', newId)
      if (persistedState !== undefined) {
        state.value = persistedState as boolean
        logger.debug(`从持久化恢复状态: ${state.value}`)
      }
    }
  })
  
  // ========== 生命周期 ==========
  
  onMounted(() => {
    logger.info('组件逻辑已初始化')
    
    // 从持久化恢复状态
    if (enablePersistence && params.componentId) {
      const persistedState = getPersistence('components', params.componentId)
      if (persistedState !== undefined) {
        state.value = persistedState as boolean
        logger.debug(`初始化时从持久化恢复状态: ${state.value}`)
      }
    }
  })
  
  onBeforeUnmount(() => {
    cleanup()
    logger.info('组件逻辑已销毁')
  })
  
  // ========== 返回接口 ==========
  
  return {
    // 状态
    state,
    computedValue,
    isLoading,
    error,
    
    // 方法
    toggle,
    setState,
    reset,
    execute,
    cleanup
  }
}

// 导出类型
export type { UseComponentParams, UseComponentReturn }
```

---

## 3. .scss 样式模板

### 模板结构说明
```scss
// styles/[component-name].scss 模板

// 1. 定义CSS自定义属性
// 2. 定义基础样式类
// 3. 定义状态修饰类
// 4. 定义动画效果
// 5. 定义响应式样式
// 6. 定义工具类
```

### 完整模板示例
```scss
/**
 * 组件样式文件
 * 使用SCSS编写，遵循BEM命名约定
 */

// ========== CSS自定义属性 ==========
:root {
  // 颜色变量
  --component-primary: #42b983;
  --component-secondary: #35495e;
  --component-success: #42b983;
  --component-warning: #f0ad4e;
  --component-danger: #d9534f;
  --component-info: #5bc0de;
  
  // 背景色变量
  --component-bg-default: #ffffff;
  --component-bg-hover: #f8f9fa;
  --component-bg-active: #e9ecef;
  --component-bg-disabled: #f5f5f5;
  
  // 文本色变量
  --component-text-default: #212529;
  --component-text-secondary: #6c757d;
  --component-text-disabled: #adb5bd;
  
  // 边框变量
  --component-border-default: #dee2e6;
  --component-border-hover: #ced4da;
  --component-border-active: #42b983;
  
  // 间距变量
  --component-spacing-xs: 0.25rem;
  --component-spacing-sm: 0.5rem;
  --component-spacing-md: 1rem;
  --component-spacing-lg: 1.5rem;
  --component-spacing-xl: 2rem;
  
  // 阴影变量
  --component-shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --component-shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --component-shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  
  // 圆角变量
  --component-radius-sm: 0.25rem;
  --component-radius-md: 0.5rem;
  --component-radius-lg: 1rem;
  --component-radius-full: 9999px;
  
  // 过渡变量
  --component-transition-fast: 150ms ease;
  --component-transition-normal: 300ms ease;
  --component-transition-slow: 500ms ease;
  
  // z-index变量
  --component-z-index-base: 1;
  --component-z-index-dropdown: 1000;
  --component-z-index-sticky: 1020;
  --component-z-index-fixed: 1030;
  --component-z-index-modal: 1040;
  --component-z-index-popover: 1050;
  --component-z-index-tooltip: 1060;
}

// ========== 基础样式类 ==========

/**
 * 组件容器
 * 使用BEM命名：.component
 */
.component {
  // 布局属性
  position: relative;
  display: inline-flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: flex-start;
  
  // 盒模型
  width: 100%;
  max-width: 100%;
  min-height: 3rem;
  box-sizing: border-box;
  
  // 视觉属性
  background-color: var(--component-bg-default);
  border: 1px solid var(--component-border-default);
  border-radius: var(--component-radius-md);
  box-shadow: var(--component-shadow-sm);
  
  // 过渡效果
  transition: all var(--component-transition-normal);
  transition-property: border-color, box-shadow, transform, opacity;
  
  // 文本属性
  color: var(--component-text-default);
  font-family: inherit;
  font-size: 0.875rem;
  line-height: 1.5;
  text-align: left;
  
  // 交互属性
  cursor: default;
  user-select: none;
  overflow: hidden;
  
  // ========== 修饰符 ==========
  
  // 尺寸修饰符
  &.--small {
    padding: var(--component-spacing-sm);
    font-size: 0.75rem;
    border-radius: var(--component-radius-sm);
  }
  
  &.--medium {
    padding: var(--component-spacing-md);
    font-size: 0.875rem;
  }
  
  &.--large {
    padding: var(--component-spacing-lg);
    font-size: 1rem;
    border-radius: var(--component-radius-lg);
  }
  
  // 变体修饰符
  &.--primary {
    border-color: var(--component-primary);
    background-color: rgba(66, 185, 131, 0.1);
    
    &:hover {
      background-color: rgba(66, 185, 131, 0.15);
    }
  }
  
  &.--secondary {
    border-color: var(--component-secondary);
    background-color: rgba(53, 73, 94, 0.1);
  }
  
  &.--outline {
    background-color: transparent;
    border: 2px solid currentColor;
  }
  
  // ========== 状态修饰符 ==========
  
  // 悬停状态
  &:hover:not(.--disabled):not(.--readonly) {
    border-color: var(--component-border-hover);
    box-shadow: var(--component-shadow-md);
    transform: translateY(-1px);
    background-color: var(--component-bg-hover);
  }
  
  // 激活状态
  &.--active {
    border-color: var(--component-border-active);
    box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.25);
    background-color: var(--component-bg-active);
    
    &:hover {
      border-color: var(--component-primary);
    }
  }
  
  // 聚焦状态
  &:focus-visible {
    outline: 2px solid var(--component-primary);
    outline-offset: 2px;
  }
  
  // 禁用状态
  &.--disabled {
    opacity: 0.6;
    cursor: not-allowed;
    pointer-events: none;
    background-color: var(--component-bg-disabled);
    color: var(--component-text-disabled);
    
    &:hover {
      transform: none;
      box-shadow: var(--component-shadow-sm);
    }
  }
  
  // 只读状态
  &.--readonly {
    cursor: default;
    user-select: text;
    
    &:hover {
      transform: none;
      box-shadow: var(--component-shadow-sm);
    }
  }
  
  // 错误状态
  &.--error {
    border-color: var(--component-danger);
    
    &:hover {
      border-color: #c9302c;
    }
  }
  
  // 警告状态
  &.--warning {
    border-color: var(--component-warning);
  }
  
  // 成功状态
  &.--success {
    border-color: var(--component-success);
  }
}

// ========== 子元素样式 ==========

/**
 * 组件标题
 * 使用BEM元素：.component__title
 */
.component__title {
  // 布局属性
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0 0 var(--component-spacing-md) 0;
  padding: 0;
  
  // 文本属性
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.2;
  color: var(--component-text-default);
  
  // 修饰符
  &.--small {
    font-size: 0.875rem;
  }
  
  &.--large {
    font-size: 1.25rem;
  }
  
  &.--with-icon {
    gap: var(--component-spacing-sm);
  }
}

/**
 * 组件内容
 * 使用BEM元素：.component__content
 */
.component__content {
  // 布局属性
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: var(--component-spacing-sm);
  
  // 文本属性
  word-break: break-word;
  overflow-wrap: break-word;
  
  // 修饰符
  &.--scrollable {
    max-height: 20rem;
    overflow-y: auto;
    
    // 自定义滚动条
    &::-webkit-scrollbar {
      width: 6px;
    }
    
    &::-webkit-scrollbar-track {
      background: transparent;
    }
    
    &::-webkit-scrollbar-thumb {
      background: rgba(0, 0, 0, 0.2);
      border-radius: var(--component-radius-full);
      
      &:hover {
        background: rgba(0, 0, 0, 0.3);
      }
    }
  }
  
  &.--centered {
    align-items: center;
    justify-content: center;
    text-align: center;
  }
}

/**
 * 组件操作栏
 * 使用BEM元素：.component__actions
 */
.component__actions {
  // 布局属性
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: var(--component-spacing-sm);
  margin-top: var(--component-spacing-md);
  padding-top: var(--component-spacing-md);
  border-top: 1px solid var(--component-border-default);
  
  // 修饰符
  &.--left {
    justify-content: flex-start;
  }
  
  &.--center {
    justify-content: center;
  }
  
  &.--right {
    justify-content: flex-end;
  }
  
  &.--space-between {
    justify-content: space-between;
  }
  
  &.--sticky {
    position: sticky;
    bottom: 0;
    background: var(--component-bg-default);
    z-index: var(--component-z-index-sticky);
  }
}

/**
 * 组件操作按钮
 * 使用BEM元素：.component__action
 */
.component__action {
  // 重置按钮样式
  @include button-reset;
  
  // 布局属性
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--component-spacing-xs);
  padding: var(--component-spacing-sm) var(--component-spacing-md);
  
  // 视觉属性
  background-color: var(--component-bg-default);
  border: 1px solid var(--component-border-default);
  border-radius: var(--component-radius-sm);
  color: var(--component-text-default);
  
  // 文本属性
  font-size: 0.875rem;
  font-weight: 500;
  line-height: 1;
  white-space: nowrap;
  
  // 过渡效果
  transition: all var(--component-transition-fast);
  
  // 交互属性
  cursor: pointer;
  user-select: none;
  
  // 悬停状态
  &:hover:not(.--disabled) {
    background-color: var(--component-bg-hover);
    border-color: var(--component-border-hover);
    transform: translateY(-1px);
  }
  
  // 激活状态
  &:active:not(.--disabled) {
    transform: translateY(0);
  }
  
  // 聚焦状态
  &:focus-visible {
    outline: 2px solid var(--component-primary);
    outline-offset: 2px;
  }
  
  // 变体修饰符
  &.--primary {
    background-color: var(--component-primary);
    border-color: var(--component-primary);
    color: white;
    
    &:hover:not(.--disabled) {
      background-color: #3aa876;
      border-color: #3aa876;
    }
  }
  
  &.--danger {
    background-color: var(--component-danger);
    border-color: var(--component-danger);
    color: white;
    
    &:hover:not(.--disabled) {
      background-color: #c9302c;
      border-color: #c9302c;
    }
  }
  
  // 状态修饰符
  &.--disabled {
    opacity: 0.6;
    cursor: not-allowed;
    pointer-events: none;
  }
  
  // 尺寸修饰符
  &.--small {
    padding: var(--component-spacing-xs) var(--component-spacing-sm);
    font-size: 0.75rem;
  }
  
  &.--large {
    padding: var(--component-spacing-md) var(--component-spacing-lg);
    font-size: 1rem;
  }
}

// ========== 动画效果 ==========

/**
 * 组件进入动画
 */
@keyframes component-enter {
  from {
    opacity: 0;
    transform: translateY(-10px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/**
 * 组件退出动画
 */
@keyframes component-exit {
  from {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
  to {
    opacity: 0;
    transform: translateY(-10px) scale(0.95);
  }
}

/**
 * 组件加载动画
 */
@keyframes component-loading {
  0%, 100% {
    opacity: 0.6;
  }
  50% {
    opacity: 1;
  }
}

// 动画类
.component {
  &.--entering {
    animation: component-enter 0.3s ease forwards;
  }
  
  &.--exiting {
    animation: component-exit 0.3s ease forwards;
  }
  
  &.--loading {
    animation: component-loading 1.5s ease-in-out infinite;
  }
}

// ========== 响应式设计 ==========

// 移动端适配
@media (max-width: 767px) {
  .component {
    &.--large-on-mobile {
      padding: var(--component-spacing-lg);
      font-size: 1rem;
    }
  }
  
  .component__actions {
    flex-direction: column;
    gap: var(--component-spacing-sm);
    
    .component__action {
      width: 100%;
      justify-content: center;
    }
  }
}

// 平板适配
@media (min-width: 768px) and (max-width: 1023px) {
  .component {
    max-width: 90%;
    margin: 0 auto;
  }
}

// 桌面端适配
@media (min-width: 1024px) {
  .component {
    max-width: 50rem;
  }
}

// ========== 工具类 ==========

/**
 * 工具类：隐藏元素
 */
.component-hidden {
  display: none !important;
  visibility: hidden !important;
  opacity: 0 !important;
}

/**
 * 工具类：可见但透明
 */
.component-transparent {
  opacity: 0.5 !important;
}

/**
 * 工具类：全宽
 */
.component-full-width {
  width: 100% !important;
  max-width: 100% !important;
}

/**
 * 工具类：无边框
 */
.component-borderless {
  border: none !important;
  box-shadow: none !important;
}

/**
 * 工具类：圆角
 */
.component-rounded {
  border-radius: var(--component-radius-lg) !important;
}

/**
 * 工具类：圆形
 */
.component-circle {
  border-radius: 50% !important;
  aspect-ratio: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
}

// ========== 混合和函数 ==========

/**
 * 重置按钮样式混合
 */
@mixin button-reset {
  margin: 0;
  padding: 0;
  background: none;
  border: none;
  font: inherit;
  color: inherit;
  cursor: pointer;
  appearance: none;
  user-select: none;
  
  &:focus {
    outline: none;
  }
}

/**
 * 文字截断混合
 */
@mixin text-truncate($lines: 1) {
  @if $lines == 1 {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  } @else {
    display: -webkit-box;
    -webkit-line-clamp: $lines;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
  }
}

/**
 * 深色模式适配
 */
@media (prefers-color-scheme: dark) {
  .component {
    background-color: #2d3748;
    border-color: #4a5568;
    color: #e2e8f0;
    
    &:hover:not(.--disabled) {
      background-color: #4a5568;
      border-color: #718096;
    }
  }
  
  .component__actions {
    border-top-color: #4a5568;
  }
}
```

---

## 4. 类型定义模板

### 模板结构说明
```typescript
// definitions/[component-name]Types.ts 模板

// 1. 导出主要接口类型
// 2. 导出Props接口
// 3. 导出Emits类型
// 4. 导出组件配置类型
// 5. 导出工具类型
// 6. 导出常量枚举
```

### 完整模板示例
```typescript
/**
 * 组件类型定义文件
 * 定义组件props、emits、配置和工具类型
 */

// ========== 基础类型 ==========

/**
 * 组件尺寸类型
 */
export type ComponentSize = 'small' | 'medium' | 'large'

/**
 * 组件变体类型
 */
export type ComponentVariant = 'default' | 'primary' | 'secondary' | 'danger' | 'warning' | 'success' | 'info' | 'outline'

/**
 * 组件状态类型
 */
export type ComponentState = 'default' | 'active' | 'disabled' | 'loading' | 'error' | 'success' | 'warning'

/**
 * 组件位置类型
 */
export type ComponentPosition = 'left' | 'center' | 'right' | 'top' | 'bottom'

// ========== Props接口 ==========

/**
 * 组件基础props接口
 * 所有组件props都应继承此接口
 */
export interface ComponentBaseProps {
  /** 组件唯一标识 */
  id?: string
  
  /** 组件类名 */
  class?: string
  
  /** 内联样式 */
  style?: Record<string, string | number>
  
  /** 数据测试ID（用于测试） */
  'data-testid'?: string
  
  /** 无障碍访问标签 */
  'aria-label'?: string
  
  /** 无障碍访问角色 */
  'aria-role'?: string
  
  /** 是否禁用组件 */
  disabled?: boolean
  
  /** 是否只读 */
  readonly?: boolean
  
  /** 是否显示组件 */
  visible?: boolean
}

/**
 * 组件配置props接口
 */
export interface ComponentConfigProps {
  /** 组件尺寸 */
  size?: ComponentSize
  
  /** 组件变体 */
  variant?: ComponentVariant
  
  /** 组件宽度 */
  width?: string | number
  
  /** 组件高度 */
  height?: string | number
  
  /** 最大宽度 */
  maxWidth?: string | number
  
  /** 最大高度 */
  maxHeight?: string | number
  
  /** 最小宽度 */
  minWidth?: string | number
  
  /** 最小高度 */
  minHeight?: string | number
  
  /** 内边距 */
  padding?: string | number
  
  /** 外边距 */
  margin?: string | number
  
  /** 圆角半径 */
  borderRadius?: string | number
  
  /** 边框宽度 */
  borderWidth?: string | number
  
  /** 边框颜色 */
  borderColor?: string
  
  /** 背景颜色 */
  backgroundColor?: string
  
  /** 文本颜色 */
  color?: string
  
  /** 字体大小 */
  fontSize?: string | number
  
  /** 字体粗细 */
  fontWeight?: string | number
  
  /** 文本对齐方式 */
  textAlign?: ComponentPosition
  
  /** 垂直对齐方式 */
  verticalAlign?: 'top' | 'middle' | 'bottom'
  
  /** 内容位置 */
  contentPosition?: ComponentPosition
  
  /** 操作栏位置 */
  actionsPosition?: ComponentPosition
}

/**
 * 组件事件props接口
 */
export interface ComponentEventProps {
  /** 点击事件回调 */
  onClick?: (event: MouseEvent) => void
  
  /** 双击事件回调 */
  onDblClick?: (event: MouseEvent) => void
  
  /** 鼠标移入事件回调 */
  onMouseEnter?: (event: MouseEvent) => void
  
  /** 鼠标移出事件回调 */
  onMouseLeave?: (event: MouseEvent) => void
  
  /** 鼠标按下事件回调 */
  onMouseDown?: (event: MouseEvent) => void
  
  /** 鼠标抬起事件回调 */
  onMouseUp?: (event: MouseEvent) => void
  
  /** 键盘按下事件回调 */
  onKeyDown?: (event: KeyboardEvent) => void
  
  /** 键盘抬起事件回调 */
  onKeyUp?: (event: KeyboardEvent) => void
  
  /** 焦点事件回调 */
  onFocus?: (event: FocusEvent) => void
  
  /** 失焦事件回调 */
  onBlur?: (event: FocusEvent) => void
  
  /** 输入事件回调 */
  onInput?: (value: string) => void
  
  /** 变化事件回调 */
  onChange?: (value: unknown) => void
  
  /** 提交事件回调 */
  onSubmit?: (event: Event) => void
}

/**
 * 组件数据props接口
 */
export interface ComponentDataProps<T = unknown> {
  /** 组件数据 */
  data?: T
  
  /** 数据加载状态 */
  loading?: boolean
  
  /** 加载中文本 */
  loadingText?: string
  
  /** 数据错误信息 */
  error?: string | Error
  
  /** 空状态文本 */
  emptyText?: string
  
  /** 空状态图标 */
  emptyIcon?: string
  
  /** 数据格式化函数 */
  formatter?: (data: T) => unknown
  
  /** 数据验证函数 */
  validator?: (data: T) => boolean | string
  
  /** 数据比较函数 */
  compare?: (a: T, b: T) => number
}

/**
 * 组件完整props接口
 * 组合所有props类型
 */
export interface ComponentProps extends 
  ComponentBaseProps, 
  ComponentConfigProps, 
  ComponentEventProps, 
  ComponentDataProps {
  /** 组件标题 */
  title?: string
  
  /** 组件描述 */
  description?: string
  
  /** 组件图标 */
  icon?: string
  
  /** 图标位置 */
  iconPosition?: 'left' | 'right' | 'top' | 'bottom'
  
  /** 图标大小 */
  iconSize?: string | number
  
  /** 图标颜色 */
  iconColor?: string
  
  /** 是否显示图标 */
  showIcon?: boolean
  
  /** 是否显示标题 */
  showTitle?: boolean
  
  /** 是否显示描述 */
  showDescription?: boolean
  
  /** 是否显示操作栏 */
  showActions?: boolean
  
  /** 操作按钮配置 */
  actions?: ComponentAction[]
  
  /** 是否可关闭 */
  closable?: boolean
  
  /** 关闭按钮位置 */
  closePosition?: ComponentPosition
  
  /** 关闭按钮图标 */
  closeIcon?: string
  
  /** 是否可拖拽 */
  draggable?: boolean
  
  /** 是否可调整大小 */
  resizable?: boolean
  
  /** 是否可折叠 */
  collapsible?: boolean
  
  /** 初始折叠状态 */
  collapsed?: boolean
  
  /** 折叠动画持续时间 */
  collapseDuration?: number
  
  /** 折叠动画缓动函数 */
  collapseEasing?: string
  
  /** 工具提示文本 */
  tooltip?: string
  
  /** 工具提示位置 */
  tooltipPosition?: ComponentPosition
  
  /** 工具提示延迟时间 */
  tooltipDelay?: number
  
  /** 弹出菜单配置 */
  popover?: ComponentPopoverConfig
  
  /** 模态框配置 */
  modal?: ComponentModalConfig
  
  /** 抽屉配置 */
  drawer?: ComponentDrawerConfig
  
  /** 选项卡配置 */
  tabs?: ComponentTabConfig[]
  
  /** 当前激活的选项卡 */
  activeTab?: string | number
  
  /** 表单字段配置 */
  form?: ComponentFormConfig
  
  /** 表格配置 */
  table?: ComponentTableConfig
  
  /** 列表配置 */
  list?: ComponentListConfig
  
  /** 网格配置 */
  grid?: ComponentGridConfig
  
  /** 卡片配置 */
  card?: ComponentCardConfig
  
  /** 面板配置 */
  panel?: ComponentPanelConfig
  
  /** 对话框配置 */
  dialog?: ComponentDialogConfig
  
  /** 通知配置 */
  notification?: ComponentNotificationConfig
  
  /** 加载器配置 */
  loader?: ComponentLoaderConfig
  
  /** 进度条配置 */
  progress?: ComponentProgressConfig
  
  /** 评分配置 */
  rating?: ComponentRatingConfig
  
  /** 滑块配置 */
  slider?: ComponentSliderConfig
  
  /** 开关配置 */
  switch?: ComponentSwitchConfig
  
  /** 选择器配置 */
  select?: ComponentSelectConfig
  
  /** 日期选择器配置 */
  datePicker?: ComponentDatePickerConfig
  
  /** 时间选择器配置 */
  timePicker?: ComponentTimePickerConfig
  
  /** 颜色选择器配置 */
  colorPicker?: ComponentColorPickerConfig
  
  /** 上传配置 */
  upload?: ComponentUploadConfig
  
  /** 编辑器配置 */
  editor?: ComponentEditorConfig
  
  /** 图表配置 */
  chart?: ComponentChartConfig
  
  /** 地图配置 */
  map?: ComponentMapConfig
  
  /** 日历配置 */
  calendar?: ComponentCalendarConfig
  
  /** 时间线配置 */
  timeline?: ComponentTimelineConfig
  
  /** 树形结构配置 */
  tree?: ComponentTreeConfig
  
  /** 分页配置 */
  pagination?: ComponentPaginationConfig
  
  /** 面包屑配置 */
  breadcrumb?: ComponentBreadcrumbConfig
  
  /** 步骤条配置 */
  steps?: ComponentStepsConfig
  
  /** 时间轴配置 */
  timeline?: ComponentTimelineConfig
  
  /** 徽标配置 */
  badge?: ComponentBadgeConfig
  
  /** 头像配置 */
  avatar?: ComponentAvatarConfig
  
  /** 标签配置 */
  tag?: ComponentTagConfig
  
  /** 链接配置 */
  link?: ComponentLinkConfig
  
  /** 图片配置 */
  image?: ComponentImageConfig
  
  /** 视频配置 */
  video?: ComponentVideoConfig
  
  /** 音频配置 */
  audio?: ComponentAudioConfig
  
  /** 文件配置 */
  file?: ComponentFileConfig
  
  /** 代码配置 */
  code?: ComponentCodeConfig
  
  /** 数学公式配置 */
  math?: ComponentMathConfig
  
  /** 富文本配置 */
  richText?: ComponentRichTextConfig
  
  /** Markdown配置 */
  markdown?: ComponentMarkdownConfig
  
  /** PDF配置 */
  pdf?: ComponentPdfConfig
  
  /** 电子表格配置 */
  spreadsheet?: ComponentSpreadsheetConfig
  
  /** 演示文稿配置 */
  presentation?: ComponentPresentationConfig
  
  /** 数据库配置 */
  database?: ComponentDatabaseConfig
  
  /** API配置 */
  api?: ComponentApiConfig
  
  /** WebSocket配置 */
  websocket?: ComponentWebSocketConfig
  
  /** SSE配置 */
  sse?: ComponentSseConfig
  
  /** GraphQL配置 */
  graphql?: ComponentGraphqlConfig
  
  /** REST配置 */
  rest?: ComponentRestConfig
  
  /** gRPC配置 */
  grpc?: ComponentGrpcConfig
  
  /** WebRTC配置 */
  webrtc?: ComponentWebrtcConfig
  
  /** WebGL配置 */
  webgl?: ComponentWebglConfig
  
  /** WebAssembly配置 */
  wasm?: ComponentWasmConfig
  
  /** WebWorker配置 */
  webworker?: ComponentWebworkerConfig
  
  /** ServiceWorker配置 */
  serviceworker?: ComponentServiceworkerConfig
  
  /** PWA配置 */
  pwa?: ComponentPwaConfig
  
  /** AMP配置 */
  amp?: ComponentAmpConfig
  
  /** SSR配置 */
  ssr?: ComponentSsrConfig
  
  /** SSG配置 */
  ssg?: ComponentSsgConfig
  
  /** ISR配置 */
  isr?: ComponentIsrConfig
  
  /** CSR配置 */
  csr?: ComponentCsrConfig
  
  /** SPA配置 */
  spa?: ComponentSpaConfig
  
  /** MPA配置 */
  mpa?: ComponentMpaConfig
  
  /** JAMstack配置 */
  jamstack?: ComponentJamstackConfig
  
  /** Headless配置 */
  headless?: ComponentHeadlessConfig
  
  /** Serverless配置 */
  serverless?: ComponentServerlessConfig
  
  /** Edge配置 */
  edge?: ComponentEdgeConfig
  
  /** Cloud配置 */
  cloud?: ComponentCloudConfig
  
  /** Container配置 */
  container?: ComponentContainerConfig
  
  /** Kubernetes配置 */
  kubernetes?: ComponentKubernetesConfig
  
  /** Docker配置 */
  docker?: ComponentDockerConfig
  
  /** CI/CD配置 */
  cicd?: ComponentCicdConfig
  
  /** DevOps配置 */
  devops?: ComponentDevopsConfig
  
  /** Git配置 */
  git?: ComponentGitConfig
  
  /** GitHub配置 */
  github?: ComponentGithubConfig
  
  /** GitLab配置 */
  gitlab?: ComponentGitlabConfig
  
  /** Bitbucket配置 */
  bitbucket?: ComponentBitbucketConfig
  
  /** Jira配置 */
  jira?: ComponentJiraConfig
  
  /** Confluence配置 */
  confluence?: ComponentConfluenceConfig
  
  /** Slack配置 */
  slack?: ComponentSlackConfig
  
  /** Teams配置 */
  teams?: ComponentTeamsConfig
  
  /** Discord配置 */
  discord?: ComponentDiscordConfig
  
  /** Zoom配置 */
  zoom?: ComponentZoomConfig
  
  /** Google Meet配置 */
  googlemeet?: ComponentGooglemeetConfig
  
  /** Microsoft Teams配置 */
  microsoftteams?: ComponentMicrosoftteamsConfig
  
  /** Webex配置 */
  webex?: ComponentWebexConfig
  
  /** Skype配置 */
  skype?: ComponentSkypeConfig
  
  /** WhatsApp配置 */
  whatsapp?: ComponentWhatsappConfig
  
  /** Telegram配置 */
  telegram?: ComponentTelegramConfig
  
  /** Signal配置 */
  signal?: ComponentSignalConfig
  
  /** Line配置 */
  line?: ComponentLineConfig
  
  /** WeChat配置 */
  wechat?: ComponentWechatConfig
  
  /** QQ配置 */
  qq?: ComponentQqConfig
  
  /** DingTalk配置 */
  dingtalk?: ComponentDingtalkConfig
  
  /** Lark配置 */
  lark?: ComponentLarkConfig
  
  /** Feishu配置 */
  feishu?: ComponentFeishuConfig
  
  /** Notion配置 */
  notion?: ComponentNotionConfig
  
  /** Airtable配置 */
  airtable?: ComponentAirtableConfig
  
  /** Coda配置 */
  coda?: ComponentCodaConfig
  
  /** Figma配置 */
  figma?: ComponentFigmaConfig
  
  /** Sketch配置 */
  sketch?: ComponentSketchConfig
  
  /** Adobe XD配置 */
  adobexd?: ComponentAdobexdConfig
  
  /** InVision配置 */
  invision?: ComponentInvisionConfig
  
  /** Marvel配置 */
  marvel?: ComponentMarvelConfig
  
  /** Framer配置 */
  framer?: ComponentFramerConfig
  
  /** Webflow配置 */
  webflow?: ComponentWebflowConfig
  
  /** Bubble配置 */
