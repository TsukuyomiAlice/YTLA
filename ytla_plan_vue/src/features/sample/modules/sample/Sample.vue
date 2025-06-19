<template>
  <ModuleFlowNavigatorWithButtons
    module-type="sample"
    flow-name="sample-main-steps"
    frame-type="main"
  />
</template>

<script setup lang="ts">
import ModuleFlowNavigatorWithButtons from '@/core/modules/layouts/ModuleFlowNavigatorWithButtons.vue'
</script>

<style scoped lang="scss">
.step-controls {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}
</style>
