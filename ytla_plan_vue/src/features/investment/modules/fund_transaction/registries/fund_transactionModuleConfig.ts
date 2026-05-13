import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { fund_transactionModuleFlowManager } from '@/features/investment/modules/fund_transaction/flows/fund_transactionFlowManager'

export const fund_transactionModuleConfig = <ModuleRegistry> {
  moduleType: 'investment',
  moduleSubType: 'fund_transaction',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/investment/modules/fund_transaction/components/Fund_transactionMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/investment/modules/fund_transaction/components/Fund_transactionSub.vue')
  ),
  displayMode: 7,
  flowManager: fund_transactionModuleFlowManager
}
