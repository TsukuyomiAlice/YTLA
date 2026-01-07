import { ref, computed, onMounted } from 'vue'
import type { Plan } from '@/core/classic/plans/planCard/definitions/planTypes.ts'
import { usePlanCardStore } from '@/core/classic/plans/planCard/stores/planCardStore.ts'
import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'

export const usePlanContainer = () => {
  const plans = ref<Plan[]>([])
  const planStore = usePlanCardStore()
  const activePlans = computed(() => planStore.activePlans)

  const fetchPlans = async () => {
    await planStore.fetchPlans()
  }

  onMounted(fetchPlans)

  const handleEditPlan = (planId: number) => {
    const plan = activePlans.value.find(c => c.plan_id === planId)
    if (plan) {
      const panelStore = usePanelStore()
      panelStore.switchPanel(`plan_${planId}`, 'planDashboard')
    }
  }

  const handleDeactivatePlan = async (planId: number) => {
    try {
      await planStore.deactivatePlan(planId)
      await fetchPlans()
    } catch (error) {

    }
  }

  const handleClosePlan = async (planId: number) => {
    try {
      await planStore.deletePlan(planId)
      await fetchPlans()
    } catch (error) {

    }
  }

  return {
    plans,
    activePlans,
    fetchPlans,
    handleEditPlan,
    handleDeactivatePlan,
    handleClosePlan
  }
}
