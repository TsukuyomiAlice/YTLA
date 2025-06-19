import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { relationModuleFlowManager } from '@/features/basic/flows/relationFlowManager'

createModuleRegistry('relation', {
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
})
