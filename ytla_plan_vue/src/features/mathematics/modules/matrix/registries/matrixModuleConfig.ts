import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { matrixModuleFlowManager } from '@/features/mathematics/modules/matrix/flows/matrixFlowManager'

export const matrixModuleConfig = <ModuleRegistry> {
  moduleType: 'mathematics',
  moduleSubType: 'matrix',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/mathematics/modules/matrix/components/MatrixMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/mathematics/modules/matrix/components/MatrixSub.vue')
  ),
  displayMode: 7,
  flowManager: matrixModuleFlowManager
}
