import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'
import { welcomeModuleFlowManager } from '@/features/planManage/modules/welcome/flows/welcomeModuleFlowManager.ts'

export const welcomeModuleConfig = <ModuleRegistry> {
  moduleType: 'planManage',
  moduleSubType: 'welcome',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/welcome/components/WelcomePageMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/welcome/components/WelcomePageSub.vue')
  ),
  displayMode: 7,
  flowManager: welcomeModuleFlowManager,
}
