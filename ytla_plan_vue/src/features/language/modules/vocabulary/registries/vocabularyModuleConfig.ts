import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { vocabularyModuleFlowManager } from '@/features/language/modules/vocabulary/flows/vocabularyFlowManager.ts'

export const vocabularyModuleConfig = <ModuleRegistry> {
  moduleType: 'language',
  moduleSubType: 'vocabulary',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/vocabulary/components/VocabularyMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/vocabulary/components/VocabularySub.vue')
  ),
  displayMode: 7,
  flowManager: vocabularyModuleFlowManager
}
