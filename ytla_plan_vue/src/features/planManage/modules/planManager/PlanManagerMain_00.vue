<template>
  <div>
    <h1>{{ $t(`planManage.PlanManagerMain_00_000`) }}</h1>
    <br>
    <p>{{ $t(`planManage.PlanManagerMain_00_001`) }}</p>
    <br>
  </div>
  <PlanCardContainer />
</template>

<script setup lang="ts">
import PlanCardContainer from '@/features/planManage/layouts/PlanCardContainer.vue'

</script>

<style scoped lang="scss">
</style>
