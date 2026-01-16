<template>
  <h1>{{ plan?.name }} - {{ $t('planManage.modules.addModule.main_00_000')}}</h1>
  <return-to-plan-dashboard-button />
  <br />
  <switch-to-module-concept-button
    @switch="currentView = 'concept'"
    :is-active="currentView === 'concept'"
  />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <switch-to-module-type-button
    @switch="currentView = 'type'"
    :is-active="currentView === 'type'"
  />

  <div v-if="currentView === 'type'" class="module-category">
    <div v-for="(modules, type) in filteredByType" :key="type">
      <h2>{{ $t(`${type}.modules._type.type_name`) }}</h2>
      <h2>{{ $t(`${type}.modules._type.type_description`) }}</h2>
      <div v-for="module in modules" :key="module.moduleSubType" class="module-item" @click="handleModuleClick(module)">
        <h3>{{ $t(`${module.moduleType}.modules.${module.moduleSubType}.subtype_name`) }}</h3>
        <h3>{{ $t(`planManage.modules.addModule.main_concept_${module.moduleConcept}`) }}</h3>
        <p>{{ $t(`${module.moduleType}.modules.${module.moduleSubType}.subtype_description`) }}</p>
      </div>
    </div>
  </div>

  <div v-else class="module-category">
    <div v-for="(modules, concept) in filteredByConcept" :key="concept">
      <h2>{{ $t(`planManage.modules.addModule.main_concept_${concept}`) }}</h2>
      <div v-for="module in modules" :key="module.moduleSubType" class="module-item" @click="handleModuleClick(module)">
        <h3>{{ $t(`${module.moduleType}.modules.${module.moduleSubType}.subtype_name`) }}</h3>
        <h3>{{ $t(`${module.moduleType}.modules._type.type_name`) }}</h3>
        <p>{{ $t(`${module.moduleType}.modules.${module.moduleSubType}.subtype_description`) }}</p>
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import ReturnToPlanDashboardButton from '@/features/planManage/modules/_type/ui/ReturnToPlanDashboardButton.vue'
import SwitchToModuleConceptButton from '@/features/planManage/modules/_type/ui/SwitchToModuleConceptButton.vue'
import SwitchToModuleTypeButton from '@/features/planManage/modules/_type/ui/SwitchToModuleTypeButton.vue'

import { usePlanCardStore } from '@/core/classic/plans/planCard/stores/planCardStore.ts'
const planStore = usePlanCardStore()
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'
const moduleProcessStore = useModuleProcessStore()
const plan = computed(() => {
  return planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId)
})

import { ref, computed } from 'vue'
import { getRegisteredModules, getModuleConfig } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

// 新增响应式状态和计算属性
const currentView = ref<'type' | 'concept'>('type')

const allModules = computed(() => {
  return getRegisteredModules().map(subType => getModuleConfig(subType)!)
})

const filteredByType = computed(() => {
  return groupBy(
    allModules.value.filter(m => m.moduleType !== 'planManage'),
    'moduleType'
  )
})

const filteredByConcept = computed(() => {
  return groupBy(
    allModules.value.filter(m => m.moduleConcept !== 'system'),
    'moduleConcept'
  )
})

function groupBy(array: any[], key: string) {
  return array.reduce((acc, obj) => {
    const keyValue = obj[key]
    acc[keyValue] = acc[keyValue] || []
    acc[keyValue].push(obj)
    return acc
  }, {})
}

import { useModuleCardStore } from '@/core/classic/modules/moduleCard/stores/moduleCardStore.ts'
const moduleStore = useModuleCardStore()
import { useLayoutStore } from '@/core/classic/frame/main/services/layoutStore.ts'
const layoutStore = useLayoutStore()
const handleModuleClick = (moduleConfig: any) => {
  moduleStore.setSelectedModule({
    moduleType: moduleConfig.moduleType,
    moduleSubType: moduleConfig.moduleSubType
  })
  if (layoutStore.isRightSideBarExpanded) {
    layoutStore.toggleExpand()
  }
}
</script>

<style scoped lang="scss">
.module-category {
  margin-top: 2rem;
  display: grid;
  gap: 1rem;

  > div {
    > h2 {
      grid-column: 1 / -1;
    }

    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(20rem, 1fr));
    gap: 1rem;
    align-items: start;
  }

  .module-item {
    padding: 1rem;
    border: 1px solid #e0e0e0;
    border-radius: 0.5rem;
    cursor: pointer;
    min-height: 8rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    &:hover {
      background-color: #f5f5f5;
    }
  }
}
</style>
