import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { userStoryModuleFlowManager } from '@/features/agile/flows/userStoryFlowManager'

export const userStoryModuleConfig = <ModuleRegistry> {
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
}
