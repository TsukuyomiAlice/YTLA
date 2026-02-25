# encode = utf-8

import os
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File


def generate(target_path, type_name, sub_type_name):
    """
    Generate dataset directory and __init__.py file
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :return: None
    """
    # Create dataset directory
    dataset_dir = os.path.join(target_path, "dataset")
    File.create_directory_if_not_exists(dataset_dir)

    # Create __init__.py file
    init_file = os.path.join(dataset_dir, "__init__.py")
    File.create_init_file(init_file)

    print(f"Generated dataset directory structure at: {dataset_dir}")
