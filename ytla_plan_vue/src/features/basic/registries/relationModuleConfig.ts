import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { relationModuleFlowManager } from '@/features/basic/flows/relationFlowManager'

export const relationModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'relation',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/relation/RelationMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/relation/RelationSub.vue')
  ),
  displayMode: 3,
  flowManager: relationModuleFlowManager
}
