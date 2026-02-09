# YTLA 后端开发指南

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
| **后端** | Python (Flask框架) |
| **数据层** | 模块独立存储 + 跨模块通信 |

## Python-Flask 架构层级

| 层级 | 0 | 1 | 2 | 3 | 4 |
|------|-----|-----|--------------|------------|------------|
| | core | 核心版本名 | 核心组件-cards | _type 缺省定义 |  |
| | | | | 细化组件 | 组件下package |
| | | | 核心组件-modules | _type 缺省定义 |  |
| | | | | 细化组件 | 组件下package |
| | | | 核心组件-plans | _type 缺省定义 |  |
| | | | | 细化组件 | 组件下package |
| | | | 核心组件-frame | _type 缺省定义 |  |
| | | | | 细化组件 | 组件下package |
| | | | 核心组件-users | _type 缺省定义 |  |
| | | | | 细化组件 | 组件下package |
| | feature | 功能名 | cards | _type 缺省定义 |  |
| | | | | 组件 | 组件下package |
| | | modules | _type 缺省定义 |  |  |
| | | | | 组件 | 组件下package |

## 后端的单个组件package结构

| package名 | 文件功能 | 文件类型 | 说明 |
|----------|----------|----------|------|
| docs | 组件设定文档 | .yaml, .json, .py | 用于自动生成 |
| instance | 实例 | .py | 组件数据实例类型 |
| process | 逻辑处理流程 | .py | 组件逻辑处理 |
| schedule | 定期自动执行 | .py | 定期自动化运行 |
| script | 调用脚本 | .py | 组装、调用包内方法或函数 |
| dataset | 数据集 | .py, .json, etc. | 预制数据集 |
| api | 对外api调用 | .py | 发送api请求，对api接收结果进行处理 |
| dao | DB访问 | .py | python sqlite3 SQLAlchemy |
| routes | api路由 | .py | python-flask Blueprint文件 |
| const | 常变量 | .py | 特定常数 |
| ai_tools | ai辅助工具 | .py | 需要交由gen ai进行处理的特定功能代码片段 |
| caller | 跨包函数调用统一方法 | .py | 跨包调用功能 |
| func | 功能性函数 | .py | 通用型函数 |

## 开发规则

1. 后端
   1. 不论是module还是card，都是从dao层开始，然后是process层，最后是route层
   2. 对于需要从其他工程获取数据的，需要在caller层定义一个函数，然后在route层调用
   3. 现在已经进行了改版，后端的代码区分为core和features两个概念
      对于core和features内部的每个子目录下，都包含有上述的目录结构
      对于core而言，这样做有利于区分核心功能的分块与解耦，并且可以与前端代码对应
      而对于features，这样做本身就和前端代码对齐

## 快速开始

```bash
# 克隆项目
git clone https://github.com/TsukuyomiAlice/YTLA

# 后端依赖安装
cd ytla_plan
pip install -r requirements.txt

# 启动开发环境
flask run
```

## 当前进展

- 已完成基础框架搭建
- 实现模块/卡片容器系统
- 支持模块间数据通信
- 内置系统模块：
  - 计划管理器（Plan Manager）
  - 工作台（Plan Dashboard）
  - 模块选择器（Module Selector）
  - 国际化支持

## 下一步计划

- 账户与权限管理系统
- 多用户协作功能
- 开发者脚手架工具
- AI 能力集成
- 社区文档完善