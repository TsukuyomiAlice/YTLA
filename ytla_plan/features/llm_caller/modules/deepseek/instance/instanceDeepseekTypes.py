"""
Type definitions for DeepSeek chat API.
This module provides data structures and conversion functions for chat messages.
"""

from typing import List, Dict, Any, Optional


class ChatMessage:
    """
    Data class representing a chat message.
    
    Attributes:
        role (str): The role of the message sender (e.g., 'user', 'assistant', 'system').
        content (str): The content of the message.
    """

    def __init__(self, role: str, content: str):
        """
        Initialize a ChatMessage instance.
        
        Args:
            role (str): The role of the message sender.
            content (str): The content of the message.
        """
        self.role = role
        self.content = content

    def to_dict(self) -> Dict[str, str]:
        """
        Convert ChatMessage to a dictionary.
        
        Returns:
            Dict[str, str]: Dictionary representation of the message.
        """
        return {
            'role': self.role,
            'content': self.content
        }


class ChatRequest:
    """
    Represents a chat request to be sent to the LLM API.
    
    Attributes:
        messages (List[ChatMessage]): A list of ChatMessage objects representing the conversation history.
        model (str): The name of the model to use for the chat.
        temperature (float): The temperature parameter for controlling randomness in generation.
        max_tokens (int): The maximum number of tokens to generate in the response.
        call_mode (str): The mode of the call (e.g., "http", "openai").
    """

    def __init__(self, messages: List[ChatMessage], model: str, temperature: float, max_tokens: int, call_mode: str):
        """
        Initialize a ChatRequest instance.
        
        Args:
            messages (List[ChatMessage]): A list of ChatMessage objects representing the conversation history.
            model (str): The name of the model to use for the chat.
            temperature (float): The temperature parameter for controlling randomness in generation.
            max_tokens (int): The maximum number of tokens to generate in the response.
            call_mode (str): The mode of the call.
        """
        self.messages = messages
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.call_mode = call_mode


class ChatResponse:
    """
    Represents a chat response received from the LLM API.
    
    Attributes:
        content (str): The text content of the response.
        model (str): The name of the model that generated the response.
        usage (Optional[dict]): Optional dictionary containing usage statistics (token counts, etc.).
    """

    def __init__(self, content: str, model: str, usage: Optional[dict] = None):
        """
        Initialize a ChatResponse instance.
        
        Args:
            content (str): The text content of the response.
            model (str): The name of the model that generated the response.
            usage (Optional[dict], optional): Dictionary containing usage statistics. Defaults to None.
        """
        self.content = content
        self.model = model
        self.usage = usage


def dict_to_chat_messages(messages: List[Dict[str, Any]]) -> List[ChatMessage]:
    """
    Convert a list of message dictionaries to ChatMessage objects.
    
    Args:
        messages (List[Dict[str, Any]]): List of message dictionaries with 'role' and 'content' keys.
        
    Returns:
        List[ChatMessage]: List of ChatMessage objects.
        
    Raises:
        ValueError: If any message dictionary is missing 'role' or 'content' keys.
    """
    chat_messages = []
    for msg in messages:
        if 'role' not in msg or 'content' not in msg:
            raise ValueError("Each message must contain 'role' and 'content' keys")
        chat_messages.append(ChatMessage(role=msg['role'], content=msg['content']))
    return chat_messages
