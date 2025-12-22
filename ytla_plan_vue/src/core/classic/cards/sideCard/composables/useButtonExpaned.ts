import { ref, watch } from 'vue'
import type { SideCardEmits, SideCardProps } from '@/core/classic/cards/sideCard/types/sideCardType.ts'

import { usePersistence } from '@/core/classic/frame/main/composables/usePersistence.ts'
const { getPersistence, setPersistence } = usePersistence()

export const useButtonExpand = (props: SideCardProps, emit: SideCardEmits) => {
  const isExpanded = ref(
    props.cardId !== undefined
      ? getPersistence('cards', 'expanded')[props.cardId] || false
      : props.initialExpanded,
  )

  watch(isExpanded, (newVal: boolean) => {
    if (props.cardId !== undefined) {
      setPersistence('cards', {
        expanded: {
          ...getPersistence('cards', 'expanded'),
          [props.cardId.toString()]: isExpanded.value,
        },
      })
    }
    emit('toggle-expanded', newVal)
  })

  const toggleExpanded = () => {
    isExpanded.value = !isExpanded.value
  }

  return { isExpanded, toggleExpanded }
}
