import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { plumYiModuleFlowManager } from '@/features/divination/modules/plumYi/flows/plumYiFlowManager.ts'

export const plumYiModuleConfig = <ModuleRegistry> {
  moduleType: 'divination',
  moduleSubType: 'plumYi',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/divination/modules/plumYi/components/PlumYiMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/divination/modules/plumYi/components/PlumYiSub.vue')
  ),
  displayMode: 7,
  flowManager: plumYiModuleFlowManager
}
