import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { meetingsModuleFlowManager } from '@/features/agile/flows/meetingsFlowManager'

export const meetingsModuleConfig = <ModuleRegistry> {
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
}
