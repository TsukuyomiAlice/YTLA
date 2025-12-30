import type { SideCardEmits, SideCardProps } from '@/core/classic/cards/sideCard/types/sideCardType.ts'

export const useButtonEdit = (props: SideCardProps, emit: SideCardEmits) => {

  const handleEdit = () => {
    if (props.cardId) {
      emit('edit', props.cardId)
    }
  }

  return { handleEdit }
}
