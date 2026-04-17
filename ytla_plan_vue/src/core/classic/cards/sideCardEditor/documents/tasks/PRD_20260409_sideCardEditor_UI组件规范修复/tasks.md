本任务进度: 未完成

# sideCardEditor UI组件规范修复 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 修复 ButtonCancel.vue 导入语句
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 移除 ButtonCancel.vue 中 useButtonCancel 导入语句的 .ts 后缀
  - 参照 ButtonAction.vue 的导入方式
- **Acceptance Criteria Addressed**: [AC-1]
- **Test Requirements**:
  - `programmatic` TR-1.1: 导入语句不包含 .ts 后缀
  - `human-judgement` TR-1.2: 与 ButtonAction.vue 的导入方式一致
- **Notes**: 保持向后兼容

## [x] Task 2: 修复 ButtonCancel.vue Props 定义
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 移除 ButtonCancel.vue 中冗余的 Props 定义
  - 直接使用 ButtonCancelProps，不进行内联扩展
  - 参照 ButtonAction.vue 的 Props 定义方式
- **Acceptance Criteria Addressed**: [AC-2]
- **Test Requirements**:
  - `programmatic` TR-2.1: 直接使用 defineProps&lt;ButtonCancelProps&gt;()
  - `programmatic` TR-2.2: 没有冗余的内联类型定义
  - `human-judgement` TR-2.3: 与 ButtonAction.vue 的定义方式一致
- **Notes**: 保持向后兼容

## [x] Task 3: 修复 ButtonCancel.vue 参数传递
- **Priority**: P0
- **Depends On**: Task 2
- **Description**: 
  - 修改 useButtonCancel 调用，只传递 props 和 emit 两个参数
  - 更新 useButtonCancel.ts 以支持 options 参数作为可选的第三个参数
  - 参照 ButtonAction.vue 的调用方式
- **Acceptance Criteria Addressed**: [AC-3]
- **Test Requirements**:
  - `programmatic` TR-3.1: useButtonCancel 只接收 props 和 emit 两个必填参数
  - `programmatic` TR-3.2: options 作为可选的第三个参数
  - `human-judgement` TR-3.3: 与 ButtonAction.vue 的调用方式一致
- **Notes**: 保持向后兼容，支持现有的 options 参数传递方式

## [x] Task 4: 移除 useButtonCancel.ts 内部接口
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 移除 useButtonCancel.ts 中的 UseButtonCancelReturn 接口定义
  - 直接返回对象，不使用显式的返回类型接口
  - 参照 useButtonAction.ts 的实现方式
- **Acceptance Criteria Addressed**: [AC-4]
- **Test Requirements**:
  - `programmatic` TR-4.1: 文件中没有 UseButtonCancelReturn 接口
  - `human-judgement` TR-4.2: 与 useButtonAction.ts 的实现方式一致
- **Notes**: 保持功能不变

## [x] Task 5: 移除 useButtonScale.ts 内部接口
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 移除 useButtonScale.ts 中的 UseButtonScaleReturn 接口定义
  - 直接返回对象，不使用显式的返回类型接口
  - 参照 useButtonAction.ts 的实现方式
- **Acceptance Criteria Addressed**: [AC-5]
- **Test Requirements**:
  - `programmatic` TR-5.1: 文件中没有 UseButtonScaleReturn 接口
  - `human-judgement` TR-5.2: 与 useButtonAction.ts 的实现方式一致
- **Notes**: 保持功能不变

## [x] Task 6: 规范 useButtonScale.ts emit 类型
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 从 definitions/ButtonScaleType.ts 导入 ButtonScaleEmits 类型
  - 使用 ButtonScaleEmits 作为 emit 参数的类型
  - 参照 useButtonAction.ts 的实现方式
- **Acceptance Criteria Addressed**: [AC-6]
- **Test Requirements**:
  - `programmatic` TR-6.1: 导入 ButtonScaleEmits 类型
  - `programmatic` TR-6.2: emit 参数使用 ButtonScaleEmits 类型
  - `human-judgement` TR-6.3: 与 useButtonAction.ts 的实现方式一致
- **Notes**: 保持功能不变

## [x] Task 7: 修复 ButtonScale.vue 样式导入
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 移除 ButtonScale.vue 样式导入中的 as * 语法
  - 参照 ButtonAction.vue 的样式导入方式
- **Acceptance Criteria Addressed**: [AC-7]
- **Test Requirements**:
  - `programmatic` TR-7.1: 样式导入不使用 as *
  - `human-judgement` TR-7.2: 与 ButtonAction.vue 的样式导入方式一致
- **Notes**: 保持样式功能不变

## [x] Task 8: 验证 TypeScript 类型检查
- **Priority**: P1
- **Depends On**: Task 1, Task 2, Task 3, Task 4, Task 5, Task 6, Task 7
- **Description**: 
  - 运行 TypeScript 编译检查
  - 确保没有类型错误
  - 验证所有导入路径正确
- **Acceptance Criteria Addressed**: [AC-8]
- **Test Requirements**:
  - `programmatic` TR-8.1: TypeScript 编译无错误
  - `programmatic` TR-8.2: 所有导入路径正确解析
  - `human-judgement` TR-8.3: 类型定义完整且正确
- **Notes**: 运行 npx tsc --noEmit 进行检查
