import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { functionModuleFlowManager } from '@/features/workshop/modules/function/flows/functionFlowManager.ts'

export const functionModuleConfig = <ModuleRegistry> {
  moduleType: 'workshop',
  moduleSubType: 'function',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/workshop/modules/function/components/FunctionMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/workshop/modules/function/components/FunctionSub.vue')
  ),
  displayMode: 7,
  flowManager: functionModuleFlowManager
}
