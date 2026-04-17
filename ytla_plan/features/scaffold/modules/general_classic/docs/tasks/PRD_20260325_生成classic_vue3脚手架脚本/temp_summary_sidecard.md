# SideCard 脚手架空模板文件小结

## 1. 概述
本小结基于对 `d:\YTLA\ytla_plan_vue\src\core\classic\cards\sideCard`（基础/父组件）和 `d:\YTLA\ytla_plan_vue\src\features\sample\cards\sample1`（具体功能实现）和 `d:\YTLA\ytla_plan_vue\src\features\sample\cards\_type`（类型共享目录）的分析，总结了SideCard类型模组应包含的脚手架空模板文件种类及规范。

**重要说明**：
- `sideCard` 是作为基础/父组件存在的，位于 `core/classic/cards/sideCard`
- 具体功能实现（如 `sample1`）位于 `features/[module_type]/cards/[sub_type]`
- 类型共享目录 `_type` 位于 `features/[module_type]/cards/_type`，包含共享的类型定义和注册表
- docs 文件不用生成，scaffold 目录已有相关生成方法
- **Vue 组件脚本规范**：script 部分只保留 prop 和 emit 的代码，其他函数通过 composables 获取（即只写 import）

## 2. SideCard 类型模组的结构

### 2.1 完整目录结构（包含 _type 和具体功能实现）
```
[module_type]/
└── cards/
    ├── _type/                    # 类型共享目录
    │   ├── avatar/               # 组件图标
    │   │   └── Avatar.vue
    │   ├── components/         # 组件（如需要）
    │   ├── definitions/        # 类型定义
    │   │   ├── cardDataType.ts
    │   │   └── cardType.ts
    │   ├── flows/              # 流程管理器（如需要）
    │   ├── locales/            # 国际化
    │   │   ├── en.json
    │   │   └── zh.json
    │   └── registries/         # 注册表
    │       ├── cardRegistry.ts
    │       └── registries.ts
    │
    └── [sub_type]/              # 具体功能实现（如 sample1）
        ├── avatar/               # 组件图标
        │   └── Avatar.vue
        ├── components/         # 主组件
        │   └── [ModuleName]Card.vue
        ├── composables/        # 组合式函数
        │   └── use[ModuleName].ts
        ├── definitions/       # 类型定义
        │   ├── [ModuleName]Type.ts
        │   └── cardDataType.ts
        ├── flows/             # 流程管理器（如需要）
        │   └── [ModuleName]FlowManager.ts
        ├── locales/           # 国际化
        │   ├── en.json
        │   └── zh.json
        ├── registries/        # 模块注册表
        │   └── registry.ts
        ├── services/          # API服务（如需要）
        │   └── [ModuleName]Service.ts
        ├── stores/           # 状态管理（如需要）
        │   └── [ModuleName]Store.ts
        ├── styles/           # 样式文件
        │   └── [module-name].scss
        └── readme.md
```

### 2.2 _type 目录文件类型明细

| 序号 | 目录 | 文件名 | 说明 |
|------|------|--------|------|
| 1 | avatar/ | Avatar.vue | 组件图标 |
| 2 | definitions/ | cardType.ts | 卡片类型定义 |
| 3 | definitions/ | cardDataType.ts | 卡片数据类型定义 |
| 4 | locales/ | en.json | 英文国际化 |
| 5 | locales/ | zh.json | 中文国际化 |
| 6 | registries/ | cardRegistry.ts | 卡片注册表 |
| 7 | registries/ | registries.ts | 注册表汇总 |

### 2.3 具体功能实现（[sub_type]）文件类型明细

| 序号 | 目录 | 文件名 | 说明 |
|------|------|--------|------|
| 1 | avatar/ | Avatar.vue | 组件图标 |
| 2 | components/ | [ModuleName]Card.vue | 主组件（使用 SideCard 基础组件） |
| 3 | composables/ | use[ModuleName].ts | 主composable |
| 4 | definitions/ | [ModuleName]Type.ts | 类型定义 |
| 5 | definitions/ | cardDataType.ts | 卡片数据类型 |
| 6 | flows/ | [ModuleName]FlowManager.ts | 流程管理器（可选） |
| 7 | locales/ | en.json | 英文国际化 |
| 8 | locales/ | zh.json | 中文国际化 |
| 9 | registries/ | registry.ts | 模块注册表 |
| 10 | services/ | [ModuleName]Service.ts | API服务（可选） |
| 11 | stores/ | [ModuleName]Store.ts | 状态管理（可选） |
| 12 | styles/ | [module-name].scss | 样式文件 |
| 13 | - | readme.md | 模块说明 |

## 3. 可以生成的模组规范空代码

### 3.1 _type 目录 - cardType.ts 模板
```typescript
export type [ModuleType]CardType = '[module_type]';

export type [ModuleType]CardSubType = '[sub_type1]' | '[sub_type2]';
```

### 3.2 _type 目录 - cardDataType.ts 模板
```typescript
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'
import type { [ModuleType]CardType, [ModuleType]CardSubType } from './cardType.ts'

export interface [ModuleType]CardData extends CardData {
  card_id: number;
  name: string;
  tags: string;
  description: string;
  card_type: [ModuleType]CardType;
  card_sub_type: [ModuleType]CardSubType;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
}
```

### 3.3 _type 目录 - cardRegistry.ts 模板
```typescript
import type { sideCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import { buildCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistryHelper.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'

const registryModules = import.meta.glob('@/features/[module_type]/cards/**/registries/registry.ts', { eager: true })

export const [moduleType]CardConfig = buildCardRegistry(SideCard, registryModules) as sideCardRegistry
```

### 3.4 具体功能实现 - 主组件模板 ([ModuleName]Card.vue)
**重要规范**：script 部分只保留 prop 和 emit 的代码，其他函数通过 composables 获取
```vue
<template>
  <SideCard
    :card-id="cardId"
    :name="name"
    :icon="iconPath"
    :background="background"
    :tags="tags"
    :description="description"
    :show-icon="true"
    :show-title="true"
    :show-tags="true"
    :showSettings="true"
    :showDeactivate="true"
    :showClose="true"
    @settings="handleEdit"
  >

    <template #top-left-actions></template>
    <template #top-actions></template>

    <template #card-content>

    </template>

    <template #left-actions-buttons>

    </template>

    <template #right-actions></template>

    <template #secondary-content>

    </template>

  </SideCard>
</template>

<script setup lang="ts">
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'
import { use[ModuleName] } from '@/features/[module_type]/cards/[module_name]/composables/use[ModuleName].ts'
import type { [ModuleName]CardData } from '@/features/[module_type]/cards/[module_name]/definitions/cardDataType.ts'

const props = defineProps({
  cardId: Number,
  name: String,
  tags: String,
  description: String,
  iconPath: String,
  background: String,
})

const emit = defineEmits<{

}>()

const { handleEdit } = use[ModuleName](props, emit)
</script>

<style scoped lang="scss">

</style>
```

### 3.5 TypeScript composable 模板 (.ts)
```typescript
import { useSideCardEditor } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditor.ts'
import type { [ModuleName]CardData } from '../definitions/cardDataType.ts'

export const use[ModuleName] = (props, emit) => {
  const handleEdit = () => {
    const { showEdit } = useSideCardEditor()
    showEdit({
      card_id: props.cardId,
      name: props.name,
      tags: props.tags,
      description: props.description,
      card_sub_type: '[module_name]',
    } as [ModuleName]CardData)
  }

  return {
    handleEdit
  }
}
```

### 3.6 主 composable 模板
```typescript
export const use[ModuleName] = (props, emit) => {

  return {

  }
}
```

### 3.7 TypeScript 类型定义模板 (cardDataType.ts)
```typescript
export interface [ModuleName]CardData {
  card_id: number
  name: string
  tags: string
  description: string
  card_sub_type: string
}
```

### 3.8 注册表模板 (registry.ts)
```typescript
import [ModuleName]Card from '../components/[ModuleName]Card.vue'
import type { [ModuleName]CardData } from '../definitions/cardDataType.ts'

export default {
  subType: '[module_name]',
  component: [ModuleName]Card,
  getSubTypeProps: (card: any) => {
    const [moduleName]Card = card as [ModuleName]CardData
    return {}
  }
}
```

### 3.9 JSON 国际化模板
```json
{
  "[module_name]_subtype_name": "[module_name](按语种填写)",
  "[module_name]_subtype_description": "(这里填入你的定义)"
}
```
