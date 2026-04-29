import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { create_cardModuleFlowManager } from '@/features/scaffold/modules/create_card/flows/create_cardFlowManager'

export const create_cardModuleConfig = <ModuleRegistry> {
  moduleType: 'scaffold',
  moduleSubType: 'create_card',
  moduleConcept: 'create_card',
  mainComponent: defineAsyncComponent(() => 
    import('@/features/scaffold/modules/create_card/components/Create_cardMain.vue')
  ),
  subComponent: defineAsyncComponent(() => 
    import('@/features/scaffold/modules/create_card/components/Create_cardSub.vue')
  ),
  displayMode: 7,
  flowManager: create_cardModuleFlowManager
}
