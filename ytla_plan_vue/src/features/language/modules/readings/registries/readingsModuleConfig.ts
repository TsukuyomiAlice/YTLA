import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { readingsModuleFlowManager } from '@/features/language/modules/readings/flows/readingsFlowManager.ts'

export const readingsModuleConfig = <ModuleRegistry> {
  moduleType: 'language',
  moduleSubType: 'readings',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/readings/components/ReadingsMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/readings/components/ReadingsSub.vue')
  ),
  displayMode: 7,
  flowManager: readingsModuleFlowManager
}
