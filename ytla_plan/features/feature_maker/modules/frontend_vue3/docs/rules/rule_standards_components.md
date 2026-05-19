# Components 代码规范

## 1 依赖限制表

| 功能域类型 | components可依赖此功能域 | components可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles | ✓ |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  | ✓ |
| services |  |  |
| policies |  |  |
| stores |  |  |
| composables | ✓ |  |
| uis | ✓ |  |
| components |  |  |
| layouts | ✓ |  |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.  

### 2.1 基础组件

```vue
<!-- components/[组件名].vue -->

<template>
  <div :class="className">
    <[UI组件1] :prop1="value1" :prop2="value2" />
    <[UI组件2] :prop="value" @event="handleEvent" />
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
import [UI组件1] from '../ui/[UI组件1].vue'
import [UI组件2] from '../ui/[UI组件2].vue'

import type { [组件名]Props, [组件名]Emits } from '../definitions'

const props = defineProps<[组件名]Props>()
const emit = defineEmits<[组件名]Emits>()

import { use[组件名] } from '../composables'

const { value1, value2, handleEvent } = use[组件名](props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/[组件名]';
</style>
```

### 2.2 带布局的组件

```vue
<!-- components/[组件名].vue -->

<template>
  <[布局组件]>
    <[UI组件1] :prop="value1" />
    <div class="content">
      <slot name="content"></slot>
    </div>
    <[UI组件2] @action="handleAction" />
  </[布局组件]>
</template>

<script setup lang="ts">
import [布局组件] from '../layouts/[布局组件].vue'
import [UI组件1] from '../ui/[UI组件1].vue'
import [UI组件2] from '../ui/[UI组件2].vue'

import type { [组件名]Props, [组件名]Emits } from '../definitions'

const props = defineProps<[组件名]Props>()
const emit = defineEmits<[组件名]Emits>()

import { use[组件名] } from '../composables'

const { value1, handleAction } = use[组件名](props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/[组件名]';
</style>
```