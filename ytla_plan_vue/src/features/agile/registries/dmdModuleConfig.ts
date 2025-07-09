import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { dmdModuleFlowManager } from '@/features/agile/flows/dmdFlowManager'

export const dmdModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'dmd',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/dmd/DmdMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/dmd/DmdSub.vue')
  ),
  displayMode: 7,
  flowManager: dmdModuleFlowManager
}
