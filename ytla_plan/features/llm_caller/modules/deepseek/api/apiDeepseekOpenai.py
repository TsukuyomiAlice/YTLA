"""
DeepSeek API implementation using OpenAI SDK.
This module provides a standardized interface for interacting with DeepSeek API through the OpenAI SDK.
"""

import openai
from openai import OpenAI
from ytla_ai.deepseek import api_key
from ..const.constDeepseekConfig import (
    BASE_URL,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS
)

deepSeek_API_key = api_key.DEEPSEEK_API_KEY_1
client = OpenAI(api_key=deepSeek_API_key, base_url=BASE_URL)


def chat_openai(messages, model=None, temperature=None, max_tokens=None, **kwargs):
    """
    Call DeepSeek chat completion API using OpenAI SDK.
    
    This function provides a standardized interface for sending chat completion requests
    to the DeepSeek API through the OpenAI-compatible client. It includes error handling
    for common API-related exceptions.
    
    :param messages: A list of message dictionaries representing the conversation history.
                     Each message should have a 'role' (e.g., 'user', 'assistant', 'system')
                     and 'content' field with the message text.
    :type messages: list[dict[str, str]]
    :param model: The DeepSeek model to use. If None, DEFAULT_MODEL will be used.
                  Supported models include 'deepseek-chat' and 'deepseek-reasoner'.
    :type model: str, optional
    :param temperature: Sampling temperature between 0.0 and 2.0. Lower values make output
                        more deterministic, higher values make output more random. If None,
                        DEFAULT_TEMPERATURE will be used.
    :type temperature: float, optional
    :param max_tokens: Maximum number of tokens in the generated response. If None,
                       DEFAULT_MAX_TOKENS will be used.
    :type max_tokens: int, optional
    :param **kwargs: Additional keyword arguments to pass to the API.
    :type **kwargs: dict
    :return: The message object from the API response containing the assistant's reply.
    :rtype: openai.types.chat.ChatCompletionMessage
    :raises openai.APIError: General API error from DeepSeek service.
    :raises openai.APIConnectionError: Failed to establish connection to the API.
    :raises openai.AuthenticationError: Invalid API key authentication.
    :raises openai.RateLimitError: API rate limit exceeded.
    """
    selected_model = model if model is not None else DEFAULT_MODEL
    selected_temperature = temperature if temperature is not None else DEFAULT_TEMPERATURE
    selected_max_tokens = max_tokens if max_tokens is not None else DEFAULT_MAX_TOKENS

    try:
        response = client.chat.completions.create(
            model=selected_model,
            messages=messages,
            temperature=selected_temperature,
            max_tokens=selected_max_tokens,
            stream=False,
            **kwargs
        )
        return response.choices[0].message
    except openai.APIConnectionError as e:
        raise e
    except openai.APIError as e:
        raise e
    except openai.AuthenticationError as e:
        raise e
    except openai.RateLimitError as e:
        raise e
    except Exception as e:
        raise openai.APIError(f"Unexpected error occurred: {str(e)}")
