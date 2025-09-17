# encode = utf-8

from ytla_ai.deepseek import caller


def chat(text, messages: list):

    # type check
    # prevent the null request
    if text == "":
        print("The text is null")
        return messages
    # prevent the wrong type
    if type(messages) is not list:
        print("The messages is not list")
        return messages

    # assemble the message -> send -> receive -> assemble the response
    messages.append({"role": "user", "content": text})
    response = caller.chat_caller(messages)
    # reasoning = response.reasoning_content
    answer = response.content
    messages.append({"role": "assistant", "content": answer})

    # return
    return messages
