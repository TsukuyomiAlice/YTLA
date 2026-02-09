# YTLA Backend Development Guide

## Project Introduction

YTLA (Your T&L Assistant) is a modular web application platform framework that allows users to quickly build personalized workflows by freely generating and combining Modules and Cards.

## Core Concepts

- **T&L Customization**
  "T" and "L" represent user-defined terms (such as Tech & Learning, Task & Logistics, etc.), giving the platform flexible application scenarios.
- **Modular Architecture**
  Split functions into reusable Modules (complete applications) and Cards (lightweight widgets) that support on-demand combination.
- **Plan-driven**
  Users can create multiple Plans, each containing a set of Modules/Cards, to implement exclusive workbenches for different scenarios.

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python (Flask framework) |
| **Data Layer** | Module-independent storage + cross-module communication |

## Python-Flask Architecture Hierarchy

| Layer | 0 | 1 | 2 | 3 | 4 |
|-------|-----|-----|--------------|------------|------------|
| | core | Core Version Name | Core Component-cards | _type Default Definition |  |
| | | | | Refined Component | Component Package |
| | | | Core Component-modules | _type Default Definition |  |
| | | | | Refined Component | Component Package |
| | | | Core Component-plans | _type Default Definition |  |
| | | | | Refined Component | Component Package |
| | | | Core Component-frame | _type Default Definition |  |
| | | | | Refined Component | Component Package |
| | | | Core Component-users | _type Default Definition |  |
| | | | | Refined Component | Component Package |
| | feature | Feature Name | cards | _type Default Definition |  |
| | | | | Component | Component Package |
| | | modules | _type Default Definition |  |  |
| | | | | Component | Component Package |

## Backend Single Component Package Structure

| Package Name | File Function | File Type | Description |
|-------------|---------------|-----------|-------------|
| docs | Component Configuration Document | .yaml, .json, .py | For automatic generation |
| instance | Instance | .py | Component data instance type |
| process | Logic Processing Flow | .py | Component logic processing |
| schedule | Regular Automatic Execution | .py | Regular automated operation |
| script | Calling Script | .py | Assemble and call methods or functions within the package |
| dataset | Dataset | .py, .json, etc. | Pre-made dataset |
| api | External API Call | .py | Send API requests and process API reception results |
| dao | DB Access | .py | python sqlite3 SQLAlchemy |
| routes | API Routes | .py | python-flask Blueprint file |
| const | Constants | .py | Specific constants |
| ai_tools | AI Assistant Tools | .py | Specific function code snippets that need to be processed by gen AI |
| caller | Cross-package Function Call Unified Method | .py | Cross-package call function |
| func | Functional Functions | .py | General functions |

## Development Rules

1. Backend
   1. Whether it is a module or a card, it starts from the dao layer, then the process layer, and finally the route layer
   2. For data that needs to be obtained from other projects, a function needs to be defined in the caller layer and then called in the route layer
   3. The backend code has been revised and divided into two concepts: core and features
      For each subdirectory within core and features, it contains the above directory structure
      For core, this helps to distinguish the division and decoupling of core functions, and can correspond to front-end code
      For features, this is aligned with front-end code

## Quick Start

```bash
# Clone the project
git clone https://github.com/TsukuyomiAlice/YTLA

# Install backend dependencies
cd ytla_plan
pip install -r requirements.txt

# Start development environment
flask run
```

## Current Progress

- Basic framework setup completed
- Module/Card container system implemented
- Cross-module data communication supported
- Built-in system modules:
  - Plan Manager
  - Plan Dashboard
  - Module Selector
  - Internationalization support

## Next Steps

- Account and permission management system
- Multi-user collaboration features
- Developer scaffolding tools
- AI capability integration
- Community documentation improvement