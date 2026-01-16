<template>
  <button
    class="mathematics-manage-btn"
    @click="handleReturnToPlanDashboard"
  >
    {{ $t(`mathematics.modules._type.ReturnToPlanDashboardButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

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
@use '../../sphere/styles/mathematics-manage-button';
</style>
