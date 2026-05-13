export class FundInfoService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 获取基金基本信息
   * @param code 基金代码
   */
  async getFundInfo(code: string): Promise<{
    success: boolean
    data?: {
      code: string
      name: string
      fund_type: string
      ratio: number
      share_accuracy: number
      fee_free_limit: number
      latest_price: number
    }
    message?: string
  }> {
    const response = await fetch(`${this.API_BASE}/fund_info/get`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    })
    if (!response.ok) throw new Error('获取基金信息失败')
    return response.json()
  }

  /**
   * 获取基金历史净值数据
   * @param code 基金代码
   */
  async getFundHistory(code: string): Promise<{
    success: boolean
    data?: Array<{
      transaction_date: string
      current_price: number
      origin_price: number
      fluctuation: number
      share_change_ratio: number
      share_change_note: string
    }>
    message?: string
  }> {
    const response = await fetch(`${this.API_BASE}/fund_info/history`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    })
    if (!response.ok) throw new Error('获取历史净值失败')
    return response.json()
  }

  /**
   * 获取基金最新净值
   * @param code 基金代码
   */
  async getFundLatestPrice(code: string): Promise<{
    success: boolean
    data?: {
      latest_price: number
      origin_price: number
    }
    message?: string
  }> {
    const response = await fetch(`${this.API_BASE}/fund_info/latest_price`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    })
    if (!response.ok) throw new Error('获取最新净值失败')
    return response.json()
  }
}
