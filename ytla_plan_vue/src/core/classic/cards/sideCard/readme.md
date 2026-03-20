<p>
  语言
 <a href="./documents/readme/zh-CN/readme.md"> 简体中文 </a>
 <a href="./documents/readme/en-US/readme.md"> English </a>
</p>


# classic - sideCard

### YTLA特性

### Official

version 1.0

前端语言及开发框架: Vue3, typescript, Vite  
适用YTLA core版本: **classic**  
文件更新日期: 2026-03-19

## 概念

SideCard 是侧边卡片渲染和交互核心模块，基于 Vue3+TypeScript+Vite 技术栈开发。该模块支持动态注册、子类型自包含等特性，提供了丰富的交互功能如卡片展开/收起、固定、编辑、背景切换等。

## 特性包目录

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

