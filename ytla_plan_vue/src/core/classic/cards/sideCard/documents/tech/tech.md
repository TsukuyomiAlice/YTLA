# SideCard 前端模块技术文档

## 目录

- [1. 模块概述](#1-模块概述)
  - [1.1 模块定位](#11-模块定位)
  - [1.2 主要功能](#12-主要功能)
  - [1.3 设计目标](#13-设计目标)
  - [1.4 在 YTLA 系统中的位置](#14-在-ytla-系统中的位置)
  - [1.5 使用场景](#15-使用场景)
- [2. 文件结构说明](#2-文件结构说明)
  - [2.1 核心目录说明](#21-核心目录说明)
  - [2.2 关键文件说明](#22-关键文件说明)
  - [2.3 文件命名规范](#23-文件命名规范)
- [3. 核心组件说明](#3-核心组件说明)
  - [3.1 SideCard 主组件](#31-sidecard-主组件)
  - [3.2 注册机制](#32-注册机制)
  - [3.3 卡片数据模型](#33-卡片数据模型)
  - [3.4 CardService 服务层](#34-cardservice-服务层)
  - [3.5 组合式函数 (Composables)](#35-组合式函数-composables)
  - [3.6 组件关系图](#36-组件关系图)
- [4. 注册机制说明](#4-注册机制说明)
  - [4.1 注册架构概览](#41-注册架构概览)
  - [4.2 核心注册组件详解](#42-核心注册组件详解)
  - [4.3 子类型自包含设计](#43-子类型自包含设计)
  - [4.4 静态扫描机制](#44-静态扫描机制)
- [5. 数据处理流程说明](#5-数据处理流程说明)
  - [5.1 数据流程图](#51-数据流程图)
  - [5.2 数据流向详细说明](#52-数据流向详细说明)
  - [5.3 核心数据处理场景](#53-核心数据处理场景)
  - [5.4 数据模型说明](#54-数据模型说明)
  - [5.5 错误处理和异常流程](#55-错误处理和异常流程)
- [6. 配置和使用说明](#6-配置和使用说明)
  - [6.1 环境要求](#61-环境要求)
  - [6.2 依赖配置](#62-依赖配置)
  - [6.3 使用步骤](#63-使用步骤)
  - [6.4 常见问题排查](#64-常见问题排查)
- [7. 扩展和开发指南](#7-扩展和开发指南)
  - [7.1 扩展架构概览](#71-扩展架构概览)
  - [7.2 添加新卡片子类型的步骤](#72-添加新卡片子类型的步骤)
  - [7.3 扩展最佳实践](#73-扩展最佳实践)
  - [7.4 常见扩展场景](#74-常见扩展场景)
  - [7.5 故障排除](#75-故障排除)

## 1. 模块概述

SideCard 前端模块是 YTLA 中处理侧边卡片渲染和交互的核心模块。该模块采用 Vue 3 + TypeScript + Vite 技术栈，提供卡片的展示、编辑、交互等完整功能，支持多种卡片类型的动态扩展。

### 1.1 模块定位

SideCard 前端模块位于 YTLA 系统的核心 UI 层，作为卡片功能的前端基础设施，为上层业务组件提供统一的卡片展示和交互接口。模块采用组件化、组合式设计，将卡片展示、状态管理、数据交互、注册机制分离，确保系统的高内聚、低耦合。

### 1.2 主要功能

- **卡片渲染**: 支持多种卡片类型的统一渲染，提供默认卡片组件
- **动态注册机制**: 通过静态扫描自动发现和注册卡片子类型，支持零配置扩展
- **统一交互界面**: 提供卡片的编辑、关闭、固定、展开、图标/背景更换等通用功能
- **数据服务封装**: 封装卡片数据的 CRUD 操作，提供统一的 API 调用接口
- **状态管理**: 支持卡片的激活状态、删除状态、固定状态、展开状态等管理
- **国际化支持**: 内置多语言支持，便于国际化扩展

### 1.3 设计目标

- **可扩展性**: 通过约定优于配置的设计，无需修改核心代码即可添加新的卡片类型
- **可维护性**: 清晰的模块分层和职责分离，便于代码维护和调试
- **灵活性**: 支持多种卡片类型和子类型，适应不同的业务场景需求
- **类型安全**: 基于 TypeScript 提供完整的类型定义，减少运行时错误
- **向后兼容**: 保留对现有卡片类型的兼容性，平滑升级

### 1.4 在 YTLA 系统中的位置

SideCard 前端模块属于 YTLA 系统的核心 UI 功能模块之一，与后端 SideCard 模块通过 API 接口协同工作。模块为上层业务组件提供卡片展示和交互能力，同时与全局状态管理、路由等系统模块集成。

### 1.5 使用场景

- **个人任务管理**: 展示和管理个人任务卡片，支持任务编辑、状态更新等
- **笔记记录**: 展示笔记卡片，支持笔记内容编辑
- **提醒设置**: 展示提醒卡片，支持提醒时间设置
- **自定义卡片类型**: 开发者可以根据业务需求扩展新的卡片类型，如习惯追踪、日程安排等

## 2. 文件结构说明

SideCard 前端模块采用标准的 Vue 3 组件架构，主要目录和文件如下：

```
sideCard/
├── avatar/
│   └── Avatar.vue
├── components/
│   └── SideCard.vue
├── composables/
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
├── definitions/
│   ├── cardDataType.ts
│   ├── cardType.ts
│   └── sideCardType.ts
├── documents/
│   ├── readme/
│   │   ├── en-US/
│   │   │   └── readme.md
│   │   └── zh-CN/
│   │       └── readme.md
│   └── tech/
│       └── tech.md
├── factories/
│   ├── cardRegistry.ts
│   ├── cardRegistryHelper.ts
│   └── cardRegistryLoader.ts
├── layouts/
│   └── ContainerSideCard.vue
├── locales/
│   ├── en.json
│   └── zh.json
├── services/
│   └── cardService.ts
├── stores/
│   └── cardStore.ts
├── styles/
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
├── ui/
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

### 2.1 核心目录说明

- **components/**: 包含 SideCard 主组件，是卡片展示的核心入口
- **composables/**: 组合式函数目录，封装卡片的各种交互逻辑
- **definitions/**: 类型定义目录，包含卡片数据类型、卡片类型等核心类型
- **factories/**: 工厂模式目录，包含卡片注册、注册表构建等核心机制
- **layouts/**: 布局组件目录，包含卡片容器布局
- **services/**: 服务层目录，封装卡片数据的 API 调用
- **stores/**: 状态管理目录（预留）
- **styles/**: 样式文件目录，使用 SCSS 编写
- **ui/**: UI 组件目录，包含卡片的各种 UI 元素
- **locales/**: 国际化文件目录
- **documents/**: 文档目录，包含用户文档和技术文档

### 2.2 关键文件说明

1. **definitions/cardType.ts**: 定义卡片类型和子类型，简化为 string 类型，零维护
2. **definitions/cardDataType.ts**: 定义卡片数据接口 CardData，描述卡片的完整数据结构
3. **factories/cardRegistryHelper.ts**: 包含注册表构建辅助函数，如 extractBaseCardProps、buildCardRegistry
4. **factories/cardRegistry.ts**: 注册表存储和管理，提供创建、获取、清除注册表的功能
5. **factories/cardRegistryLoader.ts**: 注册表加载器，使用 import.meta.glob 静态扫描注册表文件
6. **components/SideCard.vue**: SideCard 主组件，提供卡片的完整展示和交互功能
7. **services/cardService.ts**: 卡片服务类，封装所有卡片相关的 API 调用
8. **composables/useSideCard.ts**: 主组合式函数，整合卡片的核心交互逻辑

### 2.3 文件命名规范

- 组件文件使用 PascalCase 命名，如 `SideCard.vue`
- 组合式函数使用 camelCase 命名，前缀为 `use`，如 `useSideCard.ts`
- 类型定义文件使用 camelCase 命名，后缀为 `Type`，如 `cardType.ts`
- 工厂文件使用 camelCase 命名，后缀为 `Registry` 或 `Helper`
- 服务文件使用 PascalCase 命名，后缀为 `Service`，如 `cardService.ts`
- 样式文件使用 kebab-case 命名，如 `side-card.scss`
- UI 组件使用 PascalCase 命名，前缀为 `Button`、`Bar`、`Container` 等

## 3. 核心组件说明

SideCard 前端模块包含以下核心组件，每个组件都有明确的职责和接口定义。

### 3.1 SideCard 主组件

**位置**: `components/SideCard.vue`

**职责**: SideCard 主组件是卡片展示和交互的核心入口，提供完整的卡片 UI 和交互功能。

**主要功能**:
- 卡片标题展示和编辑
- 卡片标签管理
- 卡片描述展示和编辑
- 卡片图标展示和更换
- 卡片背景更换
- 卡片固定/取消固定
- 卡片展开/收起
- 卡片编辑按钮
- 卡片停用按钮
- 卡片关闭按钮
- 拖拽支持

**Props**:
- `cardId`: 卡片 ID
- `cardType`: 卡片类型
- `icon`: 图标路径
- `background`: 背景路径
- `name`: 卡片名称
- `tags`: 卡片标签（逗号分隔）
- `description`: 卡片描述
- `spanColumns`: 跨列数
- `initialExpanded`: 初始展开状态
- 其他 UI 控制属性

**Emits**:
- `edit`: 编辑事件
- `close`: 关闭事件
- `deactivate`: 停用事件
- `pin`: 固定事件
- `titleChange`: 标题变更事件
- `descriptionChange`: 描述变更事件
- 其他交互事件

### 3.2 注册机制

注册机制是 SideCard 模块的核心扩展能力，由以下几个关键文件组成：

#### 3.2.1 cardRegistryHelper.ts

**位置**: `factories/cardRegistryHelper.ts`

**职责**: 提供注册表构建的辅助函数，包括基础属性提取、注册表构建等。

**核心接口**:
```typescript
export interface SubTypeRegistry {
  subType: string
  component: Component
  getSubTypeProps: (card: CardData) => Record<string, unknown>
}
```

**核心函数**:
- `extractBaseCardProps(card: CardData)`: 从卡片数据中提取基础属性
- `buildCardRegistry(defaultComponent, registryModules)`: 构建卡片注册表

#### 3.2.2 cardRegistry.ts

**位置**: `factories/cardRegistry.ts`

**职责**: 管理卡片注册表的存储和访问，提供创建、获取、清除注册表的功能。

**核心接口**:
```typescript
export interface sideCardRegistry <T extends string = string> {
  components: Record<T, Component>
  getCardProps: (card: CardData) => Record<string, unknown>
}
```

**核心函数**:
- `createCardRegistry(namespace, config)`: 创建并注册卡片注册表
- `getCardRegistry(namespace)`: 根据命名空间获取注册表
- `getAllCardRegistries()`: 获取所有注册表
- `clearAllCardRegistries()`: 清除所有注册表

#### 3.2.3 cardRegistryLoader.ts

**位置**: `factories/cardRegistryLoader.ts`

**职责**: 使用 Vite 的 import.meta.glob 静态扫描注册表文件并自动加载。

**核心函数**:
- `loadCardRegistries()`: 扫描并加载所有卡片注册表
- `clearLoadedModules()`: 清除已加载的模块列表

### 3.3 卡片数据模型

**位置**: `definitions/cardDataType.ts`

**职责**: 定义卡片数据的完整结构，提供类型安全保障。

**核心接口**:
```typescript
export interface CardData<T = never> {
  card_id: number;
  name: string;
  tags: string;
  card_type: CardType;
  card_sub_type: CardSubType;
  description: string;
  icon_path?: string;
  background_path?: string;
  delete_flag: string;
  active_flag: string;
  _type?: T;
}
```

**辅助函数**:
- `parseTags(tagString: string)`: 将逗号分隔的标签字符串解析为标签数组

### 3.4 CardService 服务层

**位置**: `services/cardService.ts`

**职责**: 封装所有卡片相关的 API 调用，提供统一的数据访问接口。

**核心方法**:
- `fetchCards()`: 获取卡片列表
- `addCard(cardData)`: 添加新卡片
- `deleteCard(cardId)`: 删除卡片
- `deactivateCard(cardId)`: 停用卡片
- `updateCardTitle(cardId, newTitle)`: 更新卡片标题
- `updateCardDescription(cardId, description)`: 更新卡片描述
- `uploadFile(type, file)`: 上传文件（图标/背景）
- `updateCardIcon(cardId, iconName)`: 更新卡片图标
- `updateCardBackground(cardId, backgroundName)`: 更新卡片背景
- `updateCardTags(cardId, tags)`: 更新卡片标签
- `deleteCardTag(cardId, tag)`: 删除卡片标签
- `updateCard(cardId, cardData)`: 更新卡片详情

### 3.5 组合式函数 (Composables)

SideCard 模块采用 Vue 3 组合式 API，将各种交互逻辑封装为独立的 composable 函数：

**主要 composables**:
- `useSideCard.ts`: 主组合式函数，整合核心交互逻辑
- `useBarTitle.ts`: 标题栏交互逻辑
- `useBarDescription.ts`: 描述栏交互逻辑
- `useContainerTags.ts`: 标签容器交互逻辑
- `useContainerIcon.ts`: 图标容器交互逻辑
- `useButtonPin.ts`: 固定按钮交互逻辑
- `useButtonExpand.ts`: 展开按钮交互逻辑
- `useButtonClose.ts`: 关闭按钮交互逻辑
- `useButtonEdit.ts`: 编辑按钮交互逻辑
- `useButtonDeactivate.ts`: 停用按钮交互逻辑
- `useButtonChangeIcon.ts`: 更换图标按钮交互逻辑
- `useButtonChangeBackground.ts`: 更换背景按钮交互逻辑
- `useSideCardUpload.ts`: 文件上传交互逻辑
- `useContainerSideCard.ts`: 卡片容器交互逻辑

### 3.6 组件关系图

```
┌─────────────────────────────────────────────────────────────┐
│                        业务组件层                              │
│                   (使用 SideCard 组件)                        │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                    SideCard 主组件层                          │
│                  (components/SideCard.vue)                   │
└────────────────────────────┬────────────────────────────────┘
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   UI 组件层      │  │  Composables 层  │  │   布局组件层     │
│   (ui/*)        │  │  (composables/*) │  │  (layouts/*)    │
└─────────────────┘  └─────────────────┘  └─────────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   注册机制层     │
                  │  (factories/*)  │
                  └─────────────────┘
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   类型定义层     │  │   服务层        │  │   样式层        │
│  (definitions/*)│  │  (services/*)   │  │  (styles/*)     │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

组件间采用分层架构，上层依赖下层，通过接口进行通信，确保系统的松耦合和高内聚。

## 4. 注册机制说明

注册机制是 SideCard 前端模块的核心扩展能力，采用约定优于配置的设计理念，通过静态扫描实现卡片子类型的自动发现和注册。

### 4.1 注册架构概览

SideCard 前端模块的注册架构包含以下核心概念：

- **约定优于配置 (Convention over Configuration)**: 通过文件位置和命名约定实现自动发现，无需手动配置
- **子类型自包含 (Subtype Self-Containment)**: 每个子类型的所有相关代码（组件、属性提取、注册）都放在同一个目录下
- **注册表构建器模式 (Registry Builder Pattern)**: 使用 buildCardRegistry 函数统一构建注册表
- **静态扫描 (Static Scanning)**: 使用 Vite 的 import.meta.glob 实现编译时静态扫描
- **向后兼容性 (Backward Compatibility)**: 保留对现有卡片类型的兼容性

### 4.2 核心注册组件详解

#### 4.2.1 SubTypeRegistry 接口

**定义位置**: `factories/cardRegistryHelper.ts`

```typescript
export interface SubTypeRegistry {
  subType: string
  component: Component
  getSubTypeProps: (card: CardData) => Record<string, unknown>
}
```

**字段说明**:
- `subType`: 卡片子类型标识，如 'alarm'、'relax'、'sample'
- `component`: 该子类型对应的 Vue 组件
- `getSubTypeProps`: 从 CardData 中提取该子类型特定属性的函数

#### 4.2.2 extractBaseCardProps 函数

**定义位置**: `factories/cardRegistryHelper.ts`

```typescript
export function extractBaseCardProps(card: CardData): Record<string, unknown> {
  return {
    cardId: card.card_id,
    name: card.name,
    cardType: card.card_sub_type,
    tags: card.tags,
    description: card.description,
    iconPath: card.icon_path,
    background: card.background_path,
    showClose: card.delete_flag === '0',
    isActive: card.active_flag === '1'
  }
}
```

**功能**: 从 CardData 中提取所有卡片共有的基础属性，避免代码重复。

#### 4.2.3 buildCardRegistry 函数

**定义位置**: `factories/cardRegistryHelper.ts`

**功能**: 构建完整的卡片注册表，包括：
1. 合并默认组件和所有子类型组件
2. 构建子类型属性提取器映射
3. 创建统一的 getCardProps 函数

**返回值**:
```typescript
{
  components: Record<string, Component>  // 子类型 -> 组件映射
  getCardProps: (card: CardData) => Record<string, unknown>  // 获取卡片属性的统一函数
}
```

### 4.3 子类型自包含设计

子类型自包含是指每个卡片子类型的所有相关代码都放在同一个目录下，包括：

**目录结构示例**:
```
features/[featureName]/cards/[subType]/
├── components/
│   └── [SubType]Card.vue
├── definitions/
│   └── cardType.ts
└── registries/
    └── registry.ts
```

**registry.ts 示例**:
```typescript
import AlarmCard from '../components/AlarmCard.vue'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

export default {
  subType: 'alarm',
  component: AlarmCard,
  getSubTypeProps: (card: CardData) => {
    const alarmCard = card as any
    return {
      alarmTime: alarmCard.alarm_time,
      alarmDays: alarmCard.alarm_days,
      startTime: alarmCard.start_time
    }
  }
}
```

### 4.4 静态扫描机制

SideCard 模块使用 Vite 的 import.meta.glob 实现编译时静态扫描：

**扫描路径**:
```typescript
const moduleMap = import.meta.glob(
  '@/features/**/cards/_type/registries/registries.ts',
  { eager: true }
)
```

**扫描特点**:
- **静态扫描**: 在编译时进行，不影响运行时性能
- **Eager 加载**: 立即加载所有匹配的模块
- **模式匹配**: 使用 glob 模式匹配文件路径

**Feature 层 cardRegistry.ts 示例**:
```typescript
import { buildCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistryHelper.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'

const registryModules = import.meta.glob(
  '@/features/sample/cards/**/registries/registry.ts',
  { eager: true }
)

export const sampleCardConfig = buildCardRegistry(
  SideCard,
  registryModules
)
```

## 5. 数据处理流程说明

SideCard 前端模块的数据处理遵循清晰的分层架构，从数据获取、状态管理到组件渲染，每个环节都有明确的职责和规范。

### 5.1 数据流程图

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│   后端 API   │───▶│   服务层      │───▶│  组件层      │───▶│   用户界面   │
│  (REST API)  │    │ (CardService) │    │ (SideCard)  │    │   (浏览器)   │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
                        │                       │                   │
                        ▼                       ▼                   ▼
                 ┌─────────────┐        ┌─────────────┐    ┌─────────────┐
                 │  数据转换    │        │  注册表查询  │    │  事件响应    │
                 │  & 验证      │        │  & 组件渲染  │    │  & 交互反馈  │
                 └─────────────┘        └─────────────┘    └─────────────┘
```

### 5.2 数据流向详细说明

#### 5.2.1 数据获取阶段

1. **API 调用**: 业务组件通过 CardService 调用后端 API
2. **数据接收**: CardService 接收 JSON 格式的响应数据
3. **类型转换**: 将原始 JSON 数据转换为 TypeScript 类型
4. **数据验证**: 对数据进行基本的格式验证

#### 5.2.2 数据处理阶段

1. **注册表查询**: 根据 card_sub_type 查询对应的注册表
2. **组件获取**: 从注册表中获取对应的组件
3. **属性提取**: 调用 getCardProps 提取卡片属性
4. **基础属性提取**: 调用 extractBaseCardProps 提取通用属性
5. **子类型属性提取**: 调用子类型特定的 getSubTypeProps 提取特有属性
6. **属性合并**: 合并基础属性和子类型属性

#### 5.2.3 组件渲染阶段

1. **Props 传递**: 将合并后的属性传递给 SideCard 组件
2. **UI 组件渲染**: SideCard 组件渲染各种 UI 子组件
3. **插槽内容渲染**: 渲染子类型组件提供的插槽内容
4. **状态初始化**: 初始化卡片的各种状态（展开、固定等）

#### 5.2.4 交互响应阶段

1. **用户交互**: 用户点击按钮、编辑内容等
2. **事件触发**: Composable 函数触发相应的事件
3. **事件处理**: SideCard 组件处理事件，可能调用 CardService
4. **API 更新**: CardService 调用后端 API 更新数据
5. **状态更新**: 更新组件状态，重新渲染 UI

### 5.3 核心数据处理场景

#### 5.3.1 卡片列表加载流程

```
1. 业务组件调用 CardService.fetchCards()
2. CardService 发送 GET /get_cards 请求
3. 后端返回卡片列表 JSON
4. CardService 解析响应，返回 CardData[]
5. 业务组件遍历卡片列表
6. 对每个卡片：
   a. 根据 card_type 获取对应的注册表
   b. 调用 registry.getCardProps(card) 提取属性
   c. 从 registry.components 中获取对应的组件
   d. 渲染组件，传递属性
```

#### 5.3.2 卡片编辑流程

```
1. 用户点击编辑按钮
2. useButtonEdit 触发 edit 事件
3. SideCard 组件 emit('edit', cardId)
4. 业务组件监听 edit 事件
5. 业务组件打开编辑对话框/页面
6. 用户修改卡片数据
7. 业务组件调用 CardService.updateCard(cardId, newData)
8. CardService 发送 POST /update_card_detail/<card_id> 请求
9. 后端更新数据库
10. 业务组件刷新卡片列表
```

#### 5.3.3 卡片属性提取流程

```
1. 调用 registry.getCardProps(card)
2. getCardProps 调用 extractBaseCardProps(card) 提取基础属性
3. getCardProps 根据 card.card_sub_type 查找对应的 getSubTypeProps
4. 如果找到，调用 getSubTypeProps(card) 提取子类型属性
5. 合并基础属性和子类型属性
6. 返回完整的属性对象
```

### 5.4 数据模型说明

#### 5.4.1 CardData 接口

```typescript
export interface CardData<T = never> {
  card_id: number;                    // 卡片唯一标识
  name: string;                       // 卡片名称
  tags: string;                       // 卡片标签（逗号分隔）
  card_type: CardType;                // 卡片类型
  card_sub_type: CardSubType;         // 卡片子类型
  description: string;                // 卡片描述
  icon_path?: string;                 // 图标路径（可选）
  background_path?: string;           // 背景路径（可选）
  delete_flag: string;                // 删除标志（'0'=未删除，'1'=已删除）
  active_flag: string;                // 激活标志（'0'=未激活，'1'=已激活）
  _type?: T;                          // 类型参数（用于类型推断）
}
```

#### 5.4.2 卡片属性对象

```typescript
{
  // 基础属性（由 extractBaseCardProps 提取）
  cardId: number,
  name: string,
  cardType: string,
  tags: string,
  description: string,
  iconPath: string | undefined,
  background: string | undefined,
  showClose: boolean,
  isActive: boolean,
  
  // 子类型特定属性（由 getSubTypeProps 提取）
  // 例如 alarm 卡片：
  alarmTime: string,
  alarmDays: string,
  startTime: string
}
```

### 5.5 错误处理和异常流程

#### 5.5.1 错误类型

- **API 错误**: 网络请求失败、服务器错误等
- **注册表未找到错误**: 卡片类型对应的注册表未注册
- **组件未找到错误**: 卡片子类型对应的组件未注册
- **数据验证错误**: 卡片数据格式不正确
- **类型错误**: TypeScript 类型不匹配

#### 5.5.2 错误处理机制

1. **API 错误处理**: CardService 使用 try-catch 捕获网络错误，抛出友好的错误信息
2. **默认组件回退**: buildCardRegistry 会设置默认组件，确保即使子类型组件未找到也能正常显示
3. **控制台日志**: cardRegistryLoader 会输出详细的加载日志，便于调试
4. **类型安全**: TypeScript 编译时类型检查，减少运行时错误

#### 5.5.3 容错设计

- **默认组件**: 提供默认的 SideCard 组件，作为子类型组件的回退
- **属性提取容错**: getCardProps 在找不到子类型属性提取器时，只返回基础属性
- **注册表加载容错**: 单个注册表文件加载失败不影响其他注册表的加载
- **UI 容错**: 图标加载失败时显示默认图标，背景加载失败时显示默认背景

## 6. 配置和使用说明

SideCard 前端模块设计为即插即用，无需复杂配置即可使用。

### 6.1 环境要求

#### 6.1.1 软件依赖

- **Vue**: 3.0 或更高版本
- **TypeScript**: 4.0 或更高版本
- **Vite**: 2.0 或更高版本（用于静态扫描）
- **其他依赖**: 具体依赖项参考项目根目录的 `package.json` 文件

#### 6.1.2 浏览器支持

- **Chrome**: 最新版本
- **Firefox**: 最新版本
- **Safari**: 最新版本
- **Edge**: 最新版本

### 6.2 依赖配置

#### 6.2.1 项目配置

确保项目使用 Vite 作为构建工具，Vue 3 + TypeScript 作为技术栈。

#### 6.2.2 import.meta.glob 配置

Vite 的 import.meta.glob 不需要额外配置，但需要注意：
- 路径必须是静态字符串，不能使用动态模板字符串
- 使用 `{ eager: true }` 选项确保模块立即加载

### 6.3 使用步骤

#### 6.3.1 加载注册表

在应用初始化时调用 loadCardRegistries():

```typescript
import { loadCardRegistries } from '@/core/classic/cards/sideCard/factories/cardRegistryLoader.ts'

// 在应用启动时加载
loadCardRegistries()
```

#### 6.3.2 使用 SideCard 组件

在业务组件中使用 SideCard:

```vue
<template>
  <div v-for="card in cards" :key="card.card_id">
    <component
      :is="getCardComponent(card)"
      v-bind="getCardProps(card)"
      @edit="handleEdit(card.card_id)"
      @close="handleClose(card.card_id)"
    />
  </div>
</template>

<script setup lang="ts">
import { getCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

const props = defineProps<{
  cards: CardData[]
}>()

const registry = getCardRegistry('sample')!

const getCardComponent = (card: CardData) => {
  return registry.components[card.card_sub_type] || registry.components.default
}

const getCardProps = (card: CardData) => {
  return registry.getCardProps(card)
}

const handleEdit = (cardId: number) => {
  // 处理编辑
}

const handleClose = (cardId: number) => {
  // 处理关闭
}
</script>
```

#### 6.3.3 使用 CardService

```typescript
import { CardService } from '@/core/classic/cards/sideCard/services/cardService.ts'

const cardService = new CardService('http://localhost:5000')

// 获取卡片列表
const cards = await cardService.fetchCards()

// 添加新卡片
const newCard = await cardService.addCard({
  name: '新卡片',
  card_type: 'sample',
  card_sub_type: 'alarm',
  tags: '标签1,标签2',
  description: '卡片描述',
  delete_flag: '0',
  active_flag: '1'
})

// 更新卡片
await cardService.updateCard(cardId, updatedData)

// 删除卡片
await cardService.deleteCard(cardId)
```

### 6.4 常见问题排查

#### 6.4.1 注册表未找到

- **症状**: getCardRegistry 返回 undefined
- **可能原因**: 注册表未正确调用 createCardRegistry，或者命名空间不匹配
- **解决方案**: 检查 feature 层的 cardRegistry.ts 是否正确调用 createCardRegistry，命名空间是否正确

#### 6.4.2 子类型组件未找到

- **症状**: 显示默认组件而不是子类型组件
- **可能原因**: 子类型的 registry.ts 未正确导出，或者 subType 字段不匹配
- **解决方案**: 检查子类型的 registry.ts 是否正确导出，subType 字段是否与 card_sub_type 匹配

#### 6.4.3 import.meta.glob 报错

- **症状**: Vite 编译报错 "Invalid glob import syntax"
- **可能原因**: 使用了动态模板字符串作为 glob 模式
- **解决方案**: 使用静态字符串作为 glob 模式，不要使用动态模板字符串

#### 6.4.4 卡片属性未正确提取

- **症状**: 子类型特定属性未显示
- **可能原因**: getSubTypeProps 函数未正确实现，或者 CardData 中没有对应字段
- **解决方案**: 检查 getSubTypeProps 函数实现，确保 CardData 中包含所需字段

## 7. 扩展和开发指南

SideCard 前端模块设计为高度可扩展，开发者可以轻松添加新的卡片子类型。本章节提供完整的扩展开发指南。

### 7.1 扩展架构概览

SideCard 前端模块的扩展性主要体现在以下方面：

- **子类型自包含**: 每个子类型的所有代码（组件、类型定义、数据类型、注册表）都在同一个目录下
- **类型定义自包含**: 每个子类型拥有自己独立的 cardType.ts 和 cardDataType.ts
- **约定优于配置**: 通过文件位置和命名约定实现自动发现
- **注册表构建器**: 使用 buildCardRegistry 统一构建注册表
- **静态扫描**: 使用 import.meta.glob 自动发现子类型

### 7.2 添加新卡片子类型的步骤

#### 7.2.1 创建子类型目录结构

在 `features/[featureName]/cards/` 目录下创建新的子类型目录：

```
features/[featureName]/cards/[newSubType]/
├── components/
│   └── [NewSubType]Card.vue
└── registries/
    └── registry.ts
```

#### 7.2.2 创建子类型组件

在 `components/` 目录下创建子类型组件：

```vue
<template>
  <SideCard
    v-bind="sideCardProps"
    @edit="handleEdit"
    @close="handleClose"
  >
    <template #card-content>
      <!-- 子类型特定内容 -->
      <div class="new-subtype-content">
        {{ specificProp }}
      </div>
    </template>
  </SideCard>
</template>

<script setup lang="ts">
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'
import type { SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'

interface Props extends SideCardProps {
  specificProp: string
}

const props = defineProps<Props>()

const sideCardProps = computed(() => {
  const { specificProp, ...rest } = props
  return rest
})

const emit = defineEmits<{
  edit: [cardId: number]
  close: [cardId: number]
}>()

const handleEdit = () => {
  emit('edit', props.cardId)
}

const handleClose = () => {
  emit('close', props.cardId)
}
</script>

<style scoped lang="scss">
.new-subtype-content {
  // 子类型特定样式
}
</style>
```

#### 7.2.5 创建注册表文件

在 `registries/` 目录下创建 registry.ts：

```typescript
import NewSubTypeCard from '../components/NewSubTypeCard.vue'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

export default {
  subType: 'newSubType',
  component: NewSubTypeCard,
  getSubTypeProps: (card: CardData) => {
    const newSubTypeCard = card as any
    return {
      specificProp: newSubTypeCard.specific_prop
    }
  }
}
```

#### 7.2.6 更新 Feature 层 cardRegistry.ts（如需要）

如果 feature 层还没有 cardRegistry.ts，创建一个：

```typescript
import { buildCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistryHelper.ts'
import { createCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'

const registryModules = import.meta.glob(
  '@/features/[featureName]/cards/**/registries/registry.ts',
  { eager: true }
)

const [featureName]CardConfig = buildCardRegistry(
  SideCard,
  registryModules
)

createCardRegistry('[featureName]', [featureName]CardConfig)

export { [featureName]CardConfig }
```

#### 7.2.7 测试新子类型

1. 启动开发服务器
2. 检查控制台日志，确认注册表正确加载
3. 创建一个 card_sub_type 为 'newSubType' 的卡片
4. 验证卡片是否正确渲染，子类型特定内容是否显示
5. 测试各种交互功能（编辑、关闭、固定等）

### 7.3 扩展最佳实践

#### 7.3.1 代码组织规范

- **子类型自包含**: 每个子类型的所有代码都放在同一个目录下
- **单一职责**: 每个组件只负责一种卡片子类型的渲染
- **功能完整**: 子类型组件应完整实现所有必要的交互功能
- **类型安全**: 为子类型特定属性定义完整的 TypeScript 类型

#### 7.3.2 数据设计规范

- **属性命名**: 子类型特定属性使用 camelCase，对应后端的 snake_case
- **数据验证**: 在 getSubTypeProps 中进行数据验证，提供默认值
- **数据转换**: 合理处理数据格式转换，确保数据一致性

#### 7.3.3 性能考虑

- **懒加载**: 对于大型组件，可以考虑使用动态导入
- **避免过度渲染**: 使用 computed 和 memo 优化渲染性能
- **合理使用插槽**: 使用插槽而不是 props 传递复杂内容

### 7.4 常见扩展场景

#### 7.4.1 添加新的卡片子类型

- **场景**: 需要支持新的卡片子类型，如 'habit'（习惯追踪）
- **步骤**: 按照 7.2 节的步骤创建子类型目录、组件、注册表
- **关键点**: 定义 habit 特有的属性和 UI 展示

#### 7.4.2 扩展现有的子类型

- **场景**: 为现有卡片子类型添加新功能
- **步骤**: 修改现有子类型组件，添加新的功能
- **关键点**: 保持向后兼容，不影响现有功能

#### 7.4.3 自定义 SideCard 基础功能

- **场景**: 需要自定义 SideCard 的基础功能，如添加新的按钮
- **步骤**: 创建新的 composable 或 UI 组件，在 SideCard 中集成
- **关键点**: 遵循现有代码风格，保持一致性

### 7.5 故障排除

#### 7.5.1 新子类型未被扫描到

- **检查点**: 文件路径是否正确、glob 模式是否匹配、文件名是否正确
- **调试方法**: 查看 cardRegistryLoader 的控制台输出，确认扫描到的文件列表

#### 7.5.2 子类型组件未渲染

- **检查点**: registry.ts 是否正确导出、subType 字段是否匹配、组件是否正确导入
- **调试方法**: 在 buildCardRegistry 中添加日志，确认组件是否被正确注册

#### 7.5.3 子类型属性未显示

- **检查点**: getSubTypeProps 是否正确实现、CardData 中是否有对应字段、属性名是否匹配
- **调试方法**: 在 getSubTypeProps 中添加日志，确认返回的属性对象

#### 7.5.4 类型错误

- **检查点**: TypeScript 类型定义是否正确、props 是否正确传递
- **调试方法**: 检查 TypeScript 编译错误，使用类型断言临时绕过，然后修复类型定义
