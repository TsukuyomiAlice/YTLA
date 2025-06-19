import type { Component } from 'vue'
import PlanCard from '@/features/planManage/components/card/PlanCard.vue'

export interface PlanCardRegistry {
  components: { default: Component }
  getPlanProps: (plan: any) => Record<string, any>
}

const registryStore = new Map<string, PlanCardRegistry>()

export const createPlanCardRegistry = (): void => {
  registryStore.set('plan', {
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
  return registryStore.get('plan')
}

