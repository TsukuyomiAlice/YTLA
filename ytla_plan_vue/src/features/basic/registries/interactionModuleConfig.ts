import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { interactionModuleFlowManager } from '@/features/basic/flows/interactionFlowManager'

export const interactionModuleConfig = <ModuleRegistry> {
  moduleType: 'basic',
  moduleSubType: 'interaction',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/interaction/InteractionMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/basic/components/modules/interaction/InteractionSub.vue')
  ),
  displayMode: 3,
  flowManager: interactionModuleFlowManager
}
