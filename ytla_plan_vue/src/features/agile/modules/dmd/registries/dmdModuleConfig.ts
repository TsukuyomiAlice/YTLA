import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { dmdModuleFlowManager } from '@/features/agile/modules/dmd/flows/dmdFlowManager.ts'

export const dmdModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'dmd',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/dmd/components/DmdMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/dmd/components/DmdSub.vue')
  ),
  displayMode: 7,
  flowManager: dmdModuleFlowManager
}
