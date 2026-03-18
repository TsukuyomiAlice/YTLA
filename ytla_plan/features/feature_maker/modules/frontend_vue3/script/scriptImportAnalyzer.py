
import os
import re
import json


def find_vue_ts_files(root_dir):
    """
    Recursively find all Vue and TypeScript files in the given root directory.
    
    Args:
        root_dir: The root directory to search for Vue and TypeScript files
        
    Returns:
        A list of absolute file paths for all .vue and .ts files found
    """
    vue_ts_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.vue') or file.endswith('.ts'):
                vue_ts_files.append(os.path.abspath(os.path.join(root, file)))
    return vue_ts_files


def extract_script_from_vue(content):
    """
    Extract script content from a Vue file.
    
    Args:
        content: Full content of the Vue file
        
    Returns:
        Script content as a string
    """
    script_pattern = re.compile(r'<script[^>]*>(.*?)</script>', re.DOTALL)
    match = script_pattern.search(content)
    if match:
        return match.group(1)
    return ''


def extract_style_from_vue(content):
    """
    Extract style content from a Vue file.
    
    Args:
        content: Full content of the Vue file
        
    Returns:
        Style content as a string
    """
    style_pattern = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL)
    match = style_pattern.search(content)
    if match:
        return match.group(1)
    return ''


def extract_imports_from_script(content):
    """
    Extract import statements from TypeScript/JavaScript script content.
    
    Args:
        content: Script content to parse
        
    Returns:
        A list of imported module paths
    """
    imports = []
    import_pattern = re.compile(r'import\s+.*?\s+from\s+[\'"]([^\'"]+)[\'"]')
    
    for match in import_pattern.finditer(content):
        imports.append(match.group(1))
    
    return imports


def extract_style_references(content):
    """
    Extract style references from style content, supporting both @import and @use.
    
    Args:
        content: Style content to parse
        
    Returns:
        A list of style reference paths
    """
    references = []
    style_pattern = re.compile(r'@(?:import|use)\s+[\'"]([^\'"]+)[\'"]')
    
    for match in style_pattern.finditer(content):
        references.append(match.group(1))
    
    return references


def extract_imports_from_file(file_path):
    """
    Extract all imports and references from a file (Vue or TypeScript),
    categorized by import type.
    
    Args:
        file_path: Path to the file to parse
        
    Returns:
        A dictionary with categorized imports and references
    """
    result = {
        'vue_imports': [],
        'ts_imports': [],
        'style_imports': []
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if file_path.endswith('.vue'):
            script_content = extract_script_from_vue(content)
            style_content = extract_style_from_vue(content)
            
            all_imports = extract_imports_from_script(script_content)
            for imp in all_imports:
                if imp.endswith('.vue'):
                    result['vue_imports'].append(imp)
                elif imp.endswith('.ts') or not (imp.endswith('.vue') or imp.endswith('.scss') or imp.endswith('.css')):
                    result['ts_imports'].append(imp)
            
            result['style_imports'] = extract_style_references(style_content)
        
        elif file_path.endswith('.ts'):
            all_imports = extract_imports_from_script(content)
            for imp in all_imports:
                if imp.endswith('.vue'):
                    result['vue_imports'].append(imp)
                elif imp.endswith('.ts') or not (imp.endswith('.vue') or imp.endswith('.scss') or imp.endswith('.css')):
                    result['ts_imports'].append(imp)
    
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                content = f.read()
            
            if file_path.endswith('.vue'):
                script_content = extract_script_from_vue(content)
                style_content = extract_style_from_vue(content)
                
                all_imports = extract_imports_from_script(script_content)
                for imp in all_imports:
                    if imp.endswith('.vue'):
                        result['vue_imports'].append(imp)
                    elif imp.endswith('.ts') or not (imp.endswith('.vue') or imp.endswith('.scss') or imp.endswith('.css')):
                        result['ts_imports'].append(imp)
                
                result['style_imports'] = extract_style_references(style_content)
            
            elif file_path.endswith('.ts'):
                all_imports = extract_imports_from_script(content)
                for imp in all_imports:
                    if imp.endswith('.vue'):
                        result['vue_imports'].append(imp)
                    elif imp.endswith('.ts') or not (imp.endswith('.vue') or imp.endswith('.scss') or imp.endswith('.css')):
                        result['ts_imports'].append(imp)
        except Exception:
            pass
    except Exception:
        pass
    
    return result


def get_module_path(file_path, root_dir):
    """
    Convert a file path to a module path.
    
    Args:
        file_path: Absolute path to the Vue/TypeScript file
        root_dir: Root directory of the project
        
    Returns:
        Module path as a string (e.g., 'src.core.classic.frame')
    """
    rel_path = os.path.relpath(file_path, root_dir)
    return os.path.splitext(rel_path)[0].replace(os.sep, '.')


def organize_files_by_hierarchy(core_modules, features_modules, root_dir):
    """
    Organize files and their imports into a hierarchical structure.
    
    Args:
        core_modules: Dictionary of core modules and their import data
        features_modules: Dictionary of features modules and their import data
        root_dir: Root directory of the project
        
    Returns:
        A nested dictionary representing the file hierarchy with imports
    """
    hierarchy = {}
    
    all_modules = {}
    all_modules.update(core_modules)
    all_modules.update(features_modules)
    
    for (module_path, file_path), import_data in all_modules.items():
        rel_path = os.path.relpath(file_path, root_dir)
        file_path_parts = rel_path.split(os.sep)
        
        current = hierarchy
        for i, part in enumerate(file_path_parts):
            if i == len(file_path_parts) - 1:
                current[part] = {
                    "vue_imports": import_data.get('vue_imports', []),
                    "ts_imports": import_data.get('ts_imports', []),
                    "style_imports": import_data.get('style_imports', [])
                }
            else:
                if part not in current:
                    current[part] = {}
                current = current[part]
    
    return hierarchy


def categorize_modules(vue_ts_files, root_dir):
    """
    Categorize modules into core and features.
    
    Args:
        vue_ts_files: List of all Vue and TypeScript file paths
        root_dir: Root directory of the project
        
    Returns:
        Tuple of (core_modules, features_modules) where each is a dictionary
        mapping (module_path, file_path) tuples to import data
    """
    core_modules = {}
    features_modules = {}
    
    for file_path in vue_ts_files:
        module_path = get_module_path(file_path, root_dir)
        import_data = extract_imports_from_file(file_path)
        
        if module_path.startswith('src.core.'):
            core_modules[(module_path, file_path)] = import_data
        elif module_path.startswith('src.features.'):
            features_modules[(module_path, file_path)] = import_data
    
    return core_modules, features_modules


def is_problematic_import(import_path, module_type, module_path):
    """
    Check if an import path is problematic.
    
    Args:
        import_path: The imported path to check
        module_type: 'core' or 'features'
        module_path: Path of the importing module
        
    Returns:
        True if the import is problematic, False otherwise
    """
    if import_path.startswith('@/features/') or import_path.startswith('./features/'):
        if module_type == 'core':
            return True
        elif module_type == 'features':
            feature_prefix = module_path.split('.')[2]
            imported_feature = import_path.split('/')[2] if import_path.startswith('@/') else import_path.split('/')[1]
            return feature_prefix != imported_feature
    return False


def detect_problematic_imports(core_modules, features_modules):
    """
    Detect problematic imports.
    
    Args:
        core_modules: Dictionary of core modules and their import data
        features_modules: Dictionary of features modules and their import data
        
    Returns:
        Tuple of (core_imports_features, features_imports_features) where each is
        a list of tuples containing (importer_module, imported_path)
    """
    core_imports_features = []
    features_imports_features = []
    
    for (module, _), import_data in core_modules.items():
        all_imports = import_data.get('vue_imports', []) + import_data.get('ts_imports', [])
        for imp in all_imports:
            if is_problematic_import(imp, 'core', module):
                core_imports_features.append((module, imp))
    
    for (module, _), import_data in features_modules.items():
        all_imports = import_data.get('vue_imports', []) + import_data.get('ts_imports', [])
        for imp in all_imports:
            if is_problematic_import(imp, 'features', module):
                features_imports_features.append((module, imp))
    
    return core_imports_features, features_imports_features


def generate_report(core_imports_features, features_imports_features, all_files, core_modules, features_modules, output_dir, root_dir):
    """
    Generate an analysis report in JSON format.
    
    Args:
        core_imports_features: List of core modules importing from features
        features_imports_features: List of features modules importing from other features
        all_files: List of all files checked
        core_modules: Dictionary of core modules and their import data
        features_modules: Dictionary of features modules and their import data
        output_dir: Directory to save the report
        root_dir: Root directory of the project
        
    Returns:
        Path to the generated report file
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    report_path = os.path.join(output_dir, 'frontend_import_analysis_report.json')
    
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
    root_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..', '..', '..', '..'))
    vue_project_root = os.path.join(root_dir, 'ytla_plan_vue')
    
    if output_dir is None:
        output_dir = os.getcwd()
    
    src_dir = os.path.join(vue_project_root, 'src')
    core_dir = os.path.join(src_dir, 'core')
    features_dir = os.path.join(src_dir, 'features')
    
    core_files = find_vue_ts_files(core_dir)
    features_files = find_vue_ts_files(features_dir)
    
    all_files = core_files + features_files
    
    core_modules, features_modules = categorize_modules(all_files, vue_project_root)
    
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
        vue_project_root
    )
    
    return report_path


if __name__ == '__main__':
    import sys
    
    output_dir = None
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    
    report_path = analyze_imports(output_dir=output_dir)
    print('report generated:', report_path)

