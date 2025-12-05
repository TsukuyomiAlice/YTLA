<template>
  <button
    class="language-manage-btn"
    @click="handleStartAssessment"
  >
    {{ $t(`language.AssessmentStartButton_001`) }}
  </button>
</template>

<script setup lang="ts">
import { useModuleProcessStore} from '@/core/modules/_type/stores/moduleProcessStore.ts'
const moduleProcessStore = useModuleProcessStore()
const planId = moduleProcessStore.belongPlanId as number
const moduleId = moduleProcessStore.moduleId as number
import { useLanguageAssessmentStore } from '@/features/language/modules/assessment/stores/languageAssessmentStore.ts'
const languageAssessmentStore = useLanguageAssessmentStore()

const emit = defineEmits(['jumpToStep'])

const handleStartAssessment = async () => {
  await languageAssessmentStore.assessment1A(planId, moduleId, 'Ann')
  emit('jumpToStep', 1) // 触发事件而不是直接调用handleJump
}
</script>
<style scoped lang="scss">
@use '@/features/language/modules/_type/styles/language-manage-button';
</style>
