import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { create_moduleModuleFlowManager } from '@/features/scaffold/modules/create_module/flows/create_moduleFlowManager'

export const create_moduleModuleConfig = <ModuleRegistry> {
  moduleType: 'scaffold',
  moduleSubType: 'create_module',
  moduleConcept: 'create_module',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/scaffold/modules/create_module/components/Create_moduleMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/scaffold/modules/create_module/components/Create_moduleSub.vue')
  ),
  displayMode: 7,
  flowManager: create_moduleModuleFlowManager
}
