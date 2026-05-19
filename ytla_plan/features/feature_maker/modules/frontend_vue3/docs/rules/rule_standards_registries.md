# Registries 代码规范

## 1 依赖限制表

| 功能域类型 | registries可依赖此功能域 | registries可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories | ✓ |  |
| flows | ✓ |  |
| registries |  |  |
| services |  |  |
| policies |  |  |
| stores |  |  |
| composables |  |  |
| uis |  |  |
| components | ✓ |  |
| layouts |  |  |

## 2 标准代码格式

---
以下为预生成内容.  
预生成内容包含基础的注册配置和注册表汇总文件，用于模块的自动注册和加载.
---

### 2.1 card 子类型 _type 目录 cardRegistry 文件

```typescript
// registries/cardRegistry.ts

import type { sideCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import { buildCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistryHelper.ts'
import SideCard from '@/core/classic/cards/sideCard/components/SideCard.vue'

const registryModules = import.meta.glob('@/features/[模块类型]/cards/**/registries/registry.ts', { eager: true })

export const [模块类型]
CardConfig = buildCardRegistry(SideCard, registryModules) as sideCardRegistry
```

### 2.2 card 子类型 _type 目录 registries 文件

```typescript
// registries/registries.ts
// 注册表汇总文件
// 用于导入和导出所有注册表
```

### 2.3 module 子类型 ModuleConfig 文件

```typescript
// registries/[子类型]ModuleConfig.ts

import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import {

[子类型]
ModuleFlowManager
}
from
'@/features/[模块类型]/modules/[子类型]/flows/[子类型]FlowManager'

export const [子类型]
ModuleConfig = <ModuleRegistry>{
  moduleType: '[模块类型]',
  moduleSubType: '[子类型]',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/[模块类型]/modules/[子类型]/components/[子类型首字母大写]Main.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/[模块类型]/modules/[子类型]/components/[子类型首字母大写]Sub.vue')
  ),
  displayMode: 7,
  flowManager: [子类型]ModuleFlowManager
}
```

### 2.4 module 子类型 registries 文件

```typescript
// registries/registries.ts

import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import {

[子类型]
ModuleFlowManager
}
from
'@/features/[模块类型]/modules/[子类型]/flows/[子类型]FlowManager.ts'
createModuleFlowRegistry('[子类型]', [子类型]
ModuleFlowManager
)
import {

[子类型]
ModuleConfig
}
from
'@/features/[模块类型]/modules/[子类型]/registries/[子类型]ModuleConfig.ts'
createModuleRegistry('[子类型]', [子类型]
ModuleConfig
)
```

### 2.5 SideCard 子类型 registry 文件

```typescript
// registries/registry.ts

import

[子类型首字母大写]
Card
from
'../components/[子类型首字母大写]Card.vue'
import type {

[子类型首字母大写]
CardData
}
from
'../definitions/cardDataType.ts'

export default {
  subType: '[子类型]',
  component: [子类型首字母大写]Card,
  getSubTypeProps: (card: any) => {
    const [子类型]
    Card = card as [子类型首字母大写]
    CardData
    return {}
  }
}
```

---

以下为自定义内容区域，可根据业务需求按需添加额外注册逻辑.

---

### 2.5 子类型 registry 文件

```typescript
// registries/registry.ts

import

[组件名]
from
'../components/[组件名].vue'
import type {

[组件名]
Data
}
from
'../definitions/[数据类型]Type.ts'

export default {
  subType: '[子类型名称]',
  component: [组件名],
  getSubTypeProps: (card: any) => {
    const [组件名]
    Card = card as [组件名]
    Data
    return {
      [自定义属性1]: [组件名]Card.[数据字段1],
      [自定义属性2]: [组件名]Card.[数据字段2],
      [自定义属性3]: [组件名]Card.[数据字段3]
    }
  }
}
```

### 2.6 完整示例

```typescript
// registries/registry.ts

import UserCard from '../components/UserCard.vue'
import type { UserCardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'user',
  component: UserCard,
  getSubTypeProps: (card: any) => {
    const userCard = card as UserCardData
    return {
      userName: userCard.user_name,
      userAvatar: userCard.user_avatar,
      userRole: userCard.user_role,
      userDepartment: userCard.user_department
    }
  }
}
```

### 2.7 带条件判断的注册

```typescript
// registries/registry.ts

import AdvancedCard from '../components/AdvancedCard.vue'
import type { AdvancedCardData } from '../definitions/cardDataType.ts'

export default {
  subType: 'advanced',
  component: AdvancedCard,
  getSubTypeProps: (card: any) => {
    const advancedCard = card as AdvancedCardData

    return {
      title: advancedCard.title,
      content: advancedCard.content,
      priority: advancedCard.priority,
      isHighlighted: advancedCard.priority === 'high',
      badgeCount: advancedCard.notification_count ?? 0,
      extraConfig: {
        showIcon: advancedCard.show_icon === '1',
        showBadge: advancedCard.notification_count > 0,
        clickAction: advancedCard.click_action
      }
    }
  }
}
```