<template>
  <button
    class="plan-manage-btn"
    @click="handleReturnToPlan"
  >
    {{ $t(`planManage.ReturnToPlanButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { useModuleProcessStore } from '@/core/modules/stores/moduleProcessStore.ts'
import { usePanelStore } from '@/core/frame/services/panelStore.ts'

const handleReturnToPlan = () => {
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.clearModule()
  const panelStore = usePanelStore()
  panelStore.switchPanel('plan_manage', 'planManage')
}

</script>
<style scoped lang="scss">
@use '@/features/planManage/styles/plan-manage-button';
</style>
