<template>
  <button
    class="plan-manage-btn"
    @click="handleMoveToWelcome"
  >
    {{ $t(`planManage.modules._type.MoveToWelcomeButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'

const handleMoveToWelcome = () => {
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.clearModule()
  const panelStore = usePanelStore()
  panelStore.switchPanel('plan_manage', 'welcome')
}

</script>
<style scoped lang="scss">
@use '@/features/planmanage/modules/_type/styles/plan-manage-button';
</style>
