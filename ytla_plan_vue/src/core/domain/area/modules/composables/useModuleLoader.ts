import { usePanelStore } from '@/core/domain/area/frame/services/panelStore.ts'
import { getModuleConfig } from '@/core/domain/area/modules/registries/moduleRegistry.ts'

export function useModuleLoader() {
  const panelStore = usePanelStore()

  const loadModule = async (panel: string, moduleId: 'planManage' | 'welcome' | 'settings' | 'planDashboard' | 'addModule' | number) => {

    panelStore.persistCurrentModule()

    try {
      // 判断模块类型
      const moduleType = !isNaN(Number(moduleId))  ?  panelStore.activeModuleSubType : moduleId

      panelStore.switchPanel(panel, moduleId, moduleType as string)

      // 获取模块配置
      const config = getModuleConfig(moduleType as string)

      // 初始化框架状态
      if (!panelStore.contentStates.get(panel)?.has(moduleId.toString())) {
        const currentStep = panelStore.getFrameStep(panel, moduleId.toString(), 'main')

        panelStore.updateFrameState('main', {
          step: currentStep,
          state: {
            displayMode: config?.displayMode || 1,
            moduleType  // 注入模块类型信息
          }
        })

        const subStep = panelStore.getFrameStep(panel, moduleId.toString(), 'sub')
        panelStore.updateFrameState('sub', {
          step: subStep
        })
      }
    } catch (error) {
      console.error('Module loading failed:', error)
      panelStore.switchPanel('plan_manage', 'planManage')
      throw error
    }
  }

  return { loadModule }
}
