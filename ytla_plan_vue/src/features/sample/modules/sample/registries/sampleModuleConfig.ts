import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { sampleModuleFlowManager } from '@/features/sample/modules/_type/flows/sampleModuleFlowManager.ts'

export const sampleModuleConfig = <ModuleRegistry> {
  moduleType: 'sample',
  moduleSubType: 'sample',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/sample/modules/sample/components/Sample.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/sample/modules/sample/components/SampleSub.vue')
  ),
  displayMode: 7,
  flowManager: sampleModuleFlowManager,
}
