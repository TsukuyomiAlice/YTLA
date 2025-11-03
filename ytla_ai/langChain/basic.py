# encode = utf-8

# llm model start ==================================================

from langchain_openai import ChatOpenAI
from ytla_ai.deepseek import api_key

llm_1 = ChatOpenAI(model="deepseek-chat", api_key=api_key.DEEPSEEK_API_KEY_1, base_url="https://api.deepseek.com", temperature=0.0)
llm_2 = ChatOpenAI(model="deepseek-chat", api_key=api_key.DEEPSEEK_API_KEY_2, base_url="https://api.deepseek.com", temperature=0.0)

# llm model end ===========================================================

# tools start ==================================================
from langchain_core.messages import AIMessage
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
model_with_tools_2 = llm_2.bind_tools(tools=tools)
# tools end ==================================================



# langGraph start =============================================
"""
Reference
https://www.studywithgpt.com/zh-cn/tutorial/cf6hwi
ReAct代理模式
"""
from langgraph.graph import StateGraph, MessagesState, START, END

def default_answer(state: MessagesState):
    messages = state["messages"]
    response = llm_1.invoke(messages)
    return {"messages": [response]}

def should_continue(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return "default" # 原先是直接END了

def should_compare(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools_2"
    return "default" # 原先是直接END了

def has_next(state: MessagesState):
    pass

def call_model(state: MessagesState):
    messages = state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

def call_model_2(state: MessagesState):
    messages = state["messages"]
    response = model_with_tools_2.invoke(messages)
    return {"messages": [response]}

workflow = StateGraph(MessagesState)

# 定义两个节点，以便循环调用
# 这句话是从样例代码那边抄来的，但其实不太对。按照图的描述，其实并不是循环调用的含义，而是START - agent - should_continue？ tools: END 的逻辑

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)

workflow.add_node("next", has_next)

workflow.add_node("agent_2", call_model_2, defer=True)
workflow.add_node("tools_2", tool_2_node)

workflow.add_node("default", default_answer)

workflow.add_edge(START, "agent")
workflow.add_conditional_edges("agent", should_continue, ["tools", "default"])
workflow.add_edge("tools", "agent")

workflow.add_edge("agent", "next")
workflow.add_edge("next", "agent_2")

workflow.add_conditional_edges("agent_2", should_compare, ["tools_2", "default"])
workflow.add_edge("tools_2", "agent_2")

workflow.add_edge("default", END)

"""
如果使用default，那么改为使用两个END点
不使用default的场合代码如下
workflow.add_conditional_edges("agent", should_continue, ["tools", END])
workflow.add_edge("tools", "agent")
"""

app = workflow.compile()
print(app.get_graph().draw_mermaid())
# langGraph end =============================================


# chat display start  =============================================
def chat(msg):
    for chunk in app.stream({"messages": [(msg)]}, stream_mode="values"):
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
        # 捕获异常并提供默认输入
        print(f"发生错误: {e}，尝试默认问题...")
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        chat(user_input)
        break
