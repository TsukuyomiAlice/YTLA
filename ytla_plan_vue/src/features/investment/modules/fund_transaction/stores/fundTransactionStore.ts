import { defineStore } from 'pinia'
import { FundTransactionService } from '@/features/investment/modules/fund_transaction/services/fundTransactionService.ts'

const API_BASE = import.meta.env.VITE_API_BASE
const fundTransactionService = new FundTransactionService(API_BASE)

export const useFundTransactionStore = defineStore('fundTransaction', {
  state: () => ({
    fundCode: '' as string,
    transactionData: null as {
      brief: {
        code: string
        fund_name: string
        last_transaction_date: string
        latest_price: number
        holding_amount: number
        holding_share: number
        holding_average_price: number
        shown_amount: number
        shown_share: number
        profit_in_amount: number
        profit_in_share: number
        long_position_amount: number
        long_position_share: number
        short_position_share: number
        short_position_amount: number
      }
      match_list: Array<Array<any>>
      profit_list: Array<any>
      continuous_history: {
        buy_side: Array<Array<number>>
        sell_side: Array<Array<number>>
        fund_days: number
        buy_side_grades: Array<number>
        sell_side_grades: Array<number>
        latest_flows: Array<[string, number, number]>
      }
    } | null,
    isLoading: false,
    error: null as string | null,
    expandedIndex: null as number | null,
  }),
  actions: {
    setFundCode(code: string) {
      this.fundCode = code
    },

    async fetchTransactionAnalysis(code: string) {
      this.clear()
      this.isLoading = true
      this.error = null
      try {
        const response = await fundTransactionService.getTransactionAnalysis(code)
        if (response.success && response.data) {
          this.transactionData = response.data
          this.fundCode = code
        } else {
          this.error = response.message || '获取交易分析失败'
        }
      } catch (error) {
        this._handleError(error, '获取交易分析失败')
      } finally {
        this.isLoading = false
      }
    },

    toggleExpandedIndex(index: number) {
      if (this.expandedIndex === index) {
        this.expandedIndex = null
      } else {
        this.expandedIndex = index
      }
    },

    getSelectedGroup() {
      if (this.expandedIndex === null || !this.transactionData) return null
      return this.transactionData.match_list[this.expandedIndex] || null
    },

    clear() {
      this.transactionData = null
      this.expandedIndex = null
      this.error = null
    },

    _handleError(error: unknown, defaultMsg: string) {
      this.error = error instanceof Error ? error.message : defaultMsg
      console.error(this.error)
      throw error
    }
  }
})
