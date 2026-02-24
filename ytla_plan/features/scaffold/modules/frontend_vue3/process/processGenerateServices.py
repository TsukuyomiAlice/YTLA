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
    Generate services directory
    :param target_path: Target path
    :return: None
    """
    # Create services directory
    services_dir = os.path.join(target_path, "services")
    create_directory_if_not_exists(services_dir)
    
    print(f"Generated services directory structure at: {services_dir}")
