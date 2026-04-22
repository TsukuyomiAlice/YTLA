<p>
 语言 
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

# 计划管理

### YTLA关键应用

### Official

version 1.0

后端语言及开发框架: Python-Flask  
前端语言及开发框架: Vue3, typescript  
适用YTLA core版本: **classic**  
文件更新日期: 2026-2-12

## 这是一个YTLA标准框架应用

本应用为YTLA框架下的专用应用.  
请注意前后端的开发语言和框架.  
本应用仅保障在满足YTLA本体项目基础上可正常加载并运行.  
对已产生定制化的YTLA项目副本，请检查配置和兼容性.

### 重要: 关键应用

本应用为关键应用.  
对于前端页面，其它应用均需通过此应用完成调度.  
如若同时启用多个关键应用，请务必确认不同关键应用之间是否存在冲突.

## 概念

计划管理将负责完成用户在浏览器页面上创建、浏览、管理计划，模组管理的重要功能.

### 计划管理器

为用户显示所有使用中的计划、创建、管理计划等功能.

### 计划仪表盘

显示用户计划的具体情况.
添加模组、创建模组分类.

### 添加模组

用户可以选择希望添加进当前计划的模组.

### 设置

所有与计划和模组相关的设定.

### 欢迎

YTLA的介绍页面.

## 应用包目录

- planManage
    - docs (readme.md)
    - cards
        - _type (缺省)
    - modules
        - _type (缺省)
        - addModule
        - planDashboard
        - planManager
        - settings
        - welcome
          readme.md
