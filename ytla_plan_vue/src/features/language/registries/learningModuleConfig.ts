import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { learningModuleFlowManager } from '@/features/language/flows/learningFlowManager'

export const learningModuleConfig = <ModuleRegistry> {
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
}
