import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'

createModuleRegistry('timer', {
  moduleType: 'timer',
  moduleSubType: 'timer',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/timer/components/modules/timer/TimerContent.vue')),

  displayMode: 3,
})
