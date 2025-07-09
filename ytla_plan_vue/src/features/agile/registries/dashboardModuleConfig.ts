import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { dashboardModuleFlowManager } from '@/features/agile/flows/dashboardFlowManager'

export const dashboardModuleConfig = <ModuleRegistry> {
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
}
