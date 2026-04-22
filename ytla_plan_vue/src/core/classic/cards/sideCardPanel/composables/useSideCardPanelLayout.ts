import { computed, nextTick, watch, ref, onMounted, onBeforeUnmount } from 'vue'
import { useMasonryLayout } from '@/core/classic/frame/main/composables/useMasonryLayout'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore'
import { usePersistence } from '@/core/classic/frame/main/composables/usePersistence'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType'

export const useSideCardPanelLayout = () => {
  const isMasonrySupported = ref(false)
  const userAgent = navigator.userAgent.toLowerCase()
  isMasonrySupported.value = userAgent.includes('safari') || userAgent.includes('firefox')

  const { getPersistence, setPersistence } = usePersistence()
  const { debouncedUpdate } = useMasonryLayout()
  const cardStore = useCardStore()
  const visibleCards = computed(() => cardStore.filteredCards)
  const activeCards = computed(() => cardStore.activeCards)

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
      const allServerIds = cardStore.activeCards.map((c: CardData) => c.card_id)

      cardOrder.value = savedOrder
        ? savedOrder.filter((id: number) => allServerIds.includes(id))
        : [...allServerIds]

      const newServerIds = allServerIds.filter((id: number) => !cardOrder.value.includes(id))
      cardOrder.value.push(...newServerIds)
      cardOrder.value = Array.from(new Set(cardOrder.value))

      updateShownOrder()
      setPersistence('cards', { 'order': cardOrder.value })
    } finally {
      isInitializing.value = false
    }
  }

  const updateShownOrder = () => {
    const visibleIds = visibleCards.value.map((c: CardData) => c.card_id)
    cardShownOrder.value = cardOrder.value.filter((id: number) => visibleIds.includes(id))

    const newVisibleIds = visibleIds.filter((id: number) => !cardShownOrder.value.includes(id))
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

        nextTick(debouncedUpdate)
      }
    }
  }

  const orderedCards = computed(() => {
    return visibleCards.value.slice().sort((a, b) => {
      const indexA = cardShownOrder.value.indexOf(a.card_id)
      const indexB = cardShownOrder.value.indexOf(b.card_id)
      return indexA - indexB
    })
  })

  // Watch 逻辑移到这里
  let unwatchActiveCards: (() => void) | null = null
  let unwatchVisibleCards: (() => void) | null = null

  const setupWatchers = () => {
    unwatchActiveCards = watch(activeCards, () => {
      nextTick(() => {
        debouncedUpdate()
      })
    }, { deep: true })

    unwatchVisibleCards = watch(visibleCards, () => {
      nextTick(debouncedUpdate)
    }, { deep: true, immediate: true })
  }

  const cleanupWatchers = () => {
    if (unwatchActiveCards) unwatchActiveCards()
    if (unwatchVisibleCards) unwatchVisibleCards()
  }

  onMounted(async () => {
    document.addEventListener('drop', handleDrop)
    await initializeOrder()
    setupWatchers()
    await nextTick(debouncedUpdate)
  })

  onBeforeUnmount(() => {
    document.removeEventListener('drop', handleDrop)
    cleanupWatchers()
  })

  return {
    isMasonrySupported,
    orderedCards,
    cardOrder,
    handleDrop,
    debouncedUpdate,
    visibleCards,
    activeCards,
    isInitializing,
    initializeOrder,
    updateShownOrder
  }
}
