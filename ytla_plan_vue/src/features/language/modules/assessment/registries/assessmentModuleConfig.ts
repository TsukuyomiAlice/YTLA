import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { assessmentModuleFlowManager } from '@/features/language/modules/assessment/flows/assessmentFlowManager.ts'

export const assessmentModuleConfig = <ModuleRegistry> {
  moduleType: 'language',
  moduleSubType: 'assessment',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/assessment/components/AssessmentMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/assessment/components/AssessmentSub.vue')
  ),
  displayMode: 7,
  flowManager: assessmentModuleFlowManager
}
