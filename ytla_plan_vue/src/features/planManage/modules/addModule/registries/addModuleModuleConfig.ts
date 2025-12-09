import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { addModuleModuleFlowManager } from '@/features/planManage/modules/addModule/flows/addModuleModuleFlowManager.ts'

export const addModuleModuleConfig = <ModuleRegistry> {
  moduleType: 'planManage',
  moduleSubType: 'addModule',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/addModule/components/AddModuleMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/addModule/components/AddModuleSub.vue')
  ),
  displayMode: 7,
  flowManager: addModuleModuleFlowManager,
}
