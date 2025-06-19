import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { userStoryModuleFlowManager } from '@/features/agile/flows/userStoryFlowManager'

createModuleRegistry('userStory', {
  moduleType: 'agile',
  moduleSubType: 'userStory',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/userStory/UserStoryMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/userStory/UserStorySub.vue')
  ),
  displayMode: 7,
  flowManager: userStoryModuleFlowManager
})
