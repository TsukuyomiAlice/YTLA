import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { ganttChartModuleFlowManager } from '@/features/agile/flows/ganttChartFlowManager'

export const ganttChartModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'ganttChart',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/ganttChart/GanttChartMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/ganttChart/GanttChartSub.vue')
  ),
  displayMode: 7,
  flowManager: ganttChartModuleFlowManager
}
