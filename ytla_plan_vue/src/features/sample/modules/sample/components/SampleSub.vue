<template>
  <ModuleFlowNavigatorWithButtons
    module-type="sample"
    flow-name="sample-sub-steps"
    frame-type="sub"
  />
</template>

<script setup lang="ts">
import ModuleFlowNavigatorWithButtons from '@/core/domain/area/modules/layouts/ModuleFlowNavigatorWithButtons.vue'
</script>

<style scoped lang="scss">
.step-controls {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}
</style>
