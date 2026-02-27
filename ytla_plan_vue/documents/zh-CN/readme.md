<p>
 语言 
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

# ytla_plan_vue

### YTLA前端框架

### Official

version: 1.0

前端语言及开发框架:Vue3, typescript  
文件更新日期: 2026-2-12

## 开放代码，自由添加

项目完全开源，包括core在内所有的代码都以源码形式公开.  
因此，你可以根据自己的需要进行自定义的定制.  
在此之前，请阅读本文档，以确保对项目的框架有足够的了解.

## 概念

YTLA作为一个有着Web OS愿景的完整、前后端分离项目，在代码层面上有两组概念.

### Core 和 Feature

**Core** 作为驱动项目运行的底层代码，类似驱动程序  
**Feature** 作为提供用户应用的功能模块，即应用软件  
- 在Feature中，有一类特殊的应用，被成为“关键应用”.  
  这种应用可被理解为操作系统软件

### Card, Module 和 Plan

**Card** 为用户提供快捷、简易的功能  
**Module** 为用户提供应用层面服务  
**Plan** 可以让用户自由添加Module，创造独属于自己的工作台

## Vue3版本 架构层级

- project
    - core
        - 核心版本名
            - cards -核心组件
                - 组件+版本1
                    - 组件下文件
                - 组件+版本2
                    - 组件下文件
            - modules -核心组件
                - 组件+版本1
                    - 组件下文件
                - 组件+版本2
                    - 组件下文件
            - plans -核心组件
                - 组件+版本1
                    - 组件下文件
                - 组件+版本2
                    - 组件下文件
            - frame -核心组件
                - 组件+版本1
                    - 组件下文件
                - 组件+版本2
                    - 组件下文件
            - users -核心组件
                - _type (缺省定义)
                - 细化组件
                    - 组件下package
    - feature
        - 功能名
            - cards
                - _type (缺省定义)
                - 对应卡片组件类型1
                    - 组件下文件
                - 对应卡片组件类型2
                    - 组件下文件
            - modules
                - _type (缺省定义)
                - 对应卡片组件类型1
                    - 组件下文件
                - 对应卡片组件类型2
                    - 组件下文件

### 后端的单个组件package结构

项目按照组件的功能进行分类，每个组件下包含多个package，每个package负责不同的功能.  
如果使用scaffold(/features/scaffold/modules/frontend_vue3)进行初始化，你会得到以下全部package:

### 文档管理

| 文件夹名      | 文件功能 | 文件类型                  | 说明   |
|-----------|------|-----------------------|------|
| documents | 文档   | json, bk(vue,ts,etc…) | 组件文档 |

### 数据实例

| 文件夹名        | 文件功能                    | 文件类型 | 说明              |
|-------------|-------------------------|------|-----------------|
| definitions | 类型(ts type / interface) | .ts  | 卡片、模组下针对功能的对象类型 |

### 组件

| 文件夹名       | 文件功能 | 文件类型  | 说明         |
|------------|------|-------|------------|    
| components | 组件   | .vue  | 作为卡片、模组的承载 |
| layouts    | 布局   | .vue  | 作为组件的布局区块  |
| ui         | ui   | .vue  | 页面上显示的组件   |
| styles     | 式样   | .scss | 组件的显示式样    |

#### 举例：Layout文件的配置

- ../layouts/ContainerUiFile.vue
    - ../composables/ContainerUiFile.ts
    - ../styles/container-ui-file.scss

#### 举例：Component文件的配置

- ../components/ComponentFile.vue
    - ../layouts/LayoutComponentFIle.vue
    - ../uis/UiFile.vue
    - ../composables/useComponentFile.ts
    - ../styles/component-file.scss
    - ../definitions/componentType.ts

#### 举例：UI文件的配置

- ../uis/UiFile.vue
    - ../composables/useUiFile.ts
    - ../styles/ui-file.scss

#### 复合组合词命名规则

元件类型名+元件名+元件功能名，各部分首字母大写

#### layouts

- Container：容器
- Area：区域
- Column：栏目

#### uis

- Container：容器
- Bar：条形、行
- Button：按钮

#### 举例

- AreaSideCardMain
    - Area：元件类型，区域
    - SideCard：元件名（出现于component)
    - Main：元件功能

### 数据

| 文件夹名   | 文件功能   | 文件类型 | 说明               |
|--------|--------|------|------------------|
| stores | 储存(数据) | .ts  | 在浏览器内存内临时存储的数据格式 |

### 控制处理

| 文件夹名        | 文件功能  | 文件类型 | 说明                |
|-------------|-------|------|-------------------|
| composables | 组合式函数 | .ts  | vue推荐的用于控制组件的函数   |
| factories   | 工厂    | .ts  | 主要用于核心功能的管控（工厂模式） |
| registries  | 注册    | .ts  | 模组、卡片的注册式加载机制     |
| flows       | 流程    | .ts  | 卡片设置流程、模组显示页面切换用  |

### 前端通信

| 文件夹名     | 文件功能    | 文件类型 | 说明   |
|----------|---------|------|------|
| services | 服务(api) | .ts  | 后端通讯 |

### 配置

| 文件夹名    | 文件功能 | 文件类型                | 说明         |
|---------|------|---------------------|------------|
| locales | 语言   | .json               | 多语种对应文件    |
| utils   | 配置   | .ts, .json, .config | 参数、常参数等    |
| avatar  | 组件图标 | .vue, .png          | 卡片、模组的logo |
