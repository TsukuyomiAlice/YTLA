import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { relationModuleFlowManager } from '@/features/basic/modules/relation/flows/relationFlowManager.ts'

export const relationModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'relation',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/relation/components/RelationMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/relation/components/RelationSub.vue')
  ),
  displayMode: 3,
  flowManager: relationModuleFlowManager
}
