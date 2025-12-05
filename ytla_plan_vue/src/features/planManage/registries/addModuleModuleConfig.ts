import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { addModuleModuleFlowManager } from '@/features/planManage/flows/addModuleModuleFlowManager.ts'

export const addModuleModuleConfig = <ModuleRegistry> {
  moduleType: 'planManage',
  moduleSubType: 'addModule',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/addModule/AddModuleMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/addModule/AddModuleSub.vue')
  ),
  displayMode: 7,
  flowManager: addModuleModuleFlowManager,
}
