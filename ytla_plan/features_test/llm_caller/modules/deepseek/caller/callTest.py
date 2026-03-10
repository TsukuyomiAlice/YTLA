from ytla_plan.features.llm_caller.modules.deepseek.caller.callerDeepseekChat import chat

messages = [
    {"role": "user", "content": "问一个很经典的问题：3.9和3.11哪个更大？"}
]

response = chat(
    messages=messages,
    model="deepseek-chat",
    temperature=0.7,
    call_mode="openai"
)

print(response)