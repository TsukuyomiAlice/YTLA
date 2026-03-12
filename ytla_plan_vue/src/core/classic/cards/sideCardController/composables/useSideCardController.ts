import { computed, ref } from 'vue'
import { useSideCardFilter } from '@/core/classic/cards/sideCardFilter/composables/useSideCardFilter.ts'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import { useSideCardEditor } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditor.ts'

export const useSideCardController = () => {
  const { filterValue, handleFilterInput, clearFilter } = useSideCardFilter()

  const cardStore = useCardStore()
  const cards = computed(() => cardStore.cards)
  const { editorState, showCreation, closeEditor } = useSideCardEditor()
  const activeCardType = ref<string | null>(null)

  const cardTypeButtons = [
    { type: 'sample', icon: '📝', title: '添加样例卡片' },
    { type: 'timer', icon: '⏲️', title: '添加计时卡片' },
    { type: 'relax', icon: '🎲', title: '添加游戏卡片' }
  ]

  const toggleCreation = (cardType: string) => {
    if (activeCardType.value === cardType && editorState.value.visible) {
      closeEditor()
      activeCardType.value = null
    } else {
      showCreation(cardType as string)
      activeCardType.value = cardType
    }
  }

  return {
    filterValue, handleFilterInput, clearFilter,
    cards, editorState, activeCardType, cardTypeButtons,
    toggleCreation
  }
}
