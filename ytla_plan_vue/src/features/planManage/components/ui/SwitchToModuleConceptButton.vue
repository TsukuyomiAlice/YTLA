<template>
  <button
    class="plan-manage-btn"
    :class="{ active: isActive }"
    @click="handleSwitchToModuleConcept"
  >
    {{ $t(`planManage.SwitchToModuleConceptButton_001`) }}
  </button>

</template>

<script setup lang="ts">
const emit = defineEmits(['switch'])
const handleSwitchToModuleConcept = () => {
  emit('switch')
}
defineProps<{
  isActive: boolean
}>()
</script>

<style scoped lang="scss">
@use '@/features/planManage/styles/plan-manage-button';
.plan-manage-btn {
  &.active {
    background-color: #ff6b00;
    border-color: #ff6b00;
    color: white;
  }
}
</style>
