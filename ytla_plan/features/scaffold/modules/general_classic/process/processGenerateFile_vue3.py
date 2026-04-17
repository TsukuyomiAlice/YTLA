# encode = utf-8

import os
from pathlib import Path
from ytla_plan import config
from ytla_plan.features.scaffold.modules.general_classic.const import constGenerators_vue3


def generate_classic_vue3_files(is_core: bool = False, structure: str = 'cards',
                                 type_name: str = '', sub_type_name: str = ''):
    """
    Generate Classic Vue3 files using the generated scripts
    :param is_core: Whether it's a core or feature (y/n, default n)
    :param structure: Structure type (cards / modules)
    :param type_name: Type category / core version
    :param sub_type_name: SubType category / core sub feature (can be empty, if empty, referred to '_type')
    :return: Generated directory path
    """
    if not type_name:
        raise ValueError("type parameter cannot be empty")

    if not is_core and structure not in ('cards', 'modules'):
        raise ValueError("structure parameter must be 'cards' or 'modules'")

    if not sub_type_name:
        sub_type_name = '_type'

    prefix = 'core' if is_core else 'features'
    frontend_project_path = Path(config.FRONTEND_FOLDER) / 'src'

    type_path = frontend_project_path / prefix / type_name
    structure_path = type_path / structure
    target_path = structure_path / sub_type_name

    if (not type_path.exists() or not structure_path.exists()) and sub_type_name != '_type':
        generate_classic_vue3_files(is_core, structure, type_name, '')

    type_path.mkdir(parents=True, exist_ok=True)
    structure_path.mkdir(parents=True, exist_ok=True)
    target_path.mkdir(parents=True, exist_ok=True)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = Path(current_dir).parent / 'script'
    import sys
    sys.path.insert(0, str(script_dir))

    if structure == 'cards':
        if sub_type_name == '_type':
            generators = constGenerators_vue3.sidecard_type_generators
        else:
            generators = constGenerators_vue3.sidecard_generators
    elif structure == 'modules':
        if sub_type_name == '_type':
            generators = constGenerators_vue3.module_type_generators
        else:
            generators = constGenerators_vue3.module_generators
    else:
        generators = []

    base_path = str(frontend_project_path / prefix)

    for module_name, func_name in generators:
        try:
            module = __import__(module_name)
            generate_func = getattr(module, func_name)
            generate_func(base_path, type_name, sub_type_name)
        except ImportError as e:
            print(f"Error importing {module_name}: {e}")
        except AttributeError as e:
            print(f"Error getting {func_name} from {module_name}: {e}")
        finally:
            if module_name in sys.modules:
                del sys.modules[module_name]

    return str(target_path)
