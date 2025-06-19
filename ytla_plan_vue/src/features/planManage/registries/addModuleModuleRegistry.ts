import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { addModuleModuleFlowManager } from '@/features/planManage/flows/addModuleModuleFlowManager.ts'

createModuleRegistry('addModule', {
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

})
