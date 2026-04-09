# UI组件检查清单（修正版）

## 1. 本次的UI生成形式

- **重构**：将已有的UI文件进行重构，使其符合规范

## 2. 拟生成的UI列表

### ButtonFilterClear.vue
- **生成原因**：原 ButtonClear.vue 命名不符合规范，需要重命名
- **用途**：用于清除筛选器输入的按钮
- **包含的派生文件**：
  - composables/useButtonFilterClear.ts
  - styles/button-filter-clear.scss
  - definitions/ButtonFilterClearType.ts（可选）

### BarFilterInput.vue
- **生成原因**：原 FilterInput.vue 命名不符合规范（Input不是预定义元件类型），需要重命名为BarFilterInput
- **用途**：用于输入筛选关键词的输入框
- **包含的派生文件**：
  - composables/useBarFilterInput.ts
  - styles/bar-filter-input.scss
  - definitions/BarFilterInputType.ts（可选）

## 3. 需要重构的UI列表

### ButtonClear.vue
- **重构原因**：命名不符合规范，需要改为ButtonFilterClear.vue；UI组件中使用了i18n，违反关注点分离原则
- **现有的派生文件**：无专门的composables和styles文件
- **重构后的派生文件**：
  - composables/useButtonFilterClear.ts
  - styles/button-filter-clear.scss
- **变动简述**：重命名文件，调整内部引用，移除i18n使用，添加composables

### FilterInput.vue
- **重构原因**：命名不符合规范（Input不是预定义元件类型），需要改为BarFilterInput.vue；UI组件中使用了i18n，违反关注点分离原则
- **现有的派生文件**：无专门的composables和styles文件
- **重构后的派生文件**：
  - composables/useBarFilterInput.ts
  - styles/bar-filter-input.scss
- **变动简述**：重命名文件，调整内部引用，移除i18n使用，添加composables

## 注意：以下内容超出UI组件规范范围，不进行重构

- layouts/SideCardFilter.vue（布局文件）
- composables/useSideCardFilter.ts（主组件的composable）
- definitions/sideCardFilterType.ts（主组件的类型定义）
