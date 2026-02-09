# YTLA 前端开发指南

## 项目简介

YTLA (Your T&L Assistant) 是一个模块化 Web 应用平台框架，用户可通过自由生成并组合模块（Modules）和卡片（Cards）快速构建个性化工作流。

## 核心理念

- **T&L 自定义**
  "T" 和 "L" 代表用户自定义的词汇（如 Tech & Learning, Task & Logistics 等），赋予平台灵活的应用场景。
- **模块化架构**
  将功能拆分为可复用的模块（完整应用）和卡片（轻量小组件），支持按需组合。
- **计划（Plan）驱动**
  用户可创建多个计划，每个计划包含一组模块/卡片，实现不同场景的专属工作台。

## 技术栈

| 层级 | 技术 |
|------|------|
| **前端** | Vue 3 |
| **状态管理** | Pinia |
| **路由** | Vue Router |
| **样式** | SCSS |
| **HTTP客户端** | Axios |
| **动画** | GSAP, VueUse Motion |
| **图表** | ECharts |
| **3D** | Three.js |

## Vue3 架构层级

| 层级 | 0 | 1 | 2 | 3 | 4 |
|------|----------|-------|--------------|------------|-------|
| | core | 核心版本名 | 核心组件-cards | 组件+版本1 | 组件下文件 |
| | | | | 组件+版本2 | 组件下文件 |
| | | | | ... | |
| | | | 核心组件-modules | 组件+版本1 | 组件下文件 |
| | | | | 组件+版本2 | 组件下文件 |
| | | | | ... | |
| | features | 功能名 | cards | _type 缺省类型 | |
| | | | | 对应卡片组件类型1 | 组件下文件 |
| | | | | 对应卡片组件类型2 | 组件下文件 |
| | | | modules | _type 缺省类型 | |
| | | | | 对应子模块组件1 | 组件下文件 |
| | | | | 对应子模块组件2 | 组件下文件 |

## 前端的单个组件文件结构

| 文件夹名 | 文件功能 | 文件类型 | 说明 |
|----------|----------|----------|------|
| documents | 文档 | json, bk(vue,ts,etc…) | 组件文档 |
| definitions | 类型(ts type / interface) | .ts | 卡片、模组下针对功能的对象类型 |
| components | 组件 | .vue | 作为卡片、模组的承载 |
| layouts | 布局 | .vue | 作为组件的布局区块 |
| ui | ui | .vue | 页面上显示的组件 |
| composables | 组合式函数 | .ts | vue推荐的用于控制组件的函数 |
| styles | 式样 | .scss | 组件的显示式样 |
| locales | 语言 | .json | 多语种对应文件 |
| stores | 储存(数据) | .ts | 在浏览器内存内临时存储的数据格式 |
| services | 服务(api) | .ts | 后端通讯 |
| factories | 工厂 | .ts | 主要用于核心功能的管控（工厂模式） |
| registries | 注册 | .ts | 模组、卡片的注册式加载机制 |
| flows | 流程 | .ts | 卡片设置流程、模组显示页面切换用 |
| utils | 配置 | .ts, .json, .config | 参数、常参数等 |
| avatar | 组件图标 | .vue, .png | 卡片、模组的logo |

## 配置以vue文件展开

### 举例

#### UI文件的配置

- ../uis/UiFile.vue
    - ../composables/useUiFile.ts
    - ../styles/ui-file.scss

#### Layout文件的配置

- ../layouts/ContainerUiFile.vue
    - ../composables/ContainerUiFile.ts
    - ../styles/container-ui-file.scss

#### Component文件的配置

- ../componets/ComponentFile.vue
    - ../layouts/LayoutComponentFIle.vue
    - ../uis/UiFile.vue
    - ../composables/useComponentFile.ts
    - ../styles/component-file.scss
    - ../definitions/componentType.ts

## 复合组合词命名规则

元件类型名+元件名+元件功能名，各部分首字母大写

### 类型名

#### layouts

- Container：容器
- Area：区域
- Column：栏目

#### uis

- Container：容器
- Bar：条形、行
- Button：按钮

### 举例

- AreaSideCardMain
    - Area：元件类型，区域
    - SideCard：元件名（出现于component)
    - Main：元件功能

## 对卡片/模组设计的注意点

- 必须性
- 可选性
- 区域性

## 开发规则

1. 前端
   1. 组件开发遵循 Vue 3 Composition API 规范
   2. 使用 TypeScript 确保类型安全
   3. 组件样式使用 SCSS 预处理器
   4. 状态管理使用 Pinia
   5. 路由管理使用 Vue Router

## 快速开始

```bash
# 克隆项目
git clone https://github.com/TsukuyomiAlice/YTLA

# 前端依赖安装
cd ytla_plan_vue
npm install

# 启动开发环境
npm run dev

# 类型检查、编译和生产构建
npm run build

# 代码检查
npm run lint
```

## 当前进展

- 基础框架搭建完成
- 实现模块/卡片容器系统
- 支持模块间数据通信
- 内置系统模块：
  - 计划管理器（Plan Manager）
  - 工作台（Plan Dashboard）
  - 模块选择器（Module Selector）
  - 国际化支持（vue-i18n）

## 下一步计划

- 账户与权限管理系统
- 多用户协作功能
- 开发者脚手架工具
- AI 能力集成
- 社区文档完善