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


def generate_python_structure(is_core: str = 'n', structure: str = 'cards',
                              type_name: str = '', subtype: str = ''):
    """
    Generate Python backend directory structure
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

    # Calculate backend project path automatically
    current_file = Path(__file__)
    # Navigate up to \YTLA
    ytla_root = current_file.parent.parent.parent.parent.parent.parent
    backend_project_path = ytla_root / 'ytla_plan'

    # Generate target path
    type_path = backend_project_path / prefix / type_name
    base_path = type_path / structure
    target_path = base_path / subtype

    # Base directory structure
    base_structure = [
        "docs",
        "instance",
        "process",
        "schedule",
        "script",
        "dataset",
        "api",
        "dao",
        "routes",
        "const",
        "ai_tools",
        "caller",
        "func"
    ]

    # Create directory structure
    for dir_name in base_structure:
        dir_path = target_path / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)

        # Create __init__.py file
        init_file = dir_path / "__init__.py"
        with open(init_file, 'w', encoding='utf-8') as f:
            f.write('')

    # Type path __init__.py
    init_file = type_path / "__init__.py"
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write('')

    # Structure path __init__.py
    init_file = base_path / "__init__.py"
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write('')

    # Subtype path __init__.py
    init_file = target_path / "__init__.py"
    with open(init_file, 'w', encoding='utf-8') as f:
        f.write('')

    # components
    if subtype != '_type':
        component_name = first_letter_upper(subtype)
    else:
        component_name = first_letter_upper(type_name)
        subtype = first_letter_lower(type_name)

    # process directory
    process_file = target_path / "process" / f"process{component_name}.py"
    with open(process_file, 'w', encoding='utf-8') as f:
        f.write('')

    # routes directory
    routes_file = target_path / "routes" / f"route{component_name}.py"
    with open(routes_file, 'w', encoding='utf-8') as f:
        f.write('')

    return str(target_path)
