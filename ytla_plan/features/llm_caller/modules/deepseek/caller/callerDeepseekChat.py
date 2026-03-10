"""
DeepSeek chat caller wrapper providing unified interface.
This module offers a standardized way to call DeepSeek API through either HTTP or OpenAI SDK.
"""

from ..api.apiDeepseekHttp import chat_http
from ..api.apiDeepseekOpenai import chat_openai
from ..const.constDeepseekConfig import (
    CALL_MODE_HTTP,
    CALL_MODE_OPENAI,
    DEFAULT_CALL_MODE,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS,
    SUPPORTED_MODELS
)


def chat(messages, model=None, temperature=None, max_tokens=None, call_mode=None, **kwargs):
    """
    Unified chat completion interface for DeepSeek API.

    Args:
        messages (list): List of message objects with 'role' and 'content' keys.
        model (str, optional): Model identifier to use. Defaults to None, uses DEFAULT_MODEL.
        temperature (float, optional): Sampling temperature. Defaults to None, uses DEFAULT_TEMPERATURE.
        max_tokens (int, optional): Maximum tokens in response. Defaults to None, uses DEFAULT_MAX_TOKENS.
        call_mode (str, optional): Call mode to use (CALL_MODE_HTTP or CALL_MODE_OPENAI). 
                                    Defaults to None, uses DEFAULT_CALL_MODE.
        **kwargs: Additional keyword arguments passed to the API.

    Returns:
        str: The model's response message content as a string.

    Raises:
        ValueError: If model is not supported, call_mode is invalid, or messages are empty.
        Exception: Any exception occurred during API call will be caught and re-raised.
    """
    try:
        selected_model = model if model is not None else DEFAULT_MODEL
        selected_temperature = temperature if temperature is not None else DEFAULT_TEMPERATURE
        selected_max_tokens = max_tokens if max_tokens is not None else DEFAULT_MAX_TOKENS
        selected_call_mode = call_mode if call_mode is not None else DEFAULT_CALL_MODE

        if selected_model not in SUPPORTED_MODELS:
            raise ValueError(f"Model '{selected_model}' is not supported. Supported models are: {SUPPORTED_MODELS}")

        if selected_call_mode not in [CALL_MODE_HTTP, CALL_MODE_OPENAI]:
            raise ValueError(
                f"Invalid call_mode '{selected_call_mode}'. Must be either '{CALL_MODE_HTTP}' or '{CALL_MODE_OPENAI}'.")

        if selected_call_mode == CALL_MODE_HTTP:
            result = chat_http(
                messages=messages,
                model=selected_model,
                temperature=selected_temperature,
                max_tokens=selected_max_tokens,
                **kwargs
            )
            return result
        else:
            result = chat_openai(
                messages=messages,
                model=selected_model,
                temperature=selected_temperature,
                max_tokens=selected_max_tokens,
                **kwargs
            )
            return result.content

    except ValueError:
        raise
    except Exception as e:
        raise Exception(f"Error in chat caller: {str(e)}")
