# encode = utf-8

import os
from pathlib import Path
from ytla_plan import config
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File
from ytla_plan.features.scaffold.modules._type.const import constLangs
from ytla_plan.features.scaffold.modules.frontend_vue3.script import scriptGetDocTemplates as DocTemplates


def generate_documents(target_path, type_name, sub_type_name, general_feature: False, is_core=False):
    """
    Generate documents folders and readme.me files.
    :param target_path: the generate base path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :param general_feature: General feature(_type folder)
    :param is_core: Is core or feature
    :return: None
    """
    # Create readme.md file
    readme_file = os.path.join(target_path, "readme.md")
    if not os.path.exists(readme_file):
        File.create_init_file(readme_file)
        # Get language code, default to en-US if not found
        current_lang = config.LANGUAGE if config.LANGUAGE in constLangs.langs.keys() else 'en-US'
        # Add base readme template
        File.add_preset_content(readme_file, DocTemplates.get_base_readme(current_lang))

        if sub_type_name == "_type" and not general_feature:
            # Type level template
            content = DocTemplates.get_type_level_template(current_lang, type_name, is_core=is_core)
        else:
            # Subtype level template
            content = DocTemplates.get_subtype_level_template(current_lang, type_name, sub_type_name, is_core=is_core)
        # Append the template content
        with open(readme_file, 'a', encoding='utf-8') as f:
            f.write(content)

    # Create documents directory
    documents_dir = os.path.join(target_path, "documents")
    File.create_directory_if_not_exists(documents_dir)

    # Create readme directory under documents
    readme_dir = os.path.join(documents_dir, "readme")
    File.create_directory_if_not_exists(readme_dir)

    # Create language directories and readme.md files
    for lang in constLangs.langs.keys():
        lang_dir = os.path.join(readme_dir, lang)
        File.create_directory_if_not_exists(lang_dir)

        # Create readme.md file in each language directory
        lang_readme = os.path.join(lang_dir, "readme.md")
        if not os.path.exists(lang_readme):
            File.create_init_file(lang_readme)
            # Add doc readme template
            File.add_preset_content(lang_readme, DocTemplates.get_doc_readme(lang))
            
            # Add content based on level
            if sub_type_name == "_type" and not general_feature:
                # Type level template
                content = DocTemplates.get_type_level_template(lang, type_name, is_core=is_core)
            else:
                # Subtype level template
                content = DocTemplates.get_subtype_level_template(lang, type_name, sub_type_name, is_core=is_core)
            
            # Append the template content
            with open(lang_readme, 'a', encoding='utf-8') as f:
                f.write(content)

    print(f"Generated docs directory structure at: {documents_dir}")


def generate(target_path, type_name, sub_type_name, is_core=False):
    """
    Generate docs directory and readme.md files
    :param target_path: Target path
    :param type_name: Type name
    :param sub_type_name: Sub type name
    :param is_core: Is core or feature
    :return: None
    """

    # generate the detailed module docs
    generate_documents(target_path, type_name, sub_type_name, general_feature=True, is_core=is_core)

    # generate the feature description files.
    if sub_type_name == "_type":
        # The feature layer
        # It doesn't affect the exist files.
        feature_path = Path(target_path).parent.parent
        generate_documents(feature_path, type_name, sub_type_name, general_feature=False, is_core=is_core)