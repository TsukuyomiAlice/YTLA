# YTLA - python-flask 工程与文件规范

本文件规范适用于以下范围.  
文件规范提供的是一个流程上的指导，在实际操作中以用户的指定需求优先.  

## 总述

适用栈: 后端  
适用语言类型和框架: python-flask  

## 标准文件结构框架

- ytla_plan  后端总目录
  - docs  后端顶层docs
  - core  核心
      - core_version1  核心文件1
        - core_version_feature_1  核心功能1
          - core_feature_module_1  核心功能组件1
            - ai_tools  ai工具
            - api  api请求
            - caller  功能调用
            - const  常数
            - dao  数据存储
            - dataset  稳定数据集
            - docs  文档
            - func  通用函数
            - instance  实例
            - process  流程
            - routes  路由 flask-blueprint
            - schedule  计划任务
            - script  脚本
            - utils  配置文件
            - __init__.py  包init文件
            - readme.md  组件描述readme
          - core_feature_module_2  核心功能组件2，具体略
        - core_version_feature_2  核心功能2，具体略
        - readme.md 核心描述readme
      - core_version2  核心文件2，具体略
  - core_test  核心测试目录，其内部结构与core对应
  - features  应用
      - feature1  功能1
        - feature_mode_1 功能下组件形式1
          - feature_mode_module_1 功能下该组件形式的具体组件1
            - ai_tools  ai工具
            - api  api请求
            - caller  功能调用
            - const  常数
            - dao  数据存储
            - dataset  稳定数据集
            - docs  文档
            - func  通用函数
            - instance  实例
            - process  流程
            - routes  路由 flask-blueprint
            - schedule  计划任务
            - script  脚本
            - utils  配置文件
            - __init__.py  包init文件
            - readme.md  组件描述readme
          - feature_mode_module_2 功能下该组件形式的具体组件2，具体略
        - feature_mode_2 功能下组件形式2，具体略
      - feature2  功能2，具体略
      - feature3  功能3，具体略
  - features_test  应用测试目录，其内部结构与features对应
  - app.py python-flask应用启动
  - wsgi.py 后端启动
  - config.py 后端配置
  - readme.md  后端顶层readme

## 具体文件说明
命名上，除docs、utils、或者用户指定文件名的场合，一般文件命名遵循以下规则：  
package名 + 功能描述名（首字母大写）.py  
所有.py文件都应包含docstring注释，  
并且，如无特殊要求，其中所有的注释文档都应使用**英语**书写.  

### 文档管理

| package名 | 文件功能   | 文件类型                        | 说明     |
|----------|--------|-----------------------------|--------|
| docs     | 组件设定文档 | .yaml, .json, .py, .md, etc | 用于自动生成 |

### 数据实例

| package名 | 文件功能 | 文件类型 | 说明       |
|----------|------|------|----------|
| instance | 实例   | .py  | 组件数据实例类型 |

### 数据

| package名 | 文件功能 | 文件类型             | 说明              |
|----------|------|------------------|-----------------|
| dataset  | 数据集  | .py, .json, etc. | 预制数据集           |
| dao      | DB访问 | .py              | python sqlite3  |

### 逻辑处理

| package名 | 文件功能   | 文件类型 | 说明           |
|----------|--------|------|--------------|
| process  | 逻辑处理流程 | .py  | 组件逻辑处理       |
| schedule | 定期自动执行 | .py  | 定期自动化运行      |
| script   | 调用脚本   | .py  | 组装、调用包内方法或函数 |

**process**指的是完整的业务功能.  
**script**指的是在业务中需要独立执行的脚本.  
**schedule**指的是需要自动、定时、反复执行的业务流程.  

### 联动性

| package名 | 文件功能       | 文件类型 | 说明                      |
|----------|------------|------|-------------------------|
| const    | 常变量        | .py  | 特定常数                    |
| api      | 对外api调用    | .py  | 发送api请求，对api接收结果进行处理    |
| ai_tools | ai辅助工具     | .py  | 需要交由gen ai进行处理的特定功能代码片段 |
| caller   | 跨包函数调用统一方法 | .py  | 跨包调用功能                  |
| func     | 功能性函数      | .py  | 通用型函数                   |

**caller**的跨包调用指的是**跨不同feature的module调用**.  
**func**函数指的是**不依赖业务数据的独立运算函数**.  

### 前端通信

| package名 | 文件功能  | 文件类型 | 说明                       |
|----------|-------|------|--------------------------|
| routes   | api路由 | .py  | python-flask Blueprint文件 |

### 配置

| package名 | 文件功能 | 文件类型             | 说明     |
|----------|------|------------------|--------|
| utils    | 配置参数 | .py, .json, etc. | 运行配置参数 |


