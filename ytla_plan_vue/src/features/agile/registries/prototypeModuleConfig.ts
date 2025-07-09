import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { prototypeModuleFlowManager } from '@/features/agile/flows/prototypeFlowManager'

export const prototypeModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'prototype',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/prototype/PrototypeMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/prototype/PrototypeSub.vue')
  ),
  displayMode: 7,
  flowManager: prototypeModuleFlowManager
}
