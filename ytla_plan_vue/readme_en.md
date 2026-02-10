# ytla_plan_vue

### YTLA Frontend Project

### Official

version: 1.0

Frontend Language and Framework: Vue3  
File Update Date: 2026-2-10

## Open Code, Free Addition

The project is completely open source, including all code in core is publicly available in source code form.  
Therefore, you can customize it according to your needs.  
Before doing so, please read this document to ensure you have a sufficient understanding of the project's framework.

## Concepts

As a complete, front-end and back-end separated project with Web OS vision, YTLA has two sets of concepts at the code
level.

### Core and Feature

**Core** serves as the underlying code that drives the project's operation, similar to an operating system  
**Feature** serves as functional modules that provide user applications, i.e., application software

### Card, Module and Plan

**Card** provides users with quick, simple functions  
**Module** provides users with application-level services  
**Plan** allows users to freely add Modules to create their own exclusive workbench

## Vue3 Architecture Hierarchy

- project
    - core
        - Core Version Name
            - cards - Core Component
                - Component+Version1
                    - Component Files
                - Component+Version2
                    - Component Files
            - modules - Core Component
                - Component+Version1
                    - Component Files
                - Component+Version2
                    - Component Files
            - plans - Core Component
                - Component+Version1
                    - Component Files
                - Component+Version2
                    - Component Files
            - frame - Core Component
                - Component+Version1
                    - Component Files
                - Component+Version2
                    - Component Files
            - users - Core Component
                - _type (Default Definition)
                - Refined Component
                    - Component Package
    - feature
        - Feature Name
            - cards
                - _type (Default Definition)
                - Corresponding Card Component Type1
                    - Component Files
                - Corresponding Card Component Type2
                    - Component Files
            - modules
                - _type (Default Definition)
                - Corresponding Card Component Type1
                    - Component Files
                - Corresponding Card Component Type2
                    - Component Files

### Frontend Single Component File Structure

The project is classified according to component functions, each component contains multiple packages, and each package
is responsible for different functions.  
If you initialize with scaffold(/features/scaffold/modules/frontend_vue3), you will get all the following packages:

### Documentation Management

| Folder Name | File Function | File Type             | Description             |
|-------------|---------------|-----------------------|-------------------------|
| documents   | Documentation | json, bk(vue,ts,etc…) | Component documentation |

### Data Instance

| Folder Name | File Function               | File Type | Description                                |
|-------------|-----------------------------|-----------|--------------------------------------------|
| definitions | Types (ts type / interface) | .ts       | Object types for card and module functions |

### Components

| Folder Name | File Function | File Type | Description                      |
|-------------|---------------|-----------|----------------------------------|
| components  | Components    | .vue      | As card and module carriers      |
| layouts     | Layouts       | .vue      | As component layout blocks       |
| ui          | UI            | .vue      | Components displayed on the page |
| styles      | Styles        | .scss     | Component display styles         |

#### Example: Layout File Configuration

- ../layouts/ContainerUiFile.vue
    - ../composables/ContainerUiFile.ts
    - ../styles/container-ui-file.scss

#### Example: Component File Configuration

- ../components/ComponentFile.vue
    - ../layouts/LayoutComponentFIle.vue
    - ../uis/UiFile.vue
    - ../composables/useComponentFile.ts
    - ../styles/component-file.scss
    - ../definitions/componentType.ts

#### Example: UI File Configuration

- ../uis/UiFile.vue
    - ../composables/useUiFile.ts
    - ../styles/ui-file.scss

#### Compound Naming Rules

Element type name + element name + element function name, each part capitalized

#### layouts

- Container: Container
- Area: Area
- Column: Column

#### uis

- Container: Container
- Bar: Bar, Row
- Button: Button

#### Example

- AreaSideCardMain
    - Area: Element type, area
    - SideCard: Element name (appears in component)
    - Main: Element function

### Data

| Folder Name | File Function | File Type | Description                                      |
|-------------|---------------|-----------|--------------------------------------------------|
| stores      | Stores (data) | .ts       | Data format temporarily stored in browser memory |

### Control Processing

| Folder Name | File Function | File Type | Description                                             |
|-------------|---------------|-----------|---------------------------------------------------------|
| composables | Composables   | .ts       | Vue-recommended functions for controlling components    |
| factories   | Factories     | .ts       | Mainly used for core function control (factory pattern) |
| registries  | Registries    | .ts       | Module and card registration loading mechanism          |
| flows       | Flows         | .ts       | Card setting flow, module display page switching        |

### Frontend Communication

| Folder Name | File Function  | File Type | Description           |
|-------------|----------------|-----------|-----------------------|
| services    | Services (api) | .ts       | Backend communication |

### Configuration

| Folder Name | File Function   | File Type           | Description                           |
|-------------|-----------------|---------------------|---------------------------------------|
| locales     | Locales         | .json               | Multi-language corresponding files    |
| utils       | Configuration   | .ts, .json, .config | Parameters, constant parameters, etc. |
| avatar      | Component Icons | .vue, .png          | Card and module logos                 |