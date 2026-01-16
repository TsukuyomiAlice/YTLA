import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { dictionaryModuleFlowManager } from '@/features/language/modules/dictionary/flows/dictionaryFlowManager.ts'

export const dictionaryModuleConfig = <ModuleRegistry> {
  moduleType: 'language',
  moduleSubType: 'dictionary',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/dictionary/components/DictionaryMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/dictionary/components/DictionarySub.vue')
  ),
  displayMode: 7,
  flowManager: dictionaryModuleFlowManager
}
