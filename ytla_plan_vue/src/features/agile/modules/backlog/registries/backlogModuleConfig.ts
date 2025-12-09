import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { backlogModuleFlowManager } from '@/features/agile/modules/backlog/flows/backlogFlowManager.ts'

export const backlogModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'backlog',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/backlog/components/BacklogMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/backlog/components/BacklogSub.vue')
  ),
  displayMode: 7,
  flowManager: backlogModuleFlowManager
}
