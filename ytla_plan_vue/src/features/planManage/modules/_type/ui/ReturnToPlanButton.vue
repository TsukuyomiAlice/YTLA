<template>
  <button
    class="plan-manage-btn"
    @click="handleReturnToPlan"
  >
    {{ $t(`planManage.modules._type.ReturnToPlanButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'

const handleReturnToPlan = () => {
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.clearModule()
  const panelStore = usePanelStore()
  panelStore.switchPanel('plan_manage', 'planManage')
}

</script>
<style scoped lang="scss">
@use '@/features/planmanage/modules/_type/styles/plan-manage-button';
</style>
