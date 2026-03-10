# encode = utf-8

import os
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File


def generate(target_path, type_name, sub_type_name, is_core=False):
    """
    Generate definitions directory and __init__.py file
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :param is_core: Is core or feature
    :return: None
    """
    # Create definitions directory
    definitions_dir = os.path.join(target_path, "definitions")
    File.create_directory_if_not_exists(definitions_dir)

    print(f"Generated definitions directory structure at: {definitions_dir}")
