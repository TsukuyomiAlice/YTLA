import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { assessmentModuleFlowManager } from '@/features/language/flows/assessmentFlowManager'

export const assessmentModuleConfig = <ModuleRegistry> {
  moduleType: 'language',
  moduleSubType: 'assessment',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/assessment/AssessmentMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/assessment/AssessmentSub.vue')
  ),
  displayMode: 7,
  flowManager: assessmentModuleFlowManager
}
