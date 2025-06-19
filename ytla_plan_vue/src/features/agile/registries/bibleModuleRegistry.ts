import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { bibleModuleFlowManager } from '@/features/agile/flows/bibleModuleFlowManager.ts'

createModuleRegistry('bible', {
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
})
