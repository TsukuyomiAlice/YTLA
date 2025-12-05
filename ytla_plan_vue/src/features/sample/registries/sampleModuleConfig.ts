import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { sampleModuleFlowManager } from '@/features/sample/flows/sampleModuleFlowManager.ts'

export const sampleModuleConfig = <ModuleRegistry> {
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
}
