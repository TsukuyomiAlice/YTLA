import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'
import { navigatorModuleFlowManager } from '@/core/classic/busline/navigator/flows/navigatorFlowManager.ts'

export const navigatorModuleConfig = <ModuleRegistry> {
  moduleType: 'busline',
  moduleSubType: 'navigator',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/core/classic/busline/navigator/components/NavigatorMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/core/classic/busline/navigator/components/NavigatorSub.vue')
  ),
  displayMode: 7,
  flowManager: navigatorModuleFlowManager
}
