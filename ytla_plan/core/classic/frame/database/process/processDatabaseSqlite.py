# encoding = utf-8

import os
import importlib

from ytla_plan import config

def get_db_folder_path():
    """
    Retrieve the database directory path with system-appropriate separators

    Returns:
        str: Platform-dependent path using native filesystem separators
        - POSIX systems: Uses forward slashes (/)
        - Windows: Uses backslashes (\\)

    Note:
        The actual storage location differs by OS, but the relative
        path structure remains consistent
    """
    s = '/YTLA_DATAS'
    if os.name == 'posix':
        s = '/YTLA_DATAS/ytla_plan'
    if os.name == 'nt':
        s = 'D:\\YTLA_DATA\\ytla_plan'
    return s


db_folder_path = get_db_folder_path()

default_db_files = {}

# 内部状态
_initialized = False
_db_files = {}


def get_db_files():
    """
    获取 db_files，如果未初始化则自动初始化
    
    Returns:
        Merged db_files dict
    """
    global _initialized, _db_files
    if not _initialized:
        load_and_merge_db_files()
    return _db_files


# 为了保持向后兼容，提供 db_files 属性
# 注意：直接访问 db_files 不会自动初始化，请使用 get_db_files()
db_files = {}


def scan_config_files(scan_target_dir: str, config_files: list[str]) -> list[str]:
    """
    Scan a directory for config_database_sqlite.py files

    Args:
        scan_target_dir: Target directory to scan
        config_files: List to collect config file paths

    Returns:
        Updated list of config file paths
    """
    for root, dirs, files in os.walk(scan_target_dir):
        if 'utils' in dirs:
            utils_dir = os.path.join(root, 'utils')
            for file in os.listdir(utils_dir):
                if file == 'config_database_sqlite.py':
                    config_files.append(os.path.join(utils_dir, file))
    return config_files


def find_config_files():
    """
    Recursively scan core and features directories to find config_database_sqlite.py files

    Returns:
        List of found config file paths
    """
    config_files = []

    # Scan core directory
    core_dir = os.path.join(config.BACKEND_FOLDER, 'core')
    if os.path.exists(core_dir):
        config_files = scan_config_files(core_dir, config_files)

    # Scan features directory
    features_dir = os.path.join(config.BACKEND_FOLDER, 'features')
    if os.path.exists(features_dir):
        config_files = scan_config_files(features_dir, config_files)

    return config_files


def build_import_path(file_path) -> str:
    """
    Build import path based on file path

    Args:
        file_path: The file path to convert

    Returns:
        The import path as a string
    """
    relative_path = os.path.relpath(file_path, config.BACKEND_FOLDER)
    import_path = relative_path.replace(os.path.sep, '.').replace('.py', '')
    return str(import_path)


def collect_db_files_from_config(config_file_path):
    """
    Collect db_files from a single config file

    Args:
        config_file_path: Path to the config_database_sqlite.py file

    Returns:
        db_files dict from the config file, or empty dict if failed
    """
    try:
        import_path = build_import_path(config_file_path)
        module = importlib.import_module(import_path)
        if hasattr(module, 'db_files'):
            return module.db_files
    except Exception as e:
        print(f"Error importing db_files from {config_file_path}: {str(e)}")
    return {}


def load_and_merge_db_files():
    """
    Load and merge all db_files from config files and default config

    Returns:
        Merged db_files dict
    """
    global _initialized, _db_files, db_files
    
    # Start with default config
    merged_db_files = default_db_files.copy()
    
    # Find all config files
    config_files = find_config_files()
    
    # Collect and merge db_files from each config
    for config_file in config_files:
        module_db_files = collect_db_files_from_config(config_file)
        merged_db_files.update(module_db_files)
        print(f"Loaded db_files from {config_file}: {list(module_db_files.keys())}")
    
    # Update the internal state
    _db_files = merged_db_files
    db_files = merged_db_files  # 同时更新向后兼容的变量
    _initialized = True
    print(f"Total merged db_files: {list(_db_files.keys())}")
    
    return _db_files


def initialize():
    """
    Initialize the database configuration loader

    This should be called once at application startup
    """
    print("Initializing database configuration loader...")
    load_and_merge_db_files()
    print("Database configuration loader initialized successfully")
