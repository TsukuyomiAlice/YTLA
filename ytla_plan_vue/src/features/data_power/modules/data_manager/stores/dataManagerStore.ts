import { defineStore } from 'pinia'
import { DataManagerService } from '@/features/data_power/modules/data_manager/services/dataManagerService.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const API_BASE = import.meta.env.VITE_API_BASE
const dataManagerService = new DataManagerService(API_BASE)

export interface FileItem {
  file_name: string
  file_path: string
  file_size: number
  upload_time: string
  module_id: number
  module_name: string
  module_subtype_name: string
}

export const useDataManagerStore = defineStore('dataManager', {
  state: () => ({
    files: [] as FileItem[],
    isLoading: false,
    isUploading: false,
    error: null as string | null,
  }),
  actions: {
    async fetchFiles() {
      const moduleProcessStore = useModuleProcessStore()
      const planId = moduleProcessStore.belongPlanId
      if (!planId) {
        this.error = '无法获取计划ID'
        return
      }

      this.isLoading = true
      this.error = null
      try {
        const response = await dataManagerService.getFiles(planId)
        if (response.success && response.files) {
          this.files = response.files
        } else {
          this.error = response.message || '获取文件列表失败'
        }
      } catch (error) {
        this._handleError(error, '获取文件列表失败')
      } finally {
        this.isLoading = false
      }
    },

    async uploadFile(file: File) {
      const moduleProcessStore = useModuleProcessStore()
      const moduleId = moduleProcessStore.moduleId
      if (!moduleId || typeof moduleId !== 'number') {
        this.error = '无法获取模块ID'
        return { success: false }
      }

      this.isUploading = true
      this.error = null
      try {
        const response = await dataManagerService.uploadFile(file, moduleId)
        if (response.success) {
          await this.fetchFiles()
          return { success: true }
        } else {
          this.error = response.error || '上传文件失败'
          return { success: false }
        }
      } catch (error) {
        this._handleError(error, '上传文件失败')
        return { success: false }
      } finally {
        this.isUploading = false
      }
    },

    async deleteFile(filePath: string) {
      this.error = null
      try {
        const response = await dataManagerService.deleteFile(filePath)
        if (response.success) {
          await this.fetchFiles()
          return { success: true }
        } else {
          this.error = response.error || '删除文件失败'
          return { success: false }
        }
      } catch (error) {
        this._handleError(error, '删除文件失败')
        return { success: false }
      }
    },

    clearError() {
      this.error = null
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
    }
  }
})
