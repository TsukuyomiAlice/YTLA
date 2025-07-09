import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { kanbanModuleFlowManager } from '@/features/agile/flows/kanbanModuleFlowManager.ts'

export const kanbanModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'kanban',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/kanban/KanbanMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/kanban/KanbanSub.vue')
  ),
  displayMode: 3,
  flowManager: kanbanModuleFlowManager
}
