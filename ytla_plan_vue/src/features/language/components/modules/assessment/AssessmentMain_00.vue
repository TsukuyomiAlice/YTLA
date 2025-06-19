<template>
  <h1>{{ $t('language.AssessmentMain_00_000') }}</h1>
  <br>
  <p>{{ $t('language.AssessmentMain_00_001') }}</p>
  <p>{{ $t('language.AssessmentMain_00_002') }}</p>
  <p>{{ $t('language.AssessmentMain_00_003') }}</p>
  <p>{{ $t('language.AssessmentMain_00_004') }}</p>
  <p>{{ $t('language.AssessmentMain_00_005') }}</p>
  <p>{{ $t('language.AssessmentMain_00_006') }}</p>
  <br>
  <assessment-start-button @jump-to-step="handleStart"/>

</template>

<script setup lang="ts">
import AssessmentStartButton from '@/features/language/components/ui/assessment/AssessmentStartButton.vue'

const emit = defineEmits(['nextStep', 'jumpToStep'])
const handleStart = (index: number) => {
  emit('jumpToStep', index)
}
</script>
<style scoped lang="scss">

</style>
