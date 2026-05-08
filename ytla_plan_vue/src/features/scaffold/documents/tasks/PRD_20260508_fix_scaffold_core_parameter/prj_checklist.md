# Scaffold Core 参数修复 - Project Design Document

## 项目概述
本文档详细记录需要修改的所有文件及其详细信息。包含对 create_card 和 create_module 两个子模块的修改。

---

## 第一部分：create_card模块需要修改的文件

### 1. stores/scaffoldCardStore.ts
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\stores\scaffoldCardStore.ts
- **用途**: 修复 submitForm 方法中的参数传递逻辑
- **修改内容**:
  - 在 submitForm 方法中，根据 isCore 的值动态设置参数
  - 如果 isCore 为 true：
    - typeName 设置为 'classic'
    - structure 设置为用户输入的 this.typeName
  - 如果 isCore 为 false：
    - 保持现有行为，structure 固定为 'cards'
- **用途说明**: 确保向发送后端的参数符合正确的逻辑

---

### 2. components/Create_cardMain_00.vue
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\components\Create_cardMain_00.vue
- **用途**: 根据 isCore 动态显示标签
- **修改内容**:
  - 将硬编码的"类型名称"替换为动态计算的标签
  - 使用 computed 属性根据 scaffoldStore.isCore 判断显示什么
  - Core模块时显示"模块名称"，Feature模块时显示"类型名称"
  - 修改验证错误信息的文本也相应动态变化
- **用途说明**: 提供更好的用户体验，标签与实际功能对应

---

### 3. locales/zh.json
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\locales\zh.json
- **用途**: 添加中文翻译
- **修改内容**:
  - 添加新键 "label_module_name": "模块名称"
  - 添加新键 "validation_module_name_required": "请输入模块名称"
- **用途说明**: 支持中文界面

---

### 4. locales/en.json
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_card\locales\en.json
- **用途**: 添加英文翻译
- **修改内容**:
  - 添加新键 "label_module_name": "Module Name"
  - 添加新键 "validation_module_name_required": "Please enter module name"
- **用途说明**: 支持英文界面

---

## 第二部分：create_module模块需要修改的文件

### 5. stores/scaffoldModuleStore.ts
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\stores\scaffoldModuleStore.ts
- **用途**: 修复 submitForm 方法中的参数传递逻辑
- **修改内容**:
  - 在 submitForm 方法中，根据 isCore 的值动态设置参数
  - 如果 isCore 为 true：
    - typeName 设置为 'classic'
    - structure 设置为用户输入的 this.typeName
  - 如果 isCore 为 false：
    - 保持现有行为，structure 固定为 'modules'
- **用途说明**: 确保向发送后端的参数符合正确的逻辑

---

### 6. components/Create_moduleMain_00.vue
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\components\Create_moduleMain_00.vue
- **用途**: 根据 isCore 动态显示标签
- **修改内容**:
  - 将硬编码的"类型名称"替换为动态计算的标签
  - 使用 computed 属性根据 scaffoldStore.isCore 判断显示什么
  - Core模块时显示"模块名称"，Feature模块时显示"类型名称"
  - 修改验证错误信息的文本也相应动态变化
- **用途说明**: 提供更好的用户体验，标签与实际功能对应

---

### 7. locales/zh.json
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\locales\zh.json
- **用途**: 添加中文翻译
- **修改内容**:
  - 添加新键 "label_module_name": "模块名称"
  - 添加新键 "validation_module_name_required": "请输入模块名称"
- **用途说明**: 支持中文界面

---

### 8. locales/en.json
- **修改位置**: d:\YTLA\ytla_plan_vue\src\features\scaffold\modules\create_module\locales\en.json
- **用途**: 添加英文翻译
- **修改内容**:
  - 添加新键 "label_module_name": "Module Name"
  - 添加新键 "validation_module_name_required": "Please enter module name"
- **用途说明**: 支持英文界面

---

## 修改总结

### create_card模块：
- 修改文件：4个
  - stores/scaffoldCardStore.ts
  - components/Create_cardMain_00.vue
  - locales/zh.json
  - locales/en.json

### create_module模块：
- 修改文件：4个
  - stores/scaffoldModuleStore.ts
  - components/Create_moduleMain_00.vue
  - locales/zh.json
  - locales/en.json

### 总计：
- 修改文件：8个
- 不新增任何文件
- 不修改后端代码
