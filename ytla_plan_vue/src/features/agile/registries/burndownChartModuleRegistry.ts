import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { burndownChartModuleFlowManager } from '@/features/agile/flows/burndownChartFlowManager'

createModuleRegistry('burndownChart', {
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
})
