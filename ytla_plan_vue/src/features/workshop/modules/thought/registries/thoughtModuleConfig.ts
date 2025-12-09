import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { thoughtModuleFlowManager } from '@/features/workshop/modules/thought/flows/thoughtFlowManager.ts'

export const thoughtModuleConfig = <ModuleRegistry> {
  moduleType: 'workshop',
  moduleSubType: 'thought',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/workshop/modules/thought/components/ThoughtMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/workshop/modules/thought/components/ThoughtSub.vue')
  ),
  displayMode: 7,
  flowManager: thoughtModuleFlowManager
}
