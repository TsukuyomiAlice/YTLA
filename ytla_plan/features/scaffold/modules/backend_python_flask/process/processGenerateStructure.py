# encode = utf-8

from pathlib import Path
import os
from ytla_plan.features.scaffold.modules.backend_python_flask.const import constGenerators

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


def create_init_file(init_file_path: Path):
    """
    Generate a blank file. Not only for __init__.py
    :param init_file_path: The path of the init file
    :return: None
    """
    if not init_file_path.exists():
        with open(init_file_path, 'w', encoding='utf-8') as f:
            f.write('')


def generate_python_structure(is_core: str = 'n', structure: str = 'cards',
                              type_name: str = '', subtype: str = ''):
    """
    Generate Python backend directory structure
    :param is_core: Whether it's a core or feature (y/n, default n)
    :param structure: Structure type (card / module)
    :param type_name: Type category / core version
    :param subtype: SubType category / core sub feature (can be empty, if empty, referred to '_type')
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
    if not subtype:
        subtype = '_type'

    # Calculate backend project path automatically
    current_file = Path(__file__)
    # Navigate up to \YTLA
    ytla_root = current_file.parent.parent.parent.parent.parent.parent.parent
    # todo: hard code for 'ytla_plan'
    backend_project_path = ytla_root / 'ytla_plan'

    # Generate target path
    type_path = backend_project_path / prefix / type_name
    base_path = type_path / structure
    target_path = base_path / subtype

    # Create main directories
    type_path.mkdir(parents=True, exist_ok=True)
    base_path.mkdir(parents=True, exist_ok=True)
    target_path.mkdir(parents=True, exist_ok=True)

    # Create __init__.py files for main directories
    # Type path __init__.py
    init_file = type_path / "__init__.py"
    create_init_file(init_file)

    # Structure path __init__.py
    init_file = base_path / "__init__.py"
    create_init_file(init_file)

    # Subtype path __init__.py
    init_file = target_path / "__init__.py"
    create_init_file(init_file)

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

    # components
    if subtype != '_type':
        component_name = first_letter_upper(subtype)
    else:
        component_name = first_letter_upper(type_name)
        subtype = first_letter_lower(type_name)

    # Create route file
    routes_dir = target_path / "routes"
    if routes_dir.exists():
        routes_file = routes_dir / f"route{component_name}.py"
        create_init_file(routes_file)

    return str(target_path)
