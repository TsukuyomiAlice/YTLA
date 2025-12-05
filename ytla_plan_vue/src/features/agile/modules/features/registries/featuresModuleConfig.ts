import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { featuresModuleFlowManager } from '@/features/agile/modules/features/flows/featuresFlowManager.ts'

export const featuresModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'features',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/features/components/FeaturesMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/features/components/FeaturesSub.vue')
  ),
  displayMode: 7,
  flowManager: featuresModuleFlowManager
}
