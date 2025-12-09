<template>
  <button
    class="plan-manage-btn"
    @click="handleMoveToWelcome"
  >
    {{ $t(`planManage._type.MoveToWelcomeButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { useModuleProcessStore } from '@/core/domain/area/modules/stores/moduleProcessStore.ts'
import { usePanelStore } from '@/core/domain/area/frame/services/panelStore.ts'

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
