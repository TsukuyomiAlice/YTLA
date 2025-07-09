import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { readingsModuleFlowManager } from '@/features/language/flows/readingsFlowManager'

export const readingsModuleConfig = <ModuleRegistry> {
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
}
