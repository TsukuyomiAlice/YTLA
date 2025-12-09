import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { userStoryModuleFlowManager } from '@/features/agile/modules/userStory/flows/userStoryFlowManager.ts'

export const userStoryModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'userStory',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/userStory/components/UserStoryMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/userStory/components/UserStorySub.vue')
  ),
  displayMode: 7,
  flowManager: userStoryModuleFlowManager
}
