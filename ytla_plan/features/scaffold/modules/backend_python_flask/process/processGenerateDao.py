# encode = utf-8

import os
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File


def generate(target_path, type_name, sub_type_name):
    """
    Generate dao directory and __init__.py file
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :return: None
    """
    # Create dao directory
    dao_dir = os.path.join(target_path, "dao")
    File.create_directory_if_not_exists(dao_dir)

    # Create __init__.py file
    init_file = os.path.join(dao_dir, "__init__.py")
    File.create_init_file(init_file)

    print(f"Generated dao directory structure at: {dao_dir}")
