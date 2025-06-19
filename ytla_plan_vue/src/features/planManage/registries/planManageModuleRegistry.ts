import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { planManageModuleFlowManager } from '@/features/planManage/flows/planManageModuleFlowManager.ts'

createModuleRegistry('planManage', {
  moduleType: 'planManage',
  moduleSubType: 'planManage',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/planManager/PlanManagerMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/planManager/PlanManagerSub.vue')
  ),
  displayMode: 7,
  flowManager: planManageModuleFlowManager,
})
