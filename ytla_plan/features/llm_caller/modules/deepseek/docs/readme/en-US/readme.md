<p>
 language
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>


# llm_caller - deepseek

### YTLA Application Feature

### YTLA Development Team

version 1.0

Backend Language and Framework: Python-Flask  
Applicable YTLA core version: **classic**  
File Update Date: 2026-03-10

## Concepts

DeepSeek Large Language Model chat calling module, supporting both HTTP Request and OpenAI SDK calling methods. This module provides a unified interface to call the DeepSeek API, supporting chat conversations, parameter configuration, and other functionalities.

## Feature Package Directory

This module includes the following subdirectories and their purposes:

| Directory | Description |
|-----------|-------------|
| const     | Constant configuration, including API endpoints, model configurations, default parameters, etc. |
| api       | API implementation, including both HTTP and OpenAI SDK methods |
| caller    | Unified calling interface, providing encapsulation for the API layer |
| instance  | Data instance types, defining ChatMessage, ChatRequest, and other types |
| func      | Utility functions |
| routes    | Flask routes |
| process   | Business logic processing, providing high-level functions like process_simple_chat |
| docs      | Documentation directory |
| ai_tools  | AI tools |
| dao       | Data storage access |
| dataset   | Stable datasets |
| schedule  | Scheduled tasks |
| script    | Call scripts |
| utils     | Configuration parameters |

## Usage Examples

### Importing and using the chat function

```python
from features.llm_caller.modules.deepseek.caller.callerDeepseekChat import chat

messages = [
    {"role": "user", "content": "Hello, please introduce yourself"}
]

response = chat(
    messages=messages,
    model="deepseek-chat",
    temperature=0.7,
    call_mode="openai"
)

print(response)
```

### Using the process_simple_chat function (Recommended)

```python
from features.llm_caller.modules.deepseek.process.processDeepseekChat import process_simple_chat

response = process_simple_chat(
    user_message="What is artificial intelligence?",
    system_prompt="You are a professional technical consultant",
    model="deepseek-chat",
    temperature=0.5
)

print(response)
```
