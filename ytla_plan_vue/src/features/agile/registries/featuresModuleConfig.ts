import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { featuresModuleFlowManager } from '@/features/agile/flows/featuresFlowManager'

export const featuresModuleConfig = <ModuleRegistry> {
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
}
