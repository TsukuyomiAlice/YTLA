<p>
  language
 <a href="../zh-CN/readme.md"> 简体中文 </a>
 <a href="../en-US/readme.md"> English </a>
</p>


# classic - sideCard

### YTLA Application Feature

### Official

version 1.0

Frontend Language and Framework: Vue3, typescript, Vite  
Applicable YTLA core version: **classic**  
File Update Date: 2026-03-20

## Concepts

SideCard is the core module for side card rendering and interaction, developed based on Vue3+TypeScript+Vite technology stack. This module supports dynamic registration, self-contained subtypes, and provides rich interactive features such as card expand/collapse, pin, edit, background change, etc.

## Feature Package Directory

- avatar/
  - Avatar.vue
- components/
  - SideCard.vue
- composables/
  - useBarDescription.ts
  - useBarTitle.ts
  - useButtonChangeBackground.ts
  - useButtonChangeIcon.ts
  - useButtonClose.ts
  - useButtonDeactivate.ts
  - useButtonEdit.ts
  - useButtonExpand.ts
  - useButtonPin.ts
  - useContainerIcon.ts
  - useContainerSideCard.ts
  - useContainerTags.ts
  - useSideCard.ts
  - useSideCardUpload.ts
- definitions/
  - cardDataType.ts
  - cardType.ts
  - sideCardType.ts
- documents/
  - readme/
    - zh-CN/
      - readme.md
    - en-US/
      - readme.md
  - tech/
    - tech.md
  - tasks/
    - PRD_20260320_readme_维护sideCard模块readme文档/
- factories/
  - cardRegistry.ts
  - cardRegistryHelper.ts
  - cardRegistryLoader.ts
- layouts/
  - ContainerSideCard.vue
- locales/
  - en.json
  - zh.json
- services/
  - cardService.ts
- stores/
  - cardStore.ts
- styles/
  - button-expand.scss
  - button-pin.scss
  - column-component.scss
  - container-side-card.scss
  - container-tags.scss
  - side-card-transition.scss
  - side-card.scss
  - ui-button.scss
  - ui-icon.scss
  - ui-text.scss
- ui/
  - BarDescription.vue
  - BarTitle.vue
  - ButtonChangeBackground.vue
  - ButtonChangeIcon.vue
  - ButtonClose.vue
  - ButtonDeactivate.vue
  - ButtonEdit.vue
  - ButtonExpand.vue
  - ButtonPin.vue
  - ContainerIcon.vue
  - ContainerTags.vue
- readme.md

## Changelog

### 2026-03-20

- Updated feature package directory to ensure all files are included
- Updated file update date to 2026-03-20
- Added changelog
- Listed PRD folder under documents/tasks/, excluding the md files inside are not listed
