# UI组件检查清单

## 本次的UI生成形式
- **重构**：将已有的UI文件进行重构

## 拟生成的UI列表

### ButtonAdd.vue → ButtonAdd.vue（重构）
- **生成原因**：现有ButtonAdd.vue不符合UI组件规范，需要实现关注点分离
- **用途**：用于添加卡片的按钮组件
- **包含的派生文件**：
  - composables/useButtonAdd.ts（新建）
  - styles/button-add.scss（新建）
  - definitions/ButtonAddType.ts（可选，待确定）

## 需要重构的UI列表

### ButtonAdd.vue
- **重构原因**：不符合关注点分离原则，Vue文件中包含了逻辑代码，需要移动到composables文件
- **现有的派生文件**：
  - styles/side-card-controller.scss（现有共用样式）
- **重构后的派生文件**：
  - composables/useButtonAdd.ts
  - styles/button-add.scss
  - definitions/ButtonAddType.ts（可选）
- **变动简述**：将ButtonAdd.vue中的逻辑代码移动到useButtonAdd.ts，将样式代码移动到button-add.scss，Vue文件仅保留视图、导入语句和样式导入
