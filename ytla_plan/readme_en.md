# ytla_plan

### YTLA Backend Project

### Official

version: 1.0

Backend Language and Framework: Python-Flask  
File Update Date: 2026-2-10

## Open Code, Free Addition

The project is completely open source, including all code in core is publicly available in source code form.  
Therefore, you can customize it according to your needs.  
Before doing so, please read this document to ensure you have a sufficient understanding of the project's framework.

## Core Concepts

As a complete, front-end and back-end separated project with Web OS vision, YTLA has two sets of concepts at the code
level.

### Core and Feature

**Core** serves as the underlying code that drives the project's operation, similar to an operating system  
**Feature** serves as functional modules that provide user applications, i.e., application software

### Card, Module and Plan

**Card** provides users with quick, simple functions  
**Module** provides users with application-level services  
**Plan** allows users to freely add Modules to create their own exclusive workbench

## Python-Flask Architecture Hierarchy

- project
    - core
        - Core Version Name
            - cards - Core Component
                - _type (Default Definition)
                - Refined Component
                    - Component Package
            - modules - Core Component
                - _type (Default Definition)
                - Refined Component
                    - Component Package
            - plans - Core Component
                - _type (Default Definition)
                - Refined Component
                    - Component Package
            - frame - Core Component
                - _type (Default Definition)
                - Refined Component
                    - Component Package
            - users - Core Component
                - _type (Default Definition)
                - Refined Component
                    - Component Package
    - feature
        - Feature Name
            - cards
                - _type (Default Definition)
                - Component
                    - Component Package
            - modules
                - _type (Default Definition)
                - Component
                    - Component Package

### Backend Single Component Package Structure

The project is classified according to component functions, each component contains multiple packages, and each package
is responsible for different functions.  
If you initialize with scaffold(/features/scaffold/modules/backend_python), you will get all the following packages:

### Documentation Management

| Package Name | File Function                    | File Type         | Description              |
|--------------|----------------------------------|-------------------|--------------------------|
| docs         | Component Configuration Document | .yaml, .json, .py | For automatic generation |

### Data Instance

| Package Name | File Function | File Type | Description                  |
|--------------|---------------|-----------|------------------------------|
| instance     | Instance      | .py       | Component data instance type |

### Data

| Package Name | File Function | File Type        | Description               |
|--------------|---------------|------------------|---------------------------|
| dataset      | Dataset       | .py, .json, etc. | Pre-made dataset          |
| dao          | DB Access     | .py              | python sqlite3 SQLAlchemy |

### Logic Processing

| Package Name | File Function               | File Type | Description                                               |
|--------------|-----------------------------|-----------|-----------------------------------------------------------|
| process      | Logic Processing Flow       | .py       | Component logic processing                                |
| schedule     | Regular Automatic Execution | .py       | Regular automated operation                               |
| script       | Calling Script              | .py       | Assemble and call methods or functions within the package |

### Interoperability

| Package Name | File Function                              | File Type | Description                                                         |
|--------------|--------------------------------------------|-----------|---------------------------------------------------------------------|
| const        | Constants                                  | .py       | Specific constants                                                  |
| api          | External API Call                          | .py       | Send API requests and process API reception results                 |
| ai_tools     | AI Assistant Tools                         | .py       | Specific function code snippets that need to be processed by gen AI |
| caller       | Cross-package Function Call Unified Method | .py       | Cross-package call function                                         |
| func         | Functional Functions                       | .py       | General functions                                                   |

### Frontend Communication

| Package Name | File Function | File Type | Description                 |
|--------------|---------------|-----------|-----------------------------|
| routes       | API Routes    | .py       | python-flask Blueprint file |

### Configuration

| Package Name | File Function            | File Type        | Description                      |
|--------------|--------------------------|------------------|----------------------------------|
| utils        | Configuration Parameters | .py, .json, etc. | Runtime configuration parameters |