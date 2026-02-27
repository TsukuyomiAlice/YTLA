# encode = utf-8

import os
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File


def generate(target_path, type_name, sub_type_name):
    """
    Generate components directory and __init__.py file
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :return: None
    """
    # Create components directory
    components_dir = os.path.join(target_path, "components")
    File.create_directory_if_not_exists(components_dir)
    
    print(f"Generated components directory structure at: {components_dir}")
