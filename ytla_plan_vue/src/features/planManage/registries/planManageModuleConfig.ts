import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { planManageModuleFlowManager } from '@/features/planManage/flows/planManageModuleFlowManager.ts'

export const planManageModuleConfig = <ModuleRegistry> {
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
}
