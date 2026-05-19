# Factories 代码规范

## 1 依赖限制表

| 功能域类型 | factories可依赖此功能域 | factories可被此功能域依赖 |
| :--- | :--- | :--- |
| definitions | ✓ |  |
| styles |  |  |
| utils |  |  |
| locales |  |  |
| avatar |  |  |
| factories | ✓(非自身) |  |
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

以下内容仅供参考，不作为实际项目代码使用.  

---  
### 2.1 注册中心工厂

```typescript
// factories/[模块名]Registry.ts

import type { Component } from 'vue'
import type { [模块名]Type } from '../definitions/[模块名]Type.ts'
import type { [模块名]Data } from '../definitions/[模块名]DataType.ts'

export interface [模块名]Registry <T extends string = string> {
  components: Record<T, Component>
  get[模块名]Props: ([模块名]: [模块名]Data) => Record<string, unknown>
}

const [模块名]RegistryStore = new Map<string, [模块名]Registry>()

export const create[模块名]Registry = <T extends string>(
  namespace: string,
  config: [模块名]Registry<T>
): [模块名]Registry<T> => {
  [模块名]RegistryStore.set(namespace, config)
  return config
}

export const get[模块名]Registry = (namespace: [模块名]Type): [模块名]Registry | undefined => {
  return [模块名]RegistryStore.get(namespace)
}

export const getAll[模块名]Registries = (): Map<string, [模块名]Registry> => {
  return [模块名]RegistryStore
}

export const clearAll[模块名]Registries = (): void => {
  [模块名]RegistryStore.clear()
}
```

### 2.2 注册辅助工具

```typescript
// factories/[模块名]RegistryHelper.ts

import type { Component } from 'vue'
import type { [模块名]Data } from '../definitions/[模块名]DataType.ts'

export interface SubTypeRegistry {
  subType: string
  component: Component
  getSubTypeProps: ([模块名]: [模块名]Data) => Record<string, unknown>
}

export function extractBase[模块名]Props([模块名]: [模块名]Data): Record<string, unknown> {
  return {
    [模块名]Id: [模块名].[模块名]_id,
    name: [模块名].name,
    [模块名]Type: [模块名].[模块名]_sub_type,
    tags: [模块名].tags,
    description: [模块名].description,
    iconPath: [模块名].icon_path,
    background: [模块名].background_path,
    showClose: [模块名].delete_flag === '0',
    isActive: [模块名].active_flag === '1'
  }
}

export function build[模块名]Registry(
  defaultComponent: Component,
  registryModules: Record<string, unknown>
): {
  components: Record<string, Component>
  get[模块名]Props: ([模块名]: [模块名]Data) => Record<string, unknown>
} {
  const components: Record<string, Component> = { default: defaultComponent }
  const subTypePropsGetters: Record<string, ([模块名]: [模块名]Data) => Record<string, unknown>> = {}

  Object.values(registryModules).forEach((module: any) => {
    if (module.default) {
      const registry = module.default as SubTypeRegistry
      const subType = registry.subType
      if (subType && registry.component && registry.getSubTypeProps) {
        components[subType] = registry.component
        subTypePropsGetters[subType] = registry.getSubTypeProps
      }
    }
  })

  const get[模块名]Props = ([模块名]: [模块名]Data): Record<string, unknown> => {
    const baseProps = extractBase[模块名]Props([模块名])
    const subType = [模块名].[模块名]_sub_type
    const getSubTypeProps = subTypePropsGetters[subType]

    if (getSubTypeProps) {
      return {
        ...baseProps,
        ...getSubTypeProps([模块名])
      }
    }

    return baseProps
  }

  return {
    components,
    get[模块名]Props
  }
}
```

### 2.3 注册加载器

```typescript
// factories/[模块名]RegistryLoader.ts

import { getAll[模块名]Registries } from './[模块名]Registry.ts'

const loadedModules = new Set<string>()

export function load[模块名]Registries(): void {
  console.groupCollapsed('[load[模块名]Registries] Starting to load [模块名] registries')
  console.time('[load[模块名]Registries] Total time')

  const moduleMap = import.meta.glob('@/features/**/[模块名]s/_type/registries/registries.ts', { eager: true })
  const totalModules = Object.keys(moduleMap).length

  console.debug(`[load[模块名]Registries] Found ${totalModules} [模块名] registry files`)

  Object.keys(moduleMap).forEach((path, index) => {
    if (!loadedModules.has(path)) {
      loadedModules.add(path)
      console.debug(`[load[模块名]Registries] [${index + 1}/${totalModules}] [模块名] module loaded: ${path}`)
    } else {
      console.debug(`[load[模块名]Registries] [${index + 1}/${totalModules}] [模块名] module already loaded, skipping: ${path}`)
    }
  })

  console.timeEnd('[load[模块名]Registries] Total time')

  const store = getAll[模块名]Registries()
  
  if (store.size > 0) {
    console.debug(`[load[模块名]Registries] Successfully loaded ${store.size} [模块名] registries`)
    store.forEach((registry, namespace) => {
      console.debug(`[load[模块名]Registries]  - ${namespace}: ${Object.keys(registry.components || {}).length} components`)
    })
  } else {
    console.warn('[load[模块名]Registries] No [模块名] registries found, please check if registry files correctly call create[模块名]Registry')
  }

  console.groupEnd()
}

export function clearLoadedModules(): void {
  console.debug('[load[模块名]Registries] Clearing loaded [模块名] module list')
  loadedModules.clear()
}
```