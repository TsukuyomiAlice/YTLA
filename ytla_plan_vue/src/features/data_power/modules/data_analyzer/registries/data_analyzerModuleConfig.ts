import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { data_analyzerModuleFlowManager } from '@/features/data_power/modules/data_analyzer/flows/data_analyzerFlowManager'

export const data_analyzerModuleConfig = <ModuleRegistry> {
  moduleType: 'data_power',
  moduleSubType: 'data_analyzer',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_analyzer/components/Data_analyzerMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_analyzer/components/Data_analyzerSub.vue')
  ),
  displayMode: 7,
  flowManager: data_analyzerModuleFlowManager
}
