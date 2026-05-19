# Composables 代码规范

## 1 依赖限制表

| 功能域类型 | composables可依赖此功能域 | composables可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services |  |  |
| policies |  |  |
| stores | ✓ |  |
| composables |  |  |
| uis |  | ✓ |
| components |  | ✓ |
| layouts |  |  |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.  

### 2.1 基础组合式函数

```typescript
// composables/use[组件名].ts

import type { [组件名]Props, [组件名]Emits } from '../definitions'

export const use[组件名] = (props: [组件名]Props, emit: [组件名]Emits) => {
  const handleClick = () => {
    emit('click', props)
  }

  return {
    handleClick
  }
}
```

### 2.2 带状态管理的组合式函数

```typescript
// composables/use[组件名].ts

import { ref, computed } from 'vue'
import type { [组件名]Props, [组件名]Emits } from '../definitions'

export const use[组件名] = (props: [组件名]Props, emit: [组件名]Emits) => {
  const isActive = ref(false)
  const count = ref(0)

  const displayCount = computed(() => `Count: ${count.value}`)

  const toggleActive = () => {
    isActive.value = !isActive.value
    emit('toggle', isActive.value)
  }

  const increment = () => {
    count.value++
    emit('change', count.value)
  }

  return {
    isActive,
    count,
    displayCount,
    toggleActive,
    increment
  }
}
```

### 2.3 集成 Store 的组合式函数

```typescript
// composables/use[组件名].ts

import type { [组件名]Props, [组件名]Emits } from '../definitions'
import { use[模块名]Store } from '../stores'

export const use[组件名] = (props: [组件名]Props, emit: [组件名]Emits) => {
  const store = use[模块名]Store()

  const handleAction = async () => {
    try {
      await store.performAction(props.id)
      emit('success')
    } catch (error) {
      emit('error', error)
    }
  }

  return {
    handleAction
  }
}
```