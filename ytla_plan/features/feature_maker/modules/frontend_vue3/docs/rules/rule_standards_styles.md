# Styles 代码规范

## 1 依赖限制表

| 功能域类型 | styles可依赖此功能域 | styles可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions |  |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  | ✓ |
| factories |  |  |
| flows |  |  |
| registries |  |  |
| services |  |  |
| policies |  |  |
| stores |  |  |
| composables |  |  |
| uis |  | ✓ |
| components |  | ✓ |
| layouts |  | ✓ |

## 2 标准代码格式

---  

以下内容仅供参考，不作为实际项目代码使用.

---  

### 2.1 组件样式文件

```scss
// styles/[组件名-kebab-case].scss

// ============================================================================
// 组件样式规范
// 1. 定义 CSS 自定义属性（主题变量）
// 2. 定义基础样式类（BEM Block）
// 3. 定义状态修饰类（BEM Modifier）
// 4. 定义子元素样式（BEM Element）
// 5. 定义动画效果
// 6. 定义响应式设计
// ============================================================================

// CSS 自定义属性 - 便于主题切换和动态修改
.component-name {
  // 颜色变量
  --bg-color: #ffffff;
  --text-color: #1f2937;
  --border-color: #e5e7eb;

  // 间距变量
  --padding: 16px;
  --margin: 8px;

  // 尺寸变量
  --border-radius: 8px;

  // 过渡变量
  --transition-duration: 0.3s;

  // 基础样式（BEM Block）
  background-color: var(--bg-color);
  color: var(--text-color);
  border: 1px solid var(--border-color);
  padding: var(--padding);
  border-radius: var(--border-radius);
  transition: all var(--transition-duration) ease;

  // 状态修饰类（BEM Modifier）
  &--primary {
    --bg-color: #42b983;
    --text-color: #ffffff;
    --border-color: #42b983;
  }

  &--secondary {
    --bg-color: #f3f4f6;
    --text-color: #374151;
    --border-color: #d1d5db;
  }

  &--disabled {
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
  }

  &--hover:hover {
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  }

  // 尺寸修饰类
  &--small {
    --padding: 8px;
    font-size: 0.875rem;
  }

  &--large {
    --padding: 24px;
    font-size: 1.125rem;
  }

  // 子元素样式（BEM Element）
  &__title {
    font-size: 1.125rem;
    font-weight: 600;
    margin-bottom: 8px;
  }

  &__content {
    font-size: 0.875rem;
    line-height: 1.5;
  }

  &__actions {
    display: flex;
    gap: 8px;
    margin-top: 12px;
  }
}
```

### 2.2 主题变量文件

```scss
// styles/variables.scss

// ============================================================================
// 主题变量规范
// 1. 颜色系统（主题色、中性色、状态色）
// 2. 间距系统（xs, sm, md, lg, xl）
// 3. 字体系统（字体系列、字号、字重）
// 4. 圆角系统
// 5. 阴影系统
// 6. 过渡系统
// ============================================================================

// 主题色
$primary-color: #42b983;
$primary-dark: #3aa876;
$primary-light: #57c996;

$secondary-color: #646cff;
$accent-color: #f59e0b;

// 状态色
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

// 过渡系统
$transition-fast: 150ms ease;
$transition-normal: 300ms ease;
$transition-slow: 500ms ease;
```

### 2.3 混合宏文件

```scss
// styles/mixins.scss

// ============================================================================
// 混合宏规范
// 1. 响应式断点
// 2. 弹性布局
// 3. 定位辅助
// 4. 文本处理
// ============================================================================

// 响应式断点
@mixin breakpoint($size) {
  @if $size == sm {
    @media (min-width: 640px) {
      @content;
    }
  } @else if $size == md {
    @media (min-width: 768px) {
      @content;
    }
  } @else if $size == lg {
    @media (min-width: 1024px) {
      @content;
    }
  } @else if $size == xl {
    @media (min-width: 1280px) {
      @content;
    }
  }
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

// 定位辅助
@mixin absolute-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

// 文本处理
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
```