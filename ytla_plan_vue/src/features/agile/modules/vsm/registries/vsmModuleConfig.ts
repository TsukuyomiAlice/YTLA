import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { vsmModuleFlowManager } from '@/features/agile/modules/vsm/flows/vsmFlowManager.ts'

export const vsmModuleConfig = <ModuleRegistry> {
  moduleType: 'agile',
  moduleSubType: 'vsm',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/vsm/components/VsmMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/agile/modules/vsm/components/VsmSub.vue')
  ),
  displayMode: 7,
  flowManager: vsmModuleFlowManager
}
