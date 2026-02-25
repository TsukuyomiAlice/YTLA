# encode = utf-8

import os
from pathlib import Path
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File
from ytla_plan.features.scaffold.modules._type.const import langs


def generate_documents(target_path):
    """
    Generate documents folders and readme.me files.
    :param target_path: the generate base path
    :return: None
    """
    # Create readme.md file
    readme_file = os.path.join(target_path, "readme.md")
    File.create_init_file(readme_file)

    # Create documents directory
    documents_dir = os.path.join(target_path, "documents")
    File.create_directory_if_not_exists(documents_dir)

    # Create readme directory under documents
    readme_dir = os.path.join(documents_dir, "readme")
    File.create_directory_if_not_exists(readme_dir)

    # Create language directories and readme.md files
    for lang in langs.langs:
        lang_dir = os.path.join(readme_dir, lang)
        File.create_directory_if_not_exists(lang_dir)

        # Create readme.md file in each language directory
        lang_readme = os.path.join(lang_dir, "readme.md")
        File.create_init_file(lang_readme)

    print(f"Generated docs directory structure at: {documents_dir}")


def generate(target_path, type_name, sub_type_name):
    """
    Generate docs directory and readme.md files
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :return: None
    """

    # generate the detailed module docs
    generate_documents(target_path)

    # generate the feature description files.
    if sub_type_name == "_type":
        # The feature layer
        # It doesn't affect the exist files.
        feature_path = Path(target_path).parent.parent
        generate_documents(feature_path)
        # The structure layer
        structure_path = Path(target_path).parent
        generate_documents(structure_path)


def add_preset_content(file_path, content):
    """
    Add preset content to a file
    :param file_path: File path
    :param content: Content to add
    :return: Whether content was added successfully
    """
    if os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    else:
        return False
