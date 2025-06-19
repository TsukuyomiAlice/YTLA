import { defineStore } from 'pinia'
import { LanguageDictionaryService } from '@/features/language/services/languageDictionaryService'

// 依赖注入配置
const API_BASE = import.meta.env.VITE_API_BASE
const languageDictionaryService = new LanguageDictionaryService(API_BASE)

export const useLanguageDictionaryStore = defineStore('languageDictionary', {
  state: () => ({
    currentWord: '', // 当前搜索的单词
    searchResult: '', // 搜索结果（根据实际数据类型调整）
    isLoading: false,
    error: null as string | null,
  }),
  actions: {
    async searchDictionary(word: string) {
      this.isLoading = true
      this.error = null
      try {
        const response = await languageDictionaryService.searchWord(word)
        this.searchResult = response.data.meaning
        this.currentWord = word
      } catch (error) {
        this._handleError(error, '词典搜索失败')
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
