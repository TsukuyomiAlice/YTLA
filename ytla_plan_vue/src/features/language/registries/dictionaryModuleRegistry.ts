import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { dictionaryModuleFlowManager } from '@/features/language/flows/dictionaryFlowManager'

createModuleRegistry('dictionary', {
  moduleType: 'language',
  moduleSubType: 'dictionary',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/dictionary/DictionaryMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/dictionary/DictionarySub.vue')
  ),
  displayMode: 7,
  flowManager: dictionaryModuleFlowManager
})
