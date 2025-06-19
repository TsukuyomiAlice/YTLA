<template>
  <h1>{{ $t('language.AssessmentSub_00_000') }}</h1>
  <br>
  <p>{{ $t('language.AssessmentSub_00_001') }}</p>
  <a href="https://englishprofile.org">https://englishprofile.org</a>
  <p>{{ $t('language.AssessmentSub_00_002') }}</p>
  <a href="https://preply.com/en/learn/english/test-your-vocab">https://preply.com/en/learn/english/test-your-vocab</a>
  <br>
  <return-to-plan-dashboard-button />
</template>

<script setup lang="ts">

import ReturnToPlanDashboardButton from '@/features/language/components/ui/assessment/ReturnToPlanDashboardButton.vue'
</script>
<style scoped lang="scss">

</style>
