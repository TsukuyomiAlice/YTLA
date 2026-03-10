# YTLA - Docs 文件规范

本文件规范适用于以下范围.  
文件规范提供的是一个流程上的指导，在实际操作中以用户的指定需求优先.  

## 总述

适用核心名: 全部  
适用栈: 包括前后端  
适用语言类型和框架: 全部  

指定规范目录：docs  
指定规范文档：readme.md

## 标准文件结构框架

### 文档目录可出现在以下层级目录中：

- YTLA根目录
  - docs 描述YTLA
  - YTLA前端目录
    - docs 描述YTLA前端
    - core
      - core_版本名
        - docs 描述版本
        - core特性 
          - docs 描述特性
          - 具体特性
            - docs 描述具体特性
    - features
      - feature_功能名
        - docs 描述功能
        - feature_功能形式
          - feature_具体类型
            - docs 描述具体类型
  - YTLA后端目录
    - docs 描述YTLA后端
    - core
      - core_版本名
        - docs 描述版本
        - core特性 
          - docs 描述特性
          - 具体特性
            - docs 描述具体特性
    - features
      - feature_功能名
        - docs 描述功能
        - feature_功能形式
          - feature_具体类型
            - docs 描述具体类型


### 文档目录的泛用格式如下：

- 原目录
  - docs  文档目录
    - readme  readme目录，必须包含
      - en-US  英语
      - zh-CN  简体中文
      - 其它语种
    - 其它文档
  - readme.md  根目录下需有readme.md

#### 目前仅readme有强制文件格式要求.  
#### docs文档目录名称可能随语言框架设计而发生改变，而其内部保持不变.  
#### 理论上，其它文档的目录应遵循每一种文档类型，均有一个文件夹用于单独存放该类文档.  


## docs文档的书写规则

在脚手架中可以预生成readme相关目录和文档，并且会生成固定格式的表单.  
优先更新位于根目录下的readme.md.  
之后，可以在使用ai工具的过程中，要求ai同步完成docs/readme目录下的各个语种文件的更新.  
如果用ai工具生成了整个项目，那么需要要求ai先更新根目录的readme.md文档，然后同步更新docs/readme目录下的各语种对应的readme.md.  

