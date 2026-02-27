# encode = utf-8

import os


def create_directory_if_not_exists(dir_path):
    """
    Create directory if it doesn't exist
    :param dir_path: Directory path
    :return: Whether creation was successful
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        return True
    else:
        return False


def create_init_file(init_file_path):
    """
    Generate a blank file. Not only for __init__.py
    :param init_file_path: The path of the init file
    :return: Whether creation was successful
    """
    if not os.path.exists(init_file_path):
        with open(init_file_path, 'w', encoding='utf-8') as f:
            f.write('')
        return True
    else:
        # Add TODO comment to inform user file already exists
        print(f"TODO: File {init_file_path} already exists, skipping generation")
        return False


def add_preset_content(file_path, content):
    """
    Add preset content to a file
    :param file_path: The file path
    :param content: Content to add
    :return: Whether content was added successfully
    """
    if os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        return False
