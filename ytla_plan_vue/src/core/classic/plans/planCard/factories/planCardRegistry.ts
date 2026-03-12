import type { Component } from 'vue'
import PlanCard from '@/core/classic/plans/planCard/components/PlanCard.vue'

export interface PlanCardRegistry {
  components: { default: Component }
  getPlanProps: (plan: any) => Record<string, any>
}

const planCardRegistryStore = new Map<string, PlanCardRegistry>()

export const createPlanCardRegistry = (): void => {
  planCardRegistryStore.set('plan', {
    components: { default: PlanCard },
    getPlanProps: (plan) => ({
      planId: plan.plan_id,
      name: plan.name,
      tags: plan.tags,
      description: plan.description,
      icon: plan.icon_path,
      background: plan.background_path
    })
  })
}

export const getPlanCardRegistry = () => {
  return planCardRegistryStore.get('plan')
}

// 自动注册
createPlanCardRegistry()
