# encode = utf-8

from ytla_ai.deepseek import caller


def chat(messages: list, text: str, temperature: float = 0.0) -> list:
    """
    Chat with the model.

    Args:
        messages (list): The message list.
        text (str): The text to chat.
        temperature (float, optional): The temperature of the model. Defaults to 0.0.

    Returns:
        list: The message list with the response added.
    """
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
    response = caller.chat_caller(messages, temperature=temperature)

    # reasoning = response.reasoning_content
    answer = response.content
    messages.append({"role": "assistant", "content": answer})

    # return
    return messages


def add_system_message(messages: list, text: str) -> list:
    """
    Add a system message to the message list.

    Args:
        messages (list): The message list.
        text (str): The system message.

    Returns:
        list: The message list with the system message added.
    """

    # type check
    # prevent the null request
    if text == "":
        print("The text is null")
        return messages
    # prevent the wrong type
    if type(messages) is not list:
        print("The messages is not list")
        return messages

    messages.append({"role": "system", "content": text})

    # return
    return messages
