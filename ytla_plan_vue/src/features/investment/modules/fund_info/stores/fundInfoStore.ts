import { defineStore } from 'pinia'
import { FundInfoService } from '@/features/investment/modules/fund_info/services/fundInfoService.ts'

const API_BASE = import.meta.env.VITE_API_BASE
const fundInfoService = new FundInfoService(API_BASE)

export const useFundInfoStore = defineStore('fundInfo', {
  state: () => ({
    fundCode: '' as string,
    fundInfo: null as {
      code: string
      name: string
      fund_type: string
      ratio: number
      share_accuracy: number
      fee_free_limit: number
      latest_price: number
    } | null,
    fundHistory: [] as Array<{
      transaction_date: string
      current_price: number
      origin_price: number
      fluctuation: number
      share_change_ratio: number
      share_change_note: string
    }>,
    isLoading: false,
    error: null as string | null,
  }),
  actions: {
    setFundCode(code: string) {
      this.fundCode = code
    },

    async fetchFundInfo(code: string) {
      this.isLoading = true
      this.error = null
      try {
        const response = await fundInfoService.getFundInfo(code)
        if (response.success && response.data) {
          this.fundInfo = response.data
          this.fundCode = code
        } else {
          this.error = response.message || '获取基金信息失败'
        }
      } catch (error) {
        this._handleError(error, '获取基金信息失败')
      } finally {
        this.isLoading = false
      }
    },

    async fetchFundHistory(code: string) {
      this.isLoading = true
      this.error = null
      try {
        const response = await fundInfoService.getFundHistory(code)
        if (response.success && response.data) {
          this.fundHistory = response.data
        } else {
          this.error = response.message || '获取历史净值失败'
        }
      } catch (error) {
        this._handleError(error, '获取历史净值失败')
      } finally {
        this.isLoading = false
      }
    },

    async loadAllData(code: string) {
      await Promise.all([
        this.fetchFundInfo(code),
        this.fetchFundHistory(code)
      ])
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
      throw error
    }
  }
})
