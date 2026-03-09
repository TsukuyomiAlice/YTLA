# 文件规范

本文件规范适用于以下范围.  
文件规范提供的是一个流程上的指导，在实际操作中以用户的指定需求优先.  

## 总述

适用栈: 前端  
适用语言类型和框架: vue3, typescript  

## 标准文件结构框架

- ytla_plan_vue  前端总目录
  - documents  前端顶层documents
  - src  
    - core  核心
      - core_version1  核心文件1
        - core_version_feature_1  核心功能1
          - core_feature_module_1  核心功能组件1
            - avatar  图标
            - components  组件
            - composables  组合式api
            - definitions  定义
            - documents  文档
            - factories  工厂
            - flows  流程
            - layouts  布局
            - registries  注册
            - services  服务
            - stores  存储
            - styles  式样
            - ui  元件
            - utils  配置
            - readme.md  组件描述readme
          - core_feature_module_2  核心功能组件2，具体略
        - core_version_feature_2  核心功能2，具体略
        - readme.md 核心描述readme
      - core_version2  核心文件2，具体略
    - features
      - feature1  功能1
        - feature_mode_1 功能下组件形式1
          - feature_mode_module_1 功能下该组件形式的具体组件1
            - avatar  图标
            - components  组件
            - composables  组合式api
            - definitions  定义
            - documents  文档
            - factories  工厂
            - flows  流程
            - layouts  布局
            - registries  注册
            - services  服务
            - stores  存储
            - styles  式样
            - ui  元件
            - utils  配置
            - readme.md  组件描述readme 
          - feature_mode_module_2 功能下该组件形式的具体组件2，具体略
        - feature_mode_2 功能下组件形式2，具体略
      - feature2  功能2，具体略
      - feature3  功能3，具体略
    - App.vue
    - main.ts
    - index.html
    - readme.md  前端顶层readme

## 具体文件说明

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
    - ../composables/useContainerUiFile.ts
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

#### layouts可选用的元件类型名

- Container：容器
- Area：区域
- Column：栏目

#### uis可选用的元件类型名

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
