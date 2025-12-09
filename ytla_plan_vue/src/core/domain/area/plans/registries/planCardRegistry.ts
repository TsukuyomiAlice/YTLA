import type { Component } from 'vue'
import PlanCard from '@/core/domain/area/plans/components/PlanCard.vue'

export interface PlanCardRegistry {
  components: { default: Component }
  getPlanProps: (plan: any) => Record<string, any>
}

const planRegistryStore = new Map<string, PlanCardRegistry>()

export const createPlanCardRegistry = (): void => {
  planRegistryStore.set('plan', {
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
  return planRegistryStore.get('plan')
}

