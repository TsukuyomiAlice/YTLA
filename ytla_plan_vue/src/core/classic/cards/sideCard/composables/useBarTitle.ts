import { ref, nextTick } from 'vue'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import type { SideCardProps } from '@/core/classic/cards/sideCard/types/sideCardType.ts'

export const useBarTitle = (props: SideCardProps) => {
  const store = useCardStore()

  // title相关状态
  const titleRef = ref<HTMLElement | null>(null)
  const isTitleEditable = ref(false)
  const originalTitle = ref(props.name || '')

  // 选择文本的辅助函数
  const selectText = (element: Element | null) => {
    if (!element) return
    const range = document.createRange()
    range.selectNodeContents(element)
    const sel = window.getSelection()
    sel?.removeAllRanges()
    sel?.addRange(range)
  }

  // 处理title编辑完成后的事件
  const handleTitleBlur = async (e: Event) => {
    const newTitle = (e.target as HTMLElement).innerText.trim()
    isTitleEditable.value = false

    if (newTitle !== originalTitle.value && props.cardId) {
      try {
        await store.updateCardTitle(props.cardId, newTitle)
        originalTitle.value = newTitle
      } catch (error) {
        if (titleRef.value) titleRef.value.innerText = originalTitle.value
      }
    }
  }

  // 开始编辑title
  const startEditTitle = () => {
    isTitleEditable.value = true
    nextTick(() => {
      if (titleRef.value) {
        titleRef.value.focus()
        selectText(titleRef.value)
      }
    })
  }

  // 取消编辑title
  const cancelEditTitle = () => {
    isTitleEditable.value = false
    if (titleRef.value) {
      titleRef.value.innerText = originalTitle.value
    }
  }

  return { titleRef, isTitleEditable, handleTitleBlur, startEditTitle, cancelEditTitle }
}
