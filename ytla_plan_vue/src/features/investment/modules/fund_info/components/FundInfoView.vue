<template>
  <div class="fund-info-view">
    <!-- 基金信息卡片 -->
    <FundInfoCard :fund-info="fundInfoStore.fundInfo" />
    
    <!-- 净值走势图 -->
    <FundPriceChart :history="fundInfoStore.fundHistory" />
  </div>
</template>

<script setup lang="ts">
import { useFundInfoStore } from '@/features/investment/modules/fund_info/stores/fundInfoStore.ts'
import FundInfoCard from '@/features/investment/modules/fund_info/components/FundInfoCard.vue'
import FundPriceChart from '@/features/investment/modules/fund_info/components/FundPriceChart.vue'

const fundInfoStore = useFundInfoStore()
</script>

<style scoped lang="scss">
.fund-info-view {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
