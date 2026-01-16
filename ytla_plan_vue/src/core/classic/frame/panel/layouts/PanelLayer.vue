<!-- core/layouts/PanelLayer.vue -->
<template>
  <div class="panel-layer">
    <!-- 计划管理按钮 -->
    <button
      class="panel-toggle"
      :class="{ active: activePanel === 'plan_manage' }"
      @click="handlePlanManageClick"
      title="计划管理"
    >
      🏠
    </button>

    <!-- 动态生成计划按钮 -->
    <template v-for="planPanel in planPanels" :key="planPanel.id">
      <button
        class="panel-toggle"
        :class="{ active: activePanel === planPanel.id }"
        @click="handlePlanClick(planPanel)"
        v-html="getPlanIcon(planPanel)"
        :title="getPlanName(planPanel)"
      >
      </button>
    </template>
  </div>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'
import { usePlanCardStore } from '@/core/classic/plans/planCard/stores/planCardStore.ts'
import { useModuleProcessStore } from '@/core/classic/modules/moduleCard/stores/moduleProcessStore.ts'
import { useModuleLoader } from '@/core/classic/modules/moduleCard/composables/useModuleLoader.ts'
import { computed } from 'vue'
import { usePersistence } from '@/core/classic/frame/main/composables/usePersistence.ts'

const planPanels = computed(() => panelStore.planPanels)

const panelStore = usePanelStore()
const { activePanel } = storeToRefs(panelStore)

const planCardStore = usePlanCardStore()
const { loadModule } = useModuleLoader()

const handlePlanManageClick = () => {
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.clearModule()
  const hasPlan = planCardStore.plans.length > 0
  loadModule('planManage', hasPlan ? 'planManage' : 'welcome')
}

const handlePlanClick = (planPanel: { id: string }) => {
  const planId = parseInt(planPanel.id.replace('plan_', ''))
  const { getPersistence } = usePersistence()

  const panelStore = usePanelStore()
  panelStore.persistCurrentModule()

  const planPersistedData = getPersistence('plans', planPanel.id as `plan_${number}`) || {}
  const moduleToLoad = planPersistedData.currentModuleId || 'planDashboard'
  const moduleProcessStore = useModuleProcessStore()
  moduleProcessStore.setModule(moduleToLoad, planId)

  panelStore.switchPanel(
    planPanel.id,
    moduleToLoad,
    planPersistedData.modules?.[moduleToLoad]?.moduleType || 'planDashboard'
  )
  loadModule(planPanel.id, moduleToLoad)
}

const API_BASE = import.meta.env.VITE_API_BASE

const getPlanIcon = (planPanel: { id: string }) => {
  const planId = parseInt(planPanel.id.replace('plan_', ''))
  const plan = planCardStore.plans.find(p => p.plan_id === planId)
  return plan?.icon_path ? `<img src="${API_BASE}/uploads/${plan.icon_path}" class="plan-icon" alt="">` : '📋'
}
const getPlanName = (planPanel: { id: string }) => {
  const planId = parseInt(planPanel.id.replace('plan_', ''))
  const plan = planCardStore.plans.find(p => p.plan_id === planId)
  return plan?.name || '默认标题'
}
</script>

<style lang="scss">
@use '../../main/styles/layout-variables' as vars;

.panel-layer {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;

  .panel-toggle {
    padding: 0.4rem;
    border-radius: 0.3rem;
    transition: background 0.3s ease;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;

    &.active {
      background: white;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .plan-icon {
      width: 24px;
      height: 24px;
      border-radius: 4px;
      object-fit: cover;
    }
  }
}
</style>
