import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { plum_yiModuleFlowManager } from '@/features/divination/modules/plum_yi/flows/plum_yiFlowManager'

export const plum_yiModuleConfig = <ModuleRegistry> {
  moduleType: 'divination',
  moduleSubType: 'plum_yi',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/divination/modules/plum_yi/components/Plum_yiMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/divination/modules/plum_yi/components/Plum_yiSub.vue')
  ),
  displayMode: 7,
  flowManager: plum_yiModuleFlowManager
}
