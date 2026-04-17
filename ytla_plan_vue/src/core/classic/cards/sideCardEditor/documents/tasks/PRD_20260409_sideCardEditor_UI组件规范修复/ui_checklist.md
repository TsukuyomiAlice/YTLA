# UI组件核对清单

## 1. 本次的UI生成形式

- **重构**：将已有的UI文件进行规范修复

## 2. 拟生成的UI列表

无新建UI

## 3. 需要重构的UI列表

### ButtonCancel.vue
- **重构原因**：导入语句有.ts后缀，Props定义不规范，参数传递过多
- **现有的派生文件**：
  - composables/useButtonCancel.ts
  - definitions/ButtonCancelType.ts
  - styles/button-cancel.scss
- **重构后的派生文件**：
  - composables/useButtonCancel.ts（重构，移除内部接口，调整参数）
  - definitions/ButtonCancelType.ts（保持不变）
  - styles/button-cancel.scss（保持不变）
- **变动简述**：修复导入语句，修复Props定义，调整参数传递，移除composables中的内部接口

### ButtonScale.vue
- **重构原因**：样式导入使用了as *，composables包含内部接口定义，emit类型不规范
- **现有的派生文件**：
  - composables/useButtonScale.ts
  - definitions/ButtonScaleType.ts
  - styles/button-scale.scss
- **重构后的派生文件**：
  - composables/useButtonScale.ts（重构，移除内部接口，规范emit类型）
  - definitions/ButtonScaleType.ts（保持不变）
  - styles/button-scale.scss（保持不变）
- **变动简述**：修复样式导入，移除composables中的内部接口，规范emit类型定义
