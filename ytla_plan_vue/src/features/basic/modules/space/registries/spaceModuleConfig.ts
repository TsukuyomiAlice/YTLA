import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { spaceModuleFlowManager } from '@/features/basic/modules/space/flows/spaceFlowManager.ts'

export const spaceModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'space',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/space/components/SpaceMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/space/components/SpaceSub.vue')
  ),
  displayMode: 3,
  flowManager: spaceModuleFlowManager
}
