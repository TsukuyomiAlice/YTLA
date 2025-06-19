import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'
import { defineAsyncComponent } from 'vue'
import { settingsModuleFlowManager } from '@/features/planManage/flows/settingsFlowManager'

createModuleRegistry('settings', {
  moduleType: 'planManage',
  moduleSubType: 'settings',
  moduleConcept: 'space',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/settings/SettingsMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/components/modules/settings/SettingsSub.vue')
  ),
  displayMode: 7,
  flowManager: settingsModuleFlowManager
})
