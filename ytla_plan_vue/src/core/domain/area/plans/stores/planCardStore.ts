import { defineStore } from 'pinia'
import type { Plan } from '@/core/domain/area/plans/types/planTypes.ts'
import { PlanService } from '@/core/domain/area/plans/services/planService.ts'
import { usePersistence } from '@/core/domain/area/frame/composables/usePersistence.ts'
import { usePanelStore } from '@/core/domain/area/frame/services/panelStore.ts'

const { getPersistence, setPersistence } = usePersistence()

const API_BASE = import.meta.env.VITE_API_BASE
const planService = new PlanService(API_BASE)

export const usePlanCardStore = defineStore('planCard', {
  state: () => ({
    plans: [] as Plan[],
    isLoading: false,
    error: null as string | null,
    hasPlan: false
  }),
  actions: {
    async fetchPlans() {
      this.isLoading = true
      try {
        this.plans = await planService.fetchPlans()
        const hasPlan = this.plans.length > 0
        setPersistence('layout', { 'hasPlan': hasPlan })
        this.hasPlan = hasPlan
      } catch (error) {
        this._handleError(error, 'Failed to fetch planCards')
      } finally {
        this.isLoading = false
      }
    },

    async addPlan(planData: Omit<Plan, 'plan_id'>) {
      this.isLoading = true
      try {
        const newPlan = await planService.addPlan(planData)
        this.plans.push(newPlan)
        return { ok: true, data: newPlan }
      } catch (error) {
        this._handleError(error, 'Failed to add plan')
      } finally {
        this.isLoading = false
      }
    },

    async deletePlan(planId: number) {
      this.isLoading = true
      try {
        await planService.deletePlan(planId)
        this.plans = this.plans.filter(plan => plan.plan_id !== planId)
        const panelStore = usePanelStore()
        panelStore.removePlanPanel(`plan_${planId}`)
        this._cleanPlanPersistence(planId)
        setTimeout(() => {
          this._cleanPlanPersistence(planId)
          panelStore.initializeAllPlans()
        }, 50)
      } catch (error) {
        this._handleError(error, 'Failed to delete plan')
      } finally {
        this.isLoading = false
      }
    },

    _cleanPlanPersistence(planId: number) {
      const { setPersistence } = usePersistence()
      setPersistence('plans', {
        [`plan_${planId}`]: undefined
      })
      localStorage.removeItem(`ytla_persistence:plans.plan_${planId}`)
    },

    async deactivatePlan(planId: number) {
      this.isLoading = true
      try {
        await planService.deactivatePlan(planId)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (index !== -1) this.plans[index].active_flag = '0'
        const panelStore = usePanelStore()
        panelStore.removePlanPanel(`plan_${planId}`)
        this._cleanPlanPersistence(planId)
        setTimeout(() => {
          this._cleanPlanPersistence(planId)
          panelStore.initializeAllPlans()
        }, 50)
      } catch (error) {
        this._handleError(error, 'Failed to deactivate plan')
      } finally {
        this.isLoading = false
      }
    },

    async activatePlan(planId: number) {
      this.isLoading = true
      try {
        await planService.activatePlan(planId)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (index !== -1) this.plans[index].active_flag = '1'
      } catch (error) {
        this._handleError(error, 'Failed to activate plan')
      } finally {
        this.isLoading = false
      }
    },

    async updatePlanTitle(planId: number, newTitle: string) {
      this.isLoading = true
      try {
        const updatedPlan = await planService.updatePlanTitle(planId, newTitle)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (updatedPlan) {
          this.plans[index] = {
            ...this.plans[index],
            name: newTitle
          }
        }
      } catch (error) {
        this._handleError(error, 'Failed to update plan')
      } finally {
        this.isLoading = false
      }
    },

    async updatePlanDescription(planId: number, newDescription: string) {
      this.isLoading = true
      try {
        const updatedPlan = await planService.updatePlanDescription(planId, newDescription)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (updatedPlan) {
          this.plans[index] = {
            ...this.plans[index],
            description: newDescription
          }
        }
      } catch (error) {
        this._handleError(error, 'Failed to update plan')
      } finally {
        this.isLoading = false
      }
    },

    async updatePlanIcon(planId: number, iconName: string) {
      this.isLoading = true
      try {
        const updatedPlan = await planService.updatePlanIcon(planId, iconName)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (index !== -1) {
          this.plans[index] = { ...this.plans[index], icon_path: iconName }
        }
      } catch (error) {
        this._handleError(error, '图标更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async updatePlanBackground(planId: number, backgroundName: string) {
      this.isLoading = true
      try {
        const updatedPlan = await planService.updatePlanBackground(planId, backgroundName)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (index !== -1) {
          this.plans[index] = { ...this.plans[index], background_path: backgroundName }
        }
      } catch (error) {
        this._handleError(error, '背景更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async updatePlanTags(planId: number, tags: string) {
      this.isLoading = true
      try {
        const success = await planService.updatePlanTags(planId, tags)
        if (success) {
          const index = this.plans.findIndex(c => c.plan_id === planId)
          if (index !== -1) {
            this.plans[index] = {
              ...this.plans[index],
              tags: tags
            }
          }
        }
      } catch (error) {
        this._handleError(error, '标签更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async deletePlanTag(planId: number, tag: string) {
      this.isLoading = true
      try {
        await planService.deletePlanTag(planId, tag)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (index !== -1) {
          this.plans[index].tags = this.plans[index].tags
            .split(',')
            .filter(t => t !== tag)
            .join(',')
        }
      } catch (error) {
        this._handleError(error, '标签删除失败')
      } finally {
        this.isLoading = false
      }
    },

    async updatePlanModuleGroups(planId: number, moduleGroups: string, belong_module_group_old: string, belong_module_group_new: string) {
      this.isLoading = true
      try {
        const success = await planService.updatePlanModuleGroups(planId, moduleGroups, belong_module_group_old, belong_module_group_new)
        if (success) {
          const index = this.plans.findIndex(c => c.plan_id === planId)
          if (index !== -1) {
            this.plans[index] = {
              ...this.plans[index],
              module_groups: moduleGroups
            }
          }
        }
      } catch (error) {
        this._handleError(error, '模块组更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async deletePlanModuleGroup(planId: number, group: string) {
      this.isLoading = true
      try {
        await planService.deletePlanModuleGroup(planId, group)
        const index = this.plans.findIndex(c => c.plan_id === planId)
        if (index !== -1) {
          this.plans[index].module_groups = this.plans[index].module_groups
            .split(',')
            .filter(g => g !== group)
            .join(',')
        }
      } catch (error) {
        this._handleError(error, '模块组删除失败')
      } finally {
        this.isLoading = false
      }
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
      throw error
    }
  },
  getters: {
    activePlans(state): Plan[] {
      return state.plans.filter(plan =>
        plan.delete_flag === '0'
      )
    }
  }
})
