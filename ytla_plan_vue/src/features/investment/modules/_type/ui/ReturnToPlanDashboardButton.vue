<template>
  <button
    class="investment-manage-btn"
    @click="handleReturnToPlanDashboard"
  >
    {{ $t(`investment.modules._type.return_button_001`) }}
  </button>

</template>
<script setup lang="ts">
import { usePanelStore } from '@/core/classic/modules/modulePanel/stores/panelStore.ts'
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
@use '@/features/investment/modules/_type/styles/investment-manage-button';
</style>
