<template>
  <h1>{{ $t('language.modules.assessment.main_99_000') }}</h1>
  <h2>{{ $t('language.modules.assessment.main_99_001') }} {{ languageAssessmentStore.finalLevel }} </h2>
  <assessment-finish-button @jump-to-step="handleRetake"/>
</template>

<script setup lang="ts">
import AssessmentFinishButton from '@/features/language/modules/assessment/ui/AssessmentFinishButton.vue'
import { useLanguageAssessmentStore } from '@/features/language/modules/assessment/stores/languageAssessmentStore.ts'
const languageAssessmentStore = useLanguageAssessmentStore()
// 定义事件发射器（保持原有逻辑）
const emit = defineEmits(['nextStep', 'jumpToStep'])
const handleRetake = (index: number) => emit('jumpToStep', index)
</script>
<style scoped lang="scss">

</style>
