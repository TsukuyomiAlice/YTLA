import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { assessmentModuleFlowManager } from '@/features/language/flows/assessmentFlowManager'

createModuleRegistry('assessment', {
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
})
