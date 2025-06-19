import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { prototypeModuleFlowManager } from '@/features/agile/flows/prototypeFlowManager'

createModuleRegistry('prototype', {
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
})
