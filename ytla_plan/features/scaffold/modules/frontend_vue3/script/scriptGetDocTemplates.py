# encode = utf-8

import time

from ytla_plan.features.scaffold.modules.frontend_vue3.const.constDocTemplates import templates


def get_language_template(language: str):
    """
    Get language template, default to en-US if language not found
    :param language: Language code
    :return: Language template dictionary
    """
    return templates.get(language, templates.get('en-US'))


def get_base_readme(language: str) -> str:
    """
    Get base readme template
    :param language: Language code
    :return: Base readme template
    """
    lang_template = get_language_template(language)
    return lang_template['base_readme']


def get_doc_readme(language: str) -> str:
    """
    Get doc readme template
    :param language: Language code
    :return: Doc readme template
    """
    lang_template = get_language_template(language)
    return lang_template['doc_readme']


def get_type_level_template(language: str, type_name: str) -> str:
    """
    Get type level document template
    :param language: Language code
    :param type_name: Application type name
    :return: Type level document template
    """
    date_string = time.strftime('%Y-%m-%d', time.localtime())
    lang_template = get_language_template(language)
    type_template = lang_template['type_level']

    return f"""
# {type_name}

### {type_template['title']}

### {type_template['author']}

{type_template['version']}

{type_template['tech_stack'].format(date_string=date_string)}

{type_template['standard_app']}

{type_template['standard_app_desc']}

{type_template['concepts']}

{type_template['concepts_desc']}

{type_template['dir_structure']}

{type_template['dir_structure_text']}

"""


def get_subtype_level_template(language: str, feature_name: str, subtype_name: str) -> str:
    """
    Get subtype level document template
    :param language: Language code
    :param feature_name: Feature name
    :param subtype_name: Subtype name
    :return: Subtype level document template
    """
    date_string = time.strftime('%Y-%m-%d', time.localtime())
    lang_template = get_language_template(language)
    subtype_template = lang_template['subtype_level']

    # Determine subtype title
    first_line = f"{feature_name} - {subtype_name}"
    if subtype_name == '_type':
        subtype_title = subtype_template['general_title']
        first_line = feature_name
    else:
        subtype_title = subtype_template['feature_title']

    return f"""
# {first_line}

### {subtype_title}

### {subtype_template['author']}

{subtype_template['version']}

{subtype_template['tech_stack'].format(date_string=date_string)}

{subtype_template['concepts']}

{subtype_template['concepts_desc']}

{subtype_template['dir_structure']}

{subtype_template['dir_structure_text']}

"""
