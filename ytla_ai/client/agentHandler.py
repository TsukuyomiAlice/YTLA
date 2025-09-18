# encode = utf-8

def append_agent(messages: list, agent_prompt: str) -> list:
    """
    Appends or updates an agent prompt to the system message in a conversation history.

    If the messages list is empty, creates and adds a new system role message containing the agent_prompt.
    If the messages list is not empty, appends the agent_prompt to the content of the first message in the list,
    separated by a newline character.

    params:
        messages (list): List of conversation messages, where each message is typically a dictionary
            with 'role' (str) and 'content' (str) keys.
        agent_prompt (str): The prompt string to add to the system message content.

    returns:
        list: The modified messages list with the agent prompt incorporated.
    """

    if len(messages) == 0:
        messages.append({"role": "system", "content": "# 提示词"})
    if (len(messages) == 1 and (messages[0]["role"] != "system" or not messages[0]["content"].startswith("# 提示词"))) or len(messages) > 1:
        print("The messages list is not an expected messages list for agent prompt.")
    else:
        messages[0]["content"] = messages[0]["content"] + "\n" + agent_prompt
    return messages


def append_background(messages: list, background_prompt: str) -> list:

    if len(messages) == 0 or (len(messages) == 1 and messages[0]["content"].startswith("# 提示词")):
        messages.append({"role": "system", "content": "# 用户背景"})
    if not check_legal_for_adding_background(messages):
        print("The messages list is not an expected messages list for appending user background.")
    else:
        if len(messages) == 1 and messages[0]["content"].startswith("# 用户背景"):
            messages[0]["content"] = messages[0]["content"] + "\n" + background_prompt
        elif len(messages) == 2 and messages[1]["content"].startswith("# 用户背景"):
            messages[1]["content"] = messages[1]["content"] + "\n" + background_prompt
    return messages


def check_legal_for_adding_background(messages: list) -> bool:
    if len(messages) == 1:
        if messages[0]["role"] != "system":
            return False
        else:
            if not messages[0]["content"].startswith("# 提示词") and not messages[0]["content"].startswith("# 用户背景"):
                return False
        return True
    if len(messages) == 2:
        if messages[1]["role"] != "system":
            return False
        if not messages[1]["content"].startswith("# 用户背景"):
            return False
        return True
    return False
