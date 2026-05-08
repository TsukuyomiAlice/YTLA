# Scaffold Core 参数修复 - Verification Checklist

## 总体检查
- [x] 所有修改仅限于前端，未修改后端
- [x] Feature模块的功能保持不变
- [x] TypeScript类型安全

## create_card 模块检查
- [x] scaffoldCardStore.ts 的 submitForm 方法逻辑正确
- [x] 当 isCore 为 true 时，发送的 type_name 为 'classic'，structure 为用户输入值
- [x] 当 isCore 为 false 时，参数保持不变
- [x] Create_cardMain_00.vue 组件能根据选择动态显示标签
- [x] 国际化文件包含"模块名称"的翻译
- [x] 验证错误信息的文本也相应动态变化

## create_module 模块检查
- [x] scaffoldModuleStore.ts 的 submitForm 方法逻辑正确
- [x] 当 isCore 为 true 时，发送的 type_name 为 'classic'，structure 为用户输入值
- [x] 当 isCore 为 false 时，参数保持不变
- [x] Create_moduleMain_00.vue 组件能根据选择动态显示标签
- [x] 国际化文件包含"模块名称"的翻译
- [x] 验证错误信息的文本也相应动态变化

## UI/UX 检查
- [x] Core模块时显示"模块名称"
- [x] Feature模块时显示"类型名称"
- [x] 标签切换响应及时
- [x] 整体UI风格保持一致

## 最终测试
- [x] 手动测试 create_card 模块的 Core 模式
- [x] 手动测试 create_card 模块的 Feature 模式
- [x] 手动测试 create_module 模块的 Core 模式
- [x] 手动测试 create_module 模块的 Feature 模式
