# encode = utf-8

import os
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File


def generate(target_path, type_name, sub_type_name):
    """
    Generate ai_tools directory and __init__.py file
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :return: None
    """
    # Create ui directory
    ui_dir = os.path.join(target_path, "ui")
    File.create_directory_if_not_exists(ui_dir)
    
    print(f"Generated ui directory structure at: {ui_dir}")
