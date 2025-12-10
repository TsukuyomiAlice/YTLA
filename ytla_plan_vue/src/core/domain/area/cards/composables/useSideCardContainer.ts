import { ref, computed, onMounted } from 'vue'
import type { CardData } from '@/core/domain/area/cards/types/cardDataType.ts'
import { useCardStore } from '@/core/domain/area/cards/stores/cardStore.ts'
import { useSideCardEditor } from './useSideCardEditor.ts'

export const useSideCardContainer = () => {
  const cards = ref<CardData[]>([])
  const cardStore = useCardStore()
  const activeCards = computed(() => cardStore.activeCards)

  const fetchCards = async () => {
    await cardStore.fetchCards()
  }

  onMounted(fetchCards)

  const handleEditCard = (cardId: number) => {
    const card = activeCards.value.find(c => c.card_id === cardId)
    if (card) {
      const { showEdit } = useSideCardEditor()
      showEdit(card)
    }
  }

  const handleDeactivateCard = async (cardId: number) => {
    try {
      await cardStore.deactivateCard(cardId)
      await fetchCards()
    } catch (error) {

    }
  }

  const handleCloseCard = async (cardId: number) => {
    try {
      await cardStore.deleteCard(cardId)
      await fetchCards()
    } catch (error) {

    }
  }

  return {
    cards,
    activeCards,
    fetchCards,
    handleEditCard,
    handleDeactivateCard,
    handleCloseCard
  }
}
