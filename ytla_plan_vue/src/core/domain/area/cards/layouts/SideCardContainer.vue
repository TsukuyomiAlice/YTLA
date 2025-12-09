<template>
  <div class="masonry-container">
    <div :class="{ 'masonry-grid': isMasonrySupported, 'non-masonry-grid': !isMasonrySupported }">
      <transition-group name="fade-scale">
        <component
          :is="getComponent(card)"
          v-for="card in orderedCards"
          :key="card.card_id"
          :card-id="card.card_id"
          :data-card-id="card.card_id"
          :order="cardOrder.indexOf(card.card_id)"
          v-bind="getCardProps(card)"
          @edit="handleEditCard"
          @deactivate="handleDeactivateCard"
          @close="handleCloseCard"
        />
      </transition-group>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, nextTick, watch, ref, onMounted } from 'vue'
import { useSideCardContainer } from '@/core/domain/area/cards/composables/useSideCardContainer.ts'
import { useMasonryLayout } from '@/core/domain/area/frame/composables/useMasonryLayout.ts'
import { getCardRegistry } from '@/core/domain/area/cards/registries/cardRegistry.ts'
import { useCardStore } from '@/core/domain/area/cards/stores/cardStore.ts'
import { usePersistence } from '@/core/domain/area/frame/composables/usePersistence.ts'

const isMasonrySupported = ref(false)
const userAgent = navigator.userAgent.toLowerCase()
isMasonrySupported.value = userAgent.includes('safari') || userAgent.includes('firefox')


const { getPersistence, setPersistence } = usePersistence()

const {
  activeCards,
  handleEditCard,
  handleDeactivateCard,
  handleCloseCard
} = useSideCardContainer()

// layout
const { updateLayout } = useMasonryLayout()

watch(activeCards, () => {
  nextTick(() => {
    updateLayout()
  })
}, { deep: true })

const getComponent = (card: any) => {
  const registry = getCardRegistry(card.card_type)
  return registry?.components[card.card_sub_type]
}

const getCardProps = (card: any) => {
  const registry = getCardRegistry(card.card_type)
  return registry ? registry.getCardProps(card) : {}
}

// card store for react with visible cards
const cardStore = useCardStore()
const visibleCards = computed(() => cardStore.filteredCards)

// react with drag cards and card order

const cardOrder = ref<number[]>([])
const cardShownOrder = ref<number[]>([])
const isInitializing = ref(true)

const initializeOrder = async () => {
  try {
    await new Promise<void>((resolve) => {
      const check = () => {
        if (cardStore.activeCards.length > 0) {
          resolve()
        } else {
          setTimeout(check, 50)
        }
      }
      check()
    })

    const savedOrder = getPersistence('cards', 'order')
    const allServerIds = cardStore.activeCards.map(c => c.card_id)

    cardOrder.value = savedOrder
      ? savedOrder.filter((id: number) => allServerIds.includes(id))
      : [...allServerIds]

    const newServerIds = allServerIds.filter(id => !cardOrder.value.includes(id))
    cardOrder.value.push(...newServerIds)
    cardOrder.value = Array.from(new Set(cardOrder.value))

    updateShownOrder()
    setPersistence('cards', { 'order': cardOrder.value })
  } finally {
    isInitializing.value = false
  }
}

const updateShownOrder = () => {
  const visibleIds = visibleCards.value.map(c => c.card_id)
  cardShownOrder.value = cardOrder.value.filter(id => visibleIds.includes(id))

  const newVisibleIds = visibleIds.filter(id => !cardShownOrder.value.includes(id))
  cardShownOrder.value.push(...newVisibleIds)
}

const handleDrop = (e: DragEvent) => {
  if (isInitializing.value) return

  const fromId = Number(e.dataTransfer?.getData('text/plain') || 0)
  const toElement = (e.target as HTMLElement)?.closest('[data-card-id]') as HTMLElement | null
  const toId = toElement ? Number(toElement.dataset.cardId) : 0

  if (fromId && toId && fromId !== toId) {
    const newShownOrder = [...cardShownOrder.value]
    const fromIndex = newShownOrder.indexOf(fromId)
    const toIndex = newShownOrder.indexOf(toId)

    if (fromIndex > -1 && toIndex > -1) {
      newShownOrder.splice(fromIndex, 1)
      newShownOrder.splice(toIndex, 0, fromId)
      cardShownOrder.value = newShownOrder

      const globalFromIndex = cardOrder.value.indexOf(fromId)
      const globalToIndex = cardOrder.value.indexOf(toId)
      if (globalFromIndex > -1 && globalToIndex > -1) {
        const newGlobalOrder = [...cardOrder.value]
        newGlobalOrder.splice(globalFromIndex, 1)
        newGlobalOrder.splice(globalToIndex, 0, fromId)
        cardOrder.value = newGlobalOrder
        setPersistence('cards', { 'order': newGlobalOrder })
      }

      nextTick(updateLayout)
    }
  }
}

watch(visibleCards, () => {
  if (isInitializing.value) return
  updateShownOrder()
  nextTick(updateLayout)
}, { deep: true, immediate: true })

const orderedCards = computed(() => {
  return visibleCards.value.slice().sort((a, b) => {
    const indexA = cardShownOrder.value.indexOf(a.card_id)
    const indexB = cardShownOrder.value.indexOf(b.card_id)
    return indexA - indexB
  })
})

onMounted(async () => {
  document.addEventListener('drop', handleDrop)
  await initializeOrder()
  nextTick(updateLayout)
})

</script>

<style lang="scss" scoped>
@use '../styles/card-container';
</style>
