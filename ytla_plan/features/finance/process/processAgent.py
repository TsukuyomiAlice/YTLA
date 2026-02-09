# encode = utf-8

from features.finance.prompt import promptSupposal
from ytla_ai.client import contentHandler

def q_1():
    message_list = contentHandler.chat([], promptSupposal.ask_1, temperature=0)
    caller = message_list[1].get('content')
    print(caller)
    return caller


def q_2():
    message_list = [{"role": "user", "content": promptSupposal.ask_1}, {"role": "assistant", "content": promptSupposal.answer_1}]
    message_list = contentHandler.chat(message_list, promptSupposal.ask_2, temperature=0)
    caller = message_list[3].get('content')
    print(caller)
    return caller

q_2()