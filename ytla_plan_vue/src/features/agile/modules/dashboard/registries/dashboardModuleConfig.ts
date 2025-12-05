import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { dashboardModuleFlowManager } from '@/features/agile/modules/dashboard/flows/dashboardFlowManager.ts'

export const dashboardModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'dashboard',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/dashboard/components/DashboardMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/dashboard/components/DashboardSub.vue')
  ),
  displayMode: 7,
  flowManager: dashboardModuleFlowManager
}
