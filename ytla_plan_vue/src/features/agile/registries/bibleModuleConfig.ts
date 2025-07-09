import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { bibleModuleFlowManager } from '@/features/agile/flows/bibleModuleFlowManager.ts'

export const bibleModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'bible',
  moduleConcept: 'definition',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/bible/BibleMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/bible/BibleSub.vue')
  ),
  displayMode: 7,
  flowManager: bibleModuleFlowManager
}
