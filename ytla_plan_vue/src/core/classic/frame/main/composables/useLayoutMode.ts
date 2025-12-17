import { watchEffect } from 'vue'
import { useLayoutStore } from '@/core/classic/frame/main/services/layoutStore.ts'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'
import { getModuleConfig } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

export function useLayoutMode() {
  const layoutStore = useLayoutStore()
  const panelStore = usePanelStore()

  watchEffect(() => {
    const contentConfig = getModuleConfig(panelStore.activeModuleSubType)
    if (contentConfig?.displayMode) {
      layoutStore.mainContentDisplayMode = contentConfig.displayMode
    } else {
      layoutStore.mainContentDisplayMode = 1
    }
  })
}
