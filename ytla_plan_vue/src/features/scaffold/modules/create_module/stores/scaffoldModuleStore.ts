import { defineStore } from 'pinia'
import { ScaffoldModuleService, type ScaffoldModuleResponse } from '../services/scaffoldModuleService'

const API_BASE = import.meta.env.VITE_API_BASE
const scaffoldModuleService = new ScaffoldModuleService(API_BASE)

export const useScaffoldModuleStore = defineStore('scaffoldModule', {
  state: () => ({
    isCore: false,
    typeName: '',
    subTypeName: '',
    version: 'classic',
    genBackend: false,
    genFrontend: false,
    isLoading: false,
    error: null as string | null,
    result: null as ScaffoldModuleResponse | null,
  }),
  actions: {
    updateForm(field: string, value: any) {
      (this as any)[field] = value
    },

    async submitForm() {
      this.isLoading = true
      this.error = null
      try {
        const response = await scaffoldModuleService.generateScaffold({
          isCore: this.isCore,
          typeName: this.typeName,
          structure: 'modules',
          subTypeName: this.subTypeName,
          genBackend: this.genBackend,
          genFrontend: this.genFrontend
        })
        this.result = response.data
      } catch (error) {
        this._handleError(error, '脚手架生成失败')
      } finally {
        this.isLoading = false
      }
    },

    resetForm() {
      this.isCore = false
      this.typeName = ''
      this.subTypeName = ''
      this.version = 'classic'
      this.genBackend = false
      this.genFrontend = false
      this.error = null
      this.result = null
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
    },
  }
})
