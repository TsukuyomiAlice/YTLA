import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { backlogModuleFlowManager } from '@/features/agile/flows/backlogFlowManager'

createModuleRegistry('backlog', {
  moduleType: 'agile',
  moduleSubType: 'backlog',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/backlog/BacklogMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/backlog/BacklogSub.vue')
  ),
  displayMode: 7,
  flowManager: backlogModuleFlowManager
})
