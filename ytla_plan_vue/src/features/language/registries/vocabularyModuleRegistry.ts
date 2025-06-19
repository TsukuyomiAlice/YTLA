import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { vocabularyModuleFlowManager } from '@/features/language/flows/vocabularyFlowManager'

createModuleRegistry('vocabulary', {
  moduleType: 'language',
  moduleSubType: 'vocabulary',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/vocabulary/VocabularyMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/vocabulary/VocabularySub.vue')
  ),
  displayMode: 7,
  flowManager: vocabularyModuleFlowManager
})
