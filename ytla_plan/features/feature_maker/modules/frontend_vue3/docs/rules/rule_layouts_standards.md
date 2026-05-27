# 布局组件层规范文档 - 代码示例 (rule_layouts_standards.md)

## 概述

本文档专注于提供 `layouts` 目录下布局组件的编写规范和代码示例。

## 职责说明

`layouts` 目录负责：
- 定义页面整体布局结构
- 提供通用布局区块
- 组织页面组件排列

## 命名规范

### 布局类型
- **Container**: 容器布局
- **Area**: 区域布局
- **Column**: 栏目标布局

### 文件命名
- **规则**：文件名使用 PascalCase，以 `Layout` 后缀结尾
- **示例**：`ContainerLayout.vue`, `SidebarLayout.vue`, `TwoColumnLayout.vue`

## 代码模板与示例

### 基础容器布局

```vue
<!-- layouts/ContainerLayout.vue -->

<template>
  <div class="container-layout">
    <header v-if="$slots.header" class="header">
      <slot name="header" />
    </header>
    
    <main class="main-content">
      <slot />
    </main>
    
    <footer v-if="$slots.footer" class="footer">
      <slot name="footer" />
    </footer>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  maxWidth?: string;
  padding?: string;
}>();
</script>

<style scoped lang="scss">
.container-layout {
  max-width: v-bind('maxWidth || 1200px');
  margin: 0 auto;
  padding: v-bind('padding || 16px');
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
}
</style>
```

### 侧边栏布局

```vue
<!-- layouts/SidebarLayout.vue -->

<template>
  <div class="sidebar-layout">
    <aside class="sidebar" :class="{ '--collapsed': isCollapsed }">
      <slot name="sidebar" />
    </aside>
    
    <div class="content">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

defineProps<{
  sidebarWidth?: string;
  collapsedWidth?: string;
}>();

const isCollapsed = ref(false);

function toggleSidebar() {
  isCollapsed.value = !isCollapsed.value;
}

defineExpose({ toggleSidebar, isCollapsed });
</script>

<style scoped lang="scss">
.sidebar-layout {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: v-bind('sidebarWidth || 250px');
  transition: width 0.3s ease;
  flex-shrink: 0;
  
  &.--collapsed {
    width: v-bind('collapsedWidth || 60px');
  }
}

.content {
  flex: 1;
  overflow-y: auto;
}
</style>
```

### 两栏布局

```vue
<!-- layouts/TwoColumnLayout.vue -->

<template>
  <div class="two-column-layout">
    <div class="column column--left">
      <slot name="left" />
    </div>
    
    <div class="column column--right">
      <slot name="right" />
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  leftWidth?: string;
  gap?: string;
}>();
</script>

<style scoped lang="scss">
.two-column-layout {
  display: grid;
  grid-template-columns: v-bind('leftWidth || 300px') 1fr;
  gap: v-bind('gap || 24px');
}

.column {
  &--left {
    flex-shrink: 0;
  }
}
</style>
```

### 三栏布局

```vue
<!-- layouts/ThreeColumnLayout.vue -->

<template>
  <div class="three-column-layout">
    <div class="column column--left">
      <slot name="left" />
    </div>
    
    <div class="column column--center">
      <slot />
    </div>
    
    <div class="column column--right">
      <slot name="right" />
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  leftWidth?: string;
  rightWidth?: string;
  gap?: string;
}>();
</script>

<style scoped lang="scss">
.three-column-layout {
  display: grid;
  grid-template-columns: 
    v-bind('leftWidth || 200px') 
    1fr 
    v-bind('rightWidth || 200px');
  gap: v-bind('gap || 16px');
}
</style>
```

## 依赖限制

### 允许的依赖
- ✅ `components` - 业务组件
- ✅ `ui` - UI 元件
- ✅ `composables` - 组合式函数
- ✅ `definitions` - 类型定义

### 禁止的依赖
- ❌ `stores` - 状态管理（应通过 composables 访问）

## 设计原则

### 布局与内容分离
- 布局组件不包含业务逻辑
- 通过 slots 提供内容插入点

### 响应式设计
- 支持不同屏幕尺寸
- 使用弹性布局

### 可配置性
- 通过 props 配置布局参数
- 提供合理的默认值

### 可复用性
- 提取通用布局模式
- 支持多种配置组合

## 错误模式

### 反模式 1：布局中包含业务逻辑
```vue
<!-- ❌ 错误 -->
<script setup lang="ts">
// 不应该在布局中处理业务逻辑
const user = ref(null);
async function fetchUser() {
  user.value = await api.getUser();
}
</script>

<!-- ✅ 正确 -->
<script setup lang="ts">
// 布局只提供结构，内容通过 slots 传入
defineProps<{ title?: string }>();
</script>
```

### 反模式 2：固定尺寸布局
```vue
<!-- ❌ 错误 -->
<style>
.sidebar { width: 250px; }
</style>

<!-- ✅ 正确 -->
<style>
.sidebar { width: var(--sidebar-width, 250px); }
</style>
```

### 反模式 3：嵌套过深
```vue
<!-- ❌ 错误 - 布局嵌套过多 -->
<ContainerLayout>
  <SidebarLayout>
    <TwoColumnLayout>
      <!-- 内容 -->
    </TwoColumnLayout>
  </SidebarLayout>
</ContainerLayout>

<!-- ✅ 正确 - 使用组合布局 -->
<MainLayout>
  <!-- 内容 -->
</MainLayout>
```

## 验证清单

- [ ] 文件以 `Layout` 后缀结尾
- [ ] 使用 slots 提供内容插入点
- [ ] 不包含业务逻辑
- [ ] 支持响应式设计
- [ ] 通过 props 配置
- [ ] 使用弹性布局
- [ ] 不直接访问 stores
- [ ] 样式使用 scoped

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目布局组件层规范
- 文件位置：rule_layouts_standards.md