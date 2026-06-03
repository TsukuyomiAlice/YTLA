import type { PanelContentState } from '@/core/classic/busline/persistence/definitions/persistenceTypes.ts'

export type { PanelContentState }
import { persistenceStore } from '@/core/classic/busline/persistence/services/persistenceStore.ts'

//// PersistenceSchema
// 保留旧类型定义供未迁移的调用方引用
type PersistenceSchema = {
  layout: {
    swapped: boolean
    sidebarVisible: boolean
    userLanguage: string
    layoutSwapped: boolean
    hasPlan: boolean
  }
  cards: {
    pinned: Record<string, boolean>
    expanded: Record<string, boolean>
    order: number[]
  }
  planCards: {
    pinned: Record<string, boolean>
    order: number[]
  }
  plans: {
    plan_manage: {
      currentModule: 'planManage' | 'welcome' | 'settings'
      modules: {
        [module in 'planManage' | 'welcome' | 'settings']?: PanelContentState
      }
    }
    [planKey: `plan_${number}`]: {
      currentModuleId: 'planDashboard' | number
      modules: {
        [moduleId: string]: PanelContentState
      }
    }
  }
}

//// usePersistence — 委托到新的 persistenceStore
export function usePersistence() {
  return {
    getPersistence: persistenceStore.get.bind(persistenceStore),
    setPersistence: persistenceStore.set.bind(persistenceStore),
  }
}
