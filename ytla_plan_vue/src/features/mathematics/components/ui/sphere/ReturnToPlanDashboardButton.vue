<template>
  <button
    class="mathematics-manage-btn"
    @click="handleReturnToPlanDashboard"
  >
    {{ $t(`mathematics.ReturnToPlanDashboardButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { usePanelStore } from '@/core/frame/services/panelStore.ts'
import { useModuleProcessStore } from '@/core/modules/stores/moduleProcessStore.ts'

const handleReturnToPlanDashboard = () => {
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.clearModule()

  const panelStore = usePanelStore()
  panelStore.switchPanel(panelStore.activePanel, 'planDashboard')
  const planId = parseInt(panelStore.activePanel.replace('plan_', ''))
  moduleProcessStore.setModule('planDashboard', planId)
}

</script>
<style scoped lang="scss">
@use '@/features/mathematics/styles/mathematics-manage-button';
</style>
