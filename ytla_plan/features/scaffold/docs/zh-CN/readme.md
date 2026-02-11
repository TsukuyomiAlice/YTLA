<p>
 语言 
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

# 脚手架

### YTLA应用

### Official

version 1.0

后端语言及开发框架: Python-Flask  
前端语言及开发框架: Vue3  
适用YTLA core版本: **classic**  
文件更新日期: 2026-2-11

## 这是一个YTLA标准框架应用

本应用为YTLA框架下的专用应用.  
请注意前后端的开发语言和框架.  
本应用仅保障在满足YTLA本体项目基础上可正常加载并运行.  
对已产生定制化的YTLA项目副本，请检查配置和兼容性.

## 概念

脚手架可用于生成基础框架和自动化代码，以支持快速开发和扩展.  
在脚手架中，包含以下不同类型的包，并遵循不同规则定义.

### frontend_lang_framework

前端配置的生成框架.  
**lang** 表示前端使用的语言.  
**framework** 表示前端的开发框架.

### backend_lang_framework

后端配置的生成框架.  
**lang**与**framework**分别表示后端的语言和框架.

### general_version

核心版本的生成框架.  
**version** 表示工程中适用的""core""的版本名.

## 应用包目录

- YTLA (project)
    - ytla_plan (backend)
        - features
            - scaffold
                - docs (readme.md)
                - modules
                    - _type
                    - backend_python_flask
                    - frontend_vue3
                    - general_classic
                    - __init__.py
                - __init__.py
                - readme.md
    - ytla_plan_vue (frontend)
        - src
            - features
                - scaffold
                    - docs (readme.md)
                    - modules
                        - _type
                - readme.md

## 添加本应用

### 重要

1 请确保你的YTLA项目为原生版本.  
2 适用核心版本为: **classic**.  
3 你的YTLA工程中，前后端均不包含feature名为"scaffold"的目录.

如果满足上述条件，将本工程直接复制在YTLA工程目录下即可.

#### 如果有定制?

推荐检查定制配置和原生配置之间的差别后，谨慎添加本应用.