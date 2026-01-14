import type { SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'
import { ref } from 'vue'

import { useButtonPin } from '@/core/classic/cards/sideCard/composables/useButtonPin.ts'

export const useContainerSideCard = (props: SideCardProps) => {

  const isDragging = ref(false)

  // 拖动处理函数
  const handleDragStart = (e: DragEvent) => {

    const { isPinned } = useButtonPin(props)

    const cardId = props.cardId || 0
    if (isPinned.value) {
      e.preventDefault()
      return
    }
    isDragging.value = true
    e.dataTransfer?.setData('text/plain', cardId.toString() || '')
    document.body.classList.add('dragging-active')
  }

  const handleDragEnd = () => {
    isDragging.value = false
    document.body.classList.remove('dragging-active')
  }

  return { isDragging, handleDragStart, handleDragEnd }
}
