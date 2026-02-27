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
    # Create flows directory
    flows_dir = os.path.join(target_path, "flows")
    File.create_directory_if_not_exists(flows_dir)
    
    print(f"Generated flows directory structure at: {flows_dir}")
