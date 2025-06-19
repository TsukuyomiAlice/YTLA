<!-- src/features/timer/components/mainframe/TimerContent.vue -->
<template>
  <return-to-plan-dashboard-button/>
  <ModuleMainFrame>
    <div class="timer-content">
      <h2>Timer Dashboard</h2>
      <div class="cards">
        <div class="card">倒计时组件预留位</div>
        <div class="card">闹钟组件预留位</div>
      </div>
    </div>
  </ModuleMainFrame>
</template>

<script setup lang="ts">
import ModuleMainFrame from '@/core/modules/layouts/ModuleMainFrame.vue'
import ReturnToPlanDashboardButton
  from '@/features/planManage/components/ui/ReturnToPlanDashboardButton.vue'
</script>

<style lang="scss">
.timer-content {
  padding: 2rem;

  .cards {
    display: grid;
    gap: 1rem;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));

    .card {
      padding: 1.5rem;
      background: rgba(255,255,255,0.1);
      border-radius: 0.5rem;
    }
  }
}
</style>
