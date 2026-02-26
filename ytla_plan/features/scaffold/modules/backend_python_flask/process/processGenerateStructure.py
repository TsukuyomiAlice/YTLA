# encode = utf-8

import os
from pathlib import Path
from ytla_plan import config
from ytla_plan.features.scaffold.modules._type.script import scriptCreateFile as File
from ytla_plan.features.scaffold.modules.backend_python_flask.const import constGenerators


def generate_python_structure(is_core: str = 'n', structure: str = 'cards',
                              type_name: str = '', sub_type_name: str = ''):
    """
    Generate Python backend directory structure
    :param is_core: Whether it's a core or feature (y/n, default n)
    :param structure: Structure type (card / module)
    :param type_name: Type category / core version
    :param sub_type_name: SubType category / core sub feature (can be empty, if empty, referred to '_type')
    :return: Generated directory path
    """

    # Validate parameters

    if is_core.lower() != 'y' and structure not in ('cards', 'modules'):
        raise ValueError("structure parameter must be 'cards' or 'modules'")

    if is_core.lower() == 'y' and structure not in ('cards', 'modules', 'plans', 'frame', 'users'):
        raise ValueError("structure parameter must be 'cards', 'modules', 'plans', 'frame' or 'users'")

    if not type_name:
        raise ValueError("type parameter cannot be empty")

    # Determine prefix
    prefix = 'core' if is_core.lower() == 'y' else 'features'

    # Handle subtype
    if not sub_type_name:
        sub_type_name = '_type'

    backend_project_path = Path(config.BACKEND_FOLDER)

    # Generate target path
    type_path = backend_project_path / prefix / type_name
    structure_path = type_path / structure
    target_path = structure_path / sub_type_name

    # important: if the feature is a new feature, but the user set the subtype directly
    # the feature structure should be made at first.
    if (not type_path.exists() or not structure_path.exists()) and sub_type_name != '_type':
        generate_python_structure(is_core, structure, type_name, '')

    # Create main directories
    type_path.mkdir(parents=True, exist_ok=True)
    structure_path.mkdir(parents=True, exist_ok=True)
    target_path.mkdir(parents=True, exist_ok=True)

    # Create __init__.py files for main directories
    # Type path __init__.py
    init_file = type_path / "__init__.py"
    File.create_init_file(init_file)

    # Structure path __init__.py
    init_file = structure_path / "__init__.py"
    File.create_init_file(init_file)

    # Subtype path __init__.py
    init_file = target_path / "__init__.py"
    File.create_init_file(init_file)

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
            generate_func(str(target_path), type_name, sub_type_name)
        except ImportError as e:
            print(f"Error importing {module_name}: {e}")
        except AttributeError as e:
            print(f"Error getting generate function from {module_name}: {e}")
        finally:
            # Always clear module cache
            if module_name in sys.modules:
                del sys.modules[module_name]

    return str(target_path)
