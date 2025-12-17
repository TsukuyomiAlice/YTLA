import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { timerModuleFlowManager } from '@/features/timer/modules/_type/flows/timerFlowManager.ts'

export const timerModuleConfig = <ModuleRegistry> {
  moduleType: 'timer',
  moduleSubType: 'timer',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/timer/modules/timer/components/TimerMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/timer/modules/timer/components/TimerSub.vue')
  ),
  displayMode: 1,
  flowManager: timerModuleFlowManager
}
