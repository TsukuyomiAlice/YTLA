<template>
  <button
    class="language-manage-btn"
    @click="handleAssessmentNext"
  >
    {{ $t(`language.AssessmentNextButton_001`) }}
  </button>

</template>
<script setup lang="ts">
const emit = defineEmits(['nextStep'])
const handleAssessmentNext = () => {
  emit('nextStep')
}

</script>
<style scoped lang="scss">
@use '@/features/language/styles/language-manage-button';
</style>
