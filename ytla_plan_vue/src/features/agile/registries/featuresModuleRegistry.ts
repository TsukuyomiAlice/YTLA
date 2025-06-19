import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { featuresModuleFlowManager } from '@/features/agile/flows/featuresFlowManager'

createModuleRegistry('features', {
  moduleType: 'agile',
  moduleSubType: 'features',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/features/FeaturesMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/features/FeaturesSub.vue')
  ),
  displayMode: 7,
  flowManager: featuresModuleFlowManager
})
