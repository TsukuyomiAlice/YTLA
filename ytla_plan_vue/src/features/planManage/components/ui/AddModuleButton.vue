<template>
  <button
    class="plan-manage-btn"
    @click="handleAddModule"
  >
    {{ $t(`planManage.AddModuleButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'
import { useModuleProcessStore } from '@/core/modules/_type/stores/moduleProcessStore.ts'

const handleAddModule = () => {
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.clearModule()

  const panelStore = usePanelStore()
  panelStore.switchPanel(panelStore.activePanel, 'addModule')
  const planId = parseInt(panelStore.activePanel.replace('plan_', ''))
  moduleProcessStore.setModule('addModule', planId)
}

</script>
<style scoped lang="scss">
@use '@/features/planManage/styles/plan-manage-button';
</style>
