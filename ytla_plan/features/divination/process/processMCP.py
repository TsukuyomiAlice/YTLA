# encode = utf-8

from ytla_ai.client import contentHandler, agentHandler
from ytla_plan.features.divination.process import processModulePlumYi

'''
caller = {
  'request_app': <request_app_name>,
  'request_params': {<dict for the params>}
}
'''


def stub_app_caller(caller: dict):
    request_app = caller['request_app']
    if request_app == 'plum_yi':
        print(f"""
======= MCP呼叫结果 =======
request_app: {request_app}
request_params: {caller['request_params']}
==========================
""")
        params = caller['request_params']
        processModulePlumYi.hexagram_solver(input_date=params['input_date'], debug=params['debug'], lan=params['lan'])
    else:
        print(f"""
======= MCP呼叫结果 =======
unknown request app: {request_app}
request_params: {caller['request_params']}
==========================
""")


def chat_to_get_app(request_prompt: str):
    system_prompt = """
# 你的任务是根据用户的请求生成对应的caller。你的返回结果只包含caller，不要夹带其它任何内容。
## caller格式如下
{
  'request_app': <request_app_name>,
  'request_params': {<dict for the params>}
}

# 以下是你可以给用户提供的应用caller，以及具体的caller设置方法。
## 梅花易数
### 如果用户希望用时间占卜运势，可以使用梅花易数
### 梅花易数的默认caller格式如下。如果用户没有提出要求，保持以下内容输出，不要作改动。
{
  "request_app": "plum_yi",
  "request_params": {"input_date": None, "debug": False, "lan": "cn"}
}
如果用户不指定时间，或者指定的是现在时间，不要对'input_date'做处理
如果用户指定了时间，必须把'input_date'的值设置为如下形式：'%Y年%m月%d日 %H时%M分'
如果用户希望看到排卦的过程，把'debug'的值设置为True(T必须大写)
如果用户希望看到英语的结果，把'lan'的值设置为'en'
如果user content使用的语言是英语并且没有作特殊说明，把'lan'的值设置为'en'
## 计时器
### 如果用户希望添加一个计时器，可以使用计时器
### 计时器的默认caller格式如下
{
  "request_app": "timer",
  "request_params": {"time": None}
}
如果用户指定了时间，必须把'time'的值设置为如下形式：
'%H:%M:%S'
## 其他应用
### 如果用户请求的应用不在以上列表中，返回以下caller
{
  "request_app": "unknown",
  "request_params": {}
}
    """
    messages = agentHandler.append_agent([], system_prompt)
    message = contentHandler.chat(messages, request_prompt)
    caller = message[2].get('content')

    print(f"""
======== MCP 模拟结果 =======
caller: {caller}
======== MCP 呼叫结束 ==========
""")

    stub_app_caller(eval(caller))


if __name__ == '__main__':
    chat_to_get_app('Give me a devine for now')
