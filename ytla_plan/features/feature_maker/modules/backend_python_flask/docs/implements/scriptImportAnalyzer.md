# Backend Python Flask Import Analyzer

## Overview

This module analyzes import relationships in Python backend files to detect architectural boundary violations. It identifies when core modules import from features modules, and when feature modules import from other feature modules.

## Project Structure

```
backend_python_flask/
├── script/
│   └── scriptImportAnalyzer.py  # Main analyzer script
└── docs/
    └── implements/
        └── scriptImportAnalyzer.md  # This file
```

## Key Features

1. **Recursive File Scanning**: Scans `core/` directory first, then `features/` directory
2. **Python Import Parsing**: Extracts both `import module` and `from module import x` statements
3. **Problem Detection**:
   - Core modules importing from features modules
   - Feature modules importing from other feature modules
4. **JSON Report Generation**: Generates structured JSON report with categorized imports
5. **Hierarchical File Structure**: Files organized by project directory hierarchy

## Module API

### Main Entry Point

```python
def analyze_imports(file_path=None, output_dir=None)
```

- **Purpose**: Main entry point for running the import analysis
- **Parameters**:
  - `file_path`: Optional specific file to analyze (not used in full scan mode)
  - `output_dir`: Directory to save the analysis report (defaults to current directory)
- **Returns**: Path to the generated report file

## Core Functions

### `find_python_files(root_dir)`

Recursively finds all Python files in the given root directory.

### `extract_imports(file_path)`

Extracts import statements from a Python file using regex pattern matching.

### `get_module_path(file_path, root_dir)`

Converts a file path to a Python module path.

### `categorize_modules(python_files, root_dir)`

Categorizes modules into core and features based on their path.

### `organize_files_by_hierarchy(core_modules, features_modules, root_dir)`

Organizes files and their imports into a nested hierarchical structure.

### `detect_problematic_imports(core_modules, features_modules)`

Detects problematic imports:
- Core modules importing from features
- Features modules importing from other features

### `generate_report(...)`

Generates the final JSON report.

## JSON Output Structure

```json
{
  "project_root": "D:\\YTLA\\ytla_plan",
  "core_calls_features": [
    {
      "importer": "core.classic.some.module",
      "imported": "features.some.feature.module"
    }
  ],
  "features_calls_features": [
    {
      "importer": "features.featureA.module",
      "imported": "features.featureB.module"
    }
  ],
  "all_files": {
    "core": {
      "classic": {
        "cards": {
          "sideCard": {
            "dao": {
              "daoCards.py": {
                "imports": [
                  "core.classic.frame._type.func.sqliteConnector"
                ]
              }
            }
          }
        }
      }
    },
    "features": {
      ...
    }
  }
}
```

## Usage

### As a Module

```python
from features.feature_maker.modules.backend_python_flask.script.scriptImportAnalyzer import analyze_imports

report_path = analyze_imports(output_dir='./output')
```

### Command Line

```bash
python features/feature_maker/modules/backend_python_flask/script/scriptImportAnalyzer.py [output_directory]
```

## Dependencies

- **Standard Library Only**: Uses only Python built-in modules
  - `os` - File system operations
  - `re` - Regular expressions for import parsing
  - `json` - JSON report generation

## Architectural Rules Enforced

1. **Core → Features**: Forbidden
   - Core modules should not depend on feature modules
   - Core should contain only foundational code

2. **Features → Features**: Forbidden (except same feature)
   - Feature modules should not depend on other feature modules
   - Features should be independent and only depend on core

## Notes

- The analyzer first scans `core/`, then `features/`
- All imports are tracked and categorized
- Report uses UTF-8 encoding
- No third-party packages required
