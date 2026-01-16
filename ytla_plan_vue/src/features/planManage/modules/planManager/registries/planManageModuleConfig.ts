import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { planManageModuleFlowManager } from '@/features/planManage/modules/planManager/flows/planManageModuleFlowManager.ts'

export const planManageModuleConfig = <ModuleRegistry> {
  moduleType: 'planManage',
  moduleSubType: 'planManager',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/planManager/components/PlanManagerMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/planManager/components/PlanManagerSub.vue')
  ),
  displayMode: 7,
  flowManager: planManageModuleFlowManager,
}
