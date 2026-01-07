import { ref, computed, onMounted } from 'vue'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import { useSideCardEditor } from '../../sideCardEditor/composables/useSideCardEditor.ts'

export const useSideCardPanel = () => {
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
