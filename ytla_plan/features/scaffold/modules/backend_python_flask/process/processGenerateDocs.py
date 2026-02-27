# encode = utf-8

import os
from pathlib import Path
from ytla_plan import config
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File
from ytla_plan.features.scaffold.modules._type.const import langs
from ytla_plan.features.scaffold.modules.backend_python_flask.const import constLangList


def generate_docs(target_path):
    """
    Generate docs folders and readme.me files.
    :param target_path: the generate base path
    :return: None
    """
    # Create readme.md file
    readme_file = os.path.join(target_path, "readme.md")
    if not os.path.exists(readme_file):
        File.create_init_file(readme_file)
        lan = langs.langs.get(config.LANGUAGE).get('lan') if config.LANGUAGE in langs.langs.keys() \
            else langs.langs.get('en-US').get('lan')
        File.add_preset_content(readme_file, constLangList.base_readme_lang_list(lan))

    # Create docs directory
    docs_dir = os.path.join(target_path, "docs")
    File.create_directory_if_not_exists(docs_dir)

    # Create readme directory under docs
    readme_dir = os.path.join(docs_dir, "readme")
    File.create_directory_if_not_exists(readme_dir)

    # Create language directories and readme.md files
    for lang in langs.langs.keys():
        lang_dir = os.path.join(readme_dir, lang)
        File.create_directory_if_not_exists(lang_dir)

        # Create readme.md file in each language directory
        lang_readme = os.path.join(lang_dir, "readme.md")
        if not os.path.exists(lang_readme):
            File.create_init_file(lang_readme)
            File.add_preset_content(lang_readme, constLangList.doc_readme_lang_list(langs.langs.get(lang).get('lan')))

    print(f"Generated docs directory structure at: {docs_dir}")


def generate(target_path, type_name, sub_type_name):
    """
    Generate docs directory and readme.md files
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :return: None
    """

    # generate the detailed module docs
    generate_docs(target_path)

    # generate the feature description files.
    if sub_type_name == "_type":
        # The feature layer
        # It doesn't affect the exist files.
        feature_path = Path(target_path).parent.parent
        generate_docs(feature_path)
        # The structure layer
        structure_path = Path(target_path).parent
        generate_docs(structure_path)



