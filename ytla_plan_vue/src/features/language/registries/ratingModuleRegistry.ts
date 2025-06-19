import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { ratingModuleFlowManager } from '@/features/language/flows/ratingFlowManager'

createModuleRegistry('rating', {
  moduleType: 'language',
  moduleSubType: 'rating',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/rating/RatingMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/language/components/modules/rating/RatingSub.vue')
  ),
  displayMode: 7,
  flowManager: ratingModuleFlowManager
})
