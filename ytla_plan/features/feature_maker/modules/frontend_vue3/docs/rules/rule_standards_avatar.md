# Avatar 代码规范

## 1 依赖限制表

| 功能域类型 | avatar可依赖此功能域 | avatar可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions |  |  |
| styles | ✓ |  |
| utils |  |  |
| locales |  |  |
| avatar | ✓(非自身) |  |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services |  |  |
| policies |  |  |
| stores |  |  |
| composables |  |  |
| uis |  |  |
| components |  |  |
| layouts |  |  |

## 2 标准代码格式

以下内容仅供参考，不作为实际项目代码使用.

### 2.1 基础图标组件

```vue
<!-- avatar/[图标名].vue -->

<template>
  <svg
    :width="size"
    :height="size"
    :viewBox="viewBox"
    fill="none"
    :class="className"
    :style="svgStyle"
  >
    <path
      :d="pathData"
      :fill="color"
      :stroke="strokeColor"
      :stroke-width="strokeWidth"
    />
  </svg>
</template>

<script setup lang="ts">
  import { computed } from 'vue'

  interface Props {
    size?: number
    color?: string
    strokeColor?: string
    strokeWidth?: number
    className?: string
    viewBox?: string
  }

  const props = withDefaults(defineProps<Props>(), {
    size: 24,
    color: 'currentColor',
    strokeColor: 'none',
    strokeWidth: 2,
    className: '',
    viewBox: '0 0 24 24'
  })

  const pathData = 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4zm0 6c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2z'

  const svgStyle = computed(() => ({
    display: 'inline-block',
    verticalAlign: 'middle'
  }))
</script>
```

### 2.2 带状态的图标组件

```vue
<!-- avatar/[图标名]Icon.vue -->

<template>
  <svg
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    :class="[className, { 'is-active': active, 'is-disabled': disabled }]"
  >
    <defs>
      <linearGradient :id="gradientId" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" :stop-color="gradientStart" />
        <stop offset="100%" :stop-color="gradientEnd" />
      </linearGradient>
    </defs>
    <path
      :d="iconPath"
      :fill="isActive ? `url(#${gradientId})` : color"
      :stroke="strokeColor"
      :stroke-width="strokeWidth"
      :opacity="disabled ? 0.5 : 1"
    />
  </svg>
</template>

<script setup lang="ts">
  import { computed } from 'vue'

  interface Props {
    size?: number
    color?: string
    strokeColor?: string
    strokeWidth?: number
    className?: string
    active?: boolean
    disabled?: boolean
    gradientStart?: string
    gradientEnd?: string
  }

  const props = withDefaults(defineProps<Props>(), {
    size: 24,
    color: 'currentColor',
    strokeColor: 'none',
    strokeWidth: 2,
    className: '',
    active: false,
    disabled: false,
    gradientStart: '#42b983',
    gradientEnd: '#3aa876'
  })

  const gradientId = computed(() => `${props.color}-gradient-${Math.random().toString(36).substr(2, 9)}`)

  const iconPath = computed(() => {
    if (props.active) {
      return 'M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z'
    }
    return 'M21 12l-7-7-7 7 1.41 1.41L13 10.83V17h2v-6.17l4.59 4.58L21 12z'
  })
</script>

<style scoped>
  .is-active {
    transform: scale(1.1);
    transition: transform 0.2s ease;
  }

  .is-disabled {
    cursor: not-allowed;
  }
</style>
```

### 2.3 图标组合组件

```vue
<!-- avatar/IconSet.vue -->

<template>
  <div :class="className">
    <component :is="iconComponent" :size="size" :color="color" />
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue'
  import UserIcon from './UserIcon.vue'
  import SettingsIcon from './SettingsIcon.vue'
  import BellIcon from './BellIcon.vue'

  interface Props {
    name: 'user' | 'settings' | 'bell'
    size?: number
    color?: string
    className?: string
  }

  const props = withDefaults(defineProps<Props>(), {
    size: 24,
    color: 'currentColor',
    className: ''
  })

  const iconComponent = computed(() => {
    const icons: Record<string, any> = {
      user: UserIcon,
      settings: SettingsIcon,
      bell: BellIcon
    }
    return icons[props.name] || UserIcon
  })
</script>
```