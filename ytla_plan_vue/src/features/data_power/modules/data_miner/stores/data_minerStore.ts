import { defineStore } from 'pinia'
import { Data_minerService } from '@/features/data_power/modules/data_miner/services/data_minerService.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const API_BASE = import.meta.env.VITE_API_BASE
const data_minerService = new Data_minerService(API_BASE)

export interface SourceFileItem {
  file_name: string
  file_path: string
  file_size: number
  upload_time: string
  module_id: number
  module_name: string
  file_type: string
}

export interface ProcessedFileItem {
  file_name: string
  file_path: string
  file_size: number
  processed_time: string
  module_id: number
  module_name: string
  output_format: string
  source_file: string
}

export interface ViewFileContent {
  content?: string
}

export const useData_minerStore = defineStore('data_miner', {
  state: () => ({
    sourceFiles: [] as SourceFileItem[],
    processedFiles: [] as ProcessedFileItem[],
    currentViewFile: null as ProcessedFileItem | null,
    currentViewContent: null as string | null,
    isSubActive: false,
    isLoading: false,
    isProcessing: false,
    error: null as string | null,
  }),
  actions: {
    async fetchSourceFiles(planId?: number) {
      if (!planId) {
        const moduleProcessStore = useModuleProcessStore()
        const bpId = moduleProcessStore.belongPlanId
        if (!bpId) {
          this.error = '无法获取计划ID'
          return
        }
        planId = bpId
      }
      if (!planId) {
        this.error = '无法获取计划ID'
        return
      }

      this.isLoading = true
      this.error = null
      try {
        const response = await data_minerService.getSourceFiles(planId)
        if (response.success && response.files) {
          this.sourceFiles = response.files
        } else {
          this.error = response.message || '获取原始文件列表失败'
        }
      } catch (error) {
        this._handleError(error, '获取原始文件列表失败')
      } finally {
        this.isLoading = false
      }
    },

    async fetchProcessedFiles(planId?: number, moduleId?: number) {
      if (!planId) {
        const moduleProcessStore = useModuleProcessStore()
        const bpId = moduleProcessStore.belongPlanId
        if (!bpId) {
          this.error = '无法获取计划ID'
          return
        }
        planId = bpId
      }
      if (!planId) {
        this.error = '无法获取计划ID'
        return
      }

      // 若无显式传入 moduleId，尝试从 moduleProcessStore 获取当前模组 ID
      if (moduleId === undefined) {
        const moduleProcessStore = useModuleProcessStore()
        const mid = moduleProcessStore.moduleId
        if (typeof mid === 'number') {
          moduleId = mid
        }
      }

      this.isLoading = true
      this.error = null
      try {
        const response = await data_minerService.getProcessedFiles(planId, moduleId)
        if (response.success && response.files) {
          this.processedFiles = response.files
        } else {
          this.error = response.message || '获取已处理文件列表失败'
        }
      } catch (error) {
        this._handleError(error, '获取已处理文件列表失败')
      } finally {
        this.isLoading = false
      }
    },

    async processFile(planId: number, sourceFilePath: string, moduleId: number) {
      this.isProcessing = true
      this.error = null
      try {
        const response = await data_minerService.processFile(planId, sourceFilePath, moduleId)
        if (response.success) {
          await this.fetchProcessedFiles(planId)
          return { success: true, data: response.data }
        } else {
          this.error = response.error || '文件分析失败'
          return { success: false, message: response.error }
        }
      } catch (error) {
        this._handleError(error, '文件分析失败')
        return { success: false, message: this.error }
      } finally {
        this.isProcessing = false
      }
    },

    async viewProcessedFile(planId: number, filePath: string) {
      this.error = null
      try {
        const response = await data_minerService.viewProcessedFile(planId, filePath)
        if (response.success) {
          const backendData = response.content || response.data
          let result: any = {}

          // .db 文件: backendData 格式为 {tables: {tableName: {columns: [...], rows: [[...], ...]}}}
          // .json 文件: backendData 为反序列化的 JSON 对象
          if (backendData && backendData.tables) {
            const tableNames = Object.keys(backendData.tables)
            // 将每个表转为 columns/rows 对象数组格式
            const tableList = tableNames.map((name) => {
              const table = backendData.tables[name]
              const columns: string[] = table.columns || []
              const rawRows: any[][] = table.rows || []
              const rows = rawRows.map((row: any[]) => {
                const obj: Record<string, any> = {}
                columns.forEach((col, i) => { obj[col] = row[i] })
                return obj
              })
              return { name, columns, rows }
            })
            if (tableNames.length === 1) {
              // 单表: 直接展示
              result = { file_type: 'table', columns: tableList[0].columns, rows: tableList[0].rows }
            } else {
              // 多表: 逐一展示
              result = { file_type: 'multi_table', tables: tableList }
            }
          } else {
            // JSON 文件
            result = { file_type: 'json', content: JSON.stringify(backendData, null, 2) }
          }

          return { success: true, data: result }
        } else {
          this.error = response.message || '查看文件失败'
          return { success: false, message: this.error }
        }
      } catch (error) {
        this._handleError(error, '查看文件失败')
        return { success: false, message: this.error }
      }
    },

    async viewFile(file: ProcessedFileItem) {
      const moduleProcessStore = useModuleProcessStore()
      const planId = moduleProcessStore.belongPlanId
      if (!planId) {
        this.error = '无法获取计划ID'
        return { success: false }
      }

      this.error = null
      try {
        const response = await data_minerService.viewProcessedFile(planId, file.file_path)
        if (response.success) {
          this.currentViewFile = file
          this.currentViewContent = response.content || null
          this.isSubActive = true
          return { success: true }
        } else {
          this.error = response.message || '查看文件失败'
          return { success: false }
        }
      } catch (error) {
        this._handleError(error, '查看文件失败')
        return { success: false }
      }
    },

    async deleteProcessedFile(planId: number, filePath: string) {
      this.error = null
      try {
        const response = await data_minerService.deleteProcessedFile(planId, filePath)
        if (response.success) {
          await this.fetchProcessedFiles(planId)
          return { success: true }
        } else {
          this.error = response.error || '删除文件失败'
          return { success: false, message: response.error }
        }
      } catch (error) {
        this._handleError(error, '删除文件失败')
        return { success: false, message: this.error }
      }
    },

    showSubView(file: ProcessedFileItem) {
      this.currentViewFile = file
      this.isSubActive = true
    },

    hideSubView() {
      this.isSubActive = false
      this.currentViewFile = null
      this.currentViewContent = null
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
