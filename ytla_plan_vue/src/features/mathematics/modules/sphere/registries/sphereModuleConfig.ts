import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { sphereModuleFlowManager } from '@/features/mathematics/modules/sphere/flows/sphereFlowManager'

export const sphereModuleConfig = <ModuleRegistry> {
  moduleType: 'mathematics',
  moduleSubType: 'sphere',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/mathematics/modules/sphere/components/SphereMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/mathematics/modules/sphere/components/SphereSub.vue')
  ),
  displayMode: 7,
  flowManager: sphereModuleFlowManager
}
