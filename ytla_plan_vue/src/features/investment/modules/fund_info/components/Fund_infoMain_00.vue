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
      <div class="fund-info-container">
        <FundInfoCard :fund-info="fundInfoStore.fundInfo" />
        <FundPriceChart :history="fundInfoStore.fundHistory" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useFundInfoStore } from '@/features/investment/modules/fund_info/stores/fundInfoStore.ts'
import FundInfoCard from '@/features/investment/modules/fund_info/components/FundInfoCard.vue'
import FundPriceChart from '@/features/investment/modules/fund_info/components/FundPriceChart.vue'

const fundInfoStore = useFundInfoStore()

const fundCodeInput = ref('')

const isLoading = computed(() => fundInfoStore.isLoading)
const error = computed(() => fundInfoStore.error)
const hasData = computed(() => fundInfoStore.fundInfo !== null || fundInfoStore.fundHistory.length > 0)

const handleSearch = async () => {
  const code = fundCodeInput.value.trim()
  if (!code) return

  await fundInfoStore.loadAllData(code)
}
</script>

<style scoped lang="scss">
.investment-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;

  .fund-input-section {
    display: flex;
    justify-content: center;
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
    min-height: 400px;
  }
}

.fund-info-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
