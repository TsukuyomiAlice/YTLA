# SideCard 和 Module 结构分析报告

## 1. SideCard 结构分析

### 1.1 目录结构
基于 `d:\YTLA\ytla_plan_vue\src\core\classic\cards\sideCard` 的分析：

```
sideCard/
├── avatar/              # 组件图标
│   └── Avatar.vue
├── components/          # 主组件
│   └── SideCard.vue
├── composables/         # 组合式函数
│   ├── useBarDescription.ts
│   ├── useBarTitle.ts
│   ├── useButtonChangeBackground.ts
│   ├── useButtonChangeIcon.ts
│   ├── useButtonClose.ts
│   ├── useButtonDeactivate.ts
│   ├── useButtonEdit.ts
│   ├── useButtonExpand.ts
│   ├── useButtonPin.ts
│   ├── useContainerIcon.ts
│   ├── useContainerSideCard.ts
│   ├── useContainerTags.ts
│   ├── useSideCard.ts
│   └── useSideCardUpload.ts
├── definitions/         # 类型定义
│   ├── cardDataType.ts
│   ├── cardType.ts
│   └── sideCardType.ts
├── documents/           # 文档
│   ├── design/
│   │   └── archi_analyze_20260323.md
│   ├── readme/
│   │   ├── en-US/
│   │   │   └── readme.md
│   │   └── zh-CN/
│   │       └── readme.md
│   ├── tasks/
│   │   └── PRD_20260323_design_分析sideCard设计/
│   └── tech/
│       └── tech.md
├── factories/           # 工厂模式
│   ├── cardRegistry.ts
│   ├── cardRegistryHelper.ts
│   └── cardRegistryLoader.ts
├── layouts/             # 布局组件
│   └── ContainerSideCard.vue
├── locales/             # 国际化
│   ├── en.json
│   └── zh.json
├── services/            # API服务
│   └── cardService.ts
├── stores/              # 状态管理
│   └── cardStore.ts
├── styles/              # 样式文件
│   ├── button-expand.scss
│   ├── button-pin.scss
│   ├── column-component.scss
│   ├── container-side-card.scss
│   ├── container-tags.scss
│   ├── side-card-transition.scss
│   ├── side-card.scss
│   ├── ui-button.scss
│   ├── ui-icon.scss
│   └── ui-text.scss
├── ui/                  # UI组件
│   ├── BarDescription.vue
│   ├── BarTitle.vue
│   ├── ButtonChangeBackground.vue
│   ├── ButtonChangeIcon.vue
│   ├── ButtonClose.vue
│   ├── ButtonDeactivate.vue
│   ├── ButtonEdit.vue
│   ├── ButtonExpand.vue
│   ├── ButtonPin.vue
│   ├── ContainerIcon.vue
│   └── ContainerTags.vue
└── readme.md
```

### 1.2 SideCard 关键文件分析

#### 1.2.1 主组件 SideCard.vue
- 使用 `<script setup>` 语法
- 导入多个UI组件和composables
- 使用withDefaults设置props默认值
- 定义emits
- 通过useSideCard聚合所有功能

#### 1.2.2 组合式函数 useSideCard.ts
- 作为主逻辑聚合器
- 调用多个专用composables
- 统一导出所有功能

#### 1.2.3 类型定义
- sideCardType.ts: 定义SideCardProps和SideCardEmits
- cardType.ts: 卡片类型定义
- cardDataType.ts: 卡片数据类型定义

---

## 2. Module 结构分析

### 2.1 目录结构
基于 `d:\YTLA\ytla_plan_vue\src\features\basic\modules\definition` 的分析：

```
definition/
├── avatar/              # 组件图标
│   └── Avatar.vue
├── components/          # 组件
│   ├── DefinitionMain.vue
│   ├── DefinitionMain_00.vue
│   ├── DefinitionSub.vue
│   └── DefinitionSub_00.vue
├── flows/               # 流程管理器
│   └── definitionFlowManager.ts
├── locales/             # 国际化
│   ├── en.json
│   └── zh.json
└── registries/          # 模块注册表
    └── definitionModuleConfig.ts
```

### 2.2 Module 关键文件分析

#### 2.2.1 组件文件
- DefinitionMain.vue: 主组件入口，引用DefinitionMain_00.vue
- DefinitionMain_00.vue: 主流程步骤组件
- DefinitionSub.vue: 子组件入口
- DefinitionSub_00.vue: 子流程步骤组件

#### 2.2.2 流程管理器 definitionFlowManager.ts
- 实现ModuleFlowManager接口
- 注册main-steps和sub-steps两个流程
- 使用defineAsyncComponent异步加载组件

---

## 3. 对比分析

| 特性 | SideCard | Module |
|------|----------|--------|
| 主组件位置 | components/ | components/ |
| 流程管理 | 无 | flows/ |
| 注册表 | factories/ | registries/ |
| 组合式函数 | composables/ (多个) | 无 |
| UI组件 | ui/ (多个) | 无 |
| 布局 | layouts/ | 无 |
| 状态管理 | stores/ | 无 |
| 服务层 | services/ | 无 |
| 类型定义 | definitions/ | 无 |
| 文档 | documents/ (完整) | 无 |

---

## 4. 脚手架空模板文件种类总结

### 4.1 SideCard 脚手架空模板

应该包含的文件种类：
1. avatar/ Avatar.vue - 图标组件
2. components/ [ModuleName].vue - 主组件
3. composables/ use[ModuleName].ts - 主composable
4. composables/ use[功能].ts - 功能composables (多个)
5. definitions/ [ModuleName]Type.ts - 类型定义
6. definitions/ cardType.ts - 卡片类型
7. definitions/ cardDataType.ts - 卡片数据类型
8. documents/ design/, readme/, tasks/, tech/ - 文档目录
9. factories/ cardRegistry.ts - 注册表
10. factories/ cardRegistryHelper.ts - 注册表助手
11. factories/ cardRegistryLoader.ts - 注册表加载器
12. layouts/ Container[ModuleName].vue - 布局组件
13. locales/ en.json, zh.json - 国际化
14. services/ [ModuleName]Service.ts - API服务
15. stores/ [ModuleName]Store.ts - 状态管理
16. styles/ 多个.scss文件 - 样式
17. ui/ 多个UI组件.vue - UI组件
18. readme.md - 模块说明

### 4.2 Module 脚手架空模板

应该包含的文件种类：
1. avatar/ Avatar.vue - 图标组件
2. components/ [ModuleName]Main.vue - 主组件入口
3. components/ [ModuleName]Main_00.vue - 主流程步骤组件
4. components/ [ModuleName]Sub.vue - 子组件入口
5. components/ [ModuleName]Sub_00.vue - 子流程步骤组件
6. flows/ [ModuleName]FlowManager.ts - 流程管理器
7. locales/ en.json, zh.json - 国际化
8. registries/ [ModuleName]ModuleConfig.ts - 模块注册表

---

## 5. 规范空代码示例

### 5.1 SideCard 主组件模板
```vue
<template>
  
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
```

### 5.2 Module 主组件模板
```vue
<template>
  <[ModuleName]Main_00 />
</template>

<script setup lang="ts">
import [ModuleName]Main_00 from '@/features/[module_type]/components/modules/[module_sub_type]/[ModuleName]Main_00.vue'
</script>

<style scoped lang="scss">

</style>
```

### 5.3 Flow Manager 模板
```typescript
import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class [ModuleName]ModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const [moduleName]ModuleFlowManager = new [ModuleName]ModuleFlowManager()

[moduleName]ModuleFlowManager.registerFlow('[moduleName]-main-steps', [
  defineAsyncComponent(() => import('@/features/[module_type]/components/modules/[module_sub_type]/[ModuleName]Main_00.vue')),
])

[moduleName]ModuleFlowManager.registerFlow('[moduleName]-sub-steps', [
  defineAsyncComponent(() => import('@/features/[module_type]/components/modules/[module_sub_type]/[ModuleName]Sub_00.vue')),
])
```
