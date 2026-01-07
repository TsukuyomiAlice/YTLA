import type { SideCardEmits, SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'

export const useButtonClose = (props: SideCardProps, emit: SideCardEmits) => {
  const store = useCardStore()
  const handleClose = async () => {
    if (props.cardId) {
      try {
        await store.deleteCard(props.cardId)
        emit('close', props.cardId)
      } catch (error) {}
    }
  }

  return { handleClose }
}
