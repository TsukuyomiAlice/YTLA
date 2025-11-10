# encode = utf-8

# llm model start ==================================================

from langchain_openai import ChatOpenAI
from ytla_ai.deepseek import api_key

# 设置llm
llm_d1 = ChatOpenAI(model="deepseek-chat", api_key=api_key.DEEPSEEK_API_KEY_1, base_url="https://api.deepseek.com", temperature=0.0)
llm_d2 = ChatOpenAI(model="deepseek-chat", api_key=api_key.DEEPSEEK_API_KEY_2, base_url="https://api.deepseek.com", temperature=0.0)
llm_g1 = ChatOpenAI(model="glm-4.5-flash",api_key=api_key.GLM_API_KEY_1,base_url="https://open.bigmodel.cn/api/paas/v4", temperature=0.0)
llm_g2 = ChatOpenAI(model="glm-4.5-flash",api_key=api_key.GLM_API_KEY_2,base_url="https://open.bigmodel.cn/api/paas/v4", temperature=0.0)

llm_1 = llm_d1
llm_2 = llm_d2
# llm model end ===========================================================

# tools start ==================================================
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode

# 定义工具
@tool
def add(a: int, b: int) -> int:
    """计算两个数的和"""
    return a + b

@tool
def minus(a: int, b: int) -> int:
    """计算两个数的差"""
    return a - b

@tool
def multiply(a: int, b: int) -> int:
    """计算两个数的乘积"""
    return a * b

@tool
def devide(a: int, b: int):
    """计算两个数的商"""
    try:
        return a / b
    except ZeroDivisionError:
        return "除数不能为0"


tools = [add, minus, multiply, devide]
tool_node = ToolNode(tools)
message_with_multiple_tool_calls = AIMessage(
    content="",
    tool_calls=[
        {
            "name": "add",
            "args": {"a": 1, "b": 2},
            "id": "tool_call_id_1",
            "type": "tool_call",
        },
        {
            "name": "minus",
            "args": {"a": 1, "b": 2},
            "id": "tool_call_id_2",
            "type": "tool_call",
        },
        {
            "name": "multiply",
            "args": {"a": 1, "b": 2},
            "id": "tool_call_id_3",
            "type": "tool_call",
        },
        {
            "name": "devide",
            "args": {"a": 1, "b": 2},
            "id": "tool_call_id_4",
            "type": "tool_call",
        },
    ],
)

tool_node.invoke({"messages": [message_with_multiple_tool_calls]})
model_with_tools = llm_1.bind_tools(tools=tools)


# ====================
@tool
def compare(a: int, b: int) -> int:
    """比较两个数的大小"""
    if a > b:
        return f"{a}大于{b}"
    elif a < b:
        return f"{a}小于{b}"
    else:
        return f"{a}等于{b}"

tools_2 = [compare]
tool_2_node = ToolNode(tools_2)
message_with_multiple_tool_2_calls = AIMessage(
    content="",
    tool_calls=[
        {
            "name": "compare",
            "args": {"a": 1, "b": 2},
            "id": "tool_call_id_5",
            "type": "tool_call",
        },
    ],
)
tool_2_node.invoke({"messages": [message_with_multiple_tool_calls]})
model_with_tools_2 = llm_2.bind_tools(tools=tools_2)

# tools end ==================================================



# langGraph start =============================================
"""
Reference
https://www.studywithgpt.com/zh-cn/tutorial/cf6hwi
ReAct代理模式
"""
from langgraph.graph import StateGraph, MessagesState, START, END

def should_continue(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return "agent_2"

def could_compare(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools_2"
    return END # 原先是直接END了


def call_model(state: MessagesState):
    print("HINT : 现在调用了call_model_1")

    system_prompt_1 = """
    你是一个数学计算助手。你可以使用加减乘除四则运算工具
    你会接收到用户的问题。你只负责接收用户的多项式四则运算问题，或者是数值/多项式的计算结果的比较问题
    其中，你需要使用四则运算工具，计算用户提供的多项式四则运算
    你不负责进行数值比较，数值比较交给其它助手处理。
    最后你仅需返回所有的多项式四则运算的结果。
    \n"""

    messages = state["messages"]
    messages_with_system = [SystemMessage(content=system_prompt_1)] + messages
    response = model_with_tools.invoke(messages_with_system)
    return {"messages": [response]}

def call_model_2(state: MessagesState):
    print("HINT : 现在调用了call_model_2")
    system_prompt_2_a = """
    你是一个数值或计算式的比较助手。你可以使用数值比较工具。
    你会负责处理用户的多项式四则运算问题，或者是数值/多项式的计算结果的比较问题
    其中，你需要使用数值比较工具，对数值或者多项式的计算结果进行比较
    你会接收到关于计算的结果。
    最后的关于多项式四则运算的计算结果如下所示。
    \n"""

    system_prompt_2_b = """
    \n
    返回结果时，带上原表达式和计算结果
    """

    messages = state["messages"]
    messages_with_system = [SystemMessage(content=system_prompt_2_a+messages[-1].content+system_prompt_2_b)] + messages
    response = model_with_tools_2.invoke(messages_with_system)
    return {"messages": [response]}

workflow = StateGraph(MessagesState)


workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_node("agent_2", call_model_2, defer=True) # defer=True 表示在调用agent_2时，不立即执行，而是等待条件满足后再执行
workflow.add_node("tools_2", tool_2_node)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, ["tools", "agent_2"])
workflow.add_edge("tools", "agent")


workflow.add_conditional_edges("agent_2", could_compare, ["tools_2", END])
workflow.add_edge("tools_2", "agent_2")

workflow.add_edge("agent_2", END)


app = workflow.compile()
print(app.get_graph().draw_mermaid())
# langGraph end =============================================


# chat display start  =============================================
def chat(msg):
    for chunk in app.stream({"messages": [(msg)]}, stream_mode="values", config={"recursion_limit": 100}):
        chunk["messages"][-1].pretty_print()

# chat display end  =============================================

# main =================================================
while True:
    try:
        # 获取用户输入
        user_input = input("User: ")

        # 退出条件
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        chat(user_input)

    except Exception as e:
        print(f"发生错误: {e}")
        break
