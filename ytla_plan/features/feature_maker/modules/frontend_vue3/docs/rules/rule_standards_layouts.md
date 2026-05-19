# Layouts 代码规范

## 1 依赖限制表

| 功能域类型 | layouts可依赖此功能域 | layouts可被此功能域依赖 |
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
| composables |  |  |
| uis |  | ✓ |
| components |  | ✓ |
| layouts | ✓(非自身) |  |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.  

### 2.1 基础布局组件

```vue
<!-- layouts/[布局名].vue -->

<template>
  <div :class="[className, layoutClass]">
    <div class="header">
      <slot name="header"></slot>
    </div>
    <div class="body">
      <slot></slot>
    </div>
    <div class="footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { [布局名]Props, [布局名]Emits } from '../definitions'

defineProps<[布局名]Props>()
defineEmits<[布局名]Emits>()
</script>

<style lang="scss" scoped>
@use '../styles/[布局名]';
</style>
```

### 2.2 带状态的布局组件

```vue
<!-- layouts/[布局名].vue -->

<template>
  <div
    :class="[className, { '--expanded': isExpanded, '--collapsed': isCollapsed }]"
    :style="layoutStyle"
  >
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
import type { [布局名]Props, [布局名]Emits } from '../definitions'

defineProps<[布局名]Props>()
defineEmits<[布局名]Emits>()
</script>

<style lang="scss" scoped>
@use '../styles/[布局名]';
</style>
```

### 2.3 嵌套布局组件

```vue
<!-- layouts/[布局名].vue -->

<template>
  <div :class="className">
    <[父布局组件] :prop="value">
      <template #header>
        <slot name="header"></slot>
      </template>
      <div class="content">
        <slot></slot>
      </div>
      <template #footer>
        <slot name="footer"></slot>
      </template>
    </[父布局组件]>
  </div>
</template>

<script setup lang="ts">
import [父布局组件] from './[父布局组件].vue'
import type { [布局名]Props, [布局名]Emits } from '../definitions'

defineProps<[布局名]Props>()
defineEmits<[布局名]Emits>()
</script>

<style lang="scss" scoped>
@use '../styles/[布局名]';
</style>
```