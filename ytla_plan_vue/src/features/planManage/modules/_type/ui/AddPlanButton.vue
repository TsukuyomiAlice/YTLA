<template>
  <button
    class="plan-manage-btn"
    @click="handleAddPlan"
  >
    + {{ $t(`planManage.modules._type.AddPlanButton_001`) }}
  </button>
</template>

<script setup lang="ts">
import { usePlanCardStore } from '@/core/classic/plans/planCard/stores/planCardStore.ts'
const planStore = usePlanCardStore()
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'
const moduleProcessStore = useModuleProcessStore()
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'
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
@use '@/features/planmanage/modules/_type/styles/plan-manage-button';
</style>
