import { computed, ref } from 'vue'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'

export function useSideCardLayer() {
  const cardStore = useCardStore()
  const cards = computed(() => cardStore.cards)

  const fetchCards = async () => {
    try {
      await cardStore.fetchCards()
    } catch (error) {
      console.error('获取卡片失败:', error)
    }
  }

  const handleRefresh = async () => {
    try {
      await fetchCards()
      console.log('卡片列表已刷新')
    } catch (error) {
      console.error('刷新卡片失败:', error)
    }
  }

  return {
    cards,
    fetchCards,
    handleRefresh
  }
}
