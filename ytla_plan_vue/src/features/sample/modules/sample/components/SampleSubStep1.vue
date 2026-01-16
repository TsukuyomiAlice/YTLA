<template>
  <div>
    <h3>子内容步骤1</h3>
    <input
      v-model="inputData"
      @input="updateState"
      placeholder="输入内容可在步骤间保持"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount  } from 'vue'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'

const panelStore = usePanelStore()
const inputData = ref('')

onMounted(() => {
  const savedState = panelStore.getCurrentState()?.subFrame?.componentState
  inputData.value = (savedState?.step1Data || '') as string
})

onBeforeUnmount(() => {
  panelStore.persistCurrentModule()
})

const updateState = () => {
  panelStore.updateFrameState('sub',{
    state: { step1Data: inputData.value }
  })
}
</script>
