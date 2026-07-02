import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { data_managerModuleFlowManager } from '@/features/data_power/modules/data_manager/flows/data_managerFlowManager'

export const data_managerModuleConfig = <ModuleRegistry> {
  moduleType: 'data_power',
  moduleSubType: 'data_manager',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_manager/components/Data_managerMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/data_power/modules/data_manager/components/Data_managerSub.vue')
  ),
  displayMode: 7,
  flowManager: data_managerModuleFlowManager
}
