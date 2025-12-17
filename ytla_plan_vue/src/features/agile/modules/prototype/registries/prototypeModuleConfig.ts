import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { prototypeModuleFlowManager } from '@/features/agile/modules/prototype/flows/prototypeFlowManager.ts'

export const prototypeModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'prototype',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/prototype/components/PrototypeMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/prototype/components/PrototypeSub.vue')
  ),
  displayMode: 7,
  flowManager: prototypeModuleFlowManager
}
