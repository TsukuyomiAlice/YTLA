import { ref, onMounted, watch } from 'vue'
import { usePlanCardStore } from '@/features/planManage/stores/planCardStore.ts'
import { useModuleProcessStore } from '@/core/modules/_type/stores/moduleProcessStore.ts'

// activeFlag change
const planStore = usePlanCardStore()
const moduleProcessStore = useModuleProcessStore()
const activeFlag = ref('1')

export const usePlanActiveFlag = () => {
  const loadPlanData = async (planId: number) => {
    try {
      const plan = planStore.plans.find(p => p.plan_id === planId)
      if (plan) {
        activeFlag.value = plan.active_flag as string
      }
    } catch (error) {
      console.error('加载计划数据失败:', error)
    }
  }

  // 使用组件上下文
  onMounted(() => {
    if (moduleProcessStore.belongPlanId) {
      loadPlanData(moduleProcessStore.belongPlanId)
    }
  })

  watch(
    () => planStore.plans.find(p => p.plan_id === moduleProcessStore.belongPlanId),
    (newPlan) => {
      if (newPlan) {
        activeFlag.value = newPlan.active_flag || '1'
      }
    },
    { deep: true }
  )

  return { activeFlag }
}
