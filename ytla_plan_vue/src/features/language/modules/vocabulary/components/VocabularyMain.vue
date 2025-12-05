<template>
  <ModuleFlowNavigator
    ref="flowNavigator"
    module-type="vocabulary"
    flow-name="vocabulary-main-steps"
    frame-type="main"
    @next-step="handleNext"
    @prev-step="handlePrev"
  />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import ModuleFlowNavigator from '@/core/modules/_type/layouts/ModuleFlowNavigator.vue'

const flowNavigator = ref<InstanceType<typeof ModuleFlowNavigator>>()

const handleNext = () => {
  flowNavigator.value?.handleNext()
}
const handlePrev = () => {
  flowNavigator.value?.handlePrev()
}
</script>
<style scoped lang="scss">

</style>
