import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { learningModuleFlowManager } from '@/features/language/flows/learningFlowManager'

createModuleRegistry('learning', {
  moduleType: 'language',
  moduleSubType: 'learning',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/learning/LearningMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/learning/LearningSub.vue')
  ),
  displayMode: 7,
  flowManager: learningModuleFlowManager
})
