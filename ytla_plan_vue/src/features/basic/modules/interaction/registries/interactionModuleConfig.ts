import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { interactionModuleFlowManager } from '@/features/basic/modules/interaction/flows/interactionFlowManager.ts'

export const interactionModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'interaction',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/interaction/components/InteractionMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/modules/interaction/components/InteractionSub.vue')
  ),
  displayMode: 3,
  flowManager: interactionModuleFlowManager
}
