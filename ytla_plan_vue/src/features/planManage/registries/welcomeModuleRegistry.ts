import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { welcomeModuleFlowManager } from '@/features/planManage/flows/welcomeModuleFlowManager.ts'

createModuleRegistry('welcome', {
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
})
