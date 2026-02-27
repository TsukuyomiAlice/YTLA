# encoding = utf-8

import os
import importlib

from ytla_plan import config

base_dir = config.BACKEND_FOLDER


def scan_route_files(scan_target_dir: str, route_files: list[str]) -> list[str]:
    """
    Scan a directory for route files that match the rules
    :param scan_target_dir: Target directory
    :param route_files: List to collect route files
    :return route_files: Updated list of route files
    """
    for root, dirs, files in os.walk(scan_target_dir):
        if 'routes' in dirs:
            routes_dir = os.path.join(root, 'routes')
            for file in os.listdir(routes_dir):
                if file.startswith('route') and file.endswith('.py'):
                    route_files.append(os.path.join(routes_dir, file))
    return route_files


def find_route_files():
    """
    Recursively scan core and features directories to find route files that match the rules
    Rule: core(or features)/type/subtype/routes/route*.py
    :return route_files: List of found route files
    """
    route_files = []

    # Scan core directory
    core_dir = os.path.join(base_dir, 'core')
    if os.path.exists(core_dir):
        route_files = scan_route_files(core_dir, route_files)

    # Scan features directory
    features_dir = os.path.join(base_dir, 'features')
    if os.path.exists(features_dir):
        route_files = scan_route_files(features_dir, route_files)

    return route_files


def build_import_path(file_path) -> str:
    """
    Build import path based on file path
    :param file_path: The file path to convert
    :return route_files: The import path
    """
    relative_path = os.path.relpath(file_path, base_dir)
    import_path = relative_path.replace(os.path.sep, '.').replace('.py', '')
    return str(import_path)


def find_blueprint_in_module(module):
    """
    Find Blueprint instances in the module
    Convention: Blueprint instances are named *_bp
    :param module: The module to search
    :return blueprints: List of found Blueprint instances
    """
    blueprints = []
    for name, obj in module.__dict__.items():
        if name.endswith('_bp') and hasattr(obj, 'route'):
            blueprints.append(obj)
    return blueprints


def register_dynamic_blueprints(app):
    """
    Dynamically register all Blueprints
    :param app: The Flask application instance
    :return registered_blueprints: List of registered blueprint names
    """
    route_files = find_route_files()
    registered_blueprints = []

    for route_file in route_files:
        try:
            import_path = build_import_path(route_file)
            module = importlib.import_module(import_path)
            blueprints = find_blueprint_in_module(module)

            for blueprint in blueprints:
                app.register_blueprint(blueprint)
                registered_blueprints.append(blueprint.name)
                # print(f"Registered blueprint: {blueprint.name}")
        except Exception as e:
            print(f"Error registering blueprint from {route_file}: {str(e)}")

    print(f"Total registered blueprints: {len(registered_blueprints)}")
    return registered_blueprints
