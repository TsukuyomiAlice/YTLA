import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { timerModuleFlowManager } from '@/features/timer/flows/timerFlowManager'

export const timerModuleConfig = <ModuleRegistry> {
  moduleType: 'timer',
  moduleSubType: 'timer',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/timer/components/modules/timer/TimerMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/timer/components/modules/timer/TimerSub.vue')
  ),
  displayMode: 1,
  flowManager: timerModuleFlowManager
}
