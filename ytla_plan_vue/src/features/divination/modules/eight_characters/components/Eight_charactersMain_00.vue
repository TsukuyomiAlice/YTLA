<template>
  <div class="ec-main">
    <h2 class="ec-main__title">{{ $t('divination.modules.eight_characters.main.title') }}</h2>

    <!-- 状态消息 -->
    <div v-if="statusMsg" class="ec-main__status" :class="statusType">{{ statusMsg }}</div>

    <!-- 公历转八字转换 -->
    <section class="ec-main__input-section">
      <h3 class="ec-main__section-title">{{ $t('divination.modules.eight_characters.main.convert_section.title') || '公历转八字' }}</h3>
      <div class="ec-main__convert-grid">
        <div class="ec-main__form-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.convert_section.year') || '年' }}</label>
          <input v-model.number="convertYear" type="number" class="ec-main__input" min="1900" max="2100" placeholder="2024" />
        </div>
        <div class="ec-main__form-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.convert_section.month') || '月' }}</label>
          <select v-model.number="convertMonth" class="ec-main__select">
            <option value="0" disabled>--</option>
            <option v-for="m in 12" :key="m" :value="m">{{ m }}</option>
          </select>
        </div>
        <div class="ec-main__form-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.convert_section.day') || '日' }}</label>
          <select v-model.number="convertDay" class="ec-main__select">
            <option value="0" disabled>--</option>
            <option v-for="d in 31" :key="d" :value="d">{{ d }}</option>
          </select>
        </div>
        <div class="ec-main__form-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.convert_section.hour_branch') || '时辰（可选）' }}</label>
          <select v-model="convertHourBranch" class="ec-main__select">
            <option value="">{{ $t('divination.modules.eight_characters.main.convert_section.no_hour') || '不指定' }}</option>
            <option v-for="opt in hourBranchOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
          </select>
        </div>
        <div class="ec-main__form-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.convert_section.gender') || '性别' }}</label>
          <select v-model="convertGender" class="ec-main__select">
            <option value="">{{ $t('divination.modules.eight_characters.main.convert_section.no_gender') || '不指定' }}</option>
            <option value="male">{{ $t('divination.modules.eight_characters.main.convert_section.male') || '男' }}</option>
            <option value="female">{{ $t('divination.modules.eight_characters.main.convert_section.female') || '女' }}</option>
          </select>
        </div>
        <div class="ec-main__form-group ec-main__convert-btn-group">
          <label class="ec-main__label">&nbsp;</label>
          <button class="ec-main__convert-btn" :disabled="!convertYear || !convertMonth || !convertDay" @click="handleConvert">
            {{ $t('divination.modules.eight_characters.main.convert_section.convert_button') || '转换' }}
          </button>
        </div>
        <div class="ec-main__form-group ec-main__clear-btn-group">
          <label class="ec-main__label">&nbsp;</label>
          <button class="ec-main__clear-btn" @click="handleClearAll">
            {{ $t('divination.modules.eight_characters.main.clear_button') || '清空' }}
          </button>
        </div>
      </div>
      <div v-if="convertResultMsg" class="ec-main__status" :class="convertResultType">{{ convertResultMsg }}</div>
    </section>

    <!-- 输入区域 -->
    <section class="ec-main__input-section">
      <h3 class="ec-main__section-title">{{ $t('divination.modules.eight_characters.main.input_section.title') }}</h3>

      <!-- 四柱输入 -->
      <div class="ec-main__pillars">
        <div class="ec-main__pillar-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.input_section.year_pillar') }}</label>
          <div class="ec-main__pillar-inputs">
            <select v-model="yearPillar.heaven_stem" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="hs in heavenStems" :key="hs" :value="hs">{{ hs }}</option>
            </select>
            <select v-model="yearPillar.earth_branch" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="eb in earthBranches" :key="eb" :value="eb">{{ eb }}</option>
            </select>
          </div>
        </div>

        <div class="ec-main__pillar-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.input_section.month_pillar') }}</label>
          <div class="ec-main__pillar-inputs">
            <select v-model="monthPillar.heaven_stem" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="hs in heavenStems" :key="hs" :value="hs">{{ hs }}</option>
            </select>
            <select v-model="monthPillar.earth_branch" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="eb in earthBranches" :key="eb" :value="eb">{{ eb }}</option>
            </select>
          </div>
        </div>

        <div class="ec-main__pillar-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.input_section.day_pillar') }}</label>
          <div class="ec-main__pillar-inputs">
            <select v-model="dayPillar.heaven_stem" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="hs in heavenStems" :key="hs" :value="hs">{{ hs }}</option>
            </select>
            <select v-model="dayPillar.earth_branch" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="eb in earthBranches" :key="eb" :value="eb">{{ eb }}</option>
            </select>
          </div>
        </div>

        <div class="ec-main__pillar-group">
          <label class="ec-main__label">{{ $t('divination.modules.eight_characters.main.input_section.hour_pillar') }}</label>
          <div class="ec-main__pillar-inputs">
            <select v-model="hourPillar.heaven_stem" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="hs in heavenStems" :key="hs" :value="hs">{{ hs }}</option>
            </select>
            <select v-model="hourPillar.earth_branch" class="ec-main__select">
              <option value="" disabled>--</option>
              <option v-for="opt in hourBranchOptions" :key="opt.value" :value="opt.value">{{ opt.label }}</option>
            </select>
          </div>
        </div>
      </div>

      <!-- 原局分析按钮 -->
      <div class="ec-main__luck-actions">
        <button
          class="ec-main__luck-origin-btn"
          :disabled="store.isLoading"
          @click="handleAnalyzeOrigin"
        >
          {{ $t('divination.modules.eight_characters.main.origin_analysis') || '原局分析' }}
        </button>
      </div>
    </section>

    <!-- 加载状态 -->
    <div v-if="store.isLoading" class="ec-main__loading">
      {{ $t('divination.modules.eight_characters.main.loading') }}
    </div>

    <!-- 错误提示 -->
    <div v-if="store.error" class="ec-main__error">
      {{ store.error }}
      <button class="ec-main__dismiss-btn" @click="store.clearError()">✕</button>
    </div>

    <!-- 大运流年交互区（转换后立即显示） -->
    <section v-if="luckCycleGroups.length > 0" class="ec-main__result-section">
      <h3 class="ec-main__section-title">{{ $t('divination.modules.eight_characters.main.result_section.luck_cycle_table') || '大运流年排盘' }}</h3>

      <!-- 大运流年表格 -->
      <table class="ec-main__luck-table">
        <thead>
          <tr>
            <th v-for="group in luckCycleGroups" :key="group.index" class="ec-main__luck-th">
              <!-- 小运列（不可点击分析大运，点击触发原局分析） -->
              <div v-if="group.type === 'minor'"
                class="ec-main__luck-header ec-main__luck-header--minor"
                @click="handleAnalyzeOrigin"
              >
                <span class="ec-main__luck-badge ec-main__luck-badge--minor">小运</span>
                <span class="ec-main__luck-ganzhi">{{ group.ganzhi }}</span>
                <span class="ec-main__luck-age">{{ group.start_age }}-{{ group.end_age }}岁</span>
                <span class="ec-main__luck-years">{{ group.start_year }}-{{ group.end_year }}年</span>
              </div>
              <!-- 大运列（可点击分析原局+大运） -->
              <div v-else
                class="ec-main__luck-header"
                :class="{ 'ec-main__luck-header--active': selectedLuckCycle === group.ganzhi && analysisMode !== 'origin' }"
                @click="handleAnalyzeLuck(group.ganzhi)"
              >
                <span class="ec-main__luck-badge">{{ group.index }}</span>
                <span class="ec-main__luck-ganzhi">{{ group.ganzhi }}</span>
                <span class="ec-main__luck-age">{{ group.start_age }}-{{ group.end_age }}岁</span>
                <span class="ec-main__luck-years">{{ group.start_year }}-{{ group.end_year }}年</span>
              </div>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="rowIndex in maxFleetRows" :key="rowIndex">
            <td v-for="group in luckCycleGroups" :key="group.index"
              class="ec-main__fleet-td"
              :class="{ 'ec-main__fleet-td--minor': group.type === 'minor' }"
            >
              <div
                v-if="group.fleetYears[rowIndex - 1]"
                class="ec-main__fleet-cell"
                :class="{
                  'ec-main__fleet-cell--active': (group.type === 'minor' && selectedFleetYear === group.fleetYears[rowIndex - 1].ganzhi && analysisMode === 'fleet')
                    || (group.type !== 'minor' && selectedLuckCycle === group.ganzhi && selectedFleetYear === group.fleetYears[rowIndex - 1].ganzhi),
                  'ec-main__fleet-cell--current': group.fleetYears[rowIndex - 1].year === currentYear
                }"
                @click="handleFleetCellClick(group, group.fleetYears[rowIndex - 1].ganzhi)"
              >
                <span class="ec-main__fleet-year-label">{{ group.fleetYears[rowIndex - 1].year }}</span>
                <span class="ec-main__fleet-ganzhi-label">{{ group.fleetYears[rowIndex - 1].ganzhi }}</span>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- 分析结果 -->
    <section v-if="store.analysisResult" class="ec-main__result-section">
      <h3 class="ec-main__section-title">{{ $t('divination.modules.eight_characters.main.result_section.title') }}</h3>

      <!-- 四柱八字展示 -->
      <div class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">{{ $t('divination.modules.eight_characters.main.result_section.eight_characters') }}</h4>
        <div class="ec-main__four-pillars">
          <!-- 大运柱（非原局模式且选中大运时显示） -->
          <div v-if="analysisMode !== 'origin' && selectedLuckCycle" class="ec-main__pillar-card ec-main__pillar-card--luck">
            <span class="ec-main__pillar-label">大运</span>
            <span class="ec-main__pillar-stem"
                  :style="{ color: elementColors[heavenStemElement[luckCyclePillar.heaven_stem]] || '#333' }">
              {{ luckCyclePillar.heaven_stem }}
            </span>
            <span class="ec-main__pillar-branch"
                  :style="{ color: elementColors[earthBranchRelations[luckCyclePillar.earth_branch]?.element] || '#333' }">
              {{ luckCyclePillar.earth_branch }}
            </span>
            <div class="ec-main__hidden-stems">
              <span v-for="stem in (earthBranchRelations[luckCyclePillar.earth_branch]?.hidden || [])"
                    :key="stem" class="ec-main__hidden-stem"
                    :style="{ color: elementColors[heavenStemElement[stem]] || '#333' }">{{ stem }}</span>
            </div>
          </div>
          <!-- 流年柱（流年模式且选中流年时显示） -->
          <div v-if="analysisMode === 'fleet' && selectedFleetYear" class="ec-main__pillar-card ec-main__pillar-card--fleet">
            <span class="ec-main__pillar-label">流年</span>
            <span class="ec-main__pillar-stem"
                  :style="{ color: elementColors[heavenStemElement[fleetYearPillar.heaven_stem]] || '#333' }">
              {{ fleetYearPillar.heaven_stem }}
            </span>
            <span class="ec-main__pillar-branch"
                  :style="{ color: elementColors[earthBranchRelations[fleetYearPillar.earth_branch]?.element] || '#333' }">
              {{ fleetYearPillar.earth_branch }}
            </span>
            <div class="ec-main__hidden-stems">
              <span v-for="stem in (earthBranchRelations[fleetYearPillar.earth_branch]?.hidden || [])"
                    :key="stem" class="ec-main__hidden-stem"
                    :style="{ color: elementColors[heavenStemElement[stem]] || '#333' }">{{ stem }}</span>
            </div>
          </div>
          <!-- 年柱 -->
          <div class="ec-main__pillar-card">
            <span class="ec-main__pillar-label">{{ $t('divination.modules.eight_characters.main.result_section.pillar_year') }}</span>
            <span class="ec-main__pillar-stem"
                  :style="{ color: elementColors[heavenStemElement[fourPillarsData.year?.heaven_stem]] || '#333' }">
              {{ fourPillarsData.year?.heaven_stem || '--' }}
            </span>
            <span class="ec-main__pillar-branch"
                  :style="{ color: elementColors[earthBranchRelations[fourPillarsData.year?.earth_branch]?.element] || '#333' }">
              {{ fourPillarsData.year?.earth_branch || '--' }}
            </span>
            <div v-if="fourPillarsData.year?.earth_branch" class="ec-main__hidden-stems">
              <span v-for="stem in (earthBranchRelations[fourPillarsData.year.earth_branch]?.hidden || [])"
                    :key="stem" class="ec-main__hidden-stem"
                    :style="{ color: elementColors[heavenStemElement[stem]] || '#333' }">{{ stem }}</span>
            </div>
          </div>
          <!-- 月柱 -->
          <div class="ec-main__pillar-card">
            <span class="ec-main__pillar-label">{{ $t('divination.modules.eight_characters.main.result_section.pillar_month') }}</span>
            <span class="ec-main__pillar-stem"
                  :style="{ color: elementColors[heavenStemElement[fourPillarsData.month?.heaven_stem]] || '#333' }">
              {{ fourPillarsData.month?.heaven_stem || '--' }}
            </span>
            <span class="ec-main__pillar-branch"
                  :style="{ color: elementColors[earthBranchRelations[fourPillarsData.month?.earth_branch]?.element] || '#333' }">
              {{ fourPillarsData.month?.earth_branch || '--' }}
            </span>
            <div v-if="fourPillarsData.month?.earth_branch" class="ec-main__hidden-stems">
              <span v-for="stem in (earthBranchRelations[fourPillarsData.month.earth_branch]?.hidden || [])"
                    :key="stem" class="ec-main__hidden-stem"
                    :style="{ color: elementColors[heavenStemElement[stem]] || '#333' }">{{ stem }}</span>
            </div>
          </div>
          <!-- 日柱 -->
          <div class="ec-main__pillar-card">
            <span class="ec-main__pillar-label">{{ $t('divination.modules.eight_characters.main.result_section.pillar_day') }}</span>
            <span class="ec-main__pillar-stem"
                  :style="{ color: elementColors[heavenStemElement[fourPillarsData.day?.heaven_stem]] || '#333' }">
              {{ fourPillarsData.day?.heaven_stem || '--' }}
            </span>
            <span class="ec-main__pillar-branch"
                  :style="{ color: elementColors[earthBranchRelations[fourPillarsData.day?.earth_branch]?.element] || '#333' }">
              {{ fourPillarsData.day?.earth_branch || '--' }}
            </span>
            <div v-if="fourPillarsData.day?.earth_branch" class="ec-main__hidden-stems">
              <span v-for="stem in (earthBranchRelations[fourPillarsData.day.earth_branch]?.hidden || [])"
                    :key="stem" class="ec-main__hidden-stem"
                    :style="{ color: elementColors[heavenStemElement[stem]] || '#333' }">{{ stem }}</span>
            </div>
          </div>
          <!-- 时柱 -->
          <div class="ec-main__pillar-card">
            <span class="ec-main__pillar-label">{{ $t('divination.modules.eight_characters.main.result_section.pillar_hour') }}</span>
            <span class="ec-main__pillar-stem"
                  :style="{ color: elementColors[heavenStemElement[fourPillarsData.hour?.heaven_stem]] || '#333' }">
              {{ fourPillarsData.hour?.heaven_stem || '--' }}
            </span>
            <span class="ec-main__pillar-branch"
                  :style="{ color: elementColors[earthBranchRelations[fourPillarsData.hour?.earth_branch]?.element] || '#333' }">
              {{ fourPillarsData.hour?.earth_branch || '--' }}
            </span>
            <div v-if="fourPillarsData.hour?.earth_branch" class="ec-main__hidden-stems">
              <span v-for="stem in (earthBranchRelations[fourPillarsData.hour.earth_branch]?.hidden || [])"
                    :key="stem" class="ec-main__hidden-stem"
                    :style="{ color: elementColors[heavenStemElement[stem]] || '#333' }">{{ stem }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 十神分析（原局） -->
      <div v-if="tenGodsData.length > 0" class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">{{ $t('divination.modules.eight_characters.main.result_section.ten_gods') }}</h4>
        <div class="ec-main__ten-gods-grid">
          <div
            v-for="(item, index) in tenGodsData"
            :key="index"
            class="ec-main__ten-god-item"
          >
            <span class="ec-main__ten-god-name" :style="{ color: getTenGodColor(item.ten_god) }">{{ item.ten_god }}</span>
            <span class="ec-main__ten-god-ratio">{{ item.ratio }}%</span>
          </div>
        </div>
      </div>

      <!-- 大运十神权重（大运/流年模式下显示） -->
      <div v-if="analysisMode !== 'origin' && luckCycleGodsData.length > 0" class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">{{ $t('divination.modules.eight_characters.main.result_section.luck_ten_gods') }}</h4>
        <div class="ec-main__ten-gods-grid">
          <div
            v-for="(item, index) in luckCycleGodsData"
            :key="index"
            class="ec-main__ten-god-item"
          >
            <span class="ec-main__ten-god-name" :style="{ color: getTenGodColor(item.ten_god) }">{{ item.ten_god }}</span>
            <span class="ec-main__ten-god-ratio">{{ item.ratio }}%</span>
          </div>
        </div>
      </div>

      <!-- 流年十神权重（流年模式下显示） -->
      <div v-if="analysisMode === 'fleet' && fleetYearGodsData.length > 0" class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">{{ $t('divination.modules.eight_characters.main.result_section.fleet_ten_gods') }}</h4>
        <div class="ec-main__ten-gods-grid">
          <div
            v-for="(item, index) in fleetYearGodsData"
            :key="index"
            class="ec-main__ten-god-item"
          >
            <span class="ec-main__ten-god-name" :style="{ color: getTenGodColor(item.ten_god) }">{{ item.ten_god }}</span>
            <span class="ec-main__ten-god-ratio">{{ item.ratio }}%</span>
          </div>
        </div>
      </div>

      <!-- 十神占比柱状图（三联对比：原局/大运/流年） -->
      <div v-if="tenGodChartData.length > 0" class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">十神占比对比</h4>
        <div class="ec-main__chart-legend">
          <span class="ec-main__chart-legend-item">
            <span class="ec-main__chart-legend-dot ec-main__chart-legend-dot--origin"></span>原局
          </span>
          <span class="ec-main__chart-legend-item">
            <span class="ec-main__chart-legend-dot ec-main__chart-legend-dot--luck"></span>大运
          </span>
          <span class="ec-main__chart-legend-item">
            <span class="ec-main__chart-legend-dot ec-main__chart-legend-dot--fleet"></span>流年
          </span>
        </div>
        <div class="ec-main__chart-container">
          <!-- Y轴刻度 -->
          <div class="ec-main__chart-yaxis">
            <span>100%</span>
            <span>80%</span>
            <span>60%</span>
            <span>40%</span>
            <span>20%</span>
            <span>0%</span>
          </div>
          <!-- 柱状区域 -->
          <div class="ec-main__chart-bars">
            <div
              v-for="group in tenGodChartData"
              :key="group.name"
              class="ec-main__chart-group"
            >
              <div class="ec-main__chart-bar-wrapper">
                <!-- 原局柱 -->
                <div class="ec-main__chart-bar ec-main__chart-bar--origin"
                     :style="{ height: group.originRatio + '%' }"
                     :title="'原局 ' + group.name + ': ' + group.originRatio + '%'">
                  <span class="ec-main__chart-bar-val">{{ group.originRatio }}%</span>
                </div>
                <!-- 大运柱 -->
                <div v-if="analysisMode !== 'origin'"
                     class="ec-main__chart-bar ec-main__chart-bar--luck"
                     :style="{ height: group.luckRatio + '%' }"
                     :title="'大运 ' + group.name + ': ' + group.luckRatio + '%'">
                  <span class="ec-main__chart-bar-val">{{ group.luckRatio }}%</span>
                </div>
                <!-- 流年柱 -->
                <div v-if="analysisMode === 'fleet'"
                     class="ec-main__chart-bar ec-main__chart-bar--fleet"
                     :style="{ height: group.fleetRatio + '%' }"
                     :title="'流年 ' + group.name + ': ' + group.fleetRatio + '%'">
                  <span class="ec-main__chart-bar-val">{{ group.fleetRatio }}%</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- X轴标签（与柱状区域保持相同偏移对齐） -->
        <div class="ec-main__chart-xlabels">
          <span
            v-for="group in tenGodChartData"
            :key="group.name"
            class="ec-main__chart-label"
            :style="{ color: getTenGodColor(group.name) }"
          >{{ group.name }}</span>
        </div>
      </div>

      <!-- 大运分析（大运/流年模式下显示） -->
      <div v-if="analysisMode !== 'origin' && luckCycleAnalysisText" class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">{{ $t('divination.modules.eight_characters.main.result_section.luck_cycle_analysis') }}</h4>
        <p class="ec-main__analysis-text">{{ luckCycleAnalysisText }}</p>
      </div>

      <!-- 流年分析（流年模式下显示） -->
      <div v-if="analysisMode === 'fleet' && fleetYearAnalysisText" class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">{{ $t('divination.modules.eight_characters.main.result_section.fleet_year_analysis') }}</h4>
        <p class="ec-main__analysis-text">{{ fleetYearAnalysisText }}</p>
      </div>

      <!-- 综合批注（流年模式下显示） -->
      <div v-if="analysisMode === 'fleet' && summaryText" class="ec-main__result-block">
        <h4 class="ec-main__result-block-title">{{ $t('divination.modules.eight_characters.main.result_section.summary') }}</h4>
        <p class="ec-main__analysis-text ec-main__summary-text">{{ summaryText }}</p>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { computed, onActivated, reactive, ref, watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useEightCharactersStore } from '@/features/divination/modules/eight_characters/stores/eightCharactersStore.ts'

const store = useEightCharactersStore()
const { t } = useI18n()

// 天干和地支选项
const heavenStems = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
const earthBranches = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

// 天干 → 五行映射
const heavenStemElement: Record<string, string> = {
  '甲': '木', '乙': '木',
  '丙': '火', '丁': '火',
  '戊': '土', '己': '土',
  '庚': '金', '辛': '金',
  '壬': '水', '癸': '水',
}

// 地支 → { 五行, 藏干(去重) } 映射
const earthBranchRelations: Record<string, { element: string; hidden: string[] }> = {
  '子': { element: '水', hidden: ['癸'] },
  '丑': { element: '土', hidden: ['己', '癸', '辛'] },
  '寅': { element: '木', hidden: ['甲', '丙', '戊'] },
  '卯': { element: '木', hidden: ['乙'] },
  '辰': { element: '土', hidden: ['戊', '己', '癸'] },
  '巳': { element: '火', hidden: ['丙', '庚', '戊'] },
  '午': { element: '火', hidden: ['丁', '己'] },
  '未': { element: '土', hidden: ['己', '丁', '乙'] },
  '申': { element: '金', hidden: ['庚', '壬', '戊'] },
  '酉': { element: '金', hidden: ['辛'] },
  '戌': { element: '土', hidden: ['戊', '辛', '丁'] },
  '亥': { element: '水', hidden: ['壬', '甲'] },
}

// 五行 → 显示颜色
const elementColors: Record<string, string> = {
  '木': '#4CAF50',
  '火': '#F44336',
  '土': '#8D6E63',
  '金': '#FFC107',
  '水': '#2196F3',
}

// 十神 → 天干 关系表（key=日主天干, value={天干: 十神名称}）
const tenGodsRelationship: Record<string, Record<string, string>> = {
  '甲': { '甲': '比肩', '乙': '劫财', '壬': '枭神', '癸': '正印', '丙': '食神', '丁': '伤官', '庚': '七杀', '辛': '正官', '戊': '偏财', '己': '正财' },
  '乙': { '乙': '比肩', '甲': '劫财', '癸': '枭神', '壬': '正印', '丁': '食神', '丙': '伤官', '辛': '七杀', '庚': '正官', '己': '偏财', '戊': '正财' },
  '丙': { '丙': '比肩', '丁': '劫财', '甲': '枭神', '乙': '正印', '戊': '食神', '己': '伤官', '壬': '七杀', '癸': '正官', '庚': '偏财', '辛': '正财' },
  '丁': { '丁': '比肩', '丙': '劫财', '乙': '枭神', '甲': '正印', '己': '食神', '戊': '伤官', '癸': '七杀', '壬': '正官', '辛': '偏财', '庚': '正财' },
  '戊': { '戊': '比肩', '己': '劫财', '丙': '枭神', '丁': '正印', '庚': '食神', '辛': '伤官', '甲': '七杀', '乙': '正官', '壬': '偏财', '癸': '正财' },
  '己': { '己': '比肩', '戊': '劫财', '丁': '枭神', '丙': '正印', '辛': '食神', '庚': '伤官', '乙': '七杀', '甲': '正官', '癸': '偏财', '壬': '正财' },
  '庚': { '庚': '比肩', '辛': '劫财', '戊': '枭神', '己': '正印', '癸': '食神', '壬': '伤官', '丙': '七杀', '丁': '正官', '甲': '偏财', '乙': '正财' },
  '辛': { '辛': '比肩', '庚': '劫财', '己': '枭神', '戊': '正印', '壬': '食神', '癸': '伤官', '丁': '七杀', '丙': '正官', '乙': '偏财', '甲': '正财' },
  '壬': { '壬': '比肩', '癸': '劫财', '庚': '枭神', '辛': '正印', '甲': '食神', '乙': '伤官', '戊': '七杀', '己': '正官', '丙': '偏财', '丁': '正财' },
  '癸': { '癸': '比肩', '壬': '劫财', '辛': '枭神', '庚': '正印', '乙': '食神', '甲': '伤官', '己': '七杀', '戊': '正官', '丁': '偏财', '丙': '正财' },
}

// 时辰选项（带时间范围）
const hourBranchOptions = [
  { value: '子', label: '子时 (23:00 - 01:00)' },
  { value: '丑', label: '丑时 (01:00 - 03:00)' },
  { value: '寅', label: '寅时 (03:00 - 05:00)' },
  { value: '卯', label: '卯时 (05:00 - 07:00)' },
  { value: '辰', label: '辰时 (07:00 - 09:00)' },
  { value: '巳', label: '巳时 (09:00 - 11:00)' },
  { value: '午', label: '午时 (11:00 - 13:00)' },
  { value: '未', label: '未时 (13:00 - 15:00)' },
  { value: '申', label: '申时 (15:00 - 17:00)' },
  { value: '酉', label: '酉时 (17:00 - 19:00)' },
  { value: '戌', label: '戌时 (19:00 - 21:00)' },
  { value: '亥', label: '亥时 (21:00 - 23:00)' },
]

// 四柱输入数据
const yearPillar = reactive({ heaven_stem: '', earth_branch: '' })
const monthPillar = reactive({ heaven_stem: '', earth_branch: '' })
const dayPillar = reactive({ heaven_stem: '', earth_branch: '' })
const hourPillar = reactive({ heaven_stem: '', earth_branch: '' })

// 公历转八字 转换表单
const convertYear = ref<number | undefined>(undefined)
const convertMonth = ref<number>(0)
const convertDay = ref<number>(0)
const convertHourBranch = ref('')
const convertGender = ref('')

// 转换结果中的大运表和流年表
const convertLuckCycleTable = ref<Array<{type: string; index: number; ganzhi: string; start_age: number; end_age: number; start_year: number; end_year: number}>>([])
const convertFleetYears = ref<Array<{year: number; ganzhi: string}>>([])
const currentYear = new Date().getFullYear()

// 分析模式追踪
const analysisMode = ref<'origin' | 'luck' | 'fleet'>('origin')
const selectedLuckCycle = ref('')
const selectedFleetYear = ref('')

// 转换结果消息
const convertResultMsg = ref('')
const convertResultType = ref<'success' | 'error'>('success')

// 年份转干支工具函数
function yearToGanZhi(year: number): string {
  if (!year || year < 1) return ''
  const stem = heavenStems[(year - 4) % 10]
  const branch = earthBranches[(year - 4) % 12]
  return `${stem}${branch}`
}

// 从干支字符串（如"甲子"）拆分天干和地支
function splitGanZhi(ganzhi: string): { heaven_stem: string; earth_branch: string } {
  if (!ganzhi || ganzhi.length < 2) return { heaven_stem: '', earth_branch: '' }
  return { heaven_stem: ganzhi[0], earth_branch: ganzhi[1] }
}

// 公历转八字处理
async function handleConvert() {
  // 每次转换前清理分析结果
  store.analysisResult = null
  analysisMode.value = 'origin'
  selectedLuckCycle.value = ''
  selectedFleetYear.value = ''

  convertResultMsg.value = ''
  store.clearError()
  if (!convertYear.value || !convertMonth.value || !convertDay.value) {
    convertResultMsg.value = '请填写完整的年月日'
    convertResultType.value = 'error'
    return
  }
  const result = await store.convertSolarToBazi(
    convertYear.value,
    convertMonth.value,
    convertDay.value,
    convertHourBranch.value || undefined,
    convertGender.value || undefined,
  )
  if (result.success && result.data) {
    const fp = result.data.four_pillars
    // 自动填充四柱
    yearPillar.heaven_stem = fp.year.heavenly_stem
    yearPillar.earth_branch = fp.year.earthly_branch
    monthPillar.heaven_stem = fp.month.heavenly_stem
    monthPillar.earth_branch = fp.month.earthly_branch
    dayPillar.heaven_stem = fp.day.heavenly_stem
    dayPillar.earth_branch = fp.day.earthly_branch
    hourPillar.heaven_stem = fp.hour.heavenly_stem
    hourPillar.earth_branch = fp.hour.earthly_branch
    // 保存大运表和流年表
    convertLuckCycleTable.value = result.data.luck_cycle_table || []
    convertFleetYears.value = result.data.fleet_years || []
    convertResultMsg.value = `转换成功：${result.data.eight_characters}`
    convertResultType.value = 'success'
  } else {
    convertResultMsg.value = store.error || '转换失败'
    convertResultType.value = 'error'
  }
}

// 状态消息
const statusMsg = ref('')
const statusType = ref<'success' | 'error'>('success')

// ---- computed: 从 analysisResult 中提取展示数据 ----

// 四柱数据 - 匹配后端 eight_characters_parts 结构
const fourPillarsData = computed(() => {
  const r = store.analysisResult
  if (!r?.eight_characters_parts) return { year: null, month: null, day: null, hour: null }
  const p = r.eight_characters_parts
  return {
    year: p.year ? { heaven_stem: p.year.heavenly_stem, earth_branch: p.year.earthly_branch } : null,
    month: p.month ? { heaven_stem: p.month.heavenly_stem, earth_branch: p.month.earthly_branch } : null,
    day: p.day ? { heaven_stem: p.day.heavenly_stem, earth_branch: p.day.earthly_branch } : null,
    hour: p.hour ? { heaven_stem: p.hour.heavenly_stem, earth_branch: p.hour.earthly_branch } : null,
  }
})

// 构建十神名称 → 五行 的映射（基于当前日主天干）
const tenGodElementMap = computed(() => {
  const dayStem = fourPillarsData.value.day?.heaven_stem
  if (!dayStem || !tenGodsRelationship[dayStem]) return {}
  const relation = tenGodsRelationship[dayStem]  // e.g. {甲: "比肩", 乙: "劫财", ...}
  const map: Record<string, string> = {}
  for (const [stem, godName] of Object.entries(relation)) {
    map[godName] = heavenStemElement[stem] || ''
  }
  return map
})

// 获取十神名称对应的五行颜色
function getTenGodColor(tenGodName: string): string {
  const element = tenGodElementMap.value[tenGodName]
  return element ? (elementColors[element] || '#333') : '#333'
}

// 当前选中的大运柱（用于四柱展示区扩展显示）
const luckCyclePillar = computed(() => splitGanZhi(selectedLuckCycle.value))

// 当前选中的流年柱（用于四柱展示区扩展显示）
const fleetYearPillar = computed(() => splitGanZhi(selectedFleetYear.value))

// 十神权重数据 - 匹配后端 ten_god_results.origin_ratio
// 十神显示顺序
const tenGodOrder = ['比肩', '劫财', '枭神', '正印', '食神', '伤官', '七杀', '正官', '偏财', '正财']

const tenGodsData = computed(() => {
  const r = store.analysisResult
  if (!r?.ten_god_results?.origin_ratio) return []
  const ratio = r.ten_god_results.origin_ratio
  return Object.entries(ratio).map(([name, value]) => ({
    ten_god: name,
    ratio: value,
  })).sort((a, b) => tenGodOrder.indexOf(a.ten_god) - tenGodOrder.indexOf(b.ten_god))
})

// 大运输入（用于展示）
const luckCycleInput = computed(() => {
  return store.analysisResult?.input?.luck_cycle || ''
})

// 流年输入（用于展示）
const fleetYearInput = computed(() => {
  return store.analysisResult?.input?.fleet_year || ''
})

// 大运十神权重
const luckCycleGodsData = computed(() => {
  const r = store.analysisResult
  if (!r?.ten_god_results?.luck_ratio) return []
  return Object.entries(r.ten_god_results.luck_ratio).map(([name, value]) => ({
    ten_god: name,
    ratio: value,
  })).sort((a, b) => tenGodOrder.indexOf(a.ten_god) - tenGodOrder.indexOf(b.ten_god))
})

// 流年十神权重
const fleetYearGodsData = computed(() => {
  const r = store.analysisResult
  if (!r?.ten_god_results?.fleet_ratio) return []
  return Object.entries(r.ten_god_results.fleet_ratio).map(([name, value]) => ({
    ten_god: name,
    ratio: value,
  })).sort((a, b) => tenGodOrder.indexOf(a.ten_god) - tenGodOrder.indexOf(b.ten_god))
})

// 柱状图数据：十神三柱对比（合并原局/大运/流年）
const tenGodChartData = computed(() => {
  const originMap = Object.fromEntries(tenGodsData.value.map(d => [d.ten_god, d.ratio]))
  const luckMap = Object.fromEntries(luckCycleGodsData.value.map(d => [d.ten_god, d.ratio]))
  const fleetMap = Object.fromEntries(fleetYearGodsData.value.map(d => [d.ten_god, d.ratio]))

  return tenGodOrder.map(name => ({
    name,
    originRatio: originMap[name] || 0,
    luckRatio: luckMap[name] || 0,
    fleetRatio: fleetMap[name] || 0,
  }))
})

// 大运排盘表（从转换结果或 analysisResult 中读取）
const luckCycleTable = computed(() => {
  if (convertLuckCycleTable.value.length > 0) return convertLuckCycleTable.value
  return store.analysisResult?.luck_cycle_table || []
})

// 流年列表（从转换结果或 analysisResult 中读取）
const fleetYearsList = computed(() => {
  if (convertFleetYears.value.length > 0) return convertFleetYears.value
  return store.analysisResult?.fleet_years || []
})

// 大运流年分组：将流年按大运的时间范围分组
const luckCycleGroups = computed(() => {
  return luckCycleTable.value.map(luck => {
    const fleetYearsInRange = fleetYearsList.value.filter(fy =>
      fy.year >= luck.start_year && fy.year <= luck.end_year
    )
    return { ...luck, fleetYears: fleetYearsInRange }
  })
})

// 最大流年行数（表格行数）
const maxFleetRows = computed(() => {
  let max = 0
  for (const group of luckCycleGroups.value) {
    if (group.fleetYears.length > max) {
      max = group.fleetYears.length
    }
  }
  return max
})

// ---- 方法 ----

function clearStatus() {
  statusMsg.value = ''
}

const handleAnalyze = async (luckCycleStr?: string, fleetYearStr?: string) => {
  clearStatus()
  store.clearError()

  // 构建八字输入数据
  const eightCharacters = {
    year_pillar: { ...yearPillar },
    month_pillar: { ...monthPillar },
    day_pillar: { ...dayPillar },
    hour_pillar: { ...hourPillar },
  }

  // 如果未传入参数，则只分析原局
  const luckCycle = luckCycleStr || ''
  const fleetYear = fleetYearStr || ''

  // 收集出生日期信息（从转换表单），用于保存历史记录时存档
  const birthInfo = convertYear.value && convertMonth.value && convertDay.value
    ? {
        year: convertYear.value,
        month: convertMonth.value,
        day: convertDay.value,
        hour_branch: convertHourBranch.value || undefined,
        gender: convertGender.value || undefined,
      }
    : undefined

  const result = await store.analyze(eightCharacters, luckCycle, fleetYear, birthInfo)
  if (result.success) {
    statusMsg.value = '分析完成'
    statusType.value = 'success'
  } else {
    statusMsg.value = store.error || t('divination.modules.eight_characters.main.error.analysis_failed')
    statusType.value = 'error'
  }
}

// 点击"开始分析"按钮 - 只分析原局
const handleAnalyzeOrigin = async () => {
  analysisMode.value = 'origin'
  selectedLuckCycle.value = ''
  selectedFleetYear.value = ''
  await handleAnalyze()
}

// 点击大运 - 分析原局 + 大运
const handleAnalyzeLuck = async (ganzhi: string) => {
  analysisMode.value = 'luck'
  selectedLuckCycle.value = ganzhi
  selectedFleetYear.value = ''
  await handleAnalyze(ganzhi)
}

// 点击流年 - 分析原局 + 大运 + 流年
const handleAnalyzeFleet = async (luckGanzhi: string, fleetGanzhi: string) => {
  analysisMode.value = 'luck'
  selectedLuckCycle.value = luckGanzhi
  selectedFleetYear.value = fleetGanzhi
  analysisMode.value = 'fleet'
  await handleAnalyze(luckGanzhi, fleetGanzhi)
}

// 点击流年单元格（支持小运列和大运列）
const handleFleetCellClick = async (group: { type: string; ganzhi: string }, fleetGanzhi: string) => {
  if (group.type === 'minor') {
    // 小运下的流年：仅分析原局 + 流年（无大运）
    analysisMode.value = 'fleet'
    selectedLuckCycle.value = ''
    selectedFleetYear.value = fleetGanzhi
    await handleAnalyze('', fleetGanzhi)
  } else {
    // 大运下的流年：分析原局 + 大运 + 流年
    await handleAnalyzeFleet(group.ganzhi, fleetGanzhi)
  }
}

// 每次切换进该页面时清理分析结果
onActivated(() => {
  store.analysisResult = null
  analysisMode.value = 'origin'
  selectedLuckCycle.value = ''
  selectedFleetYear.value = ''
})

// 清空按钮：清除所有在 main 区域已输入或预先载入的内容
function handleClearAll() {
  // 清空四柱输入
  yearPillar.heaven_stem = ''
  yearPillar.earth_branch = ''
  monthPillar.heaven_stem = ''
  monthPillar.earth_branch = ''
  dayPillar.heaven_stem = ''
  dayPillar.earth_branch = ''
  hourPillar.heaven_stem = ''
  hourPillar.earth_branch = ''
  // 清空公历转换表单
  convertYear.value = undefined
  convertMonth.value = 0
  convertDay.value = 0
  convertHourBranch.value = ''
  convertGender.value = ''
  // 清空转换结果
  convertLuckCycleTable.value = []
  convertFleetYears.value = []
  convertResultMsg.value = ''
  // 清空分析结果
  store.analysisResult = null
  analysisMode.value = 'origin'
  selectedLuckCycle.value = ''
  selectedFleetYear.value = ''
  // 清空状态消息
  statusMsg.value = ''
  store.clearError()
}

// 当 Sub 选中历史记录时，自动填充输入，并尝试从出生日期计算大运表
watch(
  () => store.selectedRecord,
  async (record) => {
    analysisMode.value = 'origin'
    selectedLuckCycle.value = ''
    selectedFleetYear.value = ''
    convertLuckCycleTable.value = []
    convertFleetYears.value = []

    if (!record?.EIGHT_CHARACTERS) return
    const ec = record.EIGHT_CHARACTERS // 如 "癸酉辛酉壬申己丑"
    // 每2个字一柱: 年[0-1], 月[2-3], 日[4-5], 时[6-7]
    if (ec.length >= 2) {
      yearPillar.heaven_stem = ec[0] || ''
      yearPillar.earth_branch = ec[1] || ''
    }
    if (ec.length >= 4) {
      monthPillar.heaven_stem = ec[2] || ''
      monthPillar.earth_branch = ec[3] || ''
    }
    if (ec.length >= 6) {
      dayPillar.heaven_stem = ec[4] || ''
      dayPillar.earth_branch = ec[5] || ''
    }
    if (ec.length >= 8) {
      hourPillar.heaven_stem = ec[6] || ''
      hourPillar.earth_branch = ec[7] || ''
    }

    // 从 store.analysisResult 恢复大运表数据（由 selectHistoryRecord 已解析好）
    let hasLuckData = false
    if (store.analysisResult?.luck_cycle_table?.length) {
      convertLuckCycleTable.value = store.analysisResult.luck_cycle_table
      hasLuckData = true
    }
    if (store.analysisResult?.fleet_years?.length) {
      convertFleetYears.value = store.analysisResult.fleet_years
    }

    // 同步填充公历转换表单，使得后续点击大运/流年时能获取到出生日期和性别
    if (record.BIRTHDAY) {
      const parts = record.BIRTHDAY.split(/[-/]/)
      if (parts.length === 3) {
        convertYear.value = parseInt(parts[0], 10) || undefined
        convertMonth.value = parseInt(parts[1], 10) || 0
        convertDay.value = parseInt(parts[2], 10) || 0
      }
    }
    convertHourBranch.value = record.BIRTH_TIME || ''
    convertGender.value = record.GENDER || ''

    // 如果 analysisResult 中没有大运表数据，且记录有出生日期，重新计算大运表
    if (!hasLuckData && record.BIRTHDAY) {
      const parts = record.BIRTHDAY.split(/[-/]/)
      if (parts.length === 3) {
        const year = parseInt(parts[0], 10)
        const month = parseInt(parts[1], 10)
        const day = parseInt(parts[2], 10)
        if (!isNaN(year) && !isNaN(month) && !isNaN(day)) {
          const result = await store.convertSolarToBazi(
            year,
            month,
            day,
            record.BIRTH_TIME || undefined,
            record.GENDER || undefined,
          )
          if (result.success && result.data) {
            convertLuckCycleTable.value = result.data.luck_cycle_table || []
            convertFleetYears.value = result.data.fleet_years || []
          }
        }
      }
    }
  },
)
</script>

<style scoped lang="scss">
.ec-main {
  padding: 20px;

  &__title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: #333;
  }

  &__section-title {
    font-size: 1.0625rem;
    font-weight: 600;
    margin-bottom: 0.875rem;
    color: #333;
  }

  &__status {
    padding: 8px 12px;
    margin-bottom: 0.75rem;
    border-radius: 4px;
    font-size: 0.875rem;

    &.success {
      color: #2e7d32;
      background: #e8f5e9;
    }

    &.error {
      color: #d32f2f;
      background: #fdecea;
    }
  }

  &__loading {
    text-align: center;
    padding: 2rem;
    color: #666;
    font-size: 0.9375rem;
  }

  &__error {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 14px;
    margin-bottom: 1rem;
    border-radius: 6px;
    background: #fff2f0;
    border: 1px solid #ffccc7;
    color: #d32f2f;
    font-size: 0.875rem;
  }

  &__dismiss-btn {
    flex-shrink: 0;
    width: 24px;
    height: 24px;
    border: none;
    background: transparent;
    border-radius: 50%;
    cursor: pointer;
    font-size: 0.8125rem;
    color: #d32f2f;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.2s;

    &:hover {
      background-color: #ffd4d0;
    }
  }

  // ---- 输入区域 ----
  &__input-section {
    background: #fafafa;
    border: 1px solid #e8e8e8;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 1.25rem;
  }

  &__pillars {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 1.25rem;
  }

  &__pillar-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  &__label {
    font-size: 0.875rem;
    font-weight: 500;
    color: #555;
  }

  &__pillar-inputs {
    display: flex;
    gap: 8px;
  }

  &__select {
    flex: 1;
    padding: 6px 10px;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    font-size: 0.9375rem;
    background: white;
    color: #333;
    cursor: pointer;
    transition: border-color 0.2s;
    font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;

    &:focus {
      outline: none;
      border-color: #1976d2;
      box-shadow: 0 0 0 2px rgba(25, 118, 210, 0.12);
    }
  }

  &__extra-inputs {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 1rem;
  }

  &__form-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  &__input {
    padding: 6px 10px;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    font-size: 0.9375rem;
    color: #333;
    transition: border-color 0.2s;

    &:focus {
      outline: none;
      border-color: #1976d2;
      box-shadow: 0 0 0 2px rgba(25, 118, 210, 0.12);
    }

    &::placeholder {
      color: #bbb;
    }
  }

  &__convert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(185px, 1fr));
    gap: 12px;
    align-items: end;
  }

  &__convert-btn-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  &__clear-btn-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  &__convert-btn {
    padding: 6px 16px;
    border: none;
    border-radius: 4px;
    background: #388e3c;
    color: white;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s;
    white-space: nowrap;

    &:hover:not(:disabled) {
      background: #2e7d32;
    }

    &:disabled {
      background: #a5d6a7;
      cursor: not-allowed;
    }
  }

  &__clear-btn {
    padding: 6px 16px;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    background: white;
    color: #666;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;

    &:hover {
      background: #f5f5f5;
      border-color: #bbb;
      color: #333;
    }
  }

  &__year-input {
    margin-top: 4px;
    font-size: 0.8125rem;
  }

  &__actions {
    display: flex;
    justify-content: flex-start;
  }

  &__analyze-btn {
    padding: 10px 28px;
    border: none;
    border-radius: 6px;
    background: #1976d2;
    color: white;
    font-size: 0.9375rem;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s;

    &:hover:not(:disabled) {
      background: #1565c0;
    }

    &:disabled {
      background: #90caf9;
      cursor: not-allowed;
    }
  }

  // ---- 结果区域 ----
  &__result-section {
    margin-top: 1rem;
  }

  &__result-block {
    background: #fafafa;
    border: 1px solid #e8e8e8;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 1rem;
  }

  &__result-block-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.875rem;
    color: #333;
  }

  // 四柱卡片
  &__four-pillars {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 12px;

    @media (max-width: 640px) {
      grid-template-columns: repeat(3, 1fr);
    }
  }

  &__pillar-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 16px 8px;
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    gap: 4px;
  }

  &__pillar-card--luck {
    border-color: #ff9800;
    background: #fff8e1;
  }

  &__pillar-card--fleet {
    border-color: #7c4dff;
    background: #f3e5f5;
  }

  &__pillar-label {
    font-size: 0.8125rem;
    color: #888;
    font-weight: 500;
  }

  &__pillar-stem {
    font-size: 1.375rem;
    font-weight: 700;
    font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
  }

  &__pillar-branch {
    font-size: 1.375rem;
    font-weight: 700;
    font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
  }

  // 地支藏干
  &__hidden-stems {
    display: flex;
    gap: 3px;
    margin-top: 2px;
  }

  &__hidden-stem {
    font-size: 0.75rem;
    font-weight: 500;
    background: #f5f5f5;
    padding: 1px 4px;
    border-radius: 3px;
    line-height: 1.4;
  }

  // 十神网格
  &__ten-gods-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  &__ten-god-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px 16px;
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    min-width: 72px;
  }

  &__ten-god-name {
    font-size: 0.8125rem;
    color: #555;
    margin-bottom: 4px;
  }

  &__ten-god-ratio {
    font-size: 1.125rem;
    font-weight: 700;
    color: #1976d2;
  }

  // 十神占比柱状图
  &__chart-legend {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 12px;
  }

  &__chart-legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.8125rem;
    color: #555;
  }

  &__chart-legend-dot {
    display: inline-block;
    width: 12px;
    height: 12px;
    border-radius: 2px;

    &--origin { background: #42a5f5; }
    &--luck   { background: #ec407a; }
    &--fleet  { background: #7c4dff; }
  }

  &__chart-container {
    display: flex;
    gap: 8px;
    height: 240px;
  }

  &__chart-yaxis {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding-right: 8px;
    border-right: 1px solid #e0e0e0;
    width: 45px;
    text-align: right;
    flex-shrink: 0;

    span {
      font-size: 0.6875rem;
      color: #999;
    }
  }

  &__chart-bars {
    display: flex;
    flex: 1;
    justify-content: space-around;
    gap: 4px;
  }

  &__chart-group {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    flex: 1;
    max-width: 56px;
  }

  &__chart-bar-wrapper {
    display: flex;
    align-items: flex-end;
    gap: 2px;
    flex: 1;
    width: 100%;
  }

  &__chart-bar {
    flex: 1;
    border-radius: 3px 3px 0 0;
    position: relative;
    transition: height 0.3s ease;
    min-height: 2px;

    &--origin { background: #42a5f5; }
    &--luck   { background: #ec407a; }
    &--fleet  { background: #7c4dff; }
  }

  &__chart-bar-val {
    position: absolute;
    top: -16px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.625rem;
    font-weight: 600;
    color: #555;
    white-space: nowrap;
  }

  // X轴标签行（padding-left 偏移对齐 Y 轴宽度 + gap）
  &__chart-xlabels {
    display: flex;
    justify-content: space-around;
    gap: 4px;
    margin-top: 4px;
    padding-left: 54px;
  }

  &__chart-label {
    flex: 1;
    max-width: 56px;
    font-size: 0.75rem;
    font-weight: 600;
    text-align: center;
    white-space: nowrap;
  }

  // 旧表格保留（向后兼容）
  &__table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;

    th, td {
      padding: 8px 12px;
      text-align: left;
      border-bottom: 1px solid #e8e8e8;
    }

    th {
      background: #f0f0f0;
      font-weight: 600;
      color: #555;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:hover td {
      background: #f5f5f5;
    }
  }

  // 分析文本
  &__analysis-text {
    font-size: 0.9375rem;
    line-height: 1.6;
    color: #444;
    white-space: pre-wrap;
    margin: 0;
  }

  &__summary-text {
    color: #333;
    font-weight: 500;
    background: #fffbe6;
    padding: 12px 16px;
    border-radius: 6px;
    border-left: 4px solid #faad14;
  }

  // ---- 大运流年交互区 ----

  &__luck-actions {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 1rem;
  }

  &__luck-origin-btn {
    padding: 8px 20px;
    border: 2px solid #1976d2;
    border-radius: 6px;
    background: white;
    color: #1976d2;
    font-size: 0.875rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;

    &:hover:not(:disabled) {
      background: #e3f2fd;
    }

    &:disabled {
      border-color: #bbb;
      color: #999;
      cursor: not-allowed;
    }

    &--active {
      background: #1976d2;
      color: white;
      box-shadow: 0 2px 8px rgba(25, 118, 210, 0.3);

      &:hover:not(:disabled) {
        background: #1565c0;
      }
    }
  }

  &__luck-hint {
    font-size: 0.8125rem;
    color: #888;
    font-style: italic;
  }

  // ---- 大运流年表格 ----

  &__luck-table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
  }

  &__luck-th {
    padding: 0;
    border: 1px solid #e0e0e0;
    background: #fafafa;
    vertical-align: top;
  }

  &__luck-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
    padding: 10px 8px;
    cursor: pointer;
    transition: all 0.2s;
    user-select: none;

    &:hover {
      background: #eef3f9;
    }

    &--active {
      background: #e3f2fd;
      box-shadow: inset 0 -3px 0 #1976d2;

      &:hover {
        background: #bbdefb;
      }
    }

    &--minor {
      cursor: default;
      background: #f5f0eb;

      &:hover {
        background: #efe6dc;
      }
    }
  }

  &__luck-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 26px;
    height: 26px;
    background: #1976d2;
    color: white;
    border-radius: 50%;
    font-size: 0.75rem;
    font-weight: 700;

    &--minor {
      width: auto;
      height: auto;
      border-radius: 4px;
      background: #8d6e63;
      padding: 3px 8px;
      font-size: 0.75rem;
      font-weight: 600;
    }
  }

  &__luck-ganzhi {
    font-weight: 700;
    color: #c62828;
    font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
    font-size: 1rem;
  }

  &__luck-age {
    font-size: 0.75rem;
    color: #666;
  }

  &__luck-years {
    font-size: 0.75rem;
    color: #888;
  }

  // 流年列（竖直排列）
  &__fleet-td {
    padding: 0;
    border: 1px solid #e8e8e8;
    vertical-align: top;

    &--minor {
      background: #faf5f0;
    }
  }

  &__fleet-cell {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1px;
    padding: 6px 4px;
    cursor: pointer;
    transition: all 0.15s;
    border-bottom: 1px solid #f0f0f0;

    &:last-child {
      border-bottom: none;
    }

    &:hover {
      background: #f5faff;
    }

    &--active {
      background: #e3f2fd;
      box-shadow: inset 3px 0 0 #1976d2;
    }

    &--current {
      .ec-main__fleet-year-label {
        color: #e65100;
        font-weight: 600;
      }
      .ec-main__fleet-ganzhi-label {
        color: #e65100;
      }
      background: #fff8e1;

      &#{&}--active {
        background: #e3f2fd;
        .ec-main__fleet-year-label,
        .ec-main__fleet-ganzhi-label {
          color: inherit;
        }
        .ec-main__fleet-ganzhi-label {
          color: #1565c0;
        }
      }
    }
  }

  &__fleet-year-label {
    font-size: 0.6875rem;
    color: #888;
    line-height: 1.3;
  }

  &__fleet-ganzhi-label {
    font-size: 0.875rem;
    font-weight: 700;
    color: #1565c0;
    font-family: 'Noto Sans SC', 'Microsoft YaHei', sans-serif;
    line-height: 1.4;
  }
}
</style>
