# encode = utf-8

import os
from pathlib import Path


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
    Create __init__.py file if it doesn't exist
    :param init_file_path: __init__.py file path
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


def generate(target_path):
    """
    Generate schedule directory and __init__.py file
    :param target_path: Target path
    :return: None
    """
    # Create schedule directory
    schedule_dir = os.path.join(target_path, "schedule")
    create_directory_if_not_exists(schedule_dir)
    
    # Create __init__.py file
    init_file = os.path.join(schedule_dir, "__init__.py")
    create_init_file(init_file)
    
    print(f"Generated schedule directory structure at: {schedule_dir}")
