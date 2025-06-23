<template>
  <div class="masonry-container">
    <div class="plan-masonry-grid">
      <transition-group name="fade-scale">
        <component
          :is="getComponent(plan)"
          v-for="plan in orderedPlans"
          :key="plan.plan_id"
          :plan-id="plan.plan_id"
          :data-plan-id="plan.plan_id"
          :order="planOrder.indexOf(plan.plan_id)"
          v-bind="getPlanProps(plan)"
          @edit="handleEditPlan"
          @deactivate="handleDeactivatePlan"
          @close="handleClosePlan"
        />
      </transition-group>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, watch, ref, onMounted } from 'vue'
import { usePlanContainer } from '@/features/planManage/composables/usePlanContainer.ts'
import { useMasonryLayout } from '@/core/frame/composables/useMasonryLayout.ts'
import { getPlanCardRegistry } from '@/core/plans/registries/planCardRegistry.ts'
import { usePlanCardStore } from '@/features/planManage/stores/planCardStore.ts'
import { usePersistence } from '@/core/frame/composables/usePersistence.ts'

const { getPersistence, setPersistence } = usePersistence()

const {
  activePlans,
  handleEditPlan,
  handleDeactivatePlan,
  handleClosePlan
} = usePlanContainer()

// layout
const { updateLayout } = useMasonryLayout()

watch(activePlans, () => {
  nextTick(() => {
    updateLayout()
  })
}, { deep: true })

const getComponent = (plan: any) => {
  const registry = getPlanCardRegistry()
  return registry?.components.default
}

const getPlanProps = (plan: any) => {
  const registry = getPlanCardRegistry()
  return registry ? registry.getPlanProps(plan) : {}
}

// plan store for react with visible planCards
const planStore = usePlanCardStore()

// react with drag planCards and plan order
const planOrder = ref<number[]>([])
const planShownOrder = ref<number[]>([])
const isInitializing = ref(true)

const initializeOrder = async () => {
  try {
    await new Promise<void>((resolve) => {
      const check = () => {
        if (planStore.activePlans.length > 0) {
          resolve()
        } else {
          setTimeout(check, 50)
        }
      }
      check()
    })

    const savedOrder = getPersistence('planCards', 'order')
    const allServerIds = planStore.activePlans.map(c => c.plan_id)

    planOrder.value = savedOrder
      ? savedOrder.filter((id: number) => allServerIds.includes(id))
      : [...allServerIds]

    const newServerIds = allServerIds.filter(id => !planOrder.value.includes(id))
    planOrder.value.push(...newServerIds)
    planOrder.value = Array.from(new Set(planOrder.value))

    updateShownOrder()

    setPersistence('planCards', { 'order': planOrder.value })
  } finally {
    isInitializing.value = false
  }
}

const updateShownOrder = () => {
  const visibleIds = activePlans.value.map(c => c.plan_id)
  planShownOrder.value = planOrder.value.filter(id => visibleIds.includes(id))

  const newVisibleIds = visibleIds.filter(id => !planShownOrder.value.includes(id))
  planShownOrder.value.push(...newVisibleIds)
}

const handleDrop = (e: DragEvent) => {
  if (isInitializing.value) return

  const fromId = Number(e.dataTransfer?.getData('text/plain') || 0)
  const toElement = (e.target as HTMLElement)?.closest('[data-plan-id]') as HTMLElement | null
  const toId = toElement ? Number(toElement.dataset.planId) : 0

  if (fromId && toId && fromId !== toId) {
    const newShownOrder = [...planShownOrder.value]
    const fromIndex = newShownOrder.indexOf(fromId)
    const toIndex = newShownOrder.indexOf(toId)

    if (fromIndex > -1 && toIndex > -1) {
      newShownOrder.splice(fromIndex, 1)
      newShownOrder.splice(toIndex, 0, fromId)
      planShownOrder.value = newShownOrder

      const globalFromIndex = planOrder.value.indexOf(fromId)
      const globalToIndex = planOrder.value.indexOf(toId)
      if (globalFromIndex > -1 && globalToIndex > -1) {
        const newGlobalOrder = [...planOrder.value]
        newGlobalOrder.splice(globalFromIndex, 1)
        newGlobalOrder.splice(globalToIndex, 0, fromId)
        planOrder.value = newGlobalOrder
        setPersistence('planCards', { 'order': newGlobalOrder })
      }

      nextTick(updateLayout)
    }
  }
}

watch(activePlans, () => {
  if (isInitializing.value) return
  updateShownOrder()
  nextTick(updateLayout)
}, { deep: true, immediate: true })

const orderedPlans = computed(() => {
  return activePlans.value.slice().sort((a, b) => {
    const indexA = planShownOrder.value.indexOf(a.plan_id)
    const indexB = planShownOrder.value.indexOf(b.plan_id)
    return indexA - indexB
  })
})

onMounted(async () => {
  document.addEventListener('drop', handleDrop)
  await initializeOrder()
  await nextTick(updateLayout)
})

</script>

<style lang="scss" scoped>
@use '@/core/sideCards/styles/card-container';
</style>
