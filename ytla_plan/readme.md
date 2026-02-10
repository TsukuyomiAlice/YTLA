# ytla_plan

### YTLA后端工程

### Official

version: 1.0

后端语言及开发框架: Python-Flask  
文件更新日期: 2026-2-10

## 开放代码，自由添加

项目完全开源，包括core在内所有的代码都以源码形式公开.  
因此，你可以根据自己的需要进行自定义的定制.  
在此之前，请阅读本文档，以确保对项目的框架有足够的理解.

## 核心概念

YTLA作为一个有着Web OS愿景的完整、前后端分离项目，在代码层面上有两组概念。

### Core 和 Feature

**Core** 作为驱动项目运行的底层代码，类似操作系统  
**Feature** 作为提供用户应用的功能模块，即应用软件

### Card, Module 和 Plan

**Card** 为用户提供快捷、简易的功能  
**Module** 为用户提供应用层面服务  
**Plan** 可以让用户自由添加Module，创造独属于自己的工作台

## Python-Flask版本 架构层级

- project
    - core
        - 核心版本名
            - cards -核心组件
                - _type (缺省定义)
                - 细化组件
                    - 组件下package
            - modules -核心组件
                - _type (缺省定义)
                - 细化组件
                    - 组件下package
            - plans -核心组件
                - _type (缺省定义)
                - 细化组件
                    - 组件下package
            - frame -核心组件
                - _type (缺省定义)
                - 细化组件
                    - 组件下package
            - users -核心组件
                - _type (缺省定义)
                - 细化组件
                    - 组件下package
    - feature
        - 功能名
            - cards
                - _type (缺省定义)
                - 组件
                    - 组件下package
            - modules
                - _type (缺省定义)
                - 组件
                    - 组件下package

### 后端的单个组件package结构

项目按照组件的功能进行分类，每个组件下包含多个package，每个package负责不同的功能。  
如果使用scaffold(/features/scaffold/modules/backend_python)进行初始化，你会得到以下全部package:

### 文档管理

| package名 | 文件功能   | 文件类型              | 说明     |
|----------|--------|-------------------|--------|
| docs     | 组件设定文档 | .yaml, .json, .py | 用于自动生成 |

### 数据实例

| package名 | 文件功能 | 文件类型 | 说明       |
|----------|------|------|----------|
| instance | 实例   | .py  | 组件数据实例类型 |

### 数据

| package名 | 文件功能 | 文件类型             | 说明                        |
|----------|------|------------------|---------------------------|
| dataset  | 数据集  | .py, .json, etc. | 预制数据集                     |
| dao      | DB访问 | .py              | python sqlite3 SQLAlchemy |

### 逻辑处理

| package名 | 文件功能   | 文件类型 | 说明           |
|----------|--------|------|--------------|
| process  | 逻辑处理流程 | .py  | 组件逻辑处理       |
| schedule | 定期自动执行 | .py  | 定期自动化运行      |
| script   | 调用脚本   | .py  | 组装、调用包内方法或函数 |

### 联动性

| package名 | 文件功能       | 文件类型 | 说明                      |
|----------|------------|------|-------------------------|
| const    | 常变量        | .py  | 特定常数                    |
| api      | 对外api调用    | .py  | 发送api请求，对api接收结果进行处理    |
| ai_tools | ai辅助工具     | .py  | 需要交由gen ai进行处理的特定功能代码片段 |
| caller   | 跨包函数调用统一方法 | .py  | 跨包调用功能                  |
| func     | 功能性函数      | .py  | 通用型函数                   |

### 前端通信

| package名 | 文件功能  | 文件类型 | 说明                       |
|----------|-------|------|--------------------------|
| routes   | api路由 | .py  | python-flask Blueprint文件 |

### 配置

| package名 | 文件功能 | 文件类型             | 说明     |
|----------|------|------------------|--------|
| utils    | 配置参数 | .py, .json, etc. | 运行配置参数 |

