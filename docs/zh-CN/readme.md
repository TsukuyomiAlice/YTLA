<p>
 语言 
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

# YTLA - Your T&L Assistant

### 一个有着Web OS愿景的应用平台框架

### Official

version 1.0

文件更新日期: 2026-2-11

## 开放代码，自由添加

项目完全开源，所有的代码都以源码形式公开.  
因此，你可以根据自己的需要进行自定义的定制.  
在此之前，请阅读本文档，以确保对项目的框架有足够的了解.

## 概念

### 自驱动，自主，自由

这是一个自驱动的平台框架.  
借助生成式AI，结合成熟的工程规范，为用户可靠地增添、扩展他们想要的功能.    
产品名里的'T'和'L'并没有被定义 —— 这是留给用户去主动定义的.  
由此，这个平台将为用户提供高度自由的应用场景.

### 高度模块化

框架下的功能将以两种不同的模块提供给用户.  
**模块** 为用户提供完整的功能  
**卡片** 为用户提供便捷、即时的交互  
模块可以自用组合在一个或多个**计划**中，为用户提供面向各种需求的专属工作台.

### 高度可定制化

框架前后端分离，有着详尽而又灵活的架构设计.  
结合语义定义，使框架可以在多种程序语言下都能得以实现.  
具体的架构拆分定义，能确保框架在不同程序语言下能拥有相同的运行效果.

## 框架目录

- YTLA (本框架)
    - docs (readme.me)
    - frontend
        - docs
        - core
        - features
    - backend
        - docs
        - core
        - features
    - readme.md

## 使用本框架

#### 提示

目前本框架使用的是vue3和python-flask.预计未来会使用更多种类的语言.

```bash
# 克隆项目
git clone https://github.com/TsukuyomiAlice/YTLA

# 后端依赖安装
cd ytla_plan
pip install -r requirements.txt

# 前端依赖安装
cd ../ytla_plan_vue
npm install

# 启动开发环境
npm run dev & flask run
```