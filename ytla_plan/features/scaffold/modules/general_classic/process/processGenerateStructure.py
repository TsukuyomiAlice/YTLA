# encode = utf-8

from features.scaffold.modules.backend_python_flask.process.processGenerateStructure import generate_python_structure
from features.scaffold.modules.frontend_vue3.process.processGenerateStructure import generate_vue3_structure


def process_generate_structure(is_core: str = 'n', structure: str = 'cards',
                               type_name: str = '', subtype: str = '', only_backend: bool = False):
    """
    Process structure generation for core_classic
    core_classic will use backend_python and frontend_vue3
    :param is_core: Whether it's a core or feature (y/n, default n)
    :param structure: Structure type (cards / modules)
    :param type_name: Type category / core version
    :param subtype: SubType category / core sub feature (can be empty, if empty, referred to '_type')
    :param only_backend: If True, only the backend structure will be generated.
    :return: Dictionary with generation results
    """
    backend_result = None
    frontend_result = None

    try:
        # Validate parameters
        if not type_name:
            raise ValueError("type parameter cannot be empty")

        if is_core.lower() is not 'y' and structure not in ('cards', 'modules'):
            raise ValueError("structure parameter must be 'cards' or 'modules'")

        if is_core.lower() is 'y' and structure not in ('cards', 'modules', 'plans', 'frame', 'users'):
            raise ValueError("structure parameter must be 'cards', 'modules', 'plans', 'frame' or 'users'")

        # Handle subtype
        if not subtype:
            subtype = '_type'

        # Generate backend structure
        backend_result = generate_python_structure(is_core, structure, type_name, subtype)

        # Generate frontend structure
        # The basic scaffold of the frontend should be generated to provide the access point from the webpage
        if not only_backend and subtype != '_type':
            frontend_result = generate_vue3_structure(is_core, structure, type_name, subtype)

        # Return combined result
        return {
            "success": True,
            "message": "Structure generated successfully",
            "results": {
                "backend": backend_result,
                "frontend": frontend_result
            }
        }

    except Exception as e:
        # Handle errors
        return {
            "success": False,
            "message": str(e),
            "results": {
                "backend": backend_result,
                "frontend": frontend_result
            }
        }


def main():
    """
    Main function for testing
    """
    # Example usage
    result = process_generate_structure('n', 'modules', 'divination', '', False)
    print(result)


if __name__ == "__main__":
    main()