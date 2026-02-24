# encode = utf-8

from pathlib import Path
import os
from ytla_plan.features.scaffold.modules.frontend_vue3.const import constGenerators


def first_letter_upper(s):
    """
    Switch a word's first letter into uppercase.
    :param s: The string to switch to.
    :return: The string with uppercase.
    """
    if s:
        return s[0].upper() + s[1:]
    return s


def first_letter_lower(s):
    """
    Switch a word's first letter into lowercase.
    :param s: The string to switch to.
    :return: The string with lowercase.
    """
    if s:
        return s[0].lower() + s[1:]
    return s


def generate_vue3_structure(is_core: str = 'n', structure: str = 'cards',
                            type_name: str = '', subtype: str = ''):
    """
    Generate Vue3 frontend directory structure
    :param is_core: Whether it's a core or feature (y/n, default n)
    :param structure: Structure type (card / module)
    :param type_name: Type category / core version
    :param subtype: SubType category / core sub feature (can be empty, if empty, referred to '_type')
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
    ytla_root = current_file.parent.parent.parent.parent.parent.parent.parent
    # todo: hard code for 'ytla_plan_vue'
    frontend_project_path = ytla_root / 'ytla_plan_vue' / 'src'

    # Generate target path
    base_path = frontend_project_path / prefix / type_name / structure
    target_path = base_path / subtype

    # Create main directories
    base_path.mkdir(parents=True, exist_ok=True)
    target_path.mkdir(parents=True, exist_ok=True)

    # Import and call directory generators
    # Add current directory to path to import modules
    current_dir = os.path.dirname(os.path.abspath(__file__))
    import sys
    sys.path.insert(0, current_dir)

    # Define generator configuration list
    generators = constGenerators.generators

    # Import and call generators one by one
    for module_name, func_name in generators:
        try:
            # Dynamically import module
            module = __import__(module_name)
            generate_func = getattr(module, "generate")
            # Call generator
            generate_func(str(target_path))
        except ImportError as e:
            print(f"Error importing {module_name}: {e}")
        except AttributeError as e:
            print(f"Error getting generate function from {module_name}: {e}")
        finally:
            # Always clear module cache
            if module_name in sys.modules:
                del sys.modules[module_name]

    if subtype != '_type':
        component_name = first_letter_upper(subtype)
    else:
        component_name = first_letter_upper(type_name)
        subtype = first_letter_lower(type_name)

    # components directory
    components_dir = target_path / "components"
    if components_dir.exists():
        component_file = components_dir / f"{component_name}.vue"
        if not component_file.exists():
            with open(component_file, 'w', encoding='utf-8') as f:
                f.write('')

    # definitions directory
    definitions_dir = target_path / "definitions"
    if definitions_dir.exists():
        type_file = definitions_dir / f"{subtype}Type.ts"
        if not type_file.exists():
            with open(type_file, 'w', encoding='utf-8') as f:
                f.write('')

    # composables directory
    composables_dir = target_path / "composables"
    if composables_dir.exists():
        composable_file = composables_dir / f"use{component_name}.ts"
        if not composable_file.exists():
            with open(composable_file, 'w', encoding='utf-8') as f:
                f.write('')

    # styles directory
    styles_dir = target_path / "styles"
    if styles_dir.exists():
        style_file = styles_dir / f"{subtype}.scss"
        if not style_file.exists():
            with open(style_file, 'w', encoding='utf-8') as f:
                f.write('')

    # locales directory
    locales_dir = target_path / "locales"
    if locales_dir.exists():
        en_file = locales_dir / "en.json"
        if not en_file.exists():
            with open(en_file, 'w', encoding='utf-8') as f:
                f.write('{"": ""}')

        zh_file = locales_dir / "zh.json"
        if not zh_file.exists():
            with open(zh_file, 'w', encoding='utf-8') as f:
                f.write('{"": ""}')

    return str(target_path)
