from ytla_plan.features.llm_caller.modules.deepseek.caller.callerDeepseekChat import chat

messages = [
    {"role": "user", "content": "如何在对话中给你上传文档？"}
]

response = chat(
    messages=messages,
    model="deepseek-chat",
    temperature=0.0,
    call_mode="openai"
)

print(response)