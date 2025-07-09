import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { riskModuleFlowManager } from '@/features/agile/flows/riskFlowManager'

export const riskModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'risk',
  moduleConcept: 'relation',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/risk/RiskMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/risk/RiskSub.vue')
  ),
  displayMode: 7,
  flowManager: riskModuleFlowManager
}
