<template>
  <button
    class="plan-manage-btn"
    @click="handleAddPlan"
  >
    + {{ $t(`planManage.AddPlanButton_001`) }}
  </button>
</template>

<script setup lang="ts">
import { usePlanCardStore } from '@/features/planManage/stores/planCardStore.ts'
const planStore = usePlanCardStore()
import { useModuleProcessStore } from '@/core/modules/_type/stores/moduleProcessStore.ts'
const moduleProcessStore = useModuleProcessStore()
import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'
const panelStore = usePanelStore()

const handleAddPlan = async () => {
  try {
    const result = await planStore.addPlan({
      name: 'a new plan',
      description: '',
      tags: '',
      module_groups: '',
      icon_path: '',
      background_path: '',
      delete_flag: '0',
      active_flag: '1'
    })
    if (result?.ok) {
      panelStore.switchPanel(`plan_${result.data.plan_id}`, 'planDashboard')
      moduleProcessStore.setModule('planDashboard', result.data.plan_id)
    }
    await planStore.fetchPlans()
  } catch (error) {
    console.error('创建计划失败:', error)
  }
}
</script>

<style scoped lang="scss">
@use '@/features/planManage/styles/plan-manage-button';
</style>
