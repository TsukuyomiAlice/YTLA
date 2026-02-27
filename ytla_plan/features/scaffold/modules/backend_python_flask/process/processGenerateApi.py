# encode = utf-8

import os
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File


def generate(target_path, type_name, sub_type_name):
    """
    Generate api directory and __init__.py file
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :return: None
    """
    # Create api directory
    api_dir = os.path.join(target_path, "api")
    File.create_directory_if_not_exists(api_dir)

    # Create __init__.py file
    init_file = os.path.join(api_dir, "__init__.py")
    File.create_init_file(init_file)

    print(f"Generated api directory structure at: {api_dir}")
