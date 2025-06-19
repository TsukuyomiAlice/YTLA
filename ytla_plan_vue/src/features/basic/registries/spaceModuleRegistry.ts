import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { spaceModuleFlowManager } from '@/features/basic/flows/spaceFlowManager'

createModuleRegistry('space', {
  moduleType: 'basic',
  moduleSubType: 'space',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/space/SpaceMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/space/SpaceSub.vue')
  ),
  displayMode: 3,
  flowManager: spaceModuleFlowManager
})
