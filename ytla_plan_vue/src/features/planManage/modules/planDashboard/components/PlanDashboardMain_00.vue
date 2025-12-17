<template>
  <div v-if="activeFlag === '1'">

    <div class="top-section">
      <h1>{{ plan?.name }} - {{ $t('planManage.modules.planDashboard.main_00_000') }}</h1>
      <ReturnToPlanButton />
      &nbsp;&nbsp;&nbsp;&nbsp;
      <AddPlanModuleGroupButton />
      &nbsp;&nbsp;&nbsp;&nbsp;
      <AddModuleButton />
    </div>

    <div class="dashboard-layout">
      <div class="grouped-modules"
           @dragover.prevent
           @dragenter.prevent>
        <PlanModuleContainer
          v-for="(group, name) in groupedModules"
          :key="name"
          :group-name="name"
          :modules="group"
          @update:groupName="(newName) => handleUpdateGroupName(name, newName)"
          @deleteGroup="handleDeleteGroup"
        />
      </div>

      <div class="ungrouped-modules"
           @dragover.prevent
           @dragenter.prevent>
        <PlanModuleContainer
          :group-name="$t('planManage.modules.planDashboard.main_00_001')"
          :modules="ungroupedModules"
        />
      </div>
    </div>

  </div>

  <div v-if="activeFlag === '0'">
    <h1>{{ $t('planManage.modules.planDashboard.main_00_100') }}</h1>
  </div>
</template>

<script setup lang="ts">
import ReturnToPlanButton from '@/features/planManage/modules/_type/ui/ReturnToPlanButton.vue'
import AddPlanModuleGroupButton
  from '@/features/planManage/modules/_type/ui/AddPlanModuleGroupButton.vue'
import AddModuleButton from '@/features/planManage/modules/_type/ui/AddModuleButton.vue'
import { usePlanActiveFlag } from '@/core/classic/plans/planCard/composables/watchPlanActiveFlag.ts'

const { activeFlag } = usePlanActiveFlag()

import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'

const moduleProcessStore = useModuleProcessStore()

import PlanModuleContainer from '@/features/planManage/modules/planDashboard/layouts/PlanModuleContainer.vue'
import { computed, onActivated, onMounted } from 'vue'
import { useModuleCardStore } from '@/core/classic/modules/moduleCard/stores/moduleCardStore.ts'

const moduleStore = useModuleCardStore()

// 获取分组模块 (修改后的计算属性)
const groupedModules = computed(() => {
  // 获取所有分组名称（包括空分组）
  const plan = planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId)
  const allGroups = plan?.module_groups?.split(',').filter(Boolean) || []

  // 创建包含所有分组的对象
  const groupsWithModules = moduleStore.filteredModules.reduce((acc, module) => {
    if (module.belong_group_name) {
      acc[module.belong_group_name] = acc[module.belong_group_name] || []
      acc[module.belong_group_name].push(module)
    }
    return acc
  }, {} as Record<string, any[]>)

  // 添加空分组
  allGroups.forEach(group => {
    if (!groupsWithModules[group]) {
      groupsWithModules[group] = []
    }
  })

  return groupsWithModules
})

// 获取未分组模块
const ungroupedModules = computed(() => {
  return moduleStore.filteredModules.filter(m => !m.belong_group_name)
})

// 简化的加载逻辑
const loadModules = async () => {
  if (moduleProcessStore.belongPlanId) {
    await moduleStore.fetchModules(moduleProcessStore.belongPlanId)
  }
}

// 使用组件激活生命周期控制加载
onActivated(loadModules)
onMounted(loadModules)

import { usePlanCardStore } from '@/core/classic/plans/planCard/stores/planCardStore.ts'

const planStore = usePlanCardStore()
const plan = computed(() => {
  return planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId)
})

const handleUpdateGroupName = async (oldName: string, newName: string) => {
  if (!moduleProcessStore.belongPlanId) return

  try {
    // 更新模块的分组名称
    const modulesToUpdate = moduleStore.modules.filter(
      m => m.belong_plan_id === moduleProcessStore.belongPlanId &&
        m.belong_group_name === oldName
    )

    for (const module of modulesToUpdate) {
      await moduleStore.updateModule(module.module_id, {
        ...module,
        belong_group_name: newName
      })
    }

    // 更新计划中的分组名称
    const plan = planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId)
    if (plan) {
      const groups = plan.module_groups.split(',').map(g =>
        g === oldName ? newName : g
      )
      await planStore.updatePlanModuleGroups(
        moduleProcessStore.belongPlanId,
        groups.join(','),
        oldName,
        newName
      )
    }

    // 刷新模块列表
    await moduleStore.fetchModules(moduleProcessStore.belongPlanId)
  } catch (error) {
    console.error('更新分组名称失败:', error)
  }
}

const handleDeleteGroup = async (groupName: string) => {
  // 不需要额外处理，因为删除操作已经在PlanModuleContainer中完成
  // 这里只需要触发模块列表刷新
}

</script>

<style scoped>
.dashboard-layout {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.grouped-modules {
  width: 61.8vw;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-height: 80vh;
  overflow-y: auto;
}

.ungrouped-modules {
  width: 38.2vw;
  display: flex;
  flex-direction: column;
  max-height: 80vh;
  overflow-y: auto;
}
</style>
