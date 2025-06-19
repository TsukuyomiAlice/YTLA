import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import {
  whiteboardModuleFlowManager
} from '@/features/agile/flows/whiteboardModuleFlowManager.ts'

createModuleRegistry('whiteboard', {
  moduleType: 'agile',
  moduleSubType: 'whiteboard',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/whiteboard/WhiteboardMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/whiteboard/WhiteboardSub.vue')
  ),
  displayMode: 3,
  flowManager: whiteboardModuleFlowManager
})
