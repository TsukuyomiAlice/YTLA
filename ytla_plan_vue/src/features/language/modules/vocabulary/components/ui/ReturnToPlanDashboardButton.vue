<template>
  <button
    class="language-manage-btn"
    @click="handleReturnToPlanDashboard"
  >
    {{ $t(`language.ReturnToPlanDashboardButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'
import { useModuleProcessStore } from '@/core/modules/_type/stores/moduleProcessStore.ts'

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
@use '@/features/language/modules/_type/styles/language-manage-button';
</style>
