<template>
  <div class="investment-container">
    <!-- 基金代码输入区域 -->
    <div class="fund-input-section">
      <input
        v-model="fundCodeInput"
        type="text"
        placeholder="请输入基金代码"
        class="fund-code-input"
        @keyup.enter="handleSearch"
      />
      <button class="search-btn" @click="handleSearch" :disabled="isLoading">
        {{ isLoading ? '加载中...' : '查询' }}
      </button>
    </div>

    <!-- 错误信息 -->
    <div v-if="error" class="error-message">{{ error }}</div>

    <!-- 内容区域 -->
    <div v-if="hasData" class="content-area">
      <div class="left-panel">
        <FundInfoCard :fund-info="localFundInfo" />
        <div class="left-scroll-content">
          <FundPriceChart :history="localFundHistory" />
          <HoldingStats
            :brief="transactionStore.transactionData?.brief"
            :fund-days="transactionStore.transactionData?.continuous_history?.fund_days"
          />
          <ContinuousStats :continuous-history="transactionStore.transactionData?.continuous_history" />
        </div>
      </div>
      <div class="right-panel">
        <GroupAnalysisCard
          v-for="(group, index) in transactionStore.transactionData?.match_list || []"
          :key="index"
          :group="group"
          :index="index"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useFundTransactionStore } from '@/features/investment/modules/fund_transaction/stores/fundTransactionStore.ts'
import { FundInfoService } from '@/features/investment/modules/fund_info/services/fundInfoService.ts'
import FundInfoCard from '@/features/investment/modules/fund_info/components/FundInfoCard.vue'
import FundPriceChart from '@/features/investment/modules/fund_info/components/FundPriceChart.vue'
import HoldingStats from '@/features/investment/modules/fund_transaction/components/HoldingStats.vue'
import ContinuousStats from '@/features/investment/modules/fund_transaction/components/ContinuousStats.vue'
import GroupAnalysisCard from '@/features/investment/modules/fund_transaction/components/GroupAnalysisCard.vue'

const API_BASE = import.meta.env.VITE_API_BASE
const fundInfoService = new FundInfoService(API_BASE)

const transactionStore = useFundTransactionStore()

const fundCodeInput = ref('')

// 本地状态，不依赖另一个store
const localFundInfo = ref<null | {
  code: string
  name: string
  fund_type: string
  ratio: number
  share_accuracy: number
  fee_free_limit: number
  latest_price: number
}>(null)

const localFundHistory = ref<Array<{
  transaction_date: string
  current_price: number
  origin_price: number
  fluctuation: number
  share_change_ratio: number
  share_change_note: string
}>>([])

const localIsLoading = ref(false)
const localError = ref<null | string>(null)

const isLoading = computed(() => localIsLoading.value || transactionStore.isLoading)
const error = computed(() => localError.value || transactionStore.error)
const hasData = computed(() =>
  (localFundInfo.value !== null || localFundHistory.value.length > 0) ||
  transactionStore.transactionData !== null
)

const handleSearch = async () => {
  const code = fundCodeInput.value.trim()
  if (!code) return

  // 清空所有旧数据
  localFundInfo.value = null
  localFundHistory.value = []
  localError.value = null
  transactionStore.clear()

  // 两个请求并行
  localIsLoading.value = true
  try {
    await Promise.all([
      // 直接调用服务获取基金信息
      (async () => {
        const infoResponse = await fundInfoService.getFundInfo(code)
        if (infoResponse.success && infoResponse.data) {
          localFundInfo.value = infoResponse.data
        } else {
          localError.value = infoResponse.message || '获取基金信息失败'
        }

        const historyResponse = await fundInfoService.getFundHistory(code)
        if (historyResponse.success && historyResponse.data) {
          localFundHistory.value = historyResponse.data
        } else if (!localError.value) {
          localError.value = historyResponse.message || '获取历史净值失败'
        }
      })(),
      // 调用transaction store获取交易分析
      transactionStore.fetchTransactionAnalysis(code)
    ])
  } catch (err) {
    localError.value = err instanceof Error ? err.message : '加载失败'
  } finally {
    localIsLoading.value = false
  }
}
</script>

<style scoped lang="scss">
.investment-container {
  max-width: 1500px;
  margin: 0 auto;
  padding: 20px;

  .fund-input-section {
    display: flex;
    justify-content: left;
    gap: 10px;
    margin-bottom: 20px;

    .fund-code-input {
      padding: 12px 20px;
      font-size: 16px;
      border: 2px solid #e0e0e0;
      border-radius: 8px;
      width: 300px;
      outline: none;
      transition: border-color 0.3s;

      &:focus {
        border-color: #1976d2;
      }
    }

    .search-btn {
      padding: 12px 30px;
      font-size: 16px;
      background: #1976d2;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.3s;

      &:hover:not(:disabled) {
        background: #1565c0;
      }

      &:disabled {
        background: #90caf9;
        cursor: not-allowed;
      }
    }
  }

  .error-message {
    text-align: center;
    color: #d32f2f;
    padding: 10px;
    margin-bottom: 20px;
  }

  .content-area {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    height: calc(100vh - 200px);
  }

  .left-panel,
  .right-panel {
    display: flex;
    flex-direction: column;
    gap: 20px;
    height: 100%;
    overflow: hidden;
  }

  .left-panel {
    .left-scroll-content {
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
  }

  .right-panel {
    overflow-y: auto;
  }

  .left-panel > *,
  .right-panel > * {
    flex-shrink: 0;
  }
}

.fund-info-container,
.fund-transaction-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 30px;
}
</style>
