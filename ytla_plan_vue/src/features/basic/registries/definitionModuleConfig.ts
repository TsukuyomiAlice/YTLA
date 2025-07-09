import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { definitionModuleFlowManager } from '@/features/basic/flows/definitionFlowManager'

export const definitionModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'definition',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/definition/DefinitionMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/definition/DefinitionSub.vue')
  ),
  displayMode: 7,
  flowManager: definitionModuleFlowManager
}
