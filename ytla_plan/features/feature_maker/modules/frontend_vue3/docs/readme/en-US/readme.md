<p>
 language
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>


# feature_maker - frontend_vue3

### YTLA Application Feature

### Official

version 1.0

Backend Language and Framework: Python-Flask  
Applicable YTLA core version: **classic**  
File Update Date: 2026-03-09

## Concepts

The frontend_vue3 module is a Vue3 frontend import analysis tool that scans Vue and TypeScript files, detects architectural boundary violations (such as core modules importing from features modules), and generates JSON reports. This module is part of feature_maker and helps ensure architectural compliance of frontend code.

## Feature Package Directory

```
frontend_vue3/
├── __init__.py
├── ai_tools/__init__.py
├── api/__init__.py
├── caller/__init__.py
├── const/__init__.py
├── dao/__init__.py
├── dataset/__init__.py
├── docs/
│   ├── implements/scriptImportAnalyzer.md
│   ├── readme/
│   │   ├── en-US/readme.md
│   │   └── zh-CN/readme.md
│   └── rules/rule.md
├── func/__init__.py
├── instance/__init__.py
├── process/__init__.py
├── prompts/__init__.py
├── readme.md
├── routes/__init__.py
├── schedule/__init__.py
├── script/
│   ├── __init__.py
│   └── scriptImportAnalyzer.py
└── utils/__init__.py
```

**Key Directory Descriptions:**
- `script/`: Contains the main analysis script `scriptImportAnalyzer.py`
- `docs/`: Documentation directory, including implementation notes, readme multilingual versions, and rules
- `ai_tools/`, `api/`, `caller/`, `const/`, `dao/`, `dataset/`, `func/`, `instance/`, `process/`, `prompts/`, `routes/`, `schedule/`, `utils/`: Support module directories, currently empty Python packages


