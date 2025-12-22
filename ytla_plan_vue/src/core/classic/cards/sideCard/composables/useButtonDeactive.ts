import type { SideCardEmits, SideCardProps } from '@/core/classic/cards/sideCard/types/sideCardType.ts'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'

export const useButtonDeactivate = (props: SideCardProps, emit: SideCardEmits) => {
  const store = useCardStore()
  const handleDeactivate = async () => {
    if (props.cardId) {
      try {
        await store.deactivateCard(props.cardId)
        emit('deactivate', props.cardId)
      } catch (error) {}
    }
  }

  return { handleDeactivate }
}
