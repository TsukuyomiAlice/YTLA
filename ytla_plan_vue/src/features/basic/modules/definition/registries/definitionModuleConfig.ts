import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { definitionModuleFlowManager } from '@/features/basic/modules/definition/flows/definitionFlowManager.ts'

export const definitionModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'definition',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/definition/components/DefinitionMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/definition/components/DefinitionSub.vue')
  ),
  displayMode: 7,
  flowManager: definitionModuleFlowManager
}
