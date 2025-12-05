import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { ganttChartModuleFlowManager } from '@/features/agile/modules/ganttChart/flows/ganttChartFlowManager.ts'

export const ganttChartModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'ganttChart',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/ganttChart/components/GanttChartMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/ganttChart/components/GanttChartSub.vue')
  ),
  displayMode: 7,
  flowManager: ganttChartModuleFlowManager
}
