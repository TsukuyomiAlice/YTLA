import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { kanbanModuleFlowManager } from '@/features/agile/flows/kanbanModuleFlowManager.ts'

createModuleRegistry('kanban', {
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
})
