import { shallowReactive, watch } from 'vue'
import { defineStore } from 'pinia'
import { usePlanCardStore } from '@/features/planManage/stores/planCardStore.ts'
import { getModuleConfig } from '@/core/modules/_type/registries/moduleRegistry.ts'

import { type PanelContentState, usePersistence } from '@/core/frame/_type/composables/usePersistence.ts'
import { useModuleCardStore } from '@/features/planManage/stores/moduleCardStore.ts'

const { getPersistence, setPersistence } = usePersistence()

export const usePanelStore = defineStore('panel', {
  state: () => ({
    contentStates: shallowReactive(new Map<string, Map<string, PanelContentState>>()),

    activePanel: 'plan_manage',
    activeModuleId: 'planManage',
    activeModuleSubType: 'planManage'
  }),

  actions: {
    // 初始化面板模块状态
    initializeModuleState(panel: string, moduleIdentifier: any) {
      if (!this.contentStates.has(panel)) {
        this.contentStates.set(panel, new Map())
      }
      const panelModules = this.contentStates.get(panel)!
      if (!panelModules.has(moduleIdentifier)) {
        panelModules.set(moduleIdentifier, this.loadPersistedState(panel, moduleIdentifier))
      }
    },

    // 加载持久化状态
    loadPersistedState(panel: string, moduleIdentifier: any): PanelContentState {
      const moduleConfig = getModuleConfig(this.activeModuleSubType)
      const defaultState = {
        displayMode: moduleConfig?.displayMode || 1,
        moduleType: this.activeModuleSubType,
        globalFrame: { currentStep: 0, componentState: {} },
        mainFrame: { currentStep: 0, componentState: {} },
        subFrame: { currentStep: 0, componentState: {} }
      }

      // 处理计划管理模块
      if (panel === 'plan_manage') {
        const persisted = getPersistence('plans', 'plan_manage')
        return persisted?.modules[moduleIdentifier] || persisted?.modules['planManage']
      }

      // 处理具体计划模块
      if (panel.startsWith('plan_')) {
        const planKey = panel as `plan_${number}`
        const persisted = getPersistence('plans', planKey)
        return persisted?.modules[moduleIdentifier] || defaultState
      }

      return defaultState
    },

    createDefaultPanelState(moduleSubType: string) {
      const moduleConfig = getModuleConfig(moduleSubType)
      return {
        displayMode: moduleConfig?.displayMode || 1,
        moduleType: moduleSubType,
        globalFrame: { currentStep: 0, componentState: {} },
        mainFrame: { currentStep: 0, componentState: {} },
        subFrame: { currentStep: 0, componentState: {} }
      } as PanelContentState
    },

    // 持久化当前模块状态
    persistCurrentModule() {
      const panel = this.activePanel
      const moduleId = this.activeModuleId
      const moduleType = this.activeModuleSubType
      const state = this.getCurrentState() || this.createDefaultPanelState(moduleType)

      if (panel === 'plan_manage') {
        const current = getPersistence('plans', 'plan_manage') || { modules: {} }
        setPersistence('plans', {
          plan_manage: {
            ...current,
            currentModule: moduleId,
            modules: {
              ...current.modules,
              [moduleId]: state
            }
          }
        })
      } else if (panel.startsWith('plan_')) {
        const planKey = panel as `plan_${number}`
        const current = getPersistence('plans', planKey) || { modules: {} }
        setPersistence('plans', {
          [planKey]: {
            ...current,
            currentModuleId: moduleId,
            modules: {
              ...current.modules,
              [moduleId]: state
            }
          }
        })
      }
    },

    // 获取当前状态
    getCurrentState(): PanelContentState | null {
      const panel = this.activePanel
      const moduleId = this.activeModuleId
      return this.contentStates.get(panel)?.get(moduleId) || null
    },

    // 切换面板
    switchPanel(panel: string, moduleId: 'planManage' | 'welcome' | 'settings' | 'planDashboard' | 'addModule' | number, moduleType?: string) {
      const moduleStore = useModuleCardStore()

      this.persistCurrentModule()

      this.activeModuleSubType = typeof moduleId === 'string' ?
        moduleId :
        (() => {
          const module = moduleStore.modules.find(m => m.module_id === moduleId)
          return module?.module_sub_type || moduleId.toString()
        })()

      // 新增：从持久化数据加载目标面板状态
      const targetModuleId = moduleId.toString()
      this.initializeModuleState(panel, targetModuleId)

      // 获取目标模块的持久化状态
      const persistedState = this.contentStates.get(panel)?.get(targetModuleId)

      // 更新当前状态
      this.activePanel = panel
      this.activeModuleId = targetModuleId
      if (moduleType) {
        this.activeModuleSubType = moduleType
      }

      // 新增：同步框架步骤状态
      if (persistedState) {
        this.contentStates.get(panel)?.set(targetModuleId, persistedState)

        this.$forceUpdate();

        // 触发框架组件重新渲染
        this.updateFrameState('main', {
          step: persistedState.mainFrame?.currentStep ?? 0,
          state: persistedState.mainFrame?.componentState
        })
        this.updateFrameState('sub', {
          step: persistedState.subFrame?.currentStep ?? 0,
          state: persistedState.subFrame?.componentState
        })
      }
      this.persistCurrentModule()
    },

    // 新增方法：获取指定frame的当前步骤
    getFrameStep(panel: string, moduleId: string, frameType: 'global' | 'main' | 'sub'): number {
      const state = this.contentStates.get(panel)?.get(moduleId)
      return state?.[`${frameType}Frame`]?.currentStep || 0
    },

    // 统一更新方法
    updateFrameState(
      frameType: 'global' | 'main' | 'sub',
      payload: {
        step?: number
        state?: Record<string, unknown>
      }
    ) {
      const currentPanel = this.activePanel
      const currentModule = this.activeModuleId
      const panelStates = this.contentStates.get(currentPanel)

      if (!panelStates) return

      const currentState = panelStates.get(currentModule) || {
        displayMode: 7,
        moduleType: 'planDashBoard',
        globalFrame: { currentStep: 0, componentState: {} },
        mainFrame: { currentStep: 0, componentState: {} },
        subFrame: { currentStep: 0, componentState: {} }
      }

      const updatedState = {
        ...currentState,
        [`${frameType}Frame`]: {
          currentStep: payload.step ?? currentState[`${frameType}Frame`].currentStep,
          componentState: {
            ...currentState[`${frameType}Frame`].componentState,
            ...(payload.state || {})
          }
        }
      }
      panelStates.set(currentModule, updatedState)
      this.persistCurrentModule()
    },

    // this only can be used in main.ts
    async initializeAllPlans() {
      const persisted = getPersistence('plans') || {}
      Object.keys(persisted)
        .filter(key => key.startsWith('plan_'))
        .forEach(panelKey => {
          if (!this.contentStates.has(panelKey)) {
            this.contentStates.set(panelKey, new Map())
          }
        })
    },

    removePlanPanel(planKey: string) {
      // 从状态中移除
      this.contentStates.delete(planKey)

      // 如果当前激活的是该面板，则切换回管理面板
      if (this.activePanel === planKey) {
        this.switchPanel('plan_manage', 'planManage')
      }
    },

    // this only can be used in main.ts
    watchPlanStatus() {
      const planCardStore = usePlanCardStore()
      watch(
        () => planCardStore.hasPlan,
        () => {
          this.switchPanel('plan_manage', planCardStore.hasPlan ? 'planManage' : 'welcome')
        }
      )
    },

    $forceUpdate() {

    }
  },
  getters: {
    planPanels: (state) => {
      // 获取所有持久化计划键
      const persistedPlans = getPersistence('plans') || {}
      const planKeys = Object.keys(persistedPlans).filter(key =>
        key.startsWith('plan_') && key !== 'plan_manage'
      )

      // 合并当前状态和持久化状态
      const currentPlans = Array.from(state.contentStates.keys())
        .filter(key => key.startsWith('plan_') && key !== 'plan_manage' && state.contentStates.get(key)?.size)

      // 去重合并并过滤 active_flag
      const planCardStore = usePlanCardStore()
      const merged = [...new Set([...currentPlans, ...planKeys])]
        .filter(planKey => {
          const planId = parseInt(planKey.split('_')[1])
          const plan = planCardStore.plans.find(p => p.plan_id === planId)
          return plan?.active_flag === '1'
        })
        .sort((a, b) => parseInt(a.split('_')[1]) - parseInt(b.split('_')[1]))

      return merged.map(id => ({ id }))
    }
  }
})
