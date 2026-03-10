# YTLA - core classic 工程与文件规范

本文件规范适用于以下范围.  
文件规范提供的是一个流程上的指导，在实际操作中以用户的指定需求优先.

## 总述

适用核心名: classic  
core目录下仅 **classic** 适用

## 标准文件结构框架

在classic核心下包含以下目录类型.  
其中，具体的目录结构受到对应语言和框架的影响.

- 后端目录
    - core 核心
        - classic 本核心
            - cards 卡片
                - docs 卡片readme
                - sideCard 侧边栏卡片
                    - docs 侧边栏卡片readme
                    - readme.md 侧边栏卡片说明文档
                    - sideCard的其它内部配置，根据语言和框架确定
                - readme.md 卡片说明文档
            - modules 模组
            - plans 计划
            - users 用户
            - frame 框架
            - docs 后端顶层readme
            - readme.md 后端描述readme
    - features 功能
        - feature1 功能1
            - cards 功能下卡片
                - _type 该功能卡片缺省定义
                - feature_card_1 具体样式卡片1
                - feature_card_2 具体样式卡片2，下略
            - modules 功能下模组
                - _type 该功能模组缺省定义
                - feature_module_1 具体样式模组1
                - feature_module_2 具体样式模组2，下略
            - docs 功能描述文档
            - readme.md 功能描述文档 readme
- 前端目录
    - core 核心
        - classic 本核心
            - cards 卡片
                - docs 卡片readme
                - sideCard 侧边栏卡片
                    - docs 侧边栏卡片readme
                    - readme.md 侧边栏卡片说明文档
                    - sideCard的其它内部配置，根据语言和框架确定
                - readme.md 卡片说明文档
            - modules 模组
            - plans 计划
            - users 用户
            - busline 总线
            - frame 框架
            - docs 前端顶层readme
            - readme.md 前端描述readme
    - features 功能
        - feature1 功能1
            - cards 功能下卡片
                - _type 该功能卡片缺省定义
                - feature_card_1 具体样式卡片1
                - feature_card_2 具体样式卡片2，下略
            - modules 功能下模组
                - _type 该功能模组缺省定义
                - feature_module_1 具体样式模组1
                - feature_module_2 具体样式模组2，下略
            - docs 功能描述文档
            - readme.md 功能描述文档 readme

后端目录、前端目录中提到的docs目录名称，可能随构筑用程序语言下框架的命名规则而变化.

除docs外，前后端目录各自包含以下内容

| 分区       | 后端特性                                | 前端特性                                         |  
|----------|-------------------------------------|----------------------------------------------|  
| core     | cards, modules, plans, users, frame | cards, modules, plans, users, frame, busline |  
| features | cards, modules                      | cards, modules                               |

**core** 在本文件中名为 **classic**. 新的具体功能不能被创建在core内.  
**features** 中，用户可以添加、创建新的功能，且形式需被限定为card或module.  

## 各项具体特性说明

为避免混淆含义，在本段中：  
'用户'如无特殊说明，即使用者.  
应用层面特性如无特殊说明，指features.

### cards 卡片

卡片包含于前后端.  
卡片前后端通过api通信.  
在classic中，卡片特指sideCard（侧边栏卡片）.  
用户可以创建并添加卡片应用层面特性.

### modules 模组

模组包含于前后端.  
模组前后端通过api通信.  
在classic中，模组特性由plans管控.  
用户可以创建并添加模组应用层面特性.

### plans 计划

计划包含于前后端.  
计划前后端通过api通信.  
在classic中，计划特性用于管理modules.  
用户不能创建计划概念的应用层面特性.  
用户可以通过使用plan组织、管理modules。  

### frame 框架

框架包含于前后端. 
框架用于管控前后端各自的核心功能.  
用户不能创建框架概念的应用层面特性.  
框架用于支持classic核心运行.  

### busline 总线

总线包含于前端.  
总线仅用于管控前端的应用层面核心功能.  
用户不能创建总线概念的特性. 

### users 用户

用户包含于前后端.  
用户用于处理使用者（即前文所提到的'用户'）在使用应用中的各类权限.  
使用者不能创建用户概念应用层面的特性. 