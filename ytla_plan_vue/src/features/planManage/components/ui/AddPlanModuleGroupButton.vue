<template>
  <button
    class="plan-manage-btn"
    @click="handleAddPlanModuleGroup"
  >
    {{ $t(`planManage.AddPlanModuleButton_001`) }}
  </button>

</template>
<script setup lang="ts">
import { useModuleCardStore } from '@/features/planManage/stores/moduleCardStore.ts'
import { usePlanCardStore } from '@/features/planManage/stores/planCardStore.ts'
import { useModuleProcessStore } from '@/core/modules/stores/moduleProcessStore.ts'
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const moduleStore = useModuleCardStore()
const planStore = usePlanCardStore()
const moduleProcessStore = useModuleProcessStore()

// 获取当前计划的所有分组名称（从planCardStore中获取）
const existingGroups = computed(() => {
  const plan = planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId)
  return plan?.module_groups ? plan.module_groups.split(',').filter(Boolean) : []
})

const handleAddPlanModuleGroup = async () => {
  if (!moduleProcessStore.belongPlanId) return

  const baseName = t('planManage.AddPlanModuleButton_002')
  let newGroupName = baseName
  let counter = 1

  // 检查并生成唯一的分组名称
  while (existingGroups.value.includes(newGroupName)) {
    counter++
    newGroupName = `${baseName} ${counter}`
  }

  try {
    // 更新计划的module_groups字段
    const plan = planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId)
    if (plan) {
      const currentGroups = plan.module_groups ? plan.module_groups.split(',') : []
      const updatedGroups = [...currentGroups, newGroupName].filter(Boolean)

      await planStore.updatePlanModuleGroups(
        moduleProcessStore.belongPlanId,
        updatedGroups.join(','),
        '',
        '',
      )
    }

    // 刷新模块列表
    await moduleStore.fetchModules(moduleProcessStore.belongPlanId)
  } catch (error) {
    console.error('添加分组失败:', error)
  }
}
</script>

<style scoped lang="scss">
@use '@/features/planManage/styles/plan-manage-button';
</style>
