# Module 脚手架空模板文件小结

## 1. 概述
本小结基于对 `d:\YTLA\ytla_plan_vue\src\features\basic\modules\definition`（具体功能实现）和 `d:\YTLA\ytla_plan_vue\src\features\basic\modules\_type`（类型共享目录）的分析，总结了Module类型模组应包含的脚手架空模板文件种类及规范。

**重要说明**：
- 具体功能实现（如 `definition`）位于 `features/[module_type]/modules/[sub_type]`
- 类型共享目录 `_type` 位于 `features/[module_type]/modules/_type`，包含共享的类型定义和注册表
- docs 文件不用生成，scaffold 目录已有相关生成方法

## 2. Module 类型模组的结构

### 2.1 完整目录结构（包含 _type 和具体功能实现）
```
[module_type]/
└── modules/
    ├── _type/                    # 类型共享目录
    │   ├── avatar/               # 组件图标
    │   │   └── Avatar.vue
    │   ├── locales/            # 国际化
    │   │   ├── en.json
    │   │   └── zh.json
    │   └── registries/         # 注册表
    │       └── registries.ts
    │
    └── [sub_type]/              # 具体功能实现（如 definition）
        ├── avatar/               # 组件图标
        │   └── Avatar.vue
        ├── components/         # 组件
        │   ├── [ModuleName]Main.vue
        │   ├── [ModuleName]Main_00.vue
        │   ├── [ModuleName]Sub.vue
        │   └── [ModuleName]Sub_00.vue
        ├── flows/             # 流程管理器
        │   └── [ModuleName]FlowManager.ts
        ├── locales/           # 国际化
        │   ├── en.json
        │   └── zh.json
        └── registries/        # 模块注册表
            └── [ModuleName]ModuleConfig.ts
```

### 2.2 _type 目录文件类型明细

| 序号 | 目录 | 文件名 | 说明 |
|------|------|--------|------|
| 1 | avatar/ | Avatar.vue | 组件图标 |
| 2 | locales/ | en.json | 英文国际化 |
| 3 | locales/ | zh.json | 中文国际化 |
| 4 | registries/ | registries.ts | 注册表汇总 |

### 2.3 具体功能实现（[sub_type]）文件类型明细

| 序号 | 目录 | 文件名 | 说明 |
|------|------|--------|------|
| 1 | avatar/ | Avatar.vue | 组件图标 |
| 2 | components/ | [ModuleName]Main.vue | 主组件入口 |
| 3 | components/ | [ModuleName]Main_00.vue | 主流程步骤组件 |
| 4 | components/ | [ModuleName]Sub.vue | 子组件入口 |
| 5 | components/ | [ModuleName]Sub_00.vue | 子流程步骤组件 |
| 6 | flows/ | [ModuleName]FlowManager.ts | 流程管理器 |
| 7 | locales/ | en.json | 英文国际化 |
| 8 | locales/ | zh.json | 中文国际化 |
| 9 | registries/ | [ModuleName]ModuleConfig.ts | 模块注册表 |

## 3. 可以生成的模组规范空代码

### 3.1 Main 组件模板
```vue
<template>
  <[ModuleName]Main_00 />
</template>

<script setup lang="ts">
import [ModuleName]Main_00 from '@/features/[module_type]/modules/[module_sub_type]/components/[ModuleName]Main_00.vue'
</script>

<style scoped lang="scss">

</style>
```

### 3.2 Main_00 组件模板
```vue
<template>
  
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
```

### 3.3 Sub 组件模板
```vue
<template>
  <[ModuleName]Sub_00 />
</template>

<script setup lang="ts">
import [ModuleName]Sub_00 from '@/features/[module_type]/modules/[module_sub_type]/components/[ModuleName]Sub_00.vue'
</script>

<style scoped lang="scss">

</style>
```

### 3.4 Sub_00 组件模板
```vue
<template>
  
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
```

### 3.5 Flow Manager 模板
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
  defineAsyncComponent(() => import('@/features/[module_type]/modules/[module_sub_type]/components/[ModuleName]Main_00.vue')),
])

[moduleName]ModuleFlowManager.registerFlow('[moduleName]-sub-steps', [
  defineAsyncComponent(() => import('@/features/[module_type]/modules/[module_sub_type]/components/[ModuleName]Sub_00.vue')),
])
```

### 3.6 Module Config 模板
```typescript
import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/registries/moduleRegistry.ts'
import { [moduleName]ModuleFlowManager } from '@/features/[module_type]/flows/[moduleName]FlowManager'

export const [moduleName]ModuleConfig = <ModuleRegistry> {
  moduleType: '[module_type]',
  moduleSubType: '[module_sub_type]',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/[module_type]/modules/[module_sub_type]/components/[ModuleName]Main.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/[module_type]/modules/[module_sub_type]/components/[ModuleName]Sub.vue')
  ),
  displayMode: 7,
  flowManager: [moduleName]ModuleFlowManager
}
```

### 3.7 JSON 国际化模板
```json
{
  "[module_name]_subtype_name": "[module_name](按语种填写)",
  "[module_name]_subtype_description": "(这里填入你的定义)"
}
```

### 3.8 Avatar 组件模板
```vue
<template>
  
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">

</style>
```
