import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { meetingsModuleFlowManager } from '@/features/agile/flows/meetingsFlowManager'

createModuleRegistry('meetings', {
  moduleType: 'agile',
  moduleSubType: 'meetings',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/meetings/MeetingsMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/meetings/MeetingsSub.vue')
  ),
  displayMode: 7,
  flowManager: meetingsModuleFlowManager
})
