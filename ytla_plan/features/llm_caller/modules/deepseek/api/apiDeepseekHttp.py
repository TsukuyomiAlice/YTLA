"""
DeepSeek HTTP API caller implementation using requests library.
This module provides direct HTTP-based interaction with DeepSeek API.
"""

import requests
import json
from ytla_ai.deepseek import api_key
from ..const.constDeepseekConfig import (
    BASE_URL,
    DEFAULT_MODEL,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_TOKENS
)


def chat_http(messages, model=None, temperature=None, max_tokens=None, **kwargs):
    """
    Send a chat completion request to DeepSeek API using HTTP POST.

    Args:
        messages (list): List of message objects with 'role' and 'content' keys.
        model (str, optional): Model identifier to use. Defaults to None, uses DEFAULT_MODEL.
        temperature (float, optional): Sampling temperature. Defaults to None, uses DEFAULT_TEMPERATURE.
        max_tokens (int, optional): Maximum tokens in response. Defaults to None, uses DEFAULT_MAX_TOKENS.
        **kwargs: Additional keyword arguments passed to the API (top_p, frequency_penalty, presence_penalty, etc.)

    Returns:
        str: The model's response message content.

    Raises:
        requests.exceptions.RequestException: If there's an error with the HTTP request.
        KeyError: If the response structure is unexpected or missing expected keys.
        ValueError: If required parameters are missing or invalid.
    """
    if not messages:
        raise ValueError("Messages list cannot be empty")

    url = f"{BASE_URL}/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key.DEEPSEEK_API_KEY_1}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model or DEFAULT_MODEL,
        "messages": messages,
        "temperature": temperature if temperature is not None else DEFAULT_TEMPERATURE,
        "max_tokens": max_tokens if max_tokens is not None else DEFAULT_MAX_TOKENS,
        "stream": False
    }

    if "top_p" in kwargs:
        payload["top_p"] = kwargs["top_p"]
    if "frequency_penalty" in kwargs:
        payload["frequency_penalty"] = kwargs["frequency_penalty"]
    if "presence_penalty" in kwargs:
        payload["presence_penalty"] = kwargs["presence_penalty"]

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"HTTP request failed: {str(e)}")
    except KeyError as e:
        raise KeyError(f"Unexpected response structure, missing key: {str(e)}")
