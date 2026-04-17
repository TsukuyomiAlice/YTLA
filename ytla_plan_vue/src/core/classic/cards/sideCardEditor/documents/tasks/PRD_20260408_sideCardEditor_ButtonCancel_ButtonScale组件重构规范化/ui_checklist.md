# UI组件核对清单

## 1. 本次的UI生成形式

- **重构**：将已有的UI文件进行重构

## 2. 拟生成的UI列表

无新建UI

## 3. 需要重构的UI列表

### ButtonCancel.vue
- **重构原因**：不符合关注点分离原则，Vue文件中包含computed属性定义，composables文件中包含类型定义
- **现有的派生文件**：
  - composables/useButtonCancel.ts（包含类型定义）
  - styles/button-cancel.scss
- **重构后的派生文件**：
  - definitions/ButtonCancelType.ts（新增）
  - composables/useButtonCancel.ts（重构，移除类型定义，从definitions导入）
  - styles/button-cancel.scss
- **变动简述**：创建definitions类型定义文件，将composables中的类型定义移到definitions，将computed属性移动到composables，重构Vue文件仅保留视图，参照ButtonAction的实现方式

### ButtonScale.vue
- **重构原因**：不符合关注点分离原则，Vue文件中包含computed属性定义，composables文件中包含类型定义
- **现有的派生文件**：
  - composables/useButtonScale.ts（包含类型定义）
  - styles/button-scale.scss
- **重构后的派生文件**：
  - definitions/ButtonScaleType.ts（新增）
  - composables/useButtonScale.ts（重构，移除类型定义，从definitions导入）
  - styles/button-scale.scss
- **变动简述**：创建definitions类型定义文件，将composables中的类型定义移到definitions，将computed属性移动到composables，重构Vue文件仅保留视图，参照ButtonAction的实现方式
