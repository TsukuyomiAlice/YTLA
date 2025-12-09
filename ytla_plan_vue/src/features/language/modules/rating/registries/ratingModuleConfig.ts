import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { ratingModuleFlowManager } from '@/features/language/modules/rating/flows/ratingFlowManager.ts'

export const ratingModuleConfig = <ModuleRegistry> {
  moduleType: 'language',
  moduleSubType: 'rating',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/rating/components/RatingMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/modules/rating/components/RatingSub.vue')
  ),
  displayMode: 7,
  flowManager: ratingModuleFlowManager
}
