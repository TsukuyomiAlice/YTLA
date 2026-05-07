# System Navigation - The Implementation Plan (Decomposed and Prioritized Task List)

## [x] Task 1: 创建类型定义文件

- **Priority**: P0
- **Depends On**: None
- **Description**: 
  - 创建 `systemTypes.ts`，定义 SystemLevel 枚举
  - 定义 SystemConfig 接口
  - 定义 SystemButtonConfig 接口
  - 定义 SystemContext 接口
- **Acceptance Criteria Addressed**: AC-1, AC-2
- **Test Requirements**:
  - `programmatic` TR-1.1: 类型定义编译通过
  - `programmatic` TR-1.2: 类型导入/导出正确
- **Notes**: 遵循项目现有的类型定义风格

## [x] Task 2: 创建 System Config 配置文件

- **Priority**: P0
- **Depends On**: Task 1
- **Description**: 
  - 在 `@/features/planManage/config/` 目录下创建 `systemConfig.ts`
  - 配置 systemModule = 'planManage'
  - 配置 rootModule = 'planManager'
  - 配置 desktopModule = 'planDashboard'
  - 配置 rootPanel = 'plan_manage'
- **Acceptance Criteria Addressed**: AC-1
- **Test Requirements**:
  - `programmatic` TR-2.1: 配置文件能正确导出
  - `programmatic` TR-2.2: 配置内容符合要求

## [x] Task 3: 创建 System Navigator Registry

- **Priority**: P0
- **Depends On**: Task 1, Task 2
- **Description**: 
  - 创建 `systemNavigatorRegistry.ts`
  - 实现 initSystem() 函数用于初始化系统
  - 实现 registerSystemButton() 函数用于注册按钮
  - 实现 getSystemConfig() 函数获取系统配置
  - 实现 getVisibleSystemButtons() 函数获取可见按钮
  - 实现按钮组件的动态加载
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3
- **Test Requirements**:
  - `programmatic` TR-3.1: 可以成功初始化系统
  - `programmatic` TR-3.2: 可以注册按钮
  - `programmatic` TR-3.3: 可以获取可见按钮

## [x] Task 4: 创建 Navigator Store

- **Priority**: P0
- **Depends On**: Task 1, Task 2, Task 3
- **Description**: 
  - 创建 `stores/navigatorStore.ts`
  - 使用 Pinia defineStore
  - state 存储激活的按钮 ID
  - getters 获取可见的激活按钮
  - actions: setActiveButtons(), addButton(), removeButton(), clearButtons(), activateAllButtons()
- **Acceptance Criteria Addressed**: AC-1, AC-2, AC-3, AC-6
- **Test Requirements**:
  - `programmatic` TR-4.1: Store 可以正确初始化
  - `programmatic` TR-4.2: 可以激活按钮
  - `programmatic` TR-4.3: 可以移除按钮
  - `programmatic` TR-4.4: 可以获取可见按钮

## [x] Task 5: 创建 Navigation Bar 组件

- **Priority**: P0
- **Depends On**: Task 1-4
- **Description**: 
  - 创建 `components/SystemNavigationBar.vue`
  - 使用 navigatorStore 和 panelStore
  - 构建 SystemContext
  - 渲染可见的激活按钮
- **Acceptance Criteria Addressed**: AC-4, AC-5
- **Test Requirements**:
  - `programmatic` TR-5.1: 组件可以正常导入
  - `human-judgment` TR-5.2: 按钮可以正确渲染和交互

## [x] Task 6: 创建系统初始化和按钮注册文件

- **Priority**: P0
- **Depends On**: Task 1-5
- **Description**: 
  - 创建 `registries/navigatorRegistry.ts`
  - 初始化系统
  - 注册 ReturnToSystemRoot 按钮（使用 ReturnToPlanButton）
  - 注册 ReturnToPlanDesktop 按钮（使用 ReturnToPlanDashboardButton）
  - 更新 navigator 模块的 registries.ts
- **Acceptance Criteria Addressed**: AC-1, AC-2
- **Test Requirements**:
  - `programmatic` TR-6.1: 注册文件可以正确导入
  - `programmatic` TR-6.2: 按钮可以正确注册

## [x] Task 7: 更新 main.ts

- **Priority**: P1
- **Depends On**: Task 1-6
- **Description**: 
  - 在 main.ts 中引入 navigatorRegistry
  - 确保系统在应用启动时初始化
- **Acceptance Criteria Addressed**: AC-1, AC-2
- **Test Requirements**:
  - `programmatic` TR-7.1: main.ts 可以正确编译
  - `programmatic` TR-7.2: 应用可以正常启动

## [ ] Task 8: 创建使用示例文档

- **Priority**: P2
- **Depends On**: Task 1-7
- **Description**: 
  - 创建 README 文档
  - 展示如何在模块中使用 SystemNavigationBar
  - 展示如何激活按钮
- **Acceptance Criteria Addressed**: AC-4
- **Test Requirements**:
  - `human-judgment` TR-8.1: 文档清晰易懂

## [ ] Task 9: 创建国际化文件（可选）

- **Priority**: P2
- **Depends On**: Task 1
- **Description**: 
  - 更新 locales/zh.json 和 en.json
  - 添加导航相关的文本
- **Acceptance Criteria Addressed**: 
- **Test Requirements**:
  - `human-judgment` TR-9.1: 文本能正确显示
