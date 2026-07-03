export class EightCharactersService {
  constructor(private readonly API_BASE: string) {}

  /**
   * 提交八字分析
   * @param eight_characters 八字数据
   * @param luck_cycle 大运周期
   * @param fleet_year 流年
   */
  async analyze(eight_characters: any, luck_cycle: any, fleet_year: any): Promise<{
    success: boolean
    data?: any
    message?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/eight_characters_analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ eight_characters, luck_cycle, fleet_year }),
    })
    if (!response.ok) throw new Error('八字分析失败')
    return response.json()
  }

  /**
   * 保存历史记录（字段平铺，匹配后端路由）
   * @param params 包含 plan_id, module_id, birthday, birth_time, gender,
   *               eight_characters(字符串), luck_cycle, fleet_year,
   *               analysis_result, annotations, lunar_date, creator
   */
  async saveHistory(params: {
    plan_id: number
    module_id: number
    birthday?: string
    birth_time?: string
    gender?: string
    eight_characters?: string
    luck_cycle?: string
    fleet_year?: string
    analysis_result?: string
    annotations?: string
    lunar_date?: string
    creator?: string
  }): Promise<{
    success: boolean
    data?: { record_id: number }
    msg?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/eight_characters_history_save`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(params),
    })
    if (!response.ok) throw new Error('保存历史记录失败')
    return response.json()
  }

  /**
   * 获取历史记录列表
   * @param plan_id 计划ID
   * @param module_id 模块ID
   * @param creator 创建者（可选）
   * @param limit 每页条数（可选）
   * @param offset 偏移量（可选）
   */
  async getHistoryList(plan_id: number, module_id: number, creator?: string, limit?: number, offset?: number): Promise<{
    success: boolean
    data?: {
      records: Array<Record<string, any>>
      total: number
    }
    msg?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/eight_characters_history_list`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plan_id, module_id, creator, limit, offset }),
    })
    if (!response.ok) throw new Error('获取历史记录列表失败')
    return response.json()
  }

  /**
   * 获取单条历史记录详情
   * @param plan_id 计划ID
   * @param module_id 模块ID
   * @param eight_characters 八字字符串
   * @param gender 性别
   */
  async getHistoryDetail(plan_id: number, module_id: number, eight_characters: string, gender: string): Promise<{
    success: boolean
    data?: { record: Record<string, any> }
    msg?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/eight_characters_history_detail`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plan_id, module_id, eight_characters, gender }),
    })
    if (!response.ok) throw new Error('获取历史记录详情失败')
    return response.json()
  }

  /**
   * 公历日期转换为八字
   * @param year 公历年份
   * @param month 公历月份 (1-12)
   * @param day 公历日 (1-31)
   * @param hour_branch 时辰地支（可选），如 "子", "丑", ..., "亥"
   * @param gender 性别（可选），"male" 或 "female"，提供后返回大运表+流年表
   */
  async convertSolarToBazi(year: number, month: number, day: number, hour_branch?: string, gender?: string): Promise<{
    success: boolean
    data?: {
      eight_characters: string
      four_pillars: {
        year: { heavenly_stem: string; earthly_branch: string }
        month: { heavenly_stem: string; earthly_branch: string }
        day: { heavenly_stem: string; earthly_branch: string }
        hour: { heavenly_stem: string; earthly_branch: string }
      }
      luck_cycle_table?: Array<{
        index: number
        ganzhi: string
        start_age: number
        end_age: number
        start_year: number
        end_year: number
      }>
      fleet_years?: Array<{
        year: number
        ganzhi: string
      }>
    }
    msg?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/eight_characters_convert`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ year, month, day, hour_branch, gender }),
    })
    if (!response.ok) throw new Error('公历转八字失败')
    return response.json()
  }

  /**
   * 逻辑删除历史记录
   * @param plan_id 计划ID
   * @param module_id 模块ID
   * @param eight_characters 八字字符串
   * @param gender 性别
   */
  async deleteHistory(plan_id: number, module_id: number, eight_characters: string, gender: string): Promise<{
    success: boolean
    data?: any
    msg?: string
    error?: string
  }> {
    const response = await fetch(`${this.API_BASE}/eight_characters_history_delete`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ plan_id, module_id, eight_characters, gender }),
    })
    if (!response.ok) throw new Error('删除历史记录失败')
    return response.json()
  }
}
