import { defineStore } from 'pinia'
import { useModuleCardStore } from '@/features/planManage/stores/moduleCardStore.ts'

export const useModuleProcessStore = defineStore('moduleProcessStore', {
  state: () => ({
    moduleId: null as number | string | null,
    belongPlanId: null as number | null,
    moduleType: '' as string | null,

    editingModuleId: null as number | null
  }),

  getters: {
    currentModuleType(state) {
      const moduleStore = useModuleCardStore()

      if (typeof state.moduleId === 'number') {
        const found = moduleStore.modules.find(m => m.module_id === state.moduleId)
        return found?.module_sub_type || 'planDashboard'
      }

      // 字符串类型直接返回
      return state.moduleId?.toString() || 'planDashboard'
    }
  },

  actions: {
    setModule(moduleId: number | string, belongPlanId?: number, moduleType?: string) {
      const moduleStore = useModuleCardStore()

      // 新增数字类型转换逻辑
      if (typeof moduleId === 'number') {
        const found = moduleStore.modules.find(m => m.module_id === moduleId)
        this.moduleType = found?.module_sub_type || 'unknown'
      } else {
        this.moduleType = moduleId
      }
      if (moduleType) {
        this.moduleType = moduleType
      }

      this.moduleId = moduleId
      this.belongPlanId = belongPlanId || null
      this.editingModuleId = null
    },

    clearModule() {
      this.moduleId = null
      this.belongPlanId = null
      this.moduleType = ''
      this.editingModuleId = null
    },

    switchToDashboard() {
      this.moduleId = 'planDashboard'
      this.moduleType = 'planDashboard'
    },

    setEditingModule(moduleId: number) {
      this.editingModuleId = moduleId
    },

    clearEditingModule() {
      this.editingModuleId = null
    }
  }
})
