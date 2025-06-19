<template>
  <h1>
    {{ $t(`planManage.PlanManagerSub_00_000`) }}
  </h1>
  <br>
  {{ $t(`planManage.PlanManagerSub_00_001`) }}&nbsp;<AddPlanButton />
  <br>
  {{ $t(`planManage.PlanManagerSub_00_002`) }}&nbsp;<MoveToWelcomeButton />
</template>

<script setup lang="ts">
import MoveToWelcomeButton from '@/features/planManage/components/ui/MoveToWelcomeButton.vue'
import AddPlanButton from '@/features/planManage/components/ui/AddPlanButton.vue'
</script>
