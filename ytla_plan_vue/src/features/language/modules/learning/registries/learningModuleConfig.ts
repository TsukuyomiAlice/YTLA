import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { learningModuleFlowManager } from '@/features/language/modules/learning/flows/learningFlowManager.ts'

export const learningModuleConfig = <ModuleRegistry> {
  moduleType: 'language',
  moduleSubType: 'learning',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/learning/components/LearningMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/learning/components/LearningSub.vue')
  ),
  displayMode: 7,
  flowManager: learningModuleFlowManager
}
