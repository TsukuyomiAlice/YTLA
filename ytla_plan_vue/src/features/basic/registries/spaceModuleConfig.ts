import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { spaceModuleFlowManager } from '@/features/basic/flows/spaceFlowManager'

export const spaceModuleConfig = <ModuleRegistry> {
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
}
