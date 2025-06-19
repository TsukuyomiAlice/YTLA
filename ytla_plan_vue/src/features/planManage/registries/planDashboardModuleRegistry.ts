import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { planDashboardModuleFlowManager } from '@/features/planManage/flows/planDashboardModuleFlowManager.ts'

createModuleRegistry('planDashboard', {
  moduleType: 'planManage',
  moduleSubType: 'planDashboard',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/planDashboard/PlanDashboardMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/planDashboard/PlanDashboardSub.vue')
  ),
  displayMode: 7,
  flowManager: planDashboardModuleFlowManager,
})
