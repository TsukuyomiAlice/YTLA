import { ref } from 'vue'
import { getModuleConfig, type ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

//// PanelContentState
export type PanelContentState = {
  displayMode: number
  moduleType: string
  globalFrame: {
    currentStep: number
    componentState: Record<string, unknown>
  }
  mainFrame: {
    currentStep: number
    componentState: Record<string, unknown>
  }
  subFrame: {
    currentStep: number
    componentState: Record<string, unknown>
  }
}

function createDefaultPanelState(moduleType: string): PanelContentState {
  const moduleConfig = getModuleConfig(moduleType) as ModuleRegistry
  const displayMode = moduleConfig?.displayMode || 1
  return {
    displayMode: displayMode,
    moduleType: moduleType,
    globalFrame: { currentStep: 0, componentState: {} },
    mainFrame: { currentStep: 0, componentState: {} },
    subFrame: { currentStep: 0, componentState: {} }
  } as PanelContentState
}

//// PersistenceSchema
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

function createBaseStructure(): PersistenceSchema {
  return {
    layout: {
      swapped: false,
      sidebarVisible: false,
      layoutSwapped: false,
      userLanguage: 'en',
      hasPlan: false
    },
    cards: {
      pinned: {},
      expanded: {},
      order: []
    },
    planCards: {
      pinned: {},
      order: []
    },
    plans: {
      plan_manage: {
        currentModule: 'planManage',
        modules: {
          planManage: createDefaultPanelState('planManage'),
          welcome: createDefaultPanelState('welcome'),
          settings: createDefaultPanelState('settings')
        }
      }
    }
  }
}

//// initStorage
const PERSISTENCE_KEY = 'ytla_persistence'

function initStorage(): PersistenceSchema {
  const raw = localStorage.getItem(PERSISTENCE_KEY)
  if (raw) {
    try {
      return JSON.parse(raw)
    } catch {
      return createBaseStructure()
    }
  }
  return createBaseStructure()
}

//// usePersistence
const storage = ref<PersistenceSchema>(initStorage())

export function usePersistence() {

  const savePersistence = () => {
    localStorage.setItem(PERSISTENCE_KEY, JSON.stringify(storage.value))
  }

  const getPersistence = <K extends keyof PersistenceSchema>(
    module: K,
    key?: keyof PersistenceSchema[K]
  ): any => {
    if (!key) return storage.value[module]
    return storage.value[module][key]
  }

  const setPersistence = <K extends keyof PersistenceSchema>(
    module: K,
    updates: Partial<PersistenceSchema[K]>
  ) => {
    if (module === 'plans') {
      for (const key in updates) {
        if (updates[key as keyof PersistenceSchema[K]] === undefined) {
          delete storage.value[module][key]
        }
      }
    }
    storage.value[module] = { ...storage.value[module], ...updates }
    savePersistence()
  }

  return { getPersistence, setPersistence }
}
