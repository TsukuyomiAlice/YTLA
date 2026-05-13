import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { fund_infoModuleFlowManager } from '@/features/investment/modules/fund_info/flows/fund_infoFlowManager'

export const fund_infoModuleConfig = <ModuleRegistry> {
  moduleType: 'investment',
  moduleSubType: 'fund_info',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/investment/modules/fund_info/components/Fund_infoMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/investment/modules/fund_info/components/Fund_infoSub.vue')
  ),
  displayMode: 7,
  flowManager: fund_infoModuleFlowManager
}
