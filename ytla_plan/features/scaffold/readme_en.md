# YTLA Scaffold Tool Documentation

## Project Introduction

YTLA (Your T&L Assistant) is a modular web application platform framework that allows users to quickly build personalized workflows by freely generating and combining Modules and Cards.

## Scaffold Tool Overview

The scaffold tool is an important component of the YTLA platform, used for generating basic frameworks and automated code, supporting rapid development and expansion.

## core_classic Series

### core Layer

- classic: Used as the runtime of the program framework, regarded as "hardware"
    - frame: Underlying framework
    - cards: Cards
    - modules: Modules
    - plans: Plans
    - users: Users

### feature Layer

- planManage: Used for main interface operation, regarded as "OS"
- aiConnector: Used for connecting AI services, dedicated application for ai_tools
- scaffold: Used for generating basic frameworks
- Other features: Used as functions

## scaffold Package Definition

Three different packages are defined under scaffold:

- frontend_xxx: Refers to the frontend using a certain language
- backend_xxx: Refers to the backend using a certain language
- general_xxx: Refers to the version name of the core component

## Scaffold Types

### 1. Frontend Scaffold (frontend_vue3)

Used for generating Vue 3 frontend project structure, including:
- Component templates
- Layout templates
- Style templates
- Internationalization support
- Routing configuration

### 2. Backend Scaffold (backend_python)

Used for generating Python-Flask backend project structure, including:
- API route templates
- Database access templates
- Business logic templates
- Scheduled task templates

### 3. Core Scaffold (core_classic)

Used for generating core framework structure, including:
- Basic component templates
- Module management templates
- Card management templates
- Plan management templates

## Scaffold Usage Guide

### 1. Generate Frontend Project

```bash
# Generate frontend Vue 3 project structure
python -m features.scaffold.modules.frontend_vue3.process.processGenerateStructure
```

### 2. Generate Backend Project

```bash
# Generate backend Python-Flask project structure
python -m features.scaffold.modules.backend_python.process.processGenerateStructure
```

### 3. Generate Core Framework

```bash
# Generate core framework structure
python -m features.scaffold.modules.core_classic.process.processGenerateStructure
```

## Scaffold Configuration

### 1. Frontend Configuration

- Support custom component types
- Support custom layout structures
- Support custom style themes

### 2. Backend Configuration

- Support custom API routes
- Support custom database structures
- Support custom business logic

### 3. Core Configuration

- Support custom module types
- Support custom card types
- Support custom plan structures

## Development Rules

1. Scaffold Development
   1. Follow modular design principles
   2. Ensure generated code conforms to project specifications
   3. Support configurable generation to improve flexibility
   4. Maintain consistency with the core framework

## Current Progress

- Basic scaffold framework setup completed
- Support for frontend Vue 3 project generation
- Support for backend Python-Flask project generation
- Support for core framework structure generation

## Next Steps

- Enhance scaffold configuration capabilities
- Support more frontend frameworks
- Support more backend frameworks
- Integrate AI generation capabilities
- Provide visual configuration interface