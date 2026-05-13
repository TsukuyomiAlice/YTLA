<template>
  <div class="fund-transaction-view">
    <!-- 持仓统计 -->
    <HoldingStats :brief="transactionStore.transactionData?.brief" />
    
    <!-- 连续涨跌统计 -->
    <ContinuousStats :continuous-history="transactionStore.transactionData?.continuous_history" />
    
    <!-- 分组交易分析 -->
    <GroupAnalysisCard
      v-for="(group, index) in transactionStore.transactionData?.match_list || []"
      :key="index"
      :group="group"
      :index="index"
    />
  </div>
</template>

<script setup lang="ts">
import { useFundTransactionStore } from '@/features/investment/modules/fund_transaction/stores/fundTransactionStore.ts'
import HoldingStats from '@/features/investment/modules/fund_transaction/components/HoldingStats.vue'
import ContinuousStats from '@/features/investment/modules/fund_transaction/components/ContinuousStats.vue'
import GroupAnalysisCard from '@/features/investment/modules/fund_transaction/components/GroupAnalysisCard.vue'

const transactionStore = useFundTransactionStore()
</script>

<style scoped lang="scss">
.fund-transaction-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
