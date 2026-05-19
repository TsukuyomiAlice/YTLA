# UIs 代码规范

## 1 依赖限制表

| 功能域类型 | uis可依赖此功能域 | uis可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles | ✓ |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services |  |  |
| policies |  |  |
| stores |  |  |
| composables | ✓ |  |
| uis |  |  |
| components |  | ✓ |
| layouts |  | ✓ |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.  

### 2.1 基础 UI 组件

```vue
<!-- ui/[类型][名称].vue -->

<template>
  <button
    :class="className"
    @click="handleClick"
    :aria-label="ariaLabel"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import type { [类型][名称]Props, [类型][名称]Emits } from '../definitions'

defineProps<[类型][名称]Props>()
defineEmits<[类型][名称]Emits>()
</script>

<style lang="scss" scoped>
@use '../styles/ui-[组件名]';
</style>
```

### 2.2 带状态的 UI 组件

```vue
<!-- ui/[类型][名称].vue -->

<template>
  <div
    :class="[className, { '--active': isActive, '--disabled': disabled }]"
    @click="handleClick"
  >
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
import type { [类型][名称]Props, [类型][名称]Emits } from '../definitions'

defineProps<[类型][名称]Props>()
defineEmits<[类型][名称]Emits>()
</script>

<style lang="scss" scoped>
@use '../styles/ui-[组件名]';
</style>
```

### 2.3 容器型 UI 组件

```vue
<!-- ui/[类型][名称].vue -->

<template>
  <div :class="[className, containerClass]" :style="containerStyle">
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
import type { [类型][名称]Props, [类型][名称]Emits } from '../definitions'

defineProps<[类型][名称]Props>()
defineEmits<[类型][名称]Emits>()
</script>

<style lang="scss" scoped>
@use '../styles/ui-[组件名]';
</style>
```