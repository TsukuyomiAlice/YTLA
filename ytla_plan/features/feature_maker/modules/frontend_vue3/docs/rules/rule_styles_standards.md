# 样式层规范文档 - 代码示例 (rule_styles_standards.md)

## 概述

本文档专注于提供 `styles` 目录下 SCSS 样式文件的编写规范和代码示例。核心原则：**Vue 文件中不应包含任何样式代码，所有样式必须提取到 `styles` 目录下的 SCSS 文件中**。

## 职责说明

`styles` 目录负责：
- 定义组件的样式规则
- 管理主题变量和混合宏
- 提供响应式设计支持
- 实现 CSS 动画和过渡效果

## 命名规范

### 文件命名
- **规则**：文件名使用 kebab-case
- **示例**：`button-submit.scss`, `user-card.scss`, `layout-main.scss`

### 类命名
- **规则**：使用 BEM 命名规范
- **块（Block）**：`.component-name`
- **元素（Element）**：`.component-name__element`
- **修饰符（Modifier）**：`.component-name--modifier`

### 变量命名
- **规则**：使用 kebab-case，以 `$` 前缀开头
- **示例**：`$primary-color`, `$spacing-sm`, `$font-size-base`

## 代码模板与示例

### 基础样式文件

```scss
// styles/user-card.scss

// ============================================================================
// 组件样式规范
// ============================================================================
// 1. 定义 CSS 自定义属性
// 2. 定义基础样式类
// 3. 定义状态修饰类
// 4. 定义子元素样式
// 5. 定义响应式设计
// ============================================================================

// CSS 自定义属性
.user-card {
  --card-bg-color: #ffffff;
  --card-border-color: #e5e7eb;
  --card-padding: 16px;
  --card-border-radius: 8px;

  // 基础样式
  background-color: var(--card-bg-color);
  border: 1px solid var(--card-border-color);
  padding: var(--card-padding);
  border-radius: var(--card-border-radius);
  transition: all 0.3s ease;

  // 状态修饰类
  &--hover:hover {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  }

  &--disabled {
    opacity: 0.5;
    pointer-events: none;
  }

  // 尺寸修饰类
  &--small {
    padding: 8px;
    font-size: 0.875rem;
  }

  &--large {
    padding: 24px;
    font-size: 1.125rem;
  }

  // 子元素样式
  &__avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    object-fit: cover;
  }

  &__name {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 4px;
  }

  &__email {
    font-size: 0.875rem;
    color: #6b7280;
  }

  &__actions {
    display: flex;
    gap: 8px;
    margin-top: 12px;
  }
}
```

### 主题变量文件

```scss
// styles/variables.scss

// 颜色系统
$primary-color: #42b983;
$primary-dark: #3aa876;
$primary-light: #57c996;

$secondary-color: #646cff;
$accent-color: #f59e0b;

$success-color: #10b981;
$warning-color: #f59e0b;
$error-color: #ef4444;
$info-color: #3b82f6;

// 中性色
$text-primary: #1f2937;
$text-secondary: #6b7280;
$text-muted: #9ca3af;

$bg-primary: #ffffff;
$bg-secondary: #f3f4f6;
$bg-tertiary: #e5e7eb;

$border-color: #d1d5db;
$border-light: #e5e7eb;

// 间距系统
$spacing-xs: 4px;
$spacing-sm: 8px;
$spacing-md: 16px;
$spacing-lg: 24px;
$spacing-xl: 32px;
$spacing-2xl: 48px;

// 字体系统
$font-family-sans: 'Inter', system-ui, -apple-system, sans-serif;
$font-family-mono: 'JetBrains Mono', monospace;

$font-size-xs: 0.75rem;
$font-size-sm: 0.875rem;
$font-size-base: 1rem;
$font-size-lg: 1.125rem;
$font-size-xl: 1.25rem;
$font-size-2xl: 1.5rem;
$font-size-3xl: 1.875rem;

$font-weight-normal: 400;
$font-weight-medium: 500;
$font-weight-semibold: 600;
$font-weight-bold: 700;

// 圆角系统
$radius-sm: 4px;
$radius-md: 6px;
$radius-lg: 8px;
$radius-xl: 12px;
$radius-full: 9999px;

// 阴影系统
$shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
$shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
$shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
$shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

// 过渡系统
$transition-fast: 150ms ease;
$transition-normal: 300ms ease;
$transition-slow: 500ms ease;
```

### 混合宏文件

```scss
// styles/mixins.scss

// 按钮重置样式
@mixin button-reset {
  border: none;
  background: none;
  padding: 0;
  margin: 0;
  font: inherit;
  cursor: pointer;
  outline: none;
  appearance: none;
}

// 弹性布局
@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

@mixin flex-between {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

@mixin flex-col {
  display: flex;
  flex-direction: column;
}

// 响应式断点
$breakpoint-sm: 640px;
$breakpoint-md: 768px;
$breakpoint-lg: 1024px;
$breakpoint-xl: 1280px;

@mixin responsive($breakpoint) {
  @media (min-width: $breakpoint) {
    @content;
  }
}

@mixin sm {
  @include responsive($breakpoint-sm) {
    @content;
  }
}

@mixin md {
  @include responsive($breakpoint-md) {
    @content;
  }
}

@mixin lg {
  @include responsive($breakpoint-lg) {
    @content;
  }
}

@mixin xl {
  @include responsive($breakpoint-xl) {
    @content;
  }
}

// 文本截断
@mixin truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@mixin line-clamp($lines: 2) {
  display: -webkit-box;
  -webkit-line-clamp: $lines;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

// 动画
@mixin fade-in {
  animation: fadeIn 0.3s ease forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@mixin slide-up {
  animation: slideUp 0.3s ease forwards;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### Vue 组件导入样式

```vue
<!-- components/UserCard.vue -->
<script setup lang="ts">
import type { IUserCardProps } from '../definitions/user-card';
defineProps<IUserCardProps>();
</script>

<template>
  <div class="user-card">
    <img class="user-card__avatar" :src="user.avatar" :alt="user.name" />
    <div>
      <h3 class="user-card__name">{{ user.name }}</h3>
      <p class="user-card__email">{{ user.email }}</p>
    </div>
    <div class="user-card__actions">
      <button class="btn btn--primary">Edit</button>
      <button class="btn btn--danger">Delete</button>
    </div>
  </div>
</template>

<style scoped lang="scss">
// ✅ 仅导入样式文件，不编写具体样式代码
@use '../styles/user-card';
@use '../styles/buttons';
</style>
```

## 样式导入规范

### 导入顺序
```scss
// styles/user-card.scss

// 1. 第三方库导入
@use 'normalize.css';

// 2. 全局变量和混合宏
@use '../variables' as *;
@use '../mixins';

// 3. 基础样式
@use '../base/reset';
@use '../base/typography';

// 4. 同模块样式
@use './buttons';
@use './icons';
```

### Vue 文件导入
```vue
<style scoped lang="scss">
// 仅导入样式文件，不编写具体样式
@use '../styles/user-card';
@use '../styles/buttons';
</style>
```

## 设计原则

### 关注点分离
- Vue 文件中**不应该**包含任何样式代码
- 所有样式必须在 `styles` 目录下的 SCSS 文件中定义
- 使用 `@use` 导入样式文件

### 可维护性
- 使用 CSS 自定义属性实现主题切换
- 使用变量管理颜色、间距、字体等
- 使用混合宏复用样式逻辑

### 响应式设计
- 使用响应式断点系统
- 移动端优先设计
- 使用弹性布局

### 性能优化
- 避免深度选择器
- 使用 CSS 自定义属性减少重复代码
- 按需导入样式模块

## 错误模式

### 反模式 1：Vue 文件中编写样式
```vue
<!-- ❌ 错误 -->
<style scoped>
.user-card {
  padding: 16px;
  border: 1px solid #eee;
}
</style>

<!-- ✅ 正确 -->
<style scoped lang="scss">
@use '../styles/user-card';
</style>
```

### 反模式 2：使用 @import 而非 @use
```scss
// ❌ 错误
@import '../variables.scss';

// ✅ 正确
@use '../variables' as *;
```

### 反模式 3：硬编码值
```scss
// ❌ 错误
.user-card {
  padding: 16px;
  color: #42b983;
}

// ✅ 正确
.user-card {
  padding: $spacing-md;
  color: $primary-color;
}
```

## 验证清单

- [ ] Vue 文件中不包含任何样式代码
- [ ] 使用 `@use` 导入样式文件
- [ ] 使用 BEM 命名规范
- [ ] 使用变量定义颜色、间距等
- [ ] 使用混合宏复用样式
- [ ] 响应式设计使用断点系统
- [ ] 文件命名使用 kebab-case
- [ ] 没有深度选择器

---

**文档信息**
- 生成时间：2026年5月18日
- 适用场景：YTLA项目样式层规范
- 文件位置：rule_styles_standards.md