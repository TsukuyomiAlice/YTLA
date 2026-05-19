# Flows 代码规范

## 1 依赖限制表

| 功能域类型 | flows可依赖此功能域 | flows可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions |  |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories |  |  |
| flows |  |  |
| registries |  | ✓ |
| services |  |  |
| policies |  |  |
| stores |  |  |
| composables |  |  |
| uis |  |  |
| components |  |  |
| layouts |  |  |

## 2 标准代码格式

---
以下为预生成内容.  
预生成内容包含基础的流程管理器实现，用于模块的步骤流程管理.
---

### 2.1 Module 子类型 FlowManager 文件

```typescript
// flows/[子类型]FlowManager.ts

import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class [子类型首字母大写]ModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const [子类型]ModuleFlowManager = new [子类型首字母大写]ModuleFlowManager()

[子类型]ModuleFlowManager.registerFlow('[子类型]-main-steps', [
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/[子类型首字母大写]Main_00.vue')),
])

[子类型]ModuleFlowManager.registerFlow('[子类型]-sub-steps', [
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/[子类型首字母大写]Sub_00.vue')),
])
```

### 2.2 SideCard 子类型 FlowManager 文件（可选）

```typescript
// flows/[子类型]FlowManager.ts

import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class [子类型首字母大写]ModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const [子类型]ModuleFlowManager = new [子类型首字母大写]ModuleFlowManager()

[子类型]ModuleFlowManager.registerFlow('[子类型]-main-steps', [
  defineAsyncComponent(() => import('@/features/[模块类型]/cards/[子类型]/components/[子类型首字母大写]Card.vue')),
])
```

---

以下为自定义内容区域，可根据业务需求按需扩展流程管理逻辑.

---

### 2.3 扩展流程配置示例

```typescript
// flows/[子类型]FlowManager.ts

import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class [子类型首字母大写]ModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const [子类型]ModuleFlowManager = new [子类型首字母大写]ModuleFlowManager()

[子类型]ModuleFlowManager.registerFlow('create', [
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/Step1Form.vue')),
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/Step2Confirm.vue')),
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/Step3Success.vue')),
])

[子类型]ModuleFlowManager.registerFlow('edit', [
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/EditForm.vue')),
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/EditSuccess.vue')),
])

[子类型]ModuleFlowManager.registerFlow('detail', [
  defineAsyncComponent(() => import('@/features/[模块类型]/modules/[子类型]/components/DetailView.vue')),
])
```
