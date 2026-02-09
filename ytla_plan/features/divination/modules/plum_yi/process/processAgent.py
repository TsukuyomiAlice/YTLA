# encode = utf-8

from ytla_ai.client import contentHandler
from features.divination.modules.plum_yi.process import processModulePlumYi


def app_caller(caller: dict):
    request_app = caller['request_app']
    if request_app == 'plum_yi':
        params = caller['request_params']
        processModulePlumYi.hexagram_solver(input_date=params['input_date'], debug=params['debug'], lan=params['lan'])
    else:
        pass


def chat_to_get_app(request_prompt: str):
    system_prompt = """
# 提示词
# 你的任务是根据用户的请求生成对应的caller。这个caller是一个python dict，不是json。你的返回结果只包含caller，不要夹带其它任何内容。
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
如果用户不指定时间，或者指定的是现在时间，把'input_date'的值设置为None，绝对不要设置为null
如果用户指定了时间，必须把'input_date'的值设置为如下形式：'%Y年%m月%d日 %H时%M分'
如果用户希望看到排卦的过程，把'debug'的值设置为True(T必须大写)
如果用户希望看到英语的结果，把'lan'的值设置为'en'
如果user content使用的语言是英语并且没有作特殊说明，把'lan'的值设置为'en'

## 其他应用
### 如果用户请求的应用不在以上列表中，返回以下caller
{
  "request_app": "unknown",
  "request_params": {}
}
    """
    messages = contentHandler.add_system_message([], system_prompt)
    message = contentHandler.chat(messages, request_prompt)
    caller = message[2].get('content')

    app_caller(eval(caller))


if __name__ == '__main__':
    chat_to_get_app('为我现在起一卦，我需要看排卦结果')
