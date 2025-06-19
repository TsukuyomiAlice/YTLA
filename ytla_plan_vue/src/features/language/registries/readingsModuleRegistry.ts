import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { readingsModuleFlowManager } from '@/features/language/flows/readingsFlowManager'

createModuleRegistry('readings', {
  moduleType: 'language',
  moduleSubType: 'readings',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/readings/ReadingsMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/readings/ReadingsSub.vue')
  ),
  displayMode: 7,
  flowManager: readingsModuleFlowManager
})
