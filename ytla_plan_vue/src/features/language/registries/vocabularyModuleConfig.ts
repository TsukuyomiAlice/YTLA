import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { vocabularyModuleFlowManager } from '@/features/language/flows/vocabularyFlowManager'

export const vocabularyModuleConfig = <ModuleRegistry> {
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
}
