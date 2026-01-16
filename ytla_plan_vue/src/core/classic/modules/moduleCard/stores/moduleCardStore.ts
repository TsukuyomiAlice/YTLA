import { defineStore } from 'pinia'
import type { BaseModule } from '@/core/classic/modules/moduleCard/definitions/moduleTypes.ts'
import { ModuleService } from '@/core/classic/modules/moduleCard/services/moduleService.ts'

// 依赖注入配置
const API_BASE = import.meta.env.VITE_API_BASE
const moduleService = new ModuleService(API_BASE)

export const useModuleCardStore = defineStore('module', {
  state: () => ({
    modules: [] as BaseModule[],
    isLoading: false,
    error: null as string | null,
    moduleFilter: '',
    selectedModule: null as { moduleType: string; moduleSubType: string } | null
  }),
  actions: {
    async fetchModules(planId: number) {
      this.isLoading = true
      try {
        this.modules = await moduleService.fetchModules(planId)
      } catch (error) {
        this._handleError(error, 'Failed to fetch modules')
      } finally {
        this.isLoading = false
      }
    },

    async addModule(moduleData: Omit<BaseModule, 'module_id'>) {
      this.isLoading = true
      try {
        const newModule = await moduleService.addModule(moduleData)
        this.modules.push(newModule)
        return { ok: true, data: newModule }
      } catch (error) {
        this._handleError(error, 'Failed to add module')
      } finally {
        this.isLoading = false
      }
    },

    async updateModule(moduleId: number, moduleData: Omit<BaseModule, 'module_id'>) {
      this.isLoading = true
      try {
        const updatedModule = await moduleService.updateModule(moduleId, moduleData)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (index !== -1) this.modules[index] = updatedModule
        return updatedModule
      } catch (error) {
        this._handleError(error, 'Failed to update module')
      } finally {
        this.isLoading = false
      }
    },

    async deleteModule(moduleId: number) {
      this.isLoading = true
      try {
        await moduleService.deleteModule(moduleId)
        this.modules = this.modules.filter(module => module.module_id !== moduleId)
      } catch (error) {
        this._handleError(error, 'Failed to delete module')
      } finally {
        this.isLoading = false
      }
    },

    async deactivateModule(moduleId: number) {
      this.isLoading = true
      try {
        await moduleService.deactivateModule(moduleId)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (index !== -1) this.modules[index].active_flag = '0'
      } catch (error) {
        this._handleError(error, 'Failed to deactivate module')
      } finally {
        this.isLoading = false
      }
    },

    async activateModule(moduleId: number) {
      this.isLoading = true
      try {
        await moduleService.activateModule(moduleId)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (index !== -1) this.modules[index].active_flag = '1'
      } catch (error) {
        this._handleError(error, 'Failed to activate module')
      } finally {
        this.isLoading = false
      }
    },

    async updateModuleTitle(moduleId: number, newTitle: string) {
      this.isLoading = true
      try {
        const updatedModule = await moduleService.updateModuleTitle(moduleId, newTitle)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (updatedModule) {
          this.modules[index] = {
            ...this.modules[index],
            name: newTitle
          }
        }
      } catch (error) {
        this._handleError(error, 'Failed to update module')
      } finally {
        this.isLoading = false
      }
    },

    async updateModuleBelongGroupName(moduleId: number, newGroup: string) {
      this.isLoading = true
      try {
        const updatedModule = await moduleService.updateModuleBelongGroupName(moduleId, newGroup)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (updatedModule) {
          this.modules[index] = {
            ...this.modules[index],
            description: newGroup
          }
        }
      } catch (error) {
        this._handleError(error, 'Failed to update module')
      } finally {
        this.isLoading = false
      }
    },

    async updateModuleDescription(moduleId: number, newDescription: string) {
      this.isLoading = true
      try {
        const updatedModule = await moduleService.updateModuleDescription(moduleId, newDescription)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (updatedModule) {
          this.modules[index] = {
            ...this.modules[index],
            description: newDescription
          }
        }
      } catch (error) {
        this._handleError(error, 'Failed to update module')
      } finally {
        this.isLoading = false
      }
    },

    async updateModuleIcon(moduleId: number, iconName: string) {
      this.isLoading = true
      try {
        const updatedModule = await moduleService.updateModuleIcon(moduleId, iconName)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (index !== -1) {
          this.modules[index] = { ...this.modules[index], icon_path: iconName }
        }
      } catch (error) {
        this._handleError(error, '图标更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async updateModuleBackground(moduleId: number, backgroundName: string) {
      this.isLoading = true
      try {
        const updatedModule = await moduleService.updateModuleBackground(moduleId, backgroundName)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (index !== -1) {
          this.modules[index] = { ...this.modules[index], background_path: backgroundName }
        }
      } catch (error) {
        this._handleError(error, '背景更新失败')
      } finally {
        this.isLoading = false
      }
    },

    async updateModuleTags(moduleId: number, tags: string) {
      this.isLoading = true
      try {
        const success = await moduleService.updateModuleTags(moduleId, tags)
        if (success) {
          const index = this.modules.findIndex(c => c.module_id === moduleId)
          if (index !== -1) {
            this.modules[index] = {
              ...this.modules[index],
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

    async deleteModuleTag(moduleId: number, tag: string) {
      this.isLoading = true
      try {
        await moduleService.deleteModuleTag(moduleId, tag)
        const index = this.modules.findIndex(c => c.module_id === moduleId)
        if (index !== -1) {
          this.modules[index].tags = this.modules[index].tags
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

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
      throw error
    },

    updateFilter(value: string) {
      this.moduleFilter = value
    },

    setSelectedModule(payload: { moduleType: string; moduleSubType: string }) {
      this.selectedModule = payload
    },

    clearSelectedModule() {
      this.selectedModule = null
    }
  },
  getters: {
    getModuleById: (state) => (id: number) => {
      return state.modules.find(m => m.module_id === id)
    },

    activeModules(state): BaseModule[] {
      return state.modules.filter(module =>
        module.delete_flag === '0'
      )
    },

    filteredModules(state): BaseModule[] {
      const filter = state.moduleFilter.toLowerCase()
      return this.activeModules.filter(module => {
        const tags = module.tags?.toLowerCase().split(',') || []
        return tags.some(tag => tag.includes(filter)) ||
          module.module_type?.toLowerCase().includes(filter) ||
          module.module_sub_type?.toLowerCase().includes(filter)
      })
    }
  }
})
