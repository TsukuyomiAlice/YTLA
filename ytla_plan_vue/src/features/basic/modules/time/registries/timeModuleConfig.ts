import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { timeModuleFlowManager } from '@/features/basic/modules/time/flows/timeFlowManager.ts'

export const timeModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'time',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/time/components/TimeMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/time/components/TimeSub.vue')
  ),
  displayMode: 3,
  flowManager: timeModuleFlowManager
}
