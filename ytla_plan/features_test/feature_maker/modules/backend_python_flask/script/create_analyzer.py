
import os

script_content = '''import os
import re


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
    import_pattern = re.compile(r'^\\s*(import|from)\\s+([a-zA-Z0-9_.]+)')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = import_pattern.match(line)
                if match:
                    imports.append(match.group(2)))
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='gbk') as f:
                for line in f:
                    match = import_pattern.match(line)
                    if match:
                        imports.append(match.group(2)))
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
            core_modules[module_path] = imports
        elif module_path.startswith('features.'):
            features_modules[module_path] = imports
    
    return core_modules, features_modules


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
    
    for module, imports in core_modules.items():
        for imp in imports:
            if imp.startswith('features.'):
                core_imports_features.append((module, imp)))
    
    for module, imports in features_modules.items():
        feature_prefix = '.'.join(module.split('.')[:2])
        for imp in imports:
            if imp.startswith('features.') and not imp.startswith(feature_prefix):
                features_imports_features.append((module, imp)))
    
    return core_imports_features, features_imports_features


def generate_report(core_imports_features, features_imports_features, output_dir, root_dir):
    """
    Generate a Chinese analysis report in TXT format with tab separators.
    
    Args:
        core_imports_features: List of core modules importing from features
        features_imports_features: List of features modules importing from other features
        output_dir: Directory to save the report
        root_dir: Root directory of the project
        
    Returns:
        Path to the generated report file
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    report_path = os.path.join(output_dir, 'import_analysis_report.txt')
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('=' * 80 + '\\n')
        f.write('Python 导入分析报告\\n')
        f.write('=' * 80 + '\\n\\n')
        
        f.write('项目根目录: ' + root_dir + '\\n\\n')
        
        f.write('-' * 80 + '\\n')
        f.write('问题1: core 模块导入 features 模块\\n')
        f.write('-' * 80 + '\\n')
        
        if core_imports_features:
            f.write('发现 ' + str(len(core_imports_features)) + ' 个违规导入:\\n\\n')
            f.write('导入模块\\t被导入模块\\n')
            f.write('-' * 80 + '\\n')
            for importer, imported in core_imports_features:
                f.write(importer + '\\t' + imported + '\\n')
        else:
            f.write('未发现违规导入。\\n')
        
        f.write('\\n\\n')
        
        f.write('-' * 80 + '\\n')
        f.write('问题2: features 模块导入其他 features 模块\\n')
        f.write('-' * 80 + '\\n')
        
        if features_imports_features:
            f.write('发现 ' + str(len(features_imports_features)) + ' 个违规导入:\\n\\n')
            f.write('导入模块\\t被导入模块\\n')
            f.write('-' * 80 + '\\n')
            for importer, imported in features_imports_features:
                f.write(importer + '\\t' + imported + '\\n')
        else:
            f.write('未发现违规导入。\\n')
        
        f.write('\\n\\n')
        f.write('=' * 80 + '\\n')
        f.write('报告生成完成\\n')
        f.write('=' * 80 + '\\n')
    
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
    # Calculate root directory correctly
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up 4 levels from: script/ -> backend_python_flask/ -> modules/ -> feature_maker/ -> features/ -> ytla_plan/
    root_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..', '..'))
    
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
    print('报告已生成:', report_path)
'''

target_path = os.path.join(os.path.dirname(__file__), 'features', 'feature_maker', 'modules', 'backend_python_flask', 'script', 'scriptImportAnalyzer.py')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(script_content)

print(f"File created at: {target_path}")
