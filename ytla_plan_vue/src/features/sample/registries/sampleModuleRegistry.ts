import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { sampleModuleFlowManager } from '@/features/sample/flows/sampleModuleFlowManager.ts'

createModuleRegistry('sample', {
  moduleType: 'sample',
  moduleSubType: 'sample',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/sample/components/modules/sample/Sample.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/sample/components/modules/sample/SampleSub.vue')
  ),
  displayMode: 7,
  flowManager: sampleModuleFlowManager,
})
