import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { connectionModuleFlowManager } from '@/features/workshop/modules/connection/flows/connectionFlowManager.ts'

export const connectionModuleConfig = <ModuleRegistry> {
  moduleType: 'workshop',
  moduleSubType: 'connection',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/workshop/modules/connection/components/ConnectionMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/workshop/modules/connection/components/ConnectionSub.vue')
  ),
  displayMode: 7,
  flowManager: connectionModuleFlowManager
}
