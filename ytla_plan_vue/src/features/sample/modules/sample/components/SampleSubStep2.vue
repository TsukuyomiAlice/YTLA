<template>
  <div>
    <h3>子内容步骤2</h3>
    <p>从步骤1带来的数据：{{ storedData }}</p>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'

const panelStore = usePanelStore()
const storedData = computed(() => {
  return panelStore.getCurrentState()?.subFrame?.componentState?.step1Data || ''
})
</script>
