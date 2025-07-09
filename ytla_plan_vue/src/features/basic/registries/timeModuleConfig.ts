import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { timeModuleFlowManager } from '@/features/basic/flows/timeFlowManager'

export const timeModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'time',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/time/TimeMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/time/TimeSub.vue')
  ),
  displayMode: 3,
  flowManager: timeModuleFlowManager
}
