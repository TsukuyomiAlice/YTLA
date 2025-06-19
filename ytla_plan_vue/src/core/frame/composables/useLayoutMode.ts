import { watchEffect } from 'vue'
import { useLayoutStore } from '@/core/frame/services/layoutStore.ts'
import { usePanelStore } from '@/core/frame/services/panelStore.ts'
import { getModuleConfig } from '@/core/modules/registries/moduleRegistry.ts'

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
