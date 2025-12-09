<template>
  <div>
    <h1>{{ $t(`planManage.welcome.main_00_000`) }}</h1>
    <br>
    <p>{{ $t(`planManage.welcome.main_00_001`) }}</p>
    <p>{{ $t(`planManage.welcome.main_00_002`) }}</p>
    <p>{{ $t(`planManage.welcome.main_00_003`) }}</p>
    <p>{{ $t(`planManage.welcome.main_00_004`) }}</p>
    <br>
    <p>{{ $t(`planManage.welcome.main_00_005`) }}</p>
    <p>Enjoy!</p>
    <AddPlanButton />
  </div>
</template>

<script setup lang="ts">
import AddPlanButton from '@/features/planManage/modules/_type/ui/AddPlanButton.vue'

</script>
<style scoped lang="scss">

</style>
