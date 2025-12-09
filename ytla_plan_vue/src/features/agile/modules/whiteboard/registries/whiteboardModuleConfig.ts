import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { whiteboardModuleFlowManager } from '@/features/agile/modules/whiteboard/flows/whiteboardModuleFlowManager.ts'

export const whiteboardModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'whiteboard',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/whiteboard/components/WhiteboardMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/whiteboard/components/WhiteboardSub.vue')
  ),
  displayMode: 3,
  flowManager: whiteboardModuleFlowManager
}
