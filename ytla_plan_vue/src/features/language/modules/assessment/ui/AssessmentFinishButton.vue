<template>
  <button
    class="language-manage-btn"
    @click="handleRetakeAssessment"
  >
    {{ $t(`language.modules.assessment.finish_button_001`) }}
  </button>

</template>
<script setup lang="ts">
const emit = defineEmits(['jumpToStep'])

const handleRetakeAssessment = () => {
  emit('jumpToStep', 0) // 触发事件而不是直接调用handleJump
}

</script>
<style scoped lang="scss">
@use '@/features/language/modules/_type/styles/language-manage-button';
</style>
