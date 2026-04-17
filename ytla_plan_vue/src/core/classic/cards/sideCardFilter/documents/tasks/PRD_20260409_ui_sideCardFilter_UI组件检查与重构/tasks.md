本任务进度: 已完成

# SideCardFilter UI组件重构 - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 创建 ButtonFilterClear 组件及其配套文件
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 创建 ui/ButtonFilterClear.vue 组件
  - 创建 composables/useButtonFilterClear.ts
  - 创建 styles/button-filter-clear.scss
  - 移除i18n使用，通过props接收文本
- **Acceptance Criteria Addressed**: [AC-1, AC-2, AC-3]
- **Test Requirements**:
  - `programmatic` TR-1.1: ButtonFilterClear.vue 文件存在
  - `programmatic` TR-1.2: useButtonFilterClear.ts 文件存在
  - `programmatic` TR-1.3: button-filter-clear.scss 文件存在
  - `programmatic` TR-1.4: 组件通过props接收文本，不直接使用 $t()
- **Notes**: 组件命名符合"元件类型+功能描述"规范

## [x] Task 2: 创建 BarFilterInput 组件及其配套文件
- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 创建 ui/BarFilterInput.vue 组件
  - 创建 composables/useBarFilterInput.ts
  - 创建 styles/bar-filter-input.scss
  - 移除i18n使用，通过props接收placeholder
- **Acceptance Criteria Addressed": [AC-1, AC-2, AC-3]
- **Test Requirements":
  - `programmatic` TR-2.1: BarFilterInput.vue 文件存在
  - `programmatic` TR-2.2: useBarFilterInput.ts 文件存在
  - `programmatic` TR-2.3: bar-filter-input.scss 文件存在
  - `programmatic` TR-2.4: 组件通过props接收placeholder，不直接使用 $t()
- **Notes": 使用Bar作为元件类型，而非Input

## [x] Task 3: 完善样式文件
- **Priority**: P1
- **Depends On": Task 1, Task 2
- **Description": 
  - 完善 styles/side-card-filter.scss
  - 确保所有组件都有对应的样式
  - 保持样式的一致性
- **Acceptance Criteria Addressed": [AC-4]
- **Test Requirements":
  - `human-judgement` TR-3.1: 样式文件包含所有必要的样式定义
  - `human-judgement` TR-3.2: 样式使用BEM命名规范
- **Notes": 参考项目其他模块的样式风格

## [x] Task 4: 删除旧的UI组件文件
- **Priority": P2
- **Depends On": Task 1, Task 2
- **Description": 
  - 删除 ui/ButtonClear.vue
  - 删除 ui/FilterInput.vue
- **Acceptance Criteria Addressed": [AC-1]
- **Test Requirements":
  - `programmatic` TR-4.1: ButtonClear.vue 文件不存在
  - `programmatic` TR-4.2: FilterInput.vue 文件不存在
- **Notes": 确保所有引用都已更新后再删除
