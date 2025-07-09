import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { burndownChartModuleFlowManager } from '@/features/agile/flows/burndownChartFlowManager'

export const burndownChartModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'burndownChart',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/burndownChart/BurndownChartMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/burndownChart/BurndownChartSub.vue')
  ),
  displayMode: 7,
  flowManager: burndownChartModuleFlowManager
}
