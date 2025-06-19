import { defineStore } from 'pinia'
import { LanguageVocabularyService } from '@/features/language/services/languageVocabularyService'

const API_BASE = import.meta.env.VITE_API_BASE
const languageVocabularyService = new LanguageVocabularyService(API_BASE)

export const useLanguageVocabularyStore = defineStore('languageVocabulary', {
  state: () => ({
    vocabularyBooks: [] as Array<{
      record_id: number
      vocabulary_book_name: string
      word_list: string[]
    }>,
    currentBookId: 0,
    isLoading: false,
    error: null as string | null,
  }),
  actions: {
    async createNewBook(planId: number, moduleId: number, userName: string) {
      this.isLoading = true
      try {
        const response = await languageVocabularyService.createNewVocabularyBook(planId, moduleId, userName)
        this.currentBookId = response.data?.record_id || 0
        await this.fetchAllBooks(planId, moduleId, userName)
      } catch (error) {
        this._handleError(error, '创建词汇本失败')
      } finally {
        this.isLoading = false
      }
    },

    async fetchAllBooks(planId: number, moduleId: number, userName: string) {
      this.isLoading = true
      try {
        const response = await languageVocabularyService.getAllVocabularies(planId, moduleId, userName)
        this.vocabularyBooks = response.data.records
      } catch (error) {
        this._handleError(error, '获取词汇本失败')
      } finally {
        this.isLoading = false
      }
    },

    async updateWordList(planId: number, moduleId: number, recordId: number, words: string[]) {
      this.isLoading = true
      try {
        await languageVocabularyService.updateWordList(planId, moduleId, recordId, words)
        const book = this.vocabularyBooks.find(b => b.record_id === recordId)
        if (book) book.word_list = words
      } catch (error) {
        this._handleError(error, '更新单词列表失败')
      } finally {
        this.isLoading = false
      }
    },

    async updateBookName(planId: number, moduleId: number, recordId: number, newName: string) {
      this.isLoading = true
      try {
        await languageVocabularyService.updateBookName(planId, moduleId, recordId, newName)
        const book = this.vocabularyBooks.find(b => b.record_id === recordId)
        if (book) book.vocabulary_book_name = newName
      } catch (error) {
        this._handleError(error, '更新书名失败')
      } finally {
        this.isLoading = false
      }
    },

    setCurrentBook(bookId: number) {
      this.currentBookId = bookId
    },
    clearCurrentBook() {
      this.currentBookId = 0
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
      throw error
    }
  }
})
