<template>
  <div v-if="!editingModuleId">
    <PlanCardEditor
      :plan-id="moduleProcessStore.belongPlanId as number"
      mode="edit"
      @close="moduleProcessStore.clearModule"
    />
  </div>
  <div v-else>
    <ModuleCardEditor
      :module-id="editingModuleId"
      mode="edit"
      @close="moduleProcessStore.clearEditingModule"
    />
  </div>

</template>

<script setup lang="ts">
import PlanCardEditor from '@/features/planManage/layouts/PlanCardEditor.vue'
import ModuleCardEditor from '@/features/planManage/layouts/ModuleCardEditor.vue'

import { useModuleProcessStore } from '@/core/modules/_type/stores/moduleProcessStore.ts'
import { computed } from 'vue'

const moduleProcessStore = useModuleProcessStore()
const editingModuleId = computed(() => moduleProcessStore.editingModuleId)

</script>

<style scoped lang="scss">

</style>
