import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { riskModuleFlowManager } from '@/features/agile/modules/risk/flows/riskFlowManager.ts'

export const riskModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'risk',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/risk/components/RiskMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/risk/components/RiskSub.vue')
  ),
  displayMode: 7,
  flowManager: riskModuleFlowManager
}
