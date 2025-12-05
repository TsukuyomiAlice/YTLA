import { watchEffect } from 'vue'
import { useLayoutStore } from '@/core/frame/_type/services/layoutStore.ts'
import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'
import { getModuleConfig } from '@/core/modules/_type/registries/moduleRegistry.ts'

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
