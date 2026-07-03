import { defineStore } from 'pinia'
import { EightCharactersService } from '@/features/divination/modules/eight_characters/services/eightCharactersService.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const API_BASE = import.meta.env.VITE_API_BASE
const eightCharactersService = new EightCharactersService(API_BASE)

/** 数据库扁平字段的历史记录 */
export interface HistoryRecord {
  RECORD_ID: number
  BIRTHDAY: string
  LUNAR_DATE: string
  BIRTH_TIME: string
  GENDER: string
  EIGHT_CHARACTERS: string   // 八字字符串，如 "癸酉辛酉壬申己丑"
  LUCK_CYCLE: string
  FLEET_YEAR: string
  TEN_GODS_RATIO: string
  ANALYSIS_RESULT: string    // JSON 序列化的分析结果
  ANNOTATIONS: string
  CREATOR: string
  UPDATER: string
  UPDATE_DATETIME: string
  DELETE_FLG: string
}

/** 将八字对象转为后端期望的字符串，如 "癸酉辛酉壬申己丑" */
function pillarsToString(pillars: {
  year_pillar?: { heaven_stem: string; earth_branch: string }
  month_pillar?: { heaven_stem: string; earth_branch: string }
  day_pillar?: { heaven_stem: string; earth_branch: string }
  hour_pillar?: { heaven_stem: string; earth_branch: string }
}): string {
  const y = pillars.year_pillar
  const m = pillars.month_pillar
  const d = pillars.day_pillar
  const h = pillars.hour_pillar
  return `${y?.heaven_stem || ''}${y?.earth_branch || ''}${m?.heaven_stem || ''}${m?.earth_branch || ''}${d?.heaven_stem || ''}${d?.earth_branch || ''}${h?.heaven_stem || ''}${h?.earth_branch || ''}`
}

export const useEightCharactersStore = defineStore('eightCharacters', {
  state: () => ({
    analysisResult: null as any | null,
    historyRecords: [] as HistoryRecord[],
    selectedRecord: null as HistoryRecord | null,
    isLoading: false,
    error: null as string | null,
  }),
  actions: {
    async analyze(
      eightCharactersObj: {
        year_pillar: { heaven_stem: string; earth_branch: string }
        month_pillar: { heaven_stem: string; earth_branch: string }
        day_pillar: { heaven_stem: string; earth_branch: string }
        hour_pillar: { heaven_stem: string; earth_branch: string }
      },
      luck_cycle: string,
      fleet_year: string,
      birthInfo?: {
        year?: number
        month?: number
        day?: number
        hour_branch?: string
        gender?: string
      },
    ) {
      const moduleProcessStore = useModuleProcessStore()
      const planId = moduleProcessStore.belongPlanId
      const moduleId = moduleProcessStore.moduleId
      if (!planId || typeof moduleId !== 'number') {
        this.error = '无法获取计划ID或模块ID'
        return { success: false }
      }

      // 将对象转为后端期望的字符串格式
      const eightCharactersStr = pillarsToString(eightCharactersObj)

      this.isLoading = true
      this.error = null
      try {
        const response = await eightCharactersService.analyze(eightCharactersStr, luck_cycle, fleet_year)
        if (response.success && response.data) {
          this.analysisResult = response.data

          // 构造出生日期字符串
          const birthday = birthInfo?.year && birthInfo?.month && birthInfo?.day
            ? `${birthInfo.year}-${String(birthInfo.month).padStart(2, '0')}-${String(birthInfo.day).padStart(2, '0')}`
            : undefined
          const gender = birthInfo?.gender || undefined

          // 保存历史记录（后端按 eight_characters + gender 去重，存在则覆盖更新）
          await this.saveHistory({
            plan_id: planId,
            module_id: moduleId,
            eight_characters: eightCharactersStr,
            luck_cycle,
            fleet_year,
            analysis_result: JSON.stringify(response.data),
            birthday,
            birth_time: birthInfo?.hour_branch || undefined,
            gender,
          })
          await this.fetchHistoryList()
          return { success: true, data: response.data }
        } else {
          this.error = response.message || response.error || '分析失败'
          return { success: false }
        }
      } catch (error) {
        this._handleError(error, '八字分析失败')
        return { success: false }
      } finally {
        this.isLoading = false
      }
    },

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
    }) {
      this.error = null
      try {
        await eightCharactersService.saveHistory(params)
      } catch (error) {
        this._handleError(error, '保存历史记录失败')
      }
    },

    async fetchHistoryList() {
      const moduleProcessStore = useModuleProcessStore()
      const planId = moduleProcessStore.belongPlanId
      const moduleId = moduleProcessStore.moduleId
      if (!planId || typeof moduleId !== 'number') {
        this.error = '无法获取计划ID或模块ID'
        return
      }

      this.isLoading = true
      this.error = null
      try {
        const response = await eightCharactersService.getHistoryList(planId, moduleId)
        // 后端返回: { success, data: { records: [...], total: N }, msg }
        const records = response.data?.records
        if (response.success && records) {
          this.historyRecords = records
        } else {
          this.error = response.message || '获取历史记录列表失败'
        }
      } catch (error) {
        this._handleError(error, '获取历史记录列表失败')
      } finally {
        this.isLoading = false
      }
    },

    async getHistoryDetail(eight_characters: string, gender: string) {
      const moduleProcessStore = useModuleProcessStore()
      const planId = moduleProcessStore.belongPlanId
      const moduleId = moduleProcessStore.moduleId
      if (!planId || typeof moduleId !== 'number') {
        this.error = '无法获取计划ID或模块ID'
        return { success: false }
      }

      this.error = null
      try {
        const response = await eightCharactersService.getHistoryDetail(planId, moduleId, eight_characters, gender)
        // 后端返回: { success, data: { record: {...} }, msg }
        const record = response.data?.record
        if (response.success && record) {
          this.selectedRecord = record
          // 将 ANALYSIS_RESULT JSON 解析后设为 analysisResult 以便 Main 展示
          if (record.ANALYSIS_RESULT) {
            try {
              this.analysisResult = JSON.parse(record.ANALYSIS_RESULT)
            } catch {
              this.analysisResult = record.ANALYSIS_RESULT
            }
          }
          return { success: true }
        } else {
          this.error = response.message || '获取记录详情失败'
          return { success: false }
        }
      } catch (error) {
        this._handleError(error, '获取记录详情失败')
        return { success: false }
      }
    },

    selectHistoryRecord(record: HistoryRecord) {
      this.selectedRecord = record
      // 将 ANALYSIS_RESULT JSON 解析后展示
      if (record.ANALYSIS_RESULT) {
        try {
          this.analysisResult = JSON.parse(record.ANALYSIS_RESULT)
        } catch {
          this.analysisResult = record.ANALYSIS_RESULT
        }
      }
    },

    async deleteHistoryRecord(eight_characters: string, gender: string) {
      const moduleProcessStore = useModuleProcessStore()
      const planId = moduleProcessStore.belongPlanId
      const moduleId = moduleProcessStore.moduleId
      if (!planId || typeof moduleId !== 'number') {
        this.error = '无法获取计划ID或模块ID'
        return { success: false }
      }

      this.error = null
      try {
        const response = await eightCharactersService.deleteHistory(planId, moduleId, eight_characters, gender)
        if (response.success) {
          this.historyRecords = this.historyRecords.filter(
            r => !(r.EIGHT_CHARACTERS === eight_characters && r.GENDER === gender)
          )
          if (this.selectedRecord?.EIGHT_CHARACTERS === eight_characters && this.selectedRecord?.GENDER === gender) {
            this.selectedRecord = null
            this.analysisResult = null
          }
          return { success: true }
        } else {
          this.error = response.message || '删除记录失败'
          return { success: false }
        }
      } catch (error) {
        this._handleError(error, '删除记录失败')
        return { success: false }
      }
    },

    /** 公历日期转八字 */
    async convertSolarToBazi(year: number, month: number, day: number, hour_branch?: string, gender?: string) {
      this.error = null
      try {
        const response = await eightCharactersService.convertSolarToBazi(year, month, day, hour_branch, gender)
        if (response.success && response.data) {
          return { success: true, data: response.data }
        } else {
          this.error = response.msg || response.error || '转换失败'
          return { success: false }
        }
      } catch (error) {
        this._handleError(error, '公历转八字失败')
        return { success: false }
      }
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
