import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { plumYiModuleFlowManager } from '@/features/divination/flows/plumYiFlowManager'

createModuleRegistry('plumYi', {
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
})
