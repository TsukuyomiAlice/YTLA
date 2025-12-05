import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { burndownChartModuleFlowManager } from '@/features/agile/modules/burndownChart/flows/burndownChartFlowManager.ts'

export const burndownChartModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'burndownChart',
  moduleConcept: 'time',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/burndownChart/components/BurndownChartMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/burndownChart/components/BurndownChartSub.vue')
  ),
  displayMode: 7,
  flowManager: burndownChartModuleFlowManager
}
