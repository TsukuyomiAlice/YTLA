<p>
 语言
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>


# llm_caller - deepseek

### YTLA特性

### YTLA Development Team

version 1.0

后端语言及开发框架: Python-Flask  
适用YTLA core版本: **classic**  
文件更新日期: 2026-03-10

## 概念

DeepSeek 大语言模型聊天调用模组，支持 HTTP Request 和 OpenAI SDK 两种调用方式。该模组提供统一接口调用 DeepSeek API，支持聊天对话、参数配置等功能。

## 特性包目录

本模组包含以下子目录及其用途：

| 目录       | 用途说明                                  |
|----------|---------------------------------------|
| const    | 常量配置，包含 API 端点、模型配置、默认参数等       |
| api      | API 调用实现，包含 HTTP 和 OpenAI SDK 两种方式   |
| caller   | 统一调用接口，提供对 API 层的封装                  |
| instance | 数据实例类型，定义 ChatMessage、ChatRequest 等类型 |
| func     | 通用函数                                 |
| routes   | Flask 路由                              |
| process  | 业务逻辑处理，提供 process_simple_chat 等高层函数   |
| docs     | 文档目录                                  |
| ai_tools | AI 工具                                 |
| dao      | 数据存储访问                               |
| dataset  | 稳定数据集                                 |
| schedule | 计划任务                                 |
| script   | 调用脚本                                 |
| utils    | 配置参数                                 |

## 使用示例

### 导入和使用 chat 函数

```python
from features.llm_caller.modules.deepseek.caller.callerDeepseekChat import chat

messages = [
    {"role": "user", "content": "你好，请介绍一下自己"}
]

response = chat(
    messages=messages,
    model="deepseek-chat",
    temperature=0.7,
    call_mode="openai"
)

print(response)
```

### 使用 process_simple_chat 函数（推荐）

```python
from features.llm_caller.modules.deepseek.process.processDeepseekChat import process_simple_chat

response = process_simple_chat(
    user_message="什么是人工智能？",
    system_prompt="你是一个专业的技术顾问",
    model="deepseek-chat",
    temperature=0.5
)

print(response)
```
