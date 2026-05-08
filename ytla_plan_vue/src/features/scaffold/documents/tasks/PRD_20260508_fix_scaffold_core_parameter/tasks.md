# Scaffold Core 参数修复 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 修复 create_card 模块的 store 逻辑
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 修改 scaffoldCardStore.ts 中的 submitForm 方法
  - 当 isCore 为 true 时，将 typeName 设置为 'classic'，structure 设置为用户输入的 typeName
  - 当 isCore 为 false 时，保持现有行为
- **Acceptance Criteria Addressed**: [AC-1, AC-2]
- **Test Requirements**:
  - `programmatic` TR-1.1: 验证当 isCore 为 true 时，发送到后端的 type_name 为 'classic'，structure 为用户输入值
  - `programmatic` TR-1.2: 验证当 isCore 为 false 时，参数保持不变
- **Notes**: 确保不修改 scaffoldCardService.ts，只修改 store

## [x] Task 2: 修复 create_module 模块的 store 逻辑
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 修改 scaffoldModuleStore.ts 中的 submitForm 方法
  - 逻辑与 create_card 相同
- **Acceptance Criteria Addressed**: [AC-1, AC-2]
- **Test Requirements**:
  - `programmatic` TR-2.1: 验证当 isCore 为 true 时，发送到后端的 type_name 为 'classic'，structure 为用户输入值
  - `programmatic` TR-2.2: 验证当 isCore 为 false 时，参数保持不变
- **Notes**: 确保不修改 scaffoldModuleService.ts，只修改 store

## [x] Task 3: 动态修改 create_card 模块的 UI 标签
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 修改 Create_cardMain_00.vue 组件
  - 根据 scaffoldStore.isCore 动态显示"类型名称"或"模块名称"
  - 更新验证错误信息的文本
  - 使用国际化文本
- **Acceptance Criteria Addressed**: [AC-3, AC-4]
- **Test Requirements**:
  - `human-judgement` TR-3.1: 验证选择 Core 模块时显示"模块名称"
  - `human-judgement` TR-3.2: 验证选择 Feature 模块时显示"类型名称"

## [x] Task 4: 动态修改 create_module 模块的 UI 标签
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 修改 Create_moduleMain_00.vue 组件
  - 逻辑与 create_card 相同
- **Acceptance Criteria Addressed**: [AC-3, AC-4]
- **Test Requirements**:
  - `human-judgement` TR-4.1: 验证选择 Core 模块时显示"模块名称"
  - `human-judgement` TR-4.2: 验证选择 Feature 模块时显示"类型名称"

## [x] Task 5: 更新 create_card 模块的国际化文件
- **Priority**: P1
- **Depends On**: Task 3
- **Description**: 
  - 在 zh.json 和 en.json 中添加"模块名称"的翻译
  - 键名建议为 label_module_name
- **Acceptance Criteria Addressed**: [AC-3, AC-4]
- **Test Requirements**:
  - `human-judgement` TR-5.1: 验证中文翻译正确
  - `human-judgement` TR-5.2: 验证英文翻译正确

## [x] Task 6: 更新 create_module 模块的国际化文件
- **Priority**: P1
- **Depends On**: Task 4
- **Description**: 
  - 在 zh.json 和 en.json 中添加"模块名称"的翻译
  - 键名建议为 label_module_name
- **Acceptance Criteria Addressed**: [AC-3, AC-4]
- **Test Requirements**:
  - `human-judgement` TR-6.1: 验证中文翻译正确
  - `human-judgement` TR-6.2: 验证英文翻译正确

## [x] Task 7: 最终验证两个模块都正常工作
- **Priority**: P1
- **Depends On**: [Task 1, Task 2, Task 3, Task 4, Task 5, Task 6]
- **Description**: 
  - 手动测试两个模块的所有功能
  - 确保 Core 和 Feature 两种模式都正常工作
- **Acceptance Criteria Addressed**: [AC-5]
- **Test Requirements**:
  - `human-judgement` TR-7.1: 验证 create_card 模块正常工作
  - `human-judgement` TR-7.2: 验证 create_module 模块正常工作
