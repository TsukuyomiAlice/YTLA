import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { eight_charactersModuleFlowManager } from '@/features/divination/modules/eight_characters/flows/eight_charactersFlowManager'

export const eight_charactersModuleConfig = <ModuleRegistry> {
  moduleType: 'divination',
  moduleSubType: 'eight_characters',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/divination/modules/eight_characters/components/Eight_charactersMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/divination/modules/eight_characters/components/Eight_charactersSub.vue')
  ),
  displayMode: 5,
  flowManager: eight_charactersModuleFlowManager
}
