# UI组件检查清单

## 1. 本次的UI生成形式

- **重构**：将已有的UI文件进行重构，实现关注点分离

## 2. 拟重构的UI列表

### BarTitle.vue
- **重构原因**：当前组件直接从父组件接收方法作为props，未从composable正确解构，未完全实现关注点分离
- **用途**：显示和编辑侧边卡片标题
- **现有的派生文件**：
  - composables/useBarTitle.ts
  - styles/ui-text.scss
  - styles/side-card.scss
- **重构后的派生文件**：
  - composables/useBarTitle.ts（保持不变，调整使用方式）
  - styles/ui-text.scss
  - styles/side-card.scss
- **变动简述**：修改BarTitle.vue，从useBarTitle composable正确解构数据和方法，简化props定义

### ButtonPin.vue
- **重构原因**：当前组件直接从父组件接收方法作为props，未从composable正确解构，未完全实现关注点分离
- **用途**：固定/取消固定侧边卡片
- **现有的派生文件**：
  - composables/useButtonPin.ts
  - styles/ui-button.scss
  - styles/button-pin.scss
- **重构后的派生文件**：
  - composables/useButtonPin.ts（保持不变，调整使用方式）
  - styles/ui-button.scss
  - styles/button-pin.scss
- **变动简述**：修改ButtonPin.vue，从useButtonPin composable正确解构数据和方法，简化props定义

### ContainerIcon.vue
- **重构原因**：当前组件直接从父组件接收方法作为props，未从composable正确解构，未完全实现关注点分离
- **用途**：显示和移除侧边卡片图标
- **现有的派生文件**：
  - composables/useContainerIcon.ts
  - composables/useButtonChangeIcon.ts
  - styles/ui-icon.scss
- **重构后的派生文件**：
  - composables/useContainerIcon.ts（保持不变，调整使用方式）
  - composables/useButtonChangeIcon.ts
  - styles/ui-icon.scss
- **变动简述**：修改ContainerIcon.vue，从useContainerIcon composable正确解构数据和方法，简化props定义

### ButtonExpand.vue
- **重构原因**：当前组件直接从父组件接收方法作为props，未从composable正确解构，未完全实现关注点分离
- **用途**：展开/收起侧边卡片
- **现有的派生文件**：
  - composables/useButtonExpand.ts
  - styles/button-expand.scss
- **重构后的派生文件**：
  - composables/useButtonExpand.ts（保持不变，调整使用方式）
  - styles/button-expand.scss
- **变动简述**：修改ButtonExpand.vue，从useButtonExpand composable正确解构数据和方法，简化props定义

### BarDescription.vue
- **重构原因**：需要检查并确保实现关注点分离
- **用途**：显示侧边卡片描述
- **现有的派生文件**：
  - composables/useBarDescription.ts
  - styles/ui-text.scss
- **重构后的派生文件**：
  - composables/useBarDescription.ts
  - styles/ui-text.scss
- **变动简述**：检查并重构BarDescription.vue，确保从composable正确解构数据和方法

### ButtonChangeBackground.vue
- **重构原因**：需要检查并确保实现关注点分离
- **用途**：更改侧边卡片背景
- **现有的派生文件**：
  - composables/useButtonChangeBackground.ts
  - styles/ui-button.scss
- **重构后的派生文件**：
  - composables/useButtonChangeBackground.ts
  - styles/ui-button.scss
- **变动简述**：检查并重构ButtonChangeBackground.vue，确保从composable正确解构数据和方法

### ButtonChangeIcon.vue
- **重构原因**：需要检查并确保实现关注点分离
- **用途**：更改侧边卡片图标
- **现有的派生文件**：
  - composables/useButtonChangeIcon.ts
  - styles/ui-button.scss
- **重构后的派生文件**：
  - composables/useButtonChangeIcon.ts
  - styles/ui-button.scss
- **变动简述**：检查并重构ButtonChangeIcon.vue，确保从composable正确解构数据和方法

### ButtonClose.vue
- **重构原因**：需要检查并确保实现关注点分离
- **用途**：关闭侧边卡片
- **现有的派生文件**：
  - composables/useButtonClose.ts
  - styles/ui-button.scss
- **重构后的派生文件**：
  - composables/useButtonClose.ts
  - styles/ui-button.scss
- **变动简述**：检查并重构ButtonClose.vue，确保从composable正确解构数据和方法

### ButtonDeactivate.vue
- **重构原因**：需要检查并确保实现关注点分离
- **用途**：停用侧边卡片
- **现有的派生文件**：
  - composables/useButtonDeactivate.ts
  - styles/ui-button.scss
- **重构后的派生文件**：
  - composables/useButtonDeactivate.ts
  - styles/ui-button.scss
- **变动简述**：检查并重构ButtonDeactivate.vue，确保从composable正确解构数据和方法

### ButtonEdit.vue
- **重构原因**：需要检查并确保实现关注点分离
- **用途**：编辑侧边卡片
- **现有的派生文件**：
  - composables/useButtonEdit.ts
  - styles/ui-button.scss
- **重构后的派生文件**：
  - composables/useButtonEdit.ts
  - styles/ui-button.scss
- **变动简述**：检查并重构ButtonEdit.vue，确保从composable正确解构数据和方法

### ContainerTags.vue
- **重构原因**：需要检查并确保实现关注点分离
- **用途**：显示侧边卡片标签
- **现有的派生文件**：
  - composables/useContainerTags.ts
  - styles/container-tags.scss
- **重构后的派生文件**：
  - composables/useContainerTags.ts
  - styles/container-tags.scss
- **变动简述**：检查并重构ContainerTags.vue，确保从composable正确解构数据和方法
