<template>
  <h1>
    {{ $t(`planManage.modules.planManager.sub_00_000`) }}
  </h1>
  <br>
  {{ $t(`planManage.modules.planManager.sub_00_001`) }}&nbsp;<AddPlanButton />
  <br>
  {{ $t(`planManage.modules.planManager.sub_00_002`) }}&nbsp;<MoveToWelcomeButton />
</template>

<script setup lang="ts">
import MoveToWelcomeButton from '@/features/planManage/modules/_type/ui/MoveToWelcomeButton.vue'
import AddPlanButton from '@/features/planManage/modules/_type/ui/AddPlanButton.vue'
</script>
