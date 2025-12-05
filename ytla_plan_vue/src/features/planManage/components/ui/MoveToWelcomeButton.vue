<template>
  <button
    class="plan-manage-btn"
    @click="handleMoveToWelcome"
  >
    {{ $t(`planManage.MoveToWelcomeButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { useModuleProcessStore } from '@/core/modules/_type/stores/moduleProcessStore.ts'
import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'

const handleMoveToWelcome = () => {
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.clearModule()
  const panelStore = usePanelStore()
  panelStore.switchPanel('plan_manage', 'welcome')
}

</script>
<style scoped lang="scss">
@use '@/features/planManage/styles/plan-manage-button';
</style>
