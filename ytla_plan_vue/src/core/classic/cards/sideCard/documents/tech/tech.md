# SideCard - Tech 文档

## 1. 模块概述

### 1.1 模块定位

SideCard 是 YTLA 项目中侧边卡片渲染和交互的核心模块，提供了一套完整的侧边卡片组件系统。该模块基于 Vue 3 + TypeScript + Vite 技术栈开发，采用现代化的前端架构设计。

### 1.2 主要功能

SideCard 模块提供以下核心功能：

- **动态卡片注册机制** - 支持通过命名空间动态注册不同类型的卡片组件
- **丰富的交互功能**：
  - 卡片展开/收起
  - 卡片固定/取消固定
  - 卡片编辑
  - 卡片停用/激活
  - 卡片关闭
  - 图标更换
  - 背景更换
  - 标签管理（添加、删除）
  - 标题和描述编辑
- **拖拽支持** - 支持卡片拖拽重排
- **状态管理** - 基于 Pinia 的完整状态管理
- **API 集成** - 与后端 API 完整集成

### 1.3 设计目标

- **高可扩展性** - 通过组件注册机制支持灵活扩展新的卡片类型
- **组件化** - 采用组合式 API（Composables）实现功能复用
- **类型安全** - 完整的 TypeScript 类型定义
- **易于维护** - 清晰的代码结构和职责分离

### 1.4 技术栈

- **框架**: Vue 3 (Composition API)
- **语言**: TypeScript
- **构建工具**: Vite
- **状态管理**: Pinia
- **样式**: SCSS

---

## 2. 文件结构说明

### 2.1 目录结构

```
sideCard/
├── avatar/                    # 头像组件
│   └── Avatar.vue
├── components/                # 核心组件
│   └── SideCard.vue          # 主组件
├── composables/               # 组合式函数
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
│   ├── useSideCard.ts         # 主 composable
│   └── useSideCardUpload.ts
├── definitions/               # 类型定义
│   ├── cardDataType.ts
│   ├── cardType.ts
│   └── sideCardType.ts
├── documents/                 # 文档目录
│   ├── readme/
│   ├── tech/                  # Tech 文档目录
│   └── tasks/
├── factories/                 # 工厂类
│   ├── cardRegistry.ts
│   ├── cardRegistryHelper.ts
│   └── cardRegistryLoader.ts
├── layouts/                   # 布局组件
│   └── ContainerSideCard.vue
├── locales/                   # 国际化
│   ├── en.json
│   └── zh.json
├── services/                  # 服务层
│   └── cardService.ts
├── stores/                    # 状态管理
│   └── cardStore.ts
├── styles/                    # 样式文件
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
├── ui/                        # UI 组件
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

### 2.2 核心目录说明

| 目录 | 说明 |
|------|------|
| `components/` | 包含 SideCard 主组件 |
| `composables/` | 所有组合式函数，实现功能逻辑的复用 |
| `definitions/` | TypeScript 类型定义文件 |
| `factories/` | 卡片注册工厂类 |
| `layouts/` | 布局组件 |
| `services/` | API 服务层 |
| `stores/` | Pinia 状态管理 |
| `styles/` | SCSS 样式文件 |
| `ui/` | 可复用的 UI 组件 |

### 2.3 关键文件说明

| 文件 | 说明 |
|------|------|
| `components/SideCard.vue` | SideCard 主组件，整合所有功能 |
| `composables/useSideCard.ts` | 主 composable，整合所有子 composables |
| `definitions/sideCardType.ts` | SideCard 组件 Props 和 Emits 类型定义 |
| `definitions/cardDataType.ts` | 卡片数据模型定义 |
| `factories/cardRegistry.ts` | 卡片注册机制实现 |
| `stores/cardStore.ts` | Pinia store，管理卡片状态 |
| `services/cardService.ts` | API 服务封装 |

---

## 3. 核心组件说明

### 3.1 SideCard 主组件

**文件**: `components/SideCard.vue`

SideCard 是模块的主组件，负责整合所有 UI 组件和功能逻辑。

**主要职责**:
- 接收并处理 Props
- 定义 Emits 事件
- 调用 useSideCard composable 获取所有功能
- 组织 UI 布局结构
- 提供插槽供扩展

**组件结构**:
```
ContainerSideCard (外层容器)
├── 主显示区
│   ├── 左上角按钮区
│   │   ├── ButtonPin
│   │   ├── ButtonChangeIcon
│   │   ├── ButtonChangeBackground
│   │   └── top-left-actions slot
│   ├── 右上角按钮区
│   │   ├── ButtonEdit
│   │   ├── ButtonDeactivate
│   │   ├── ButtonClose
│   │   └── top-actions slot
│   └── 主内容区
│       ├── Header
│       │   ├── ContainerIcon
│       │   └── BarTitle
│       ├── ContainerTags
│       └── card-content slot
├── 主按钮区
│   ├── left-actions-buttons slot
│   ├── right-actions slot
│   └── ButtonExpand
└── 副内容区 (展开时显示)
    ├── BarDescription
    └── secondary-content slot
```

### 3.2 UI 组件

SideCard 模块包含以下 UI 组件：

| 组件 | 文件 | 功能 |
|------|------|------|
| BarTitle | `ui/BarTitle.vue` | 标题栏，支持编辑 |
| BarDescription | `ui/BarDescription.vue` | 描述栏，支持编辑 |
| ButtonPin | `ui/ButtonPin.vue` | 固定/取消固定按钮 |
| ButtonChangeIcon | `ui/ButtonChangeIcon.vue` | 更换图标按钮 |
| ButtonChangeBackground | `ui/ButtonChangeBackground.vue` | 更换背景按钮 |
| ButtonEdit | `ui/ButtonEdit.vue` | 编辑按钮 |
| ButtonDeactivate | `ui/ButtonDeactivate.vue` | 停用按钮 |
| ButtonClose | `ui/ButtonClose.vue` | 关闭按钮 |
| ButtonExpand | `ui/ButtonExpand.vue` | 展开/收起按钮 |
| ContainerIcon | `ui/ContainerIcon.vue` | 图标容器 |
| ContainerTags | `ui/ContainerTags.vue` | 标签容器 |

### 3.3 布局组件

**ContainerSideCard** (`layouts/ContainerSideCard.vue`)

外层容器组件，负责：
- 卡片整体布局
- 拖拽功能支持
- 固定状态样式
- 展开状态样式
- 背景样式

---

## 4. 数据模型和类型定义

### 4.1 SideCardProps

**文件**: `definitions/sideCardType.ts`

SideCard 组件的 Props 定义：

```typescript
interface SideCardProps {
  cardId?: number              // 卡片 ID
  cardType?: string            // 卡片类型
  icon?: string                // 图标路径
  background?: string          // 背景路径
  name?: string                // 卡片名称
  tags?: string                // 标签（逗号分隔）
  description?: string         // 描述
  spanColumns?: number         // 跨列数
  initialExpanded?: boolean    // 初始展开状态
  showIcon?: boolean           // 是否显示图标
  showTitle?: boolean          // 是否显示标题
  showTags?: boolean           // 是否显示标签
  showSettings?: boolean       // 是否显示设置按钮
  showDeactivate?: boolean     // 是否显示停用按钮
  showClose?: boolean          // 是否显示关闭按钮
  order?: number               // 排序
}
```

### 4.2 SideCardEmits

**文件**: `definitions/sideCardType.ts`

SideCard 组件的 Emits 定义：

```typescript
type SideCardEmits = {
  (e: 'toggle-expanded', state: boolean): void
  (e: 'settings'): void
  (e: 'deactivate', id?: number): void
  (e: 'close', id?: number): void
  (e: 'left-action', action: string): void
  (e: 'update:tags', tags: string): void
  (e: 'edit', id: number): void
}
```

### 4.3 CardData

**文件**: `definitions/cardDataType.ts`

卡片数据模型：

```typescript
interface CardData<T = never> {
  card_id: number                    // 卡片 ID
  name: string                       // 名称
  tags: string                       // 标签
  card_type: CardType                // 卡片类型
  card_sub_type: CardSubType         // 卡片子类型
  description: string                // 描述
  icon_path?: string                 // 图标路径
  background_path?: string           // 背景路径
  delete_flag: string                // 删除标记
  active_flag: string                // 激活标记
  _type?: T                          // 扩展类型
}
```

**辅助函数**:
- `parseTags(tagString: string): string[]` - 解析标签字符串为数组

### 4.4 其他类型

**CardType 和 CardSubType** (`definitions/cardType.ts`):
```typescript
type CardType = string;
type CardSubType = string;
```

---

## 5. 核心 Composables 说明

### 5.1 useSideCard

**文件**: `composables/useSideCard.ts`

主 composable，整合所有子 composables 的功能。

**职责**:
- 组合所有子 composables
- 统一暴露状态和方法给组件使用
- 协调各功能模块之间的交互

**返回的状态和方法**:
```typescript
{
  // 拖拽
  isDragging, handleDragStart, handleDragEnd,
  
  // 固定
  isPinned, togglePin,
  
  // 图标
  fullIconPath, iconUploadInput, triggerIconUpload, handleIconUpload,
  
  // 背景
  containerStyle, bgUploadInput, triggerBgUpload, handleBgUpload,
  
  // 文件上传
  handleFileUpload,
  
  // 编辑
  handleEdit,
  
  // 停用
  handleDeactivate,
  
  // 关闭
  handleClose,
  
  // 图标容器
  handleIconError, removeIcon,
  
  // 标题
  titleRef, isTitleEditable, handleTitleBlur, startEditTitle, cancelEditTitle,
  
  // 描述
  descriptionRef, isDescriptionEditable, handleDescriptionBlur, startEditDescription, cancelEditDescription,
  
  // 展开
  isExpanded, toggleExpanded,
  
  // 标签
  tagsArray, isAddingTag, newTag, tagInput, shouldShowAddButton, showAddButton, 
  startAddingTag, addNewTag, removeTag, handleTagInput, cancelAddTag,
  
  // 左侧操作
  handleLeftAction
}
```

### 5.2 子 Composables

| Composable | 文件 | 功能 |
|------------|------|------|
| useContainerSideCard | `composables/useContainerSideCard.ts` | 容器拖拽功能 |
| useButtonPin | `composables/useButtonPin.ts` | 固定/取消固定 |
| useButtonChangeIcon | `composables/useButtonChangeIcon.ts` | 更换图标 |
| useButtonChangeBackground | `composables/useButtonChangeBackground.ts` | 更换背景 |
| useButtonEdit | `composables/useButtonEdit.ts` | 编辑按钮 |
| useButtonDeactivate | `composables/useButtonDeactivate.ts` | 停用按钮 |
| useButtonClose | `composables/useButtonClose.ts` | 关闭按钮 |
| useButtonExpand | `composables/useButtonExpand.ts` | 展开/收起 |
| useContainerIcon | `composables/useContainerIcon.ts` | 图标容器 |
| useBarTitle | `composables/useBarTitle.ts` | 标题编辑 |
| useBarDescription | `composables/useBarDescription.ts` | 描述编辑 |
| useContainerTags | `composables/useContainerTags.ts` | 标签管理 |
| useSideCardUpload | `composables/useSideCardUpload.ts` | 文件上传 |

---

## 6. 状态管理说明

### 6.1 cardStore

**文件**: `stores/cardStore.ts`

基于 Pinia 的状态管理，管理所有卡片的状态。

**State (状态)**:
```typescript
{
  cards: CardData[]              // 卡片列表
  isLoading: boolean              // 加载状态
  error: string | null            // 错误信息
  cardFilter: string              // 卡片筛选
}
```

**Actions (操作)**:

| 操作 | 说明 |
|------|------|
| `fetchCards()` | 获取所有卡片 |
| `addCard(cardData)` | 添加新卡片 |
| `updateCard(cardId, cardData)` | 更新卡片 |
| `deleteCard(cardId)` | 删除卡片 |
| `deactivateCard(cardId)` | 停用卡片 |
| `updateCardTitle(cardId, newTitle)` | 更新卡片标题 |
| `updateCardDescription(cardId, newDescription)` | 更新卡片描述 |
| `updateCardIcon(cardId, iconName)` | 更新卡片图标 |
| `updateCardBackground(cardId, backgroundName)` | 更新卡片背景 |
| `updateCardTags(cardId, tags)` | 更新卡片标签 |
| `deleteCardTag(cardId, tag)` | 删除卡片标签 |
| `updateFilter(value)` | 更新筛选条件 |

**Getters (计算属性)**:

| Getter | 说明 |
|--------|------|
| `activeCards` | 获取激活且未删除的卡片 |
| `filteredCards` | 获取筛选后的卡片（按标签、类型、子类型筛选） |

---

## 7. 服务层 API 说明

### 7.1 CardService

**文件**: `services/cardService.ts`

封装所有与后端 API 的交互。

**构造函数**:
```typescript
constructor(API_BASE: string)
```

**API 方法**:

| 方法 | HTTP 方法 | 端点 | 说明 |
|------|-----------|------|------|
| `fetchCards()` | GET | `/get_cards` | 获取所有卡片 |
| `addCard(cardData)` | POST | `/add_card` | 添加卡片 |
| `deleteCard(cardId)` | POST | `/delete_card/{cardId}` | 删除卡片 |
| `deactivateCard(cardId)` | POST | `/deactivate_card/{cardId}` | 停用卡片 |
| `updateCardTitle(cardId, newTitle)` | POST | `/update_card/{cardId}` | 更新标题 |
| `updateCardDescription(cardId, description)` | POST | `/update_card/{cardId}` | 更新描述 |
| `uploadFile(type, file)` | POST | `/upload/{type}` | 上传文件（icon/background） |
| `updateCardIcon(cardId, iconName)` | POST | `/update_card/{cardId}` | 更新图标 |
| `updateCardBackground(cardId, backgroundName)` | POST | `/update_card/{cardId}` | 更新背景 |
| `updateCardTags(cardId, tags)` | POST | `/update_card/{cardId}/tags` | 更新标签 |
| `deleteCardTag(cardId, tag)` | DELETE | `/update_card/{cardId}/tags` | 删除标签 |
| `updateCard(cardId, cardData)` | POST | `/update_card_detail/{cardId}` | 更新卡片详情 |

---

## 8. 组件注册机制说明

### 8.1 cardRegistry

**文件**: `factories/cardRegistry.ts`

提供动态卡片组件注册机制。

**核心接口**:
```typescript
interface sideCardRegistry<T extends string = string> {
  components: Record<T, Component>
  getCardProps: (card: CardData) => Record<string, unknown>
}
```

**核心方法**:

| 方法 | 说明 |
|------|------|
| `createCardRegistry(namespace, config)` | 创建并注册卡片注册表 |
| `getCardRegistry(namespace)` | 获取指定命名空间的注册表 |
| `getAllCardRegistries()` | 获取所有注册表 |
| `clearAllCardRegistries()` | 清空所有注册表 |

**使用示例**:
```typescript
// 注册卡片类型
createCardRegistry('my-card-type', {
  components: {
    default: MyCardComponent
  },
  getCardProps: (card) => ({
    // 根据 card 数据返回 props
  })
})

// 获取注册表
const registry = getCardRegistry('my-card-type')
```

### 8.2 其他工厂类

| 文件 | 说明 |
|------|------|
| `factories/cardRegistryHelper.ts` | 注册表辅助函数 |
| `factories/cardRegistryLoader.ts` | 注册表加载器 |

---

## 9. 使用示例

### 9.1 基本使用

```vue
<template>
  <SideCard
    :card-id="1"
    name="我的卡片"
    description="这是一个示例卡片"
    tags="标签1,标签2"
    @edit="handleEdit"
    @close="handleClose"
  >
    <template #card-content>
      <!-- 卡片内容 -->
    </template>
  </SideCard>
</template>

<script setup lang="ts">
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'

const handleEdit = (id: number) => {
  console.log('编辑卡片', id)
}

const handleClose = (id?: number) => {
  console.log('关闭卡片', id)
}
</script>
```

### 9.2 使用 Store

```typescript
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore'

const cardStore = useCardStore()

// 获取卡片
await cardStore.fetchCards()

// 访问激活的卡片
console.log(cardStore.activeCards)

// 添加卡片
await cardStore.addCard({
  name: '新卡片',
  tags: '标签1',
  card_type: 'default',
  card_sub_type: 'default',
  description: '描述',
  delete_flag: '0',
  active_flag: '1'
})
```

---

## 10. 扩展开发

### 10.1 添加新的卡片类型

1. 创建卡片组件
2. 使用 `createCardRegistry` 注册
3. 实现 `getCardProps` 函数

### 10.2 添加新的 Composable

1. 在 `composables/` 目录下创建新文件
2. 实现 composable 逻辑
3. 在 `useSideCard.ts` 中集成
4. 暴露给组件使用

---

**文档版本**: 1.0  
**最后更新**: 2026-04-09  
**维护者**: Official
