<template>
  <button
    class="plan-manage-btn"
    :class="{ active: isActive }"
    @click="handleSwitchToModuleType"
  >
    {{ $t(`planManage.modules._type.SwitchToModuleTypeButton_001`) }}
  </button>

</template>

<script setup lang="ts">
const emit = defineEmits(['switch'])
const handleSwitchToModuleType = () => {
  emit('switch')
}
defineProps<{
  isActive: boolean
}>()
</script>

<style scoped lang="scss">
@use '@/features/planmanage/modules/_type/styles/plan-manage-button';
.plan-manage-btn {
  &.active {
    background-color: #ff6b00;
    border-color: #ff6b00;
    color: white;
  }
}
</style>
