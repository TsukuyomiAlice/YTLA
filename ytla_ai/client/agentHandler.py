# encode = utf-8

"""
SYSTEM PROMPT GUIDE
This agent handler helps to add the following two kinds of system prompts:
1 system agent
2 user background agent
You can only add either system agent or user background agent or both.
But, if you want to add a system agent, you must call append_system_agent first and ensure the system agent prompt is listed in the 1st place.
"""

def append_system_agent(messages: list, agent_prompt: str) -> list:
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
    """
    Appends user background information to a list of chat messages under specific conditions.

    This function modifies the input `messages` list by either adding a new system message
    for user background or appending the `background_prompt` to an existing system message
    that starts with "# 用户背景", after validating the message list structure.

    Args:
        messages (list): A list of chat message dictionaries. Each dictionary should have
            "role" (e.g., "system") and "content" keys.
        background_prompt (str): The user background information to be added to the messages.

    Returns:
        list: The modified list of messages with user background information integrated,
            or the original list if validation fails.

    Description:
        1. **Initial System Message Check**: If `messages` is empty OR contains exactly one
            message whose content starts with "# 提示词", appends a new system message
            {"role": "system", "content": "# 用户背景"} to `messages`.
        2. **Validation Check**: Uses `check_legal_for_adding_background(messages)` to validate
            if the message list structure is suitable for adding background. If validation fails,
            prints "The messages list is not an expected messages list for appending user background."
        3. **Background Integration**: If validation passes:
            - If `messages` has 1 element and the first message's content starts with "# 用户背景",
                appends `background_prompt` to that message's content (separated by a newline).
            - If `messages` has 2 elements and the second message's content starts with "# 用户背景",
                appends `background_prompt` to that message's content (separated by a newline).

    """
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
    """
    Validates if the message list structure is suitable for adding user background information.

    This function checks if the messages list meets specific structural requirements that allow
    for safe addition of user background information. It ensures proper message role types and
    content formatting.

    Args:
        messages (list): A list of chat message dictionaries. Each dictionary should have
            "role" (str) and "content" (str) keys.

    Returns:
        bool: True if the messages list structure is valid for adding background information,
            False otherwise.

    Validation Rules:
        The function returns True only in these specific cases:

        1. Single message list:
            - Message must have "system" role
            - Content must start with either "# 提示词" or "# 用户背景"

        2. Two-message list:
            - Second message must have "system" role
            - Second message content must start with "# 用户背景"

        All other cases (different lengths or不符合上述条件的内容) return False.
        """
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
