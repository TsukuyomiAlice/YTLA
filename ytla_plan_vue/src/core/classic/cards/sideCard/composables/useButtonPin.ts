import type { SideCardProps } from '@/core/classic/cards/sideCard/types/sideCardType.ts'
import { usePersistence } from '@/core/classic/frame/main/composables/usePersistence.ts'
const { getPersistence, setPersistence } = usePersistence()
import { ref } from 'vue'

export const useButtonPin = (props: SideCardProps) => {

  const isPinned = ref(
    props.cardId !== undefined
      ? getPersistence('cards', 'pinned')[props.cardId.toString()] || false
      : false
  )

  const togglePin = () => {
    const cardId = props.cardId || 0
    isPinned.value = !isPinned.value
    setPersistence('cards', {
      pinned: {
        ...getPersistence('cards', 'pinned'),
        [cardId.toString()]: isPinned.value
      }
    })
  }

  return { isPinned, togglePin }
}
