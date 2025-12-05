import { defineStore } from 'pinia'
import { LanguageAssessmentService } from '@/features/language/modules/assessment/services/languageAssessmentService.ts'

// 依赖注入配置
const API_BASE = import.meta.env.VITE_API_BASE
const languageAssessmentService = new LanguageAssessmentService(API_BASE)

export const useLanguageAssessmentStore = defineStore('languageAssessment', {
  state: () => ({
    recordId: 0,
    step1Wordlist: [] as string[],
    step2Questions: [] as string[],
    step2Answers: [] as number[],
    step2NotFinished: false,
    finalLevel: 'B1',
    isLoading: false,
    error: null as string | null,
  }),
  actions: {
    async assessment1A(planId: number, moduleId: number, userName: string) {
      this.isLoading = true
      try {
        const response = await languageAssessmentService.assessmentStart(planId, moduleId, userName)
        this.recordId = response.data.record_id
        this.step1Wordlist = response.data.word_list
      } catch (error) {
        this._handleError(error, 'Failed to get response')
      } finally {
        this.isLoading = false
      }
    },

    async assessment1B(planId: number, moduleId: number, step1aAnswer: string[]) {
      this.isLoading = true
      try {
        const response = await languageAssessmentService.assessmentStep1a(planId, moduleId, this.recordId, step1aAnswer)
        this.recordId = response.data.record_id
        this.step1Wordlist = response.data.word_list
      } catch (error) {
        this._handleError(error, 'Failed to get response')
      } finally {
        this.isLoading = false
      }
    },

    async assessment2(planId: number, moduleId: number, step1bAnswer: string[]) {
      this.isLoading = true
      try {
        const response = await languageAssessmentService.assessmentStep1b(planId, moduleId, this.recordId, step1bAnswer)
        this.recordId = response.data.record_id
        this.step2Questions = response.data.question_list
      } catch (error) {
        this._handleError(error, 'Failed to get response')
      } finally {
        this.isLoading = false
      }
    },

    async assessmentFinal(planId: number, moduleId: number, step2Answer: number[]) {
      this.isLoading = true
      try {
        const response = await languageAssessmentService.assessmentStep2(planId, moduleId, this.recordId, step2Answer)
        this.step2NotFinished = response.data.is_step_2
        this.finalLevel = response.data.final_result
        this.step2Questions = response.data.question_list
      } catch (error) {
        this._handleError(error, 'Failed to get response')
      } finally {
        this.isLoading = false
      }
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
      throw error
    },
  }
})
