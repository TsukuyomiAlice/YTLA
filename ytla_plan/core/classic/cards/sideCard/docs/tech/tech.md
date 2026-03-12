# SideCard 模块技术文档

## 目录

- [1. 模块概述](#1-模块概述)
  - [1.1 模块定位](#11-模块定位)
  - [1.2 主要功能](#12-主要功能)
  - [1.3 设计目标](#13-设计目标)
  - [1.4 在 YTLA 系统中的位置](#14-在-ytla-系统中的位置)
  - [1.5 使用场景](#15-使用场景)
- [2. 文件结构说明](#2-文件结构说明)
  - [2.1 核心目录说明](#21-核心目录说明)
  - [2.2 关键文件说明](#22-关键文件说明)
  - [2.3 文件命名规范](#23-文件命名规范)
- [3. 核心组件说明](#3-核心组件说明)
  - [3.1 CardHandler 抽象基类](#31-cardhandler-抽象基类)
  - [3.2 CardHandlerFactory 工厂类](#32-cardhandlerfactory-工厂类)
  - [3.3 CardHandlerSample 示例类](#33-cardhandlersample-示例类)
  - [3.4 processCards 业务逻辑模块](#34-processcards-业务逻辑模块)
  - [3.5 daoCards 数据访问模块](#35-daocards-数据访问模块)
  - [3.6 routeCards API 路由模块](#36-routecards-api-路由模块)
  - [3.7 组件关系图](#37-组件关系图)
- [4. API 接口说明](#4-api-接口说明)
  - [4.1 API 端点概览](#41-api-端点概览)
  - [4.2 详细接口说明](#42-详细接口说明)
  - [4.3 认证和授权](#43-认证和授权)
  - [4.4 使用示例](#44-使用示例)
- [5. 数据处理流程说明](#5-数据处理流程说明)
  - [5.1 数据流程图](#51-数据流程图)
  - [5.2 数据流向详细说明](#52-数据流向详细说明)
  - [5.3 核心数据处理场景](#53-核心数据处理场景)
  - [5.4 数据模型说明](#54-数据模型说明)
  - [5.5 错误处理和异常流程](#55-错误处理和异常流程)
- [6. 配置和部署说明](#6-配置和部署说明)
  - [6.1 环境要求](#61-环境要求)
  - [6.2 配置选项](#62-配置选项)
  - [6.3 部署步骤](#63-部署步骤)
  - [6.4 环境变量配置](#64-环境变量配置)
  - [6.5 常见问题排查](#65-常见问题排查)
  - [6.6 性能优化建议](#66-性能优化建议)
- [7. 扩展和开发指南](#7-扩展和开发指南)
  - [7.1 扩展架构概览](#71-扩展架构概览)
  - [7.2 添加新卡片类型的步骤](#72-添加新卡片类型的步骤)
  - [7.3 扩展最佳实践](#73-扩展最佳实践)
  - [7.4 集成测试指南](#74-集成测试指南)
  - [7.5 常见扩展场景](#75-常见扩展场景)
  - [7.6 代码贡献指南](#76-代码贡献指南)
  - [7.7 故障排除](#77-故障排除)

## 1. 模块概述

SideCard 模块是 YTLA 中处理侧边卡片功能的核心模块。该模块负责管理系统中的各种卡片类型，如任务卡片、笔记卡片、提醒卡片等，提供卡片的创建、更新、查询、删除等完整生命周期管理功能。

### 1.1 模块定位
SideCard 模块位于 YTLA 系统的核心层，作为卡片功能的基础设施，为上层的业务逻辑和用户界面提供统一的卡片管理接口。模块采用分层架构设计，将数据持久化、业务逻辑处理、API 接口和动态扩展机制分离，确保系统的高内聚、低耦合。

### 1.2 主要功能
- **卡片管理**: 提供卡片的增删改查（CRUD）操作，支持软删除和激活状态管理。
- **动态处理器加载**: 通过 CardHandlerFactory 自动扫描和注册卡片处理器，支持动态扩展新的卡片类型。
- **统一 API 接口**: 提供 RESTful API 接口，供前端和其他模块调用。
- **数据持久化**: 使用 SQLite 数据库存储卡片数据，通过 DAO 层封装数据库操作。
- **卡片处理器抽象**: 定义 CardHandler 抽象基类，规范不同卡片类型的业务逻辑实现。

### 1.3 设计目标
- **可扩展性**: 通过动态加载机制，无需修改核心代码即可添加新的卡片类型。
- **可维护性**: 清晰的模块分层和职责分离，便于代码维护和调试。
- **灵活性**: 支持多种卡片类型和子类型，适应不同的业务场景需求。
- **可靠性**: 完善的错误处理和日志记录机制，确保系统稳定运行。

### 1.4 在 YTLA 系统中的位置
SideCard 模块属于 YTLA 系统的核心功能模块之一，与其他模块如用户管理、权限控制、通知系统等协同工作。模块通过统一的 API 接口与前端界面交互，同时为其他业务模块提供卡片数据支持。

### 1.5 使用场景
- **个人任务管理**: 用户创建和管理个人任务卡片，设置任务优先级、截止日期等。
- **笔记记录**: 创建笔记卡片，记录重要信息和想法。
- **提醒设置**: 设置定时提醒卡片，用于重要事件提醒。
- **自定义卡片类型**: 开发者可以根据业务需求扩展新的卡片类型，如习惯追踪、日程安排等。

## 2. 文件结构说明

SideCard 模块采用标准的 Python 包结构，主要目录和文件如下：

```
sideCard/
├── __init__.py
├── readme.md
├── ai_tools/
│   └── __init__.py
├── api/
│   └── __init__.py
├── caller/
│   └── __init__.py
├── const/
│   └── __init__.py
├── dao/
│   ├── __init__.py
│   └── daoCards.py
├── dataset/
│   └── __init__.py
├── docs/
│   └── readme/
│       ├── en-US/
│       │   └── readme.md
│       └── zh-CN/
│           └── readme.md
├── func/
│   └── __init__.py
├── instance/
│   └── __init__.py
├── process/
│   ├── __init__.py
│   ├── processCardHandler.py
│   ├── processCardHandlerFactory.py
│   ├── processCardHandlerSample.py
│   └── processCards.py
├── prompts/
│   └── __init__.py
├── routes/
│   ├── __init__.py
│   └── routeCards.py
├── schedule/
│   └── __init__.py
├── script/
│   └── __init__.py
└── utils/
    └── __init__.py
```

### 2.1 核心目录说明

- **process/**: 包含卡片处理的核心逻辑，包括 CardHandler 抽象基类、工厂类和业务处理函数。
- **dao/**: 数据访问层，包含数据库操作和卡片实例类。
- **routes/**: API 路由层，定义 RESTful 端点。
- **docs/**: 文档目录，包含多语言用户文档。
- **其他目录**: 预留的功能目录，目前主要为空，用于未来功能扩展。

### 2.2 关键文件说明

1. **processCardHandler.py**: 定义 CardHandler 抽象基类，规范卡片处理器的接口。
2. **processCardHandlerFactory.py**: 实现 CardHandlerFactory 类，负责动态扫描、加载和注册卡片处理器。
3. **processCards.py**: 包含卡片业务逻辑函数，如卡片的增删改查操作。
4. **daoCards.py**: 数据库访问对象，提供对 CARDS 表的 CRUD 操作。
5. **routeCards.py**: Flask 蓝图定义，提供卡片管理的 REST API。

### 2.3 文件命名规范

- 处理器文件以 `process` 前缀开头，如 `processCardHandler.py`
- 数据访问文件以 `dao` 前缀开头，如 `daoCards.py`
- 路由文件以 `route` 前缀开头，如 `routeCards.py`
- 配置文件通常放在 `const/` 目录下

## 3. 核心组件说明

SideCard 模块包含以下核心组件，每个组件都有明确的职责和接口定义。

### 3.1 CardHandler 抽象基类

**位置**: `process/processCardHandler.py`

**职责**: 定义卡片处理器的统一接口，所有具体的卡片处理器必须继承此类并实现抽象方法。

**主要方法**:
- `handle(data: dict, mode: str, card_id: int = 0) -> bool`: 处理卡片的添加或更新操作
- `parse_detail(detail: dict) -> dict`: 解析卡片详情数据，根据卡片子类型进行定制化解析
- `soft_update(card_id: int, action: str) -> dict`: 执行卡片的软更新操作
- `get_default_name() -> str`: 获取卡片的默认名称（静态方法）

**设计目的**: 通过抽象基类确保所有卡片处理器遵循相同的接口规范，便于工厂类统一管理和调用。

### 3.2 CardHandlerFactory 工厂类

**位置**: `process/processCardHandlerFactory.py`

**职责**: 负责动态扫描、加载和注册卡片处理器，提供处理器实例的获取功能。

**核心方法**:
- `register_handler(card_type, card_sub_type, handler)`: 手动注册卡片处理器
- `get_handler(card_type, card_sub_type)`: 根据卡片类型和子类型获取对应的处理器实例
- `scan_card_handler_files()`: 扫描 features 目录下的卡片处理器文件
- `load_and_register_handlers()`: 动态加载并注册所有卡片处理器
- `get_card_type_from_sub_type(card_sub_type)`: 根据卡片子类型推断卡片类型

**设计特点**:
- 懒加载模式：只有在首次获取处理器时才进行扫描和注册
- 自动发现：自动扫描 features 目录下的处理器文件，无需手动注册
- 错误隔离：单个处理器加载失败不影响其他处理器的注册

### 3.3 CardHandlerSample 示例类

**位置**: `process/processCardHandlerSample.py`

**职责**: 提供卡片处理器的实现示例，展示如何继承 CardHandler 并实现抽象方法。

**示例作用**:
- 演示卡片处理器的基本结构
- 提供新处理器开发的参考模板
- 展示日志装饰器的使用方法

### 3.4 processCards 业务逻辑模块

**位置**: `process/processCards.py`

**职责**: 封装卡片管理的核心业务逻辑，提供高层级的卡片操作函数。

**主要函数**:
- `get_cards(**kwargs)`: 获取卡片列表，支持按卡片类型过滤
- `update_card(card_id, update_params)`: 更新卡片的基本信息
- `soft_delete_card(card_id)`: 软删除卡片（标记删除标志）
- `deactivate_card(card_id)`: 停用卡片（标记为未激活）
- `card_router(data, mode, card_id=0)`: 卡片操作的路由函数，根据卡片类型调用对应的处理器
- `parse_card_data(card)`: 解析卡片数据，调用对应处理器解析详情参数
- `soft_update_card(card_id, action)`: 执行卡片的软更新操作

**设计原则**: 业务逻辑与数据访问分离，通过工厂类获取处理器，确保业务逻辑的清晰和可维护性。

### 3.5 daoCards 数据访问模块

**位置**: `dao/daoCards.py`

**职责**: 封装对 CARDS 表的数据库操作，提供卡片数据的持久化能力。

**核心组件**:
- **Instance 类**: 卡片实例类，提供面向对象的卡片数据操作
- **CRUD 函数**: 提供卡片的增删改查操作函数
- **数据库连接**: 使用 SQLite 数据库，通过 sqliteConnector 执行查询

**主要函数**:
- `add_card(card_type, card_sub_type, card)`: 添加新卡片
- `get_cards(**kwargs)`: 查询卡片列表
- `update_card_detail(card)`: 更新卡片详情
- `soft_delete_card(card_id)`: 软删除卡片
- `get_card_type_info(card_id)`: 获取卡片的类型信息

**设计特点**: 使用参数化查询防止 SQL 注入，提供面向对象和函数式两种操作方式。

### 3.6 routeCards API 路由模块

**位置**: `routes/routeCards.py`

**职责**: 定义卡片管理的 RESTful API 接口，处理 HTTP 请求并调用业务逻辑。

**API 端点**:
- `GET /get_cards`: 获取卡片列表
- `POST /add_card`: 添加新卡片
- `POST /update_card_detail/<card_id>`: 更新卡片详情
- `POST /card_action/<card_id>/<action>`: 执行卡片动作（软更新）
- `POST /update_card/<card_id>`: 更新卡片基本信息
- `POST /update_card/<card_id>/tags`: 更新卡片标签
- `POST /delete_card/<card_id>`: 删除卡片
- `POST /deactivate_card/<card_id>`: 停用卡片

**设计特点**: 使用 Flask Blueprint 组织路由，添加日志装饰器记录请求信息，统一的错误处理机制。

### 3.7 组件关系图

```
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────────┐
│   API 路由层     │────▶│   业务逻辑层         │────▶│   数据处理层     │
│  (routeCards)   │     │   (processCards)     │     │   (daoCards)     │
└─────────────────┘     └──────────────────────┘     └──────────────────┘
         │                        │                           │
         │                        │                           │
         ▼                        ▼                           ▼
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────────┐
│   HTTP 请求      │     │   CardHandlerFactory │     │   数据库         │
│   (Flask)       │     │   (工厂模式)          │     │   (SQLite)       │
└─────────────────┘     └──────────────────────┘     └──────────────────┘
                                │
                                │
                                ▼
                       ┌──────────────────┐
                       │   CardHandler    │
                       │   (具体处理器)    │
                       └──────────────────┘
```
组件间采用分层架构，上层依赖下层，通过接口进行通信，确保系统的松耦合和高内聚。

## 4. API 接口说明

SideCard 模块提供完整的 RESTful API 接口，用于卡片的管理和操作。所有 API 均通过 Flask Blueprint 暴露，支持 JSON 格式的请求和响应。

### 4.1 API 端点概览

| 方法 | 端点 | 功能描述 | 认证要求 |
|------|------|----------|----------|
| GET | `/get_cards` | 获取卡片列表 | 可选 |
| POST | `/add_card` | 添加新卡片 | 必需 |
| POST | `/update_card_detail/<int:card_id>` | 更新卡片详情 | 必需 |
| POST | `/card_action/<int:card_id>/<action>` | 执行卡片动作（软更新） | 必需 |
| POST | `/update_card/<int:card_id>` | 更新卡片基本信息 | 必需 |
| POST | `/update_card/<int:card_id>/tags` | 更新卡片标签 | 必需 |
| POST | `/delete_card/<int:card_id>` | 删除卡片（软删除） | 必需 |
| POST | `/deactivate_card/<int:card_id>` | 停用卡片 | 必需 |

### 4.2 详细接口说明

#### 4.2.1 获取卡片列表
- **端点**: `GET /get_cards`
- **功能**: 获取系统中的卡片列表，支持按卡片类型过滤
- **请求参数**:
  - `card_type` (可选): 卡片类型，用于过滤特定类型的卡片
- **响应格式**:
```json
{
  "success": true,
  "cards": [
    {
      "card_id": 1,
      "name": "示例卡片",
      "card_type": "task",
      "card_sub_type": "daily",
      "tags": "工作,重要",
      "description": "这是一个示例卡片",
      "icon_path": "/icons/task.png",
      "background_path": "/backgrounds/default.jpg",
      "detail_params": {
        "priority": "high",
        "due_date": "2024-12-31"
      },
      "delete_flag": "0",
      "active_flag": "1"
    }
  ]
}
```
- **错误响应**:
```json
{
  "success": false,
  "error": "错误信息"
}
```

#### 4.2.2 添加新卡片
- **端点**: `POST /add_card`
- **功能**: 添加新的卡片到系统
- **请求体**:
```json
{
  "name": "新卡片",
  "card_type": "task",
  "card_sub_type": "daily",
  "tags": "工作,重要",
  "description": "卡片描述",
  "icon_path": "/icons/task.png",
  "background_path": "/backgrounds/default.jpg",
  "detail_params": {
    "priority": "medium",
    "due_date": "2024-12-31"
  }
}
```
- **响应格式**:
```json
{
  "success": true
}
```
- **说明**: 卡片添加成功后，系统会自动调用对应的卡片处理器处理卡片数据。

#### 4.2.3 更新卡片详情
- **端点**: `POST /update_card_detail/<int:card_id>`
- **功能**: 更新指定卡片的详细信息
- **请求体**: 包含需要更新的字段，字段名需与卡片详情中的字段对应
- **响应格式**:
```json
{
  "success": true
}
```

#### 4.2.4 执行卡片动作（软更新）
- **端点**: `POST /card_action/<int:card_id>/<action>`
- **功能**: 执行卡片的特定动作，如标记完成、取消完成等
- **路径参数**:
  - `card_id`: 卡片ID
  - `action`: 动作名称，如 "complete", "cancel" 等
- **响应格式**:
```json
{
  "success": true,
  "data": {
    "updated_fields": ["status", "completion_time"]
  }
}
```

#### 4.2.5 更新卡片基本信息
- **端点**: `POST /update_card/<int:card_id>`
- **功能**: 更新卡片的基本信息，如名称、描述、标签等
- **请求体**: 包含需要更新的字段
- **响应格式**:
```json
{
  "success": true
}
```

#### 4.2.6 更新卡片标签
- **端点**: `POST /update_card/<int:card_id>/tags`
- **功能**: 更新卡片的标签信息
- **请求体**:
```json
{
  "tags": "新标签1,新标签2"
}
```
- **响应格式**:
```json
{
  "success": true
}
```

#### 4.2.7 删除卡片
- **端点**: `POST /delete_card/<int:card_id>`
- **功能**: 软删除指定卡片（标记删除标志，不物理删除）
- **响应格式**:
```json
{
  "success": true
}
```

#### 4.2.8 停用卡片
- **端点**: `POST /deactivate_card/<int:card_id>`
- **功能**: 停用指定卡片（标记为未激活状态）
- **响应格式**:
```json
{
  "success": true
}
```

### 4.3 认证和授权
- **认证方式**: 基于 JWT Token 的认证（具体实现依赖系统整体认证方案）
- **授权要求**: 部分敏感操作需要用户权限验证
- **错误码**:
  - `401 Unauthorized`: 未提供有效的认证令牌
  - `403 Forbidden`: 用户无权执行该操作
  - `404 Not Found`: 卡片不存在
  - `500 Internal Server Error`: 服务器内部错误

### 4.4 使用示例
```python
import requests

# 获取卡片列表
response = requests.get('http://localhost:5000/get_cards')
cards = response.json()['cards']

# 添加新卡片
new_card = {
    "name": "新任务",
    "card_type": "task",
    "card_sub_type": "work",
    "tags": "工作,重要",
    "description": "完成项目文档",
    "detail_params": {
        "priority": "high",
        "due_date": "2024-12-31"
    }
}
response = requests.post('http://localhost:5000/add_card', json=new_card)
```

## 5. 数据处理流程说明

SideCard 模块的数据处理遵循清晰的分层架构，从数据接收、业务处理到数据存储，每个环节都有明确的职责和规范。

### 5.1 数据流程图

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│  前端/客户端  │───▶│   API 路由层  │───▶│ 业务逻辑层  │───▶│ 数据访问层  │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
                        │                       │                   │
                        ▼                       ▼                   ▼
                 ┌─────────────┐        ┌─────────────┐    ┌─────────────┐
                 │  请求验证    │        │  处理器工厂  │    │  数据库操作  │
                 │  & 日志记录  │        │  & 处理器调用 │    │  & 事务管理  │
                 └─────────────┘        └─────────────┘    └─────────────┘
```

### 5.2 数据流向详细说明

#### 5.2.1 数据接收阶段
1. **客户端请求**: 前端或其他客户端通过 HTTP 请求调用 SideCard API
2. **路由处理**: `routeCards.py` 中的 Flask Blueprint 接收请求，进行基本的请求验证和日志记录
3. **参数解析**: 解析请求参数和 JSON 数据，转换为 Python 字典格式

#### 5.2.2 业务处理阶段
1. **业务逻辑调用**: 路由层调用 `processCards.py` 中的相应业务函数
2. **处理器获取**: 通过 `CardHandlerFactory.get_handler()` 根据卡片类型和子类型获取对应的处理器实例
3. **处理器执行**: 调用处理器的 `handle()`、`parse_detail()` 或 `soft_update()` 方法执行具体的业务逻辑
4. **数据转换**: 处理器对数据进行业务特定的转换和处理

#### 5.2.3 数据存储阶段
1. **DAO 层调用**: 业务逻辑层调用 `daoCards.py` 中的数据库操作函数
2. **实例对象操作**: 使用 `Instance` 类进行面向对象的数据库操作，或直接使用 CRUD 函数
3. **数据库执行**: 通过 `sqliteConnector` 执行参数化 SQL 查询，确保数据安全和一致性
4. **事务管理**: 关键操作使用数据库事务保证数据完整性

#### 5.2.4 响应返回阶段
1. **结果封装**: 将处理结果封装为标准化的响应格式
2. **错误处理**: 捕获和处理过程中出现的异常，转换为友好的错误信息
3. **响应返回**: 将 JSON 格式的响应返回给客户端

### 5.3 核心数据处理场景

#### 5.3.1 卡片添加流程
```
1. 客户端发送 POST /add_card 请求
2. 路由层接收请求，调用 processCards.card_router(data, 'add')
3. card_router 根据 data 中的 card_type 和 card_sub_type 调用 CardHandlerFactory.get_handler()
4. 工厂类动态加载对应的卡片处理器（如未加载则先扫描注册）
5. 调用处理器的 handle() 方法处理卡片数据
6. handle() 方法调用 daoCards.add_card() 将卡片数据存储到数据库
7. 返回处理结果给客户端
```

#### 5.3.2 卡片查询流程
```
1. 客户端发送 GET /get_cards 请求
2. 路由层调用 processCards.get_cards()
3. get_cards() 调用 daoCards.get_cards() 获取原始卡片数据
4. 对每个卡片，根据其 card_type 和 card_sub_type 调用对应的处理器解析 detail_params
5. 合并基础卡片数据和解析后的详情数据
6. 返回完整的卡片列表给客户端
```

#### 5.3.3 卡片更新流程
```
1. 客户端发送 POST /update_card_detail/<card_id> 请求
2. 路由层调用 processCards.card_router(data, 'update', card_id)
3. card_router 根据卡片ID获取卡片类型信息
4. 调用对应的处理器处理更新数据
5. 处理器调用 daoCards.update_card_detail() 更新数据库
6. 返回更新结果给客户端
```

### 5.4 数据模型说明

#### 5.4.1 数据库表结构
```sql
CREATE TABLE CARDS (
    CARD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    CARD_TYPE TEXT NOT NULL,
    CARD_SUB_TYPE TEXT,
    TAGS TEXT,
    DESCRIPTION TEXT,
    ICON_PATH TEXT,
    BACKGROUND_PATH TEXT,
    DETAIL_PARAMS TEXT NOT NULL,
    ACTIVE_FLAG TEXT DEFAULT '1',
    DELETE_FLAG TEXT DEFAULT '0'
)
```

#### 5.4.2 核心数据字段
- **CARD_ID**: 卡片唯一标识，自增主键
- **NAME**: 卡片显示名称
- **CARD_TYPE/CARD_SUB_TYPE**: 卡片类型和子类型，用于路由到对应的处理器
- **DETAIL_PARAMS**: JSON 格式的卡片详情数据，不同卡片类型有不同结构
- **ACTIVE_FLAG/DELETE_FLAG**: 状态标志，支持软删除和激活状态管理

#### 5.4.3 数据转换规则
- **数据库到对象**: `Instance` 类将数据库记录转换为对象属性
- **对象到字典**: `convert_to_dict()` 函数将 `Instance` 对象转换为字典
- **字典到JSON**: `json.dumps()` 将字典转换为 JSON 字符串存储
- **JSON到字典**: `json.loads()` 将存储的 JSON 字符串解析为字典

### 5.5 错误处理和异常流程

#### 5.5.1 错误类型
- **验证错误**: 请求参数不符合要求
- **处理器未找到错误**: 卡片类型对应的处理器未注册
- **数据库错误**: SQL 执行失败或数据不一致
- **业务逻辑错误**: 卡片状态不符合操作要求

#### 5.5.2 错误处理机制
1. **异常捕获**: 使用 try-except 块捕获各级异常
2. **错误日志**: 使用 `process_log` 和 `router_log` 装饰器记录错误信息
3. **错误响应**: 统一返回 `{"success": false, "error": "错误信息"}` 格式
4. **错误恢复**: 数据库操作失败时自动回滚事务

#### 5.5.3 容错设计
- **处理器加载容错**: 单个处理器加载失败不影响其他处理器注册
- **数据库连接池**: 使用连接池管理数据库连接，避免连接泄漏
- **请求超时处理**: 长时间操作设置超时限制，避免阻塞
- **数据备份**: 定期备份卡片数据，防止数据丢失

## 6. 配置和部署说明

SideCard 模块设计为即插即用，但为了适应不同的部署环境，提供了一些配置选项和部署指导。

### 6.1 环境要求

#### 6.1.1 软件依赖
- **Python**: 3.8 或更高版本
- **Flask**: 2.0 或更高版本（用于 API 路由）
- **SQLite**: 3.0 或更高版本（嵌入式数据库）
- **其他依赖**: 具体依赖项参考项目根目录的 `requirements.txt` 文件

#### 6.1.2 系统要求
- **内存**: 至少 256MB 可用内存
- **存储**: 至少 100MB 可用磁盘空间（用于数据库和日志）
- **网络**: 如果提供 API 服务，需要网络端口访问权限

### 6.2 配置选项

#### 6.2.1 数据库配置
- **数据库路径**: 默认使用 `life_plan` 数据库，可通过修改 `daoCards.py` 中的 `db_name` 变量更改
- **表名**: 卡片表默认为 `CARDS`，可通过修改 `table_name` 变量更改
- **连接参数**: 数据库连接参数通过 `sqliteConnector` 模块统一管理

#### 6.2.2 处理器扫描配置
- **扫描目录**: 默认扫描 `features/` 目录下的卡片处理器，可通过修改 `processCardHandlerFactory.py` 中的 `features_dir` 逻辑调整
- **文件匹配规则**: 处理器文件需满足 `process*.py` 命名模式，可通过修改 `scan_card_handler_files` 方法调整
- **懒加载设置**: 处理器工厂默认使用懒加载模式，首次调用时扫描注册

#### 6.2.3 日志配置
- **日志级别**: 通过 `loggerConfig` 模块统一配置日志级别
- **日志文件**: 日志文件路径和格式可在系统配置中设置
- **请求日志**: API 请求日志通过 `router_log` 装饰器自动记录
- **处理日志**: 业务处理日志通过 `process_log` 装饰器自动记录

#### 6.2.4 API 配置
- **API 前缀**: 可通过修改 `routeCards.py` 中的 Blueprint 注册前缀调整 API 路径
- **CORS 设置**: 跨域资源共享配置需在 Flask 应用层设置
- **速率限制**: API 速率限制需在应用层或通过中间件实现

### 6.3 部署步骤

#### 6.3.1 本地开发环境部署
1. **克隆代码**: 获取项目代码到本地
2. **安装依赖**: 运行 `pip install -r requirements.txt` 安装 Python 依赖
3. **数据库初始化**: 系统首次启动时会自动创建 `CARDS` 表（如果不存在）
4. **启动服务**: 运行 Flask 应用，SideCard 模块会自动集成到应用中
5. **验证部署**: 访问 `GET /get_cards` 接口验证模块是否正常工作

#### 6.3.2 生产环境部署
1. **环境隔离**: 使用虚拟环境或容器隔离 Python 环境
2. **数据库优化**: 根据数据量调整 SQLite 配置参数，或迁移到更强大的数据库（如 PostgreSQL）
3. **安全配置**: 配置 HTTPS、API 认证、防火墙规则等安全措施
4. **监控设置**: 设置日志监控、性能监控和错误告警
5. **备份策略**: 定期备份数据库文件，制定数据恢复方案

#### 6.3.3 容器化部署
```dockerfile
# 基于 Python 官方镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 5000

# 启动命令
CMD ["python", "app.py"]
```

### 6.4 环境变量配置

SideCard 模块支持通过环境变量进行配置，以下为可用的环境变量：

| 环境变量 | 默认值 | 说明 |
|----------|--------|------|
| `CARDS_DB_PATH` | `life_plan` | 数据库文件路径 |
| `CARDS_TABLE_NAME` | `CARDS` | 卡片表名 |
| `CARDS_SCAN_DIR` | `features/` | 处理器扫描目录 |
| `CARDS_LOG_LEVEL` | `INFO` | 日志级别 |
| `CARDS_API_PREFIX` | `/card` | API 路径前缀 |

环境变量在模块初始化时读取，优先级高于代码中的硬编码配置。

### 6.5 常见问题排查

#### 6.5.1 处理器无法加载
- **症状**: 添加卡片时提示 "Unregistered card type"
- **可能原因**: 处理器文件命名不符合规范、处理器类未继承 CardHandler、处理器文件不在扫描目录中
- **解决方案**: 检查处理器文件命名、类定义和文件位置，查看工厂类加载日志

#### 6.5.2 数据库连接失败
- **症状**: API 调用返回数据库错误
- **可能原因**: 数据库文件权限问题、磁盘空间不足、数据库文件损坏
- **解决方案**: 检查数据库文件权限和磁盘空间，尝试修复或重建数据库

#### 6.5.3 API 响应缓慢
- **症状**: API 请求响应时间过长
- **可能原因**: 数据库查询未优化、处理器扫描耗时、系统资源不足
- **解决方案**: 优化数据库查询语句、调整处理器扫描策略、增加系统资源

#### 6.5.4 数据不一致
- **症状**: 卡片数据显示异常或丢失
- **可能原因**: 并发操作导致的数据竞争、事务未正确使用、数据迁移问题
- **解决方案**: 检查事务使用情况、优化并发控制、验证数据迁移脚本

### 6.6 性能优化建议

1. **数据库索引**: 在 `CARD_TYPE`、`CARD_SUB_TYPE`、`ACTIVE_FLAG` 等常用查询字段上创建索引
2. **查询优化**: 避免 `SELECT *`，只查询需要的字段，合理使用分页
3. **缓存策略**: 对频繁读取的卡片数据添加缓存层（如 Redis）
4. **连接池**: 使用数据库连接池管理数据库连接，避免频繁创建连接
5. **异步处理**: 将耗时的卡片处理操作改为异步任务，提高 API 响应速度

## 7. 扩展和开发指南

SideCard 模块设计为高度可扩展，开发者可以轻松添加新的卡片类型和处理器。本章节提供完整的扩展开发指南。

### 7.1 扩展架构概览

SideCard 模块的扩展性主要体现在以下方面：
- **动态处理器发现**: 通过 CardHandlerFactory 自动扫描和注册新的卡片处理器
- **抽象接口设计**: CardHandler 抽象基类定义了统一的处理器接口
- **配置化扩展**: 通过目录结构和命名约定实现无配置扩展

### 7.2 添加新卡片类型的步骤

#### 7.2.1 创建处理器文件
1. 在 `features/<feature_name>/cards/sideCard/process/` 目录下创建新的处理器文件
2. 文件命名遵循 `process<CardType>Handler.py` 模式，如 `processTaskHandler.py`
3. 文件内容需包含继承自 CardHandler 的处理器类

#### 7.2.2 实现处理器类
```python
# encode = utf-8

from core.classic.frame._type.func.loggerConfig import process_log
from core.classic.cards.sideCard.process.processCardHandler import CardHandler

class TaskCardHandler(CardHandler):
    # 定义卡片类型和子类型（类属性）
    card_type = 'task'
    card_sub_type = 'daily'
    
    def __init__(self):
        # 初始化逻辑
        pass
    
    @process_log
    def handle(self, data: dict, mode: str, card_id: int = 0) -> bool:
        """处理任务的添加或更新"""
        # 实现具体的业务逻辑
        if mode == 'add':
            return self._add_task(data)
        elif mode == 'update':
            return self._update_task(card_id, data)
        return False
    
    @process_log
    def parse_detail(self, detail: dict) -> dict:
        """解析任务详情数据"""
        # 实现详情数据解析逻辑
        return {
            'priority': detail.get('priority', 'medium'),
            'due_date': detail.get('due_date'),
            'status': detail.get('status', 'pending')
        }
    
    @process_log
    def soft_update(self, card_id: int, action: str) -> dict:
        """执行任务的软更新操作"""
        # 实现软更新逻辑
        if action == 'complete':
            return self._complete_task(card_id)
        elif action == 'cancel':
            return self._cancel_task(card_id)
        return {'success': False, 'error': f'未知动作: {action}'}
    
    @staticmethod
    def get_default_name(self) -> str:
        """获取任务的默认名称"""
        return '任务卡片'
    
    # 私有方法实现具体业务逻辑
    def _add_task(self, data: dict) -> bool:
        # 添加任务的具体实现
        return True
    
    def _update_task(self, card_id: int, data: dict) -> bool:
        # 更新任务的具体实现
        return True
    
    def _complete_task(self, card_id: int) -> dict:
        # 完成任务的具体实现
        return {'success': True, 'completed_at': '2024-12-31'}
    
    def _cancel_task(self, card_id: int) -> dict:
        # 取消任务的具体实现
        return {'success': True, 'cancelled_at': '2024-12-31'}
```

#### 7.2.3 配置卡片类型属性
- **card_type**: 卡片类型标识，如 'task', 'note', 'reminder' 等
- **card_sub_type**: 卡片子类型标识，如 'daily', 'work', 'personal' 等
- 这两个属性必须作为类属性定义，工厂类依赖它们进行注册

#### 7.2.4 测试新处理器
1. 启动应用，检查处理器是否被自动扫描和注册
2. 调用相关 API 测试新卡片类型的添加、查询、更新等功能
3. 验证业务逻辑是否正确执行

### 7.3 扩展最佳实践

#### 7.3.1 代码组织规范
- **单一职责**: 每个处理器只处理一种卡片类型
- **功能完整**: 处理器应完整实现所有抽象方法
- **错误处理**: 在处理器内部进行充分的错误处理和验证
- **日志记录**: 使用 `@process_log` 装饰器记录关键操作

#### 7.3.2 数据设计规范
- **详情数据结构**: 设计清晰的详情数据结构，便于前端使用
- **数据验证**: 在处理器中进行数据验证，确保数据质量
- **数据转换**: 合理处理数据格式转换，确保数据一致性

#### 7.3.3 性能考虑
- **懒加载**: 耗时的初始化操作应延迟到首次使用时执行
- **缓存策略**: 频繁访问的数据考虑添加缓存
- **批量操作**: 支持批量操作，减少数据库访问次数

### 7.4 集成测试指南

#### 7.4.1 单元测试
```python
import unittest
from features.task.cards.sideCard.process.processTaskHandler import TaskCardHandler

class TestTaskCardHandler(unittest.TestCase):
    def setUp(self):
        self.handler = TaskCardHandler()
    
    def test_handle_add(self):
        data = {'name': '测试任务', 'priority': 'high'}
        result = self.handler.handle(data, 'add')
        self.assertTrue(result)
    
    def test_parse_detail(self):
        detail = {'priority': 'high', 'due_date': '2024-12-31'}
        result = self.handler.parse_detail(detail)
        self.assertIn('priority', result)
        self.assertEqual(result['priority'], 'high')
```

#### 7.4.2 集成测试
1. **API 测试**: 测试新卡片类型的完整 API 流程
2. **数据库测试**: 验证数据是否正确存储和检索
3. **并发测试**: 测试多用户同时操作新卡片类型的情况
4. **错误测试**: 测试异常情况下的系统行为

### 7.5 常见扩展场景

#### 7.5.1 添加新的卡片类型
- **场景**: 需要支持新的卡片类型，如 'habit'（习惯追踪）
- **步骤**: 创建 `processHabitHandler.py`，实现 HabitCardHandler 类
- **关键点**: 定义 habit 特有的详情数据结构和业务逻辑

#### 7.5.2 添加卡片子类型
- **场景**: 在现有卡片类型下添加新的子类型，如 'task' 类型下的 'urgent' 子类型
- **步骤**: 创建新的处理器或扩展现有处理器
- **关键点**: 保持与现有卡片类型的兼容性

#### 7.5.3 扩展现有处理器功能
- **场景**: 为现有卡片类型添加新功能
- **步骤**: 修改现有处理器，添加新的方法或扩展现有方法
- **关键点**: 保持向后兼容，不影响现有功能

### 7.6 代码贡献指南

#### 7.6.1 代码规范
- **命名规范**: 遵循项目现有的命名约定
- **注释要求**: 为复杂的业务逻辑添加注释
- **文档更新**: 扩展功能时同步更新相关文档

#### 7.6.2 提交要求
1. **功能完整**: 确保新功能完整实现并通过测试
2. **测试覆盖**: 为新功能添加相应的单元测试和集成测试
3. **文档更新**: 更新技术文档和用户文档
4. **代码审查**: 提交代码前进行自我审查，确保代码质量

#### 7.6.3 版本管理
- **特性分支**: 在新特性分支上进行开发
- **合并请求**: 通过合并请求将代码合并到主分支
- **版本标签**: 重要功能发布时添加版本标签

### 7.7 故障排除

#### 7.7.1 处理器未被注册
- **检查点**: 文件命名、类属性定义、继承关系、扫描目录
- **调试方法**: 查看工厂类加载日志，确认扫描过程

#### 7.7.2 业务逻辑错误
- **检查点**: 方法实现、数据验证、错误处理
- **调试方法**: 添加详细日志，使用调试工具逐步执行

#### 7.7.3 性能问题
- **检查点**: 数据库查询、循环逻辑、资源管理
- **调试方法**: 使用性能分析工具定位瓶颈，优化关键路径