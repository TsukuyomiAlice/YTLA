"""
Utility functions for DeepSeek LLM caller module.
"""
from typing import List, Any, Dict
from ..instance.instanceDeepseekTypes import ChatMessage


def dict_to_chat_messages(data: List[dict]) -> List[ChatMessage]:
    """
    Convert a list of dictionaries to a list of ChatMessage objects.
    
    Args:
        data: A list of dictionaries, each containing 'role' and 'content' keys.
        
    Returns:
        A list of ChatMessage objects created from the input data.
        
    Raises:
        ValueError: If any dictionary in the input list does not have 'role' or 'content' keys.
    """
    messages = []
    for item in data:
        if 'role' not in item or 'content' not in item:
            raise ValueError("Each dictionary must contain 'role' and 'content' keys.")
        messages.append(ChatMessage(role=item['role'], content=item['content']))
    return messages


def chat_messages_to_dict(messages: List[ChatMessage]) -> List[dict]:
    """
    Convert a list of ChatMessage objects to a list of dictionaries.
    
    Args:
        messages: A list of ChatMessage objects to convert.
        
    Returns:
        A list of dictionaries, each containing 'role' and 'content' keys corresponding to the ChatMessage attributes.
    """
    return [{'role': msg.role, 'content': msg.content} for msg in messages]


def validate_messages(messages: Any) -> bool:
    """
    Validate that the input is a valid list of messages.
    
    Args:
        messages: The input to validate. Can be a list of ChatMessage objects or a list of dictionaries.
        
    Returns:
        True if the input is a valid list of messages, False otherwise.
    """
    if not isinstance(messages, list):
        return False

    if len(messages) == 0:
        return True

    first_item = messages[0]

    if isinstance(first_item, ChatMessage):
        return all(isinstance(msg, ChatMessage) for msg in messages)
    elif isinstance(first_item, dict):
        return all(
            isinstance(msg, dict) and
            'role' in msg and
            'content' in msg and
            isinstance(msg['role'], str) and
            isinstance(msg['content'], str)
            for msg in messages
        )
    else:
        return False
