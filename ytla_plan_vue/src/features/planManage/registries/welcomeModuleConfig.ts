import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { welcomeModuleFlowManager } from '@/features/planManage/flows/welcomeModuleFlowManager.ts'

export const welcomeModuleConfig = <ModuleRegistry> {
  moduleType: 'planManage',
  moduleSubType: 'welcome',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/welcome/WelcomePageMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/welcome/WelcomePageSub.vue')
  ),
  displayMode: 7,
  flowManager: welcomeModuleFlowManager,
}
