import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { definitionModuleFlowManager } from '@/features/basic/flows/definitionFlowManager'

createModuleRegistry('definition', {
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
})
