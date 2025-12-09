<template>
  <ModuleFlowNavigator
    ref="flowNavigator"
    module-type="sphere"
    flow-name="sphere-main-steps"
    frame-type="main"
    @jump-to-step="handleJump"
    @next-step="handleNext"
  />

</template>

<script setup lang="ts">
import { ref } from 'vue'
import ModuleFlowNavigator from '@/core/domain/area/modules/layouts/ModuleFlowNavigator.vue'

const flowNavigator = ref<InstanceType<typeof ModuleFlowNavigator>>()

const handleJump = (index: number) => {
  flowNavigator.value?.handleJump(index)
}

const handleNext = () => {
  flowNavigator.value?.handleNext()
}
</script>
<style scoped lang="scss">

</style>
