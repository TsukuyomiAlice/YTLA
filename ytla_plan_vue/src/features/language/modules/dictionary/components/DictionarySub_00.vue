<template>
  <h1>{{ $t('language.DictionarySub_00_000') }}</h1>
  <br>
  <p>{{ $t('language.DictionarySub_00_001') }}</p>
  <p>{{ $t('language.DictionarySub_00_002') }}</p>
  <return-to-plan-dashboard-button />
</template>

<script setup lang="ts">

import ReturnToPlanDashboardButton
  from '@/features/language/modules/dictionary/components/ui/ReturnToPlanDashboardButton.vue'
</script>
<style scoped lang="scss">

</style>
