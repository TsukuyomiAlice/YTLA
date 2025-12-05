import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { meetingsModuleFlowManager } from '@/features/agile/modules/meetings/flows/meetingsFlowManager.ts'

export const meetingsModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'meetings',
  moduleConcept: 'interaction',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/meetings/components/MeetingsMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/meetings/components/MeetingsSub.vue')
  ),
  displayMode: 7,
  flowManager: meetingsModuleFlowManager
}
