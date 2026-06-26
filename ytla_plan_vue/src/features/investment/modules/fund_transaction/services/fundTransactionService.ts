export class FundTransactionService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 获取基金交易分析数据
   * @param plan_id 计划ID
   * @param module_id 模块ID
   * @param code 基金代码
   */
  async getTransactionAnalysis(plan_id: number, module_id: number, code: string): Promise<{
    success: boolean
    data?: {
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
      match_list: Array<Array<{
        transaction_id: number
        code: string
        fund_name: string
        transaction_date: string
        transaction_type: string
        transaction_price: number
        transaction_amount: number
        transaction_share: number
        transaction_profit: number
        transaction_profit_pct: number
        transaction_base_price: number
        transaction_base_amount: number
        transaction_base_share: number
        transaction_profit_to_base: number
        transaction_profit_pct_to_base: number
        order_id: number
        memo: string
        analyze_transaction_profit: number
        transaction_profit_amount: number
        transaction_profit_share: number
        analyze_transaction_profit_pct: number
        analyze_transaction_type: string
        analyze_transaction_stage: string
        analyze_group_profit_amount: number
        analyze_group_profit_share: number
      }>>
      profit_list: Array<{
        date: string
        profit_amount: number
        profit_share: number
        total_profit_amount: number
        total_profit_share: number
      }>
      continuous_history: {
        buy_side: Array<Array<number>>
        sell_side: Array<Array<number>>
        fund_days: number
        buy_side_grades: Array<number>
        sell_side_grades: Array<number>
        latest_flows: Array<[string, number, number]>
      }
    }
    message?: string
  }> {
    const response = await fetch(`${this.API_BASE}/fund_transaction/analysis`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plan_id, module_id, code })
    })
    if (!response.ok) throw new Error('获取交易分析失败')
    return response.json()
  }
}
