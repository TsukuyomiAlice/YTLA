# encode = utf-8

from pathlib import Path


def first_letter_upper(s):
    if s:
        return s[0].upper() + s[1:]
    return s


def first_letter_lower(s):
    if s:
        return s[0].lower() + s[1:]
    return s


def generate_vue3_structure(is_core: str = 'n', structure: str = 'cards',
                            type_name: str = '', subtype: str = ''):
    """
    Generate Vue3 frontend directory structure
    :param is_core: Whether it's a core skill (y/n, default n)
    :param structure: Structure type (card / module)
    :param type_name: Function category / core version
    :param subtype: Function subcategory / core subproject (can be empty, if empty, referred to '_type')
    :return: Generated directory path
    """
    # Validate parameters
    if not type_name:
        raise ValueError("type parameter cannot be empty")

    if structure not in ['cards', 'modules']:
        raise ValueError("structure parameter must be 'cards' or 'modules'")

    # Handle subtype
    if not subtype:
        subtype = '_type'

    # Determine prefix
    prefix = 'core' if is_core.lower() == 'y' else 'features'

    # Calculate frontend project path automatically
    current_file = Path(__file__)
    # Navigate up to \YTLA
    ytla_root = current_file.parent.parent.parent.parent.parent.parent
    frontend_project_path = ytla_root / 'ytla_plan_vue' / 'src'

    # Generate target path
    base_path = frontend_project_path / prefix / type_name / structure

    target_path = base_path / subtype

    # Base directory structure
    base_structure = [
        "documents",
        "definitions",
        "components",
        "layouts",
        "ui",
        "composables",
        "styles",
        "locales",
        "stores",
        "services",
        "factories",
        "registries",
        "flows",
        "utils",
        "avatar"
    ]

    # Create directory structure
    for dir_name in base_structure:
        dir_path = target_path / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)

    if subtype != '_type':
        component_name = first_letter_upper(subtype)
    else:
        component_name = first_letter_upper(type_name)
        subtype = first_letter_lower(type_name)

    # components directory
    component_file = target_path / "components" / f"{component_name}.vue"
    with open(component_file, 'w', encoding='utf-8') as f:
        f.write('')

    # definitions directory
    type_file = target_path / "definitions" / f"{subtype}Type.ts"
    with open(type_file, 'w', encoding='utf-8') as f:
        f.write('')

    # composables directory
    composable_file = target_path / "composables" / f"use{component_name}.ts"
    with open(composable_file, 'w', encoding='utf-8') as f:
        f.write('')

    # styles directory
    style_file = target_path / "styles" / f"{subtype}.scss"
    with open(style_file, 'w', encoding='utf-8') as f:
        f.write('')

    # locales directory
    en_file = target_path / "locales" / "en.json"
    with open(en_file, 'w', encoding='utf-8') as f:
        f.write('{"": ""}')

    zh_file = target_path / "locales" / "zh.json"
    with open(zh_file, 'w', encoding='utf-8') as f:
        f.write('{"": ""}')

    return str(target_path)
