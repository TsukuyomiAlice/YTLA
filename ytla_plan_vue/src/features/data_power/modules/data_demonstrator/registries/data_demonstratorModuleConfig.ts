import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { data_demonstratorModuleFlowManager } from '@/features/data_power/modules/data_demonstrator/flows/data_demonstratorFlowManager'

export const data_demonstratorModuleConfig = <ModuleRegistry> {
  moduleType: 'data_power',
  moduleSubType: 'data_demonstrator',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_demonstrator/components/Data_demonstratorMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_demonstrator/components/Data_demonstratorSub.vue')
  ),
  displayMode: 7,
  flowManager: data_demonstratorModuleFlowManager
}
