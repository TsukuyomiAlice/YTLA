import { ref, computed, onMounted } from 'vue'
import type { Plan } from '@/core/plans/_type/types/planTypes.ts'
import { usePlanCardStore } from '@/features/planManage/stores/planCardStore.ts'
import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'

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
