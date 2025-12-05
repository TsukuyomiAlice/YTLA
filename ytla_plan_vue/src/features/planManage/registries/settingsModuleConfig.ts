import { defineAsyncComponent } from 'vue'
import type { ModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'
import { settingsModuleFlowManager } from '@/features/planManage/flows/settingsFlowManager'

export const settingsModuleConfig = <ModuleRegistry> {
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
}
