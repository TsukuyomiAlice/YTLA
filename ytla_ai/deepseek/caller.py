# encode = utf-8
# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

"""
Base information
"""
deepSeek_API_key = "sk-1a09e92cc2334b2b9a39b07a1a85e686"
base_url = "https://api.deepseek.com"
client = OpenAI(api_key=deepSeek_API_key, base_url=base_url)

"""
settings
"""
temperature = 0.0


def chat_caller(messages, model="deepseek-chat"):
    """
    Call the chat API
    :param messages: the messages to send
    :param model: the model to use. The alternative is "deepseek-reasoner" for using thought chain
    :return: the response from the API
    """

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False,
        temperature=temperature
    )

    return response.choices[0].message

