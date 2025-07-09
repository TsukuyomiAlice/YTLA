import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { vsmModuleFlowManager } from '@/features/agile/flows/vsmFlowManager'

export const vsmModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'vsm',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/vsm/VsmMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/components/modules/vsm/VsmSub.vue')
  ),
  displayMode: 7,
  flowManager: vsmModuleFlowManager
}
