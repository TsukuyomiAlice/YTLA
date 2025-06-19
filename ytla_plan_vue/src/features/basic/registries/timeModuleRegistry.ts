import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { timeModuleFlowManager } from '@/features/basic/flows/timeFlowManager'

createModuleRegistry('time', {
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
})
