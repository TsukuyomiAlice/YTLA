import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { matrixModuleFlowManager } from '@/features/mathematics/flows/matrixFlowManager'

export const matrixModuleConfig = <ModuleRegistry> {
  moduleType: 'mathematics',
  moduleSubType: 'matrix',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/mathematics/components/modules/matrix/MatrixMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/mathematics/components/modules/matrix/MatrixSub.vue')
  ),
  displayMode: 7,
  flowManager: matrixModuleFlowManager
}
