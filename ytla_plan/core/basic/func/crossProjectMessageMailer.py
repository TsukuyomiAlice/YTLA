# coding=utf-8

import os
import json

"""
If you want to use this function, you should do the following steps:
1 set the message file receive folder position in utilConfigs.py
2 define the message's structure
3 create caller file in each project you will use to send messages to this project
"""

# CAUTION: You should define this in utilConfigs.py
receiver_folder_position = ''


def slash():
    """Get appropriate path separator for current operating system.

    Returns:
        str: '/' for POSIX systems (Linux/macOS), '\\' for NT systems (Windows)

    Example:
        >>> sep = slash()
        sep = '\\' if os.name == 'nt' else '/'
    """
    s = '/'
    if os.name == 'posix':
        s = '/'
    if os.name == 'nt':
        s = '\\'
    return s


class Message:
    """Represents a cross-project message object.

    Attributes:
        message_type (str): Category identifier for message grouping
        message_name (str): Unique identifier for the message
        message_time (str): Timestamp in ISO format (YYYY-MM-DD HH:MM:SS)
        message (dict): Payload data in key-value format
    """

    def __init__(self, message_name: str):
        self.message_type: str = ' '
        self.message_name = message_name
        self.message_time: str = ''
        self.message: dict = {}


def send_message(message: Message):
    """Serialize and save message object to target directory.

    Creates JSON file with naming convention:
    {type}_{timestamp}_{name}.json

    Args:
        message (Message): Message instance to be sent

    Raises:
        OSError: If target directory is invalid or inaccessible

    Example:
        >>> msg = Message("status_update")
        >>> msg.message_type = "system"
        >>> send_message(msg)
    """
    message_file_name = (f'{receiver_folder_position}{slash()}'
                         f'_{message.message_type}_{message.message_time}_{message.message_name}.json')
    message_info = {'message_type': message.message_type,
                    'message_name': message.message_name,
                    'message_time': message.message_time,
                    'message': message.message}
    with open(message_file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(message_info))


def receive_message():
    """Retrieve incoming messages from designated folder.

    Returns:
        list: Filename strings of available messages in receiver folder

    Raises:
        FileNotFoundError: If receiver folder is not configured properly

    Example:
        >>> messages = receive_message()
        >>> print(messages)
        ['_system_2023-01-01_project_update.json']
    """
    message_file_list = os.listdir(receiver_folder_position)
    return message_file_list
