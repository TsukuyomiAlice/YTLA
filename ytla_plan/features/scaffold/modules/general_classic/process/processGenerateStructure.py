# encode = utf-8

from features.scaffold.modules.backend_python_flask.process.processGenerateStructure import generate_python_structure
from features.scaffold.modules.frontend_vue3.process.processGenerateStructure import generate_vue3_structure


def process_generate_structure(is_core: str = 'n', structure: str = 'cards',
                               type_name: str = '', sub_type_name: str = '', only_backend: bool = False):
    """
    Process structure generation for core_classic
    core_classic will use backend_python and frontend_vue3
    :param is_core: Whether it's a core or feature (y/n, default n)
    :param structure: Structure type (cards / modules for feature, while cards, modules, plans, frame, users for core)
    :param type_name: Type category / core version
    :param sub_type_name: SubType category / core sub feature (can be empty, if empty, referred to '_type')
    :param only_backend: If True, only the backend structure will be generated.
    :return: Dictionary with generation results
    """
    backend_result = None
    frontend_result = None

    try:
        # Validate parameters
        if not type_name:
            raise ValueError("type parameter cannot be empty")

        if is_core.lower() != 'y' and structure not in ('cards', 'modules'):
            raise ValueError("structure parameter must be 'cards' or 'modules'")

        if is_core.lower() == 'y' and structure not in ('cards', 'modules', 'plans', 'frame', 'users'):
            raise ValueError("structure parameter must be 'cards', 'modules', 'plans', 'frame' or 'users'")

        # Handle subtype
        if not sub_type_name:
            sub_type_name = '_type'

        # Generate backend structure
        backend_result = generate_python_structure(is_core, structure, type_name, sub_type_name)

        # Generate frontend structure
        # The basic scaffold of the frontend should be generated to provide the access point from the webpage
        if not only_backend and sub_type_name != '_type':
            frontend_result = generate_vue3_structure(is_core, structure, type_name, sub_type_name)

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
    result1 = process_generate_structure('n', 'modules', 'unique', 'test1', False)
    print(result1)
    result2 = process_generate_structure('n', 'modules', 'unique', 'test2', True)
    print(result2)
    result3 = process_generate_structure('n', 'cards', 'unique', 'test3', False)
    print(result3)


if __name__ == "__main__":
    main()