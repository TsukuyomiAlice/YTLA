<template>
  <div class="system-navigation-bar">
    <component
      v-for="button in visibleActiveButtons"
      :is="button.component"
      :key="button.buttonId"
    />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { storeToRefs } from 'pinia'
import { useNavigatorStore } from '@/core/classic/busline/navigator/stores/navigatorStore.ts'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const navigatorStore = useNavigatorStore()
const panelStore = usePanelStore()
const moduleProcessStore = useModuleProcessStore()

const { activePanel } = storeToRefs(panelStore)
const { currentModuleType } = storeToRefs(moduleProcessStore)

const systemContext = computed(() => {
  let activePlanId: string | undefined
  if (activePanel.value.startsWith('plan_') && activePanel.value !== 'plan_manage') {
    activePlanId = activePanel.value.split('_')[1]
  }

  return {
    currentPanel: activePanel.value,
    currentModuleType: currentModuleType.value,
    activePlanId
  }
})

const visibleActiveButtons = computed(() => {
  return navigatorStore.activeButtons(systemContext.value)
})
</script>

<style lang="scss" scoped>
.system-navigation-bar {
  display: flex;
  gap: 8px;
  align-items: center;
}
</style>
