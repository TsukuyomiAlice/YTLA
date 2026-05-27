<template>
  <div class="sub-container">
    <return-to-plan-dashboard-button />
    <div v-if="selectedGroup" class="group-display">
      <GroupAnalysisCard 
        :group="selectedGroup" 
        :index="transactionStore.expandedIndex || 0"
        :force-expand="true"
      />
    </div>
    <div v-else class="empty-hint">
      <p>请在左侧点击一组交易记录来查看详情</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import ReturnToPlanDashboardButton from '@/features/investment/modules/_type/ui/ReturnToPlanDashboardButton.vue'
import GroupAnalysisCard from '@/features/investment/modules/fund_transaction/components/GroupAnalysisCard.vue'
import { useFundTransactionStore } from '@/features/investment/modules/fund_transaction/stores/fundTransactionStore.ts'

const transactionStore = useFundTransactionStore()

const selectedGroup = computed(() => {
  return transactionStore.getSelectedGroup()
})
</script>

<style scoped lang="scss">
.sub-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;

  .group-display {
    margin-top: 20px;
  }

  .empty-hint {
    margin-top: 40px;
    text-align: center;
    color: #999;
    font-size: 16px;
  }
}
</style>
