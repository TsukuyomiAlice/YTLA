import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { plumYiModuleFlowManager } from '@/features/divination/flows/plumYiFlowManager'

export const plumYiModuleConfig = <ModuleRegistry> {
  moduleType: 'divination',
  moduleSubType: 'plumYi',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/divination/components/modules/plumYi/PlumYiMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/divination/components/modules/plumYi/PlumYiSub.vue')
  ),
  displayMode: 7,
  flowManager: plumYiModuleFlowManager
}
