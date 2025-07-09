import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { backlogModuleFlowManager } from '@/features/agile/flows/backlogFlowManager'

export const backlogModuleConfig = <ModuleRegistry> {
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
}
