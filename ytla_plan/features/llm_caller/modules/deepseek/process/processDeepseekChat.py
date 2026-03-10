"""
Process layer for DeepSeek chat functionality.
This module provides high-level processing functions for chat requests.
"""

from typing import Optional, List, Dict, Any
from ..caller.callerDeepseekChat import chat
from ..instance.instanceDeepseekTypes import ChatMessage, ChatRequest, ChatResponse, dict_to_chat_messages
from ..const.constDeepseekConfig import DEFAULT_MODEL, DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS, DEFAULT_CALL_MODE


def process_chat_request(chat_request: ChatRequest) -> ChatResponse:
    """
    Process a chat request and return a chat response.
    
    This function takes a ChatRequest object, prepares the necessary parameters,
    calls the underlying chat function, and constructs a ChatResponse object.
    
    Args:
        chat_request (ChatRequest): The chat request object containing messages,
            model, temperature, max_tokens, and call_mode.
            
    Returns:
        ChatResponse: The chat response object containing the response content,
            model used, and optional usage statistics.
            
    Raises:
        Exception: Any exception occurred during processing will be caught and re-raised.
    """
    try:
        messages_dict = [msg.to_dict() for msg in chat_request.messages]

        result_content = chat(
            messages=messages_dict,
            model=chat_request.model,
            temperature=chat_request.temperature,
            max_tokens=chat_request.max_tokens,
            call_mode=chat_request.call_mode
        )

        chat_response = ChatResponse(
            content=result_content,
            model=chat_request.model,
            usage=None
        )

        return chat_response

    except Exception as e:
        raise Exception(f"Error processing chat request: {str(e)}")


def process_simple_chat(user_message: str, system_prompt: Optional[str] = None, **kwargs) -> str:
    """
    Provide a simplified interface for chat functionality.
    
    This function takes a user message string and an optional system prompt,
    constructs the appropriate message list, calls process_chat_request,
    and returns just the response content string.
    
    Args:
        user_message (str): The user's message content.
        system_prompt (Optional[str], optional): An optional system prompt to guide the model.
            Defaults to None.
        **kwargs: Additional keyword arguments that can include:
            - model (str): Model identifier to use
            - temperature (float): Sampling temperature
            - max_tokens (int): Maximum tokens in response
            - call_mode (str): Call mode to use
            
    Returns:
        str: The model's response message content as a string.
        
    Raises:
        Exception: Any exception occurred during processing will be caught and re-raised.
    """
    try:
        messages: List[ChatMessage] = []

        if system_prompt:
            messages.append(ChatMessage(role="system", content=system_prompt))

        messages.append(ChatMessage(role="user", content=user_message))

        model = kwargs.get('model', DEFAULT_MODEL)
        temperature = kwargs.get('temperature', DEFAULT_TEMPERATURE)
        max_tokens = kwargs.get('max_tokens', DEFAULT_MAX_TOKENS)
        call_mode = kwargs.get('call_mode', DEFAULT_CALL_MODE)

        chat_request = ChatRequest(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            call_mode=call_mode
        )

        chat_response = process_chat_request(chat_request)

        return chat_response.content

    except Exception as e:
        raise Exception(f"Error in simple chat: {str(e)}")
