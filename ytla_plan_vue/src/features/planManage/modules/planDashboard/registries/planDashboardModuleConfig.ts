import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { planDashboardModuleFlowManager } from '@/features/planManage/modules/planDashboard/flows/planDashboardModuleFlowManager.ts'

export const planDashboardModuleConfig = <ModuleRegistry> {
  moduleType: 'planManage',
  moduleSubType: 'planDashboard',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/planDashboard/components/PlanDashboardMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/planDashboard/components/PlanDashboardSub.vue')
  ),
  displayMode: 7,
  flowManager: planDashboardModuleFlowManager,
}
