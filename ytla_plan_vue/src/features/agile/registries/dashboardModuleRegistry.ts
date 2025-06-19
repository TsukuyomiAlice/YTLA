import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { dashboardModuleFlowManager } from '@/features/agile/flows/dashboardFlowManager'

createModuleRegistry('dashboard', {
  moduleType: 'agile',
  moduleSubType: 'dashboard',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/dashboard/DashboardMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/dashboard/DashboardSub.vue')
  ),
  displayMode: 7,
  flowManager: dashboardModuleFlowManager
})
