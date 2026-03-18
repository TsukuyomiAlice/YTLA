
import os
import re
import json


def find_python_files(root_dir):
    """
    Recursively find all Python files in the given root directory.
    
    Args:
        root_dir: The root directory to search for Python files
        
    Returns:
        A list of absolute file paths for all .py files found
    """
    python_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.abspath(os.path.join(root, file)))
    return python_files


def extract_imports(file_path):
    """
    Extract import statements from a Python file.
    
    Args:
        file_path: Path to the Python file to parse
        
    Returns:
        A list of imported module paths
    """
    imports = []
    import_pattern = re.compile(r'^\s*(import|from)\s+([a-zA-Z0-9_.]+)')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = import_pattern.match(line)
                if match:
                    imports.append(match.group(2))
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                for line in f:
                    match = import_pattern.match(line)
                    if match:
                        imports.append(match.group(2))
        except Exception:
            pass
    except Exception:
        pass
    
    return imports


def get_module_path(file_path, root_dir):
    """
    Convert a file path to a module path.
    
    Args:
        file_path: Absolute path to the Python file
        root_dir: Root directory of the project
        
    Returns:
        Module path as a string (e.g., 'core.classic.frame')
    """
    rel_path = os.path.relpath(file_path, root_dir)
    if rel_path.endswith('__init__.py'):
        dir_path = os.path.dirname(rel_path)
        if dir_path == '.':
            return ''
        return dir_path.replace(os.sep, '.')
    else:
        return os.path.splitext(rel_path)[0].replace(os.sep, '.')


def categorize_modules(python_files, root_dir):
    """
    Categorize modules into core and features.
    
    Args:
        python_files: List of all Python file paths
        root_dir: Root directory of the project
        
    Returns:
        Tuple of (core_modules, features_modules) where each is a dictionary
        mapping module paths to lists of imported modules
    """
    core_modules = {}
    features_modules = {}
    
    for file_path in python_files:
        module_path = get_module_path(file_path, root_dir)
        imports = extract_imports(file_path)
        
        if module_path.startswith('core.'):
            core_modules[(module_path, file_path)] = imports
        elif module_path.startswith('features.'):
            features_modules[(module_path, file_path)] = imports
    
    return core_modules, features_modules


def organize_files_by_hierarchy(core_modules, features_modules, root_dir):
    """
    Organize files and their imports into a hierarchical structure.
    
    Args:
        core_modules: Dictionary of core modules and their imports
        features_modules: Dictionary of features modules and their imports
        root_dir: Root directory of the project
        
    Returns:
        A nested dictionary representing the file hierarchy with imports
    """
    hierarchy = {}
    
    all_modules = {}
    all_modules.update(core_modules)
    all_modules.update(features_modules)
    
    for (module_path, file_path), imports in all_modules.items():
        rel_path = os.path.relpath(file_path, root_dir)
        file_path_parts = rel_path.split(os.sep)
        
        current = hierarchy
        for i, part in enumerate(file_path_parts):
            if i == len(file_path_parts) - 1:
                current[part] = {"imports": imports}
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]
    
    return hierarchy


def detect_problematic_imports(core_modules, features_modules):
    """
    Detect problematic imports.
    
    Args:
        core_modules: Dictionary of core modules and their imports
        features_modules: Dictionary of features modules and their imports
        
    Returns:
        Tuple of (core_imports_features, features_imports_features) where each is
        a list of tuples containing (importer_module, imported_module)
    """
    core_imports_features = []
    features_imports_features = []
    
    for (module, _), imports in core_modules.items():
        for imp in imports:
            if imp.startswith('features.'):
                core_imports_features.append((module, imp))
    
    for (module, _), imports in features_modules.items():
        feature_prefix = '.'.join(module.split('.')[:2])
        for imp in imports:
            if imp.startswith('features.') and not imp.startswith(feature_prefix):
                features_imports_features.append((module, imp))
    
    return core_imports_features, features_imports_features


def generate_report(core_imports_features, features_imports_features, all_files, core_modules, features_modules, output_dir, root_dir):
    """
    Generate an analysis report in JSON format.
    
    Args:
        core_imports_features: List of core modules importing from features
        features_imports_features: List of features modules importing from other features
        all_files: List of all files checked
        core_modules: Dictionary of core modules and their imports
        features_modules: Dictionary of features modules and their imports
        output_dir: Directory to save the report
        root_dir: Root directory of the project
        
    Returns:
        Path to the generated report file
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    report_path = os.path.join(output_dir, 'import_analysis_report.json')
    
    core_calls_features = [
        {"importer": importer, "imported": imported}
        for importer, imported in core_imports_features
    ]
    
    features_calls_features = [
        {"importer": importer, "imported": imported}
        for importer, imported in features_imports_features
    ]
    
    report_data = {
        "project_root": root_dir,
        "core_calls_features": core_calls_features,
        "features_calls_features": features_calls_features,
        "all_files": organize_files_by_hierarchy(core_modules, features_modules, root_dir)
    }
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    
    return report_path


def analyze_imports(file_path=None, output_dir=None):
    """
    Main entry point for the import analyzer.
    
    Args:
        file_path: Optional specific file to analyze (not used in full scan mode)
        output_dir: Directory to save the analysis report. If None, defaults to the current directory.
        
    Returns:
        Path to the generated report file
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..', '..', '..'))
    
    if output_dir is None:
        output_dir = os.getcwd()
    
    core_dir = os.path.join(root_dir, 'core')
    features_dir = os.path.join(root_dir, 'features')
    
    core_files = find_python_files(core_dir)
    features_files = find_python_files(features_dir)
    
    all_files = core_files + features_files
    
    core_modules, features_modules = categorize_modules(all_files, root_dir)
    
    core_imports_features, features_imports_features = detect_problematic_imports(
        core_modules, features_modules
    )
    
    report_path = generate_report(
        core_imports_features,
        features_imports_features,
        all_files,
        core_modules,
        features_modules,
        output_dir,
        root_dir
    )
    
    return report_path


if __name__ == '__main__':
    import sys
    
    output_dir = None
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    
    report_path = analyze_imports(output_dir=output_dir)
    print('report generated:', report_path)
