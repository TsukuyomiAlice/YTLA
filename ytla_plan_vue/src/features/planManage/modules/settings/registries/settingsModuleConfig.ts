import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'
import { settingsModuleFlowManager } from '@/features/planManage/modules/settings/flows/settingsFlowManager.ts'

export const settingsModuleConfig = <ModuleRegistry> {
  moduleType: 'planManage',
  moduleSubType: 'settings',
  moduleConcept: 'system',
  mainComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/settings/components/SettingsMain.vue')
  ),
  subComponent: defineAsyncComponent(() =>
    import('@/features/planManage/modules/settings/components/SettingsSub.vue')
  ),
  displayMode: 7,
  flowManager: settingsModuleFlowManager
}
