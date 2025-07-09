import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

export const timerModuleConfig = <ModuleRegistry> {
  moduleType: 'timer',
  moduleSubType: 'timer',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/timer/components/modules/timer/TimerMain.vue')),

  displayMode: 3,
}
