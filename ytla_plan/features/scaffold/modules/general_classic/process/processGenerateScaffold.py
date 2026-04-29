# encode = utf-8

from features.scaffold.modules.general_classic.process.processGenerateStructure import process_generate_structure


def generate_scaffold(is_core: bool, type_name: str, structure: str, sub_type_name: str, gen_backend: bool, gen_frontend: bool):
    """
    Generate scaffold by calling process_generate_structure
    :param is_core: Whether it's a core or feature
    :param type_name: Type category / core version name
    :param structure: Structure type
    :param sub_type_name: SubType category / core sub feature
    :param gen_backend: If True, the backend structure will be generated
    :param gen_frontend: If True, the frontend structure will be generated
    :return: Dictionary with generation results
    """
    try:
        if not type_name:
            raise ValueError("type_name parameter cannot be empty")

        if not is_core and structure not in ('cards', 'modules'):
            raise ValueError("structure parameter must be 'cards' or 'modules' for feature")

        if is_core and structure not in ('cards', 'modules', 'plans', 'frame', 'users'):
            raise ValueError("structure parameter must be 'cards', 'modules', 'plans', 'frame' or 'users' for core")

        result = process_generate_structure(
            is_core=is_core,
            type_name=type_name,
            structure=structure,
            sub_type_name=sub_type_name,
            gen_backend=gen_backend,
            gen_frontend=gen_frontend
        )

        return result

    except ValueError as ve:
        return {
            "success": False,
            "message": str(ve),
            "results": {
                "backend": None,
                "frontend": None
            }
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error generating scaffold: {str(e)}",
            "results": {
                "backend": None,
                "frontend": None
            }
        }
