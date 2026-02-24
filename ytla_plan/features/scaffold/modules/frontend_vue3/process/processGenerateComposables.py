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


def generate(target_path):
    """
    Generate composables directory
    :param target_path: Target path
    :return: None
    """
    # Create composables directory
    composables_dir = os.path.join(target_path, "composables")
    create_directory_if_not_exists(composables_dir)
    
    print(f"Generated composables directory structure at: {composables_dir}")
