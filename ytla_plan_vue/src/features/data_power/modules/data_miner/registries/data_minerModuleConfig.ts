import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { data_minerModuleFlowManager } from '@/features/data_power/modules/data_miner/flows/data_minerFlowManager'

export const data_minerModuleConfig = <ModuleRegistry> {
  moduleType: 'data_power',
  moduleSubType: 'data_miner',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_miner/components/Data_minerMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_miner/components/Data_minerSub.vue')
  ),
  displayMode: 7,
  flowManager: data_minerModuleFlowManager
}
