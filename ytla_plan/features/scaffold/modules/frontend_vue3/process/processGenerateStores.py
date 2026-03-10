# encode = utf-8

import os
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File


def generate(target_path, type_name, sub_type_name, is_core=False):
    """
    Generate ai_tools directory and __init__.py file
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :param is_core: Is core or feature
    :return: None
    """
    # Create stores directory
    stores_dir = os.path.join(target_path, "stores")
    File.create_directory_if_not_exists(stores_dir)
    
    print(f"Generated stores directory structure at: {stores_dir}")
