<template>
  <h1>{{ $t('language.modules.assessment.main_00_000') }}</h1>
  <br>
  <p>{{ $t('language.modules.assessment.main_00_001') }}</p>
  <p>{{ $t('language.modules.assessment.main_00_002') }}</p>
  <p>{{ $t('language.modules.assessment.main_00_003') }}</p>
  <p>{{ $t('language.modules.assessment.main_00_004') }}</p>
  <p>{{ $t('language.modules.assessment.main_00_005') }}</p>
  <p>{{ $t('language.modules.assessment.main_00_006') }}</p>
  <br>
  <assessment-start-button @jump-to-step="handleStart"/>

</template>

<script setup lang="ts">
import AssessmentStartButton from '@/features/language/modules/assessment/ui/AssessmentStartButton.vue'

const emit = defineEmits(['nextStep', 'jumpToStep'])
const handleStart = (index: number) => {
  emit('jumpToStep', index)
}
</script>
<style scoped lang="scss">

</style>
