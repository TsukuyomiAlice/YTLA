# YTLA Frontend Development Guide

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
| **Frontend** | Vue 3 |
| **State Management** | Pinia |
| **Routing** | Vue Router |
| **Styling** | SCSS |
| **HTTP Client** | Axios |
| **Animation** | GSAP, VueUse Motion |
| **Charts** | ECharts |
| **3D** | Three.js |

## Vue3 Architecture Hierarchy

| Layer | 0 | 1 | 2 | 3 | 4 |
|-------|----------|-------|--------------|------------|-------|
| | core | Core Version Name | Core Component-cards | Component+Version1 | Component Files |
| | | | | Component+Version2 | Component Files |
| | | | | ... | |
| | | | Core Component-modules | Component+Version1 | Component Files |
| | | | | Component+Version2 | Component Files |
| | | | | ... | |
| | features | Feature Name | cards | _type Default Type | |
| | | | | Corresponding Card Component Type1 | Component Files |
| | | | | Corresponding Card Component Type2 | Component Files |
| | | | modules | _type Default Type | |
| | | | | Corresponding Sub-module Component1 | Component Files |
| | | | | Corresponding Sub-module Component2 | Component Files |

## Frontend Single Component File Structure

| Folder Name | File Function | File Type | Description |
|-------------|---------------|-----------|-------------|
| documents | Documentation | json, bk(vue,ts,etc…) | Component documentation |
| definitions | Types (ts type / interface) | .ts | Object types for card and module functions |
| components | Components | .vue | As card and module carriers |
| layouts | Layouts | .vue | As component layout blocks |
| ui | UI | .vue | Components displayed on the page |
| composables | Composables | .ts | Vue-recommended functions for controlling components |
| styles | Styles | .scss | Component display styles |
| locales | Locales | .json | Multi-language corresponding files |
| stores | Stores (data) | .ts | Data format temporarily stored in browser memory |
| services | Services (api) | .ts | Backend communication |
| factories | Factories | .ts | Mainly used for core function control (factory pattern) |
| registries | Registries | .ts | Module and card registration loading mechanism |
| flows | Flows | .ts | Card setting flow, module display page switching |
| utils | Configuration | .ts, .json, .config | Parameters, constant parameters, etc. |
| avatar | Component Icons | .vue, .png | Card and module logos |

## Configuration Expanded with Vue Files

### Examples

#### UI File Configuration

- ../uis/UiFile.vue
    - ../composables/useUiFile.ts
    - ../styles/ui-file.scss

#### Layout File Configuration

- ../layouts/ContainerUiFile.vue
    - ../composables/ContainerUiFile.ts
    - ../styles/container-ui-file.scss

#### Component File Configuration

- ../componets/ComponentFile.vue
    - ../layouts/LayoutComponentFIle.vue
    - ../uis/UiFile.vue
    - ../composables/useComponentFile.ts
    - ../styles/component-file.scss
    - ../definitions/componentType.ts

## Compound Naming Rules

Element type name + element name + element function name, each part capitalized

### Type Names

#### layouts

- Container: Container
- Area: Area
- Column: Column

#### uis

- Container: Container
- Bar: Bar, Row
- Button: Button

### Example

- AreaSideCardMain
    - Area: Element type, area
    - SideCard: Element name (appears in component)
    - Main: Element function

## Design Considerations for Cards/Modules

- Necessity
- Optionality
- Regionality

## Development Rules

1. Frontend
   1. Component development follows Vue 3 Composition API specifications
   2. Use TypeScript to ensure type safety
   3. Component styles use SCSS preprocessor
   4. State management uses Pinia
   5. Routing management uses Vue Router

## Quick Start

```bash
# Clone the project
git clone https://github.com/TsukuyomiAlice/YTLA

# Install frontend dependencies
cd ytla_plan_vue
npm install

# Start development environment
npm run dev

# Type-check, compile and minify for production
npm run build

# Lint with ESLint
npm run lint
```

## Current Progress

- Basic framework setup completed
- Module/Card container system implemented
- Cross-module data communication supported
- Built-in system modules:
  - Plan Manager
  - Plan Dashboard
  - Module Selector
  - Internationalization support (vue-i18n)

## Next Steps

- Account and permission management system
- Multi-user collaboration features
- Developer scaffolding tools
- AI capability integration
- Community documentation improvement