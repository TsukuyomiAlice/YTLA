<template>
  <div class="step3-container">
    <div class="area-a">
      <h2>主内容步骤 3-a</h2>
      <p>这是主内容的第三个步骤的详细信息a。</p>
    </div>
    <div class="area-b">
      <h2>主内容步骤 3-b</h2>
      <p>这是主内容的第三个步骤的详细信息b。</p>
    </div>
  </div>
  <return-to-plan-dashboard-button/>
</template>

<script setup lang="ts">
// 这里可以添加步骤 3 的逻辑
import ReturnToPlanDashboardButton
  from '@/features/planManage/components/ui/ReturnToPlanDashboardButton.vue'
</script>

<style scoped lang="scss">
.step3-container {
  display: flex;
  gap: 2rem;

  .area-a {
    flex: 3;
    background: rgba(255 255 255 / 0.8);
    padding: 1.5rem;
  }

  .area-b {
    flex: 2;
    background: rgba(255 255 255 / 0.9);
    padding: 1.5rem;
  }
}
</style>
