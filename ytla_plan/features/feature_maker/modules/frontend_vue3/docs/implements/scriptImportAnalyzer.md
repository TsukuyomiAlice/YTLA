# Frontend Vue3 Import Analyzer

## Overview

This module analyzes import relationships in Vue and TypeScript frontend files to detect architectural boundary violations. It identifies when core modules import from features modules, and when feature modules import from other feature modules.

## Project Structure

```
frontend_vue3/
├── script/
│   └── scriptImportAnalyzer.py  # Main analyzer script
└── docs/
    └── implements/
        └── scriptImportAnalyzer.md  # This file
```

## Key Features

1. **Recursive File Scanning**: Scans `src/core/` directory first, then `src/features/` directory
2. **Multi-File Support**: Handles both `.vue` and `.ts` files
3. **Vue File Parsing**:
   - Extracts `<script>` content for imports
   - Extracts `<style>` content for SCSS references
4. **Import Categorization**:
   - `vue_imports`: Imports of Vue files (.vue)
   - `ts_imports`: Imports of TypeScript files (.ts or modules)
   - `style_imports`: SCSS/CSS style references (@import or @use)
5. **Problem Detection**:
   - Core modules importing from features modules
   - Feature modules importing from other feature modules
6. **JSON Report Generation**: Generates structured JSON report
7. **Hierarchical File Structure**: Files organized by project directory hierarchy

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

### `find_vue_ts_files(root_dir)`

Recursively finds all Vue and TypeScript files in the given root directory.

### `extract_script_from_vue(content)`

Extracts `<script>` tag content from a Vue file using regex.

### `extract_style_from_vue(content)`

Extracts `<style>` tag content from a Vue file using regex.

### `extract_imports_from_script(content)`

Extracts ES6 import statements from TypeScript/JavaScript content.

### `extract_style_references(content)`

Extracts style references from style content, supporting both `@import` and `@use` syntax.

### `extract_imports_from_file(file_path)`

Extracts all imports and references from a file, categorized by type:
- `vue_imports`: Vue file imports
- `ts_imports`: TypeScript/module imports
- `style_imports`: SCSS/CSS style references

### `get_module_path(file_path, root_dir)`

Converts a file path to a module path string.

### `organize_files_by_hierarchy(core_modules, features_modules, root_dir)`

Organizes files and their imports into a nested hierarchical structure.

### `categorize_modules(vue_ts_files, root_dir)`

Categorizes modules into core and features based on their path.

### `is_problematic_import(import_path, module_type, module_path)`

Checks if an import path violates architectural boundaries.

### `detect_problematic_imports(core_modules, features_modules)`

Detects problematic imports:
- Core modules importing from features
- Features modules importing from other features

### `generate_report(...)`

Generates the final JSON report.

## JSON Output Structure

```json
{
  "project_root": "D:\\YTLA\\ytla_plan_vue",
  "core_calls_features": [
    {
      "importer": "src.core.classic.frame.main.avatar.Avatar",
      "imported": "@/features/some/component"
    }
  ],
  "features_calls_features": [
    {
      "importer": "src.features.featureA.component",
      "imported": "@/features/featureB/component"
    }
  ],
  "all_files": {
    "src": {
      "core": {
        "classic": {
          "frame": {
            "main": {
              "avatar": {
                "Avatar.vue": {
                  "vue_imports": [
                    "@/core/classic/frame/main/utils/timeUtils"
                  ],
                  "ts_imports": [],
                  "style_imports": [
                    "@use './styles/layout.scss'",
                    "@import './styles/colors.scss'"
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
}
```

## Usage

### As a Module

```python
from features.feature_maker.modules.frontend_vue3.script.scriptImportAnalyzer import analyze_imports

report_path = analyze_imports(output_dir='./output')
```

### Command Line

```bash
python features/feature_maker/modules/frontend_vue3/script/scriptImportAnalyzer.py [output_directory]
```

## Dependencies

- **Standard Library Only**: Uses only Python built-in modules
  - `os` - File system operations
  - `re` - Regular expressions for parsing
  - `json` - JSON report generation

## Import Types Categorized

### `vue_imports`
- Files ending with `.vue` extension
- Example: `@/components/MyComponent.vue`

### `ts_imports`
- Files ending with `.ts` extension
- Modules without file extensions
- Example: `@/utils/helpers`, `./utils.ts`

### `style_imports`
- SCSS/CSS files referenced via `@import` or `@use`
- Example: `@use './styles/variables.scss'`, `@import './styles/mixins.scss'`

## Architectural Rules Enforced

1. **Core → Features**: Forbidden
   - Core modules should not depend on feature modules
   - Core should contain only foundational code

2. **Features → Features**: Forbidden (except same feature)
   - Feature modules should not depend on other feature modules
   - Features should be independent and only depend on core

## Notes

- The analyzer first scans `src/core/`, then `src/features/`
- Vue files are parsed to extract both script imports and style references
- TypeScript files are parsed for imports only
- Style references support both `@import` (legacy) and `@use` (modern Sass)
- All imports are tracked and categorized by type
- Report uses UTF-8 encoding
- No third-party packages required
- Frontend project is located in `ytla_plan_vue/` directory
