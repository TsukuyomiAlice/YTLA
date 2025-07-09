import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { sphereModuleFlowManager } from '@/features/mathematics/flows/sphereFlowManager'

createModuleRegistry('sphere', {
  moduleType: 'mathematics',
  moduleSubType: 'sphere',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/mathematics/components/modules/sphere/SphereMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/mathematics/components/modules/sphere/SphereSub.vue')
  ),
  displayMode: 7,
  flowManager: sphereModuleFlowManager
})
