<p>
 语言
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>

# feature_maker - frontend_vue3

### YTLA特性

### Official

version 1.0

后端语言及开发框架: Python-Flask  
适用YTLA core版本: **classic**  
文件更新日期: 2026-03-09

## 概念

frontend_vue3 模块是一个 Vue3 前端导入分析工具，用于扫描 Vue 和 TypeScript 文件，检测架构边界违规（如 core 模块导入
features 模块），并生成 JSON 报告。该模块是 feature_maker 的一部分，用于确保前端代码的架构合规性。

## 特性包目录

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

**主要目录说明：**

- `script/`: 包含主分析脚本 `scriptImportAnalyzer.py`
- `docs/`: 文档目录，包含实现说明、readme 多语言版本和规则
- `ai_tools/`, `api/`, `caller/`, `const/`, `dao/`, `dataset/`, `func/`, `instance/`, `process/`, `prompts/`, `routes/`,
  `schedule/`, `utils/`: 支持模块目录，目前为空的 Python 包

