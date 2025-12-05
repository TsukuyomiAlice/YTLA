import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { kanbanModuleFlowManager } from '@/features/agile/modules/kanban/flows/kanbanModuleFlowManager.ts'

export const kanbanModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'kanban',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/kanban/components/KanbanMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/kanban/components/KanbanSub.vue')
  ),
  displayMode: 3,
  flowManager: kanbanModuleFlowManager
}
