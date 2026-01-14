import { ref, nextTick } from 'vue'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import type { SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'

export const useBarDescription = (props: SideCardProps) => {
  const store = useCardStore()

  // description相关状态
  const descriptionRef = ref<HTMLElement | null>(null)
  const isDescriptionEditable = ref(false)
  const originalDescription = ref(props.description || '')

  // 选择文本的辅助函数
  const selectText = (element: Element | null) => {
    if (!element) return
    const range = document.createRange()
    range.selectNodeContents(element)
    const sel = window.getSelection()
    sel?.removeAllRanges()
    sel?.addRange(range)
  }

  // 处理description编辑完成后的事件
  const handleDescriptionBlur = async (e: Event) => {
    const newDescription = (e.target as HTMLElement).innerText.trim()
    isDescriptionEditable.value = false

    if (newDescription !== originalDescription.value && props.cardId) {
      try {
        await store.updateCardDescription(props.cardId, newDescription)
        originalDescription.value = newDescription
      } catch (error) {
        if (descriptionRef.value) descriptionRef.value.innerText = originalDescription.value
      }
    }
  }

  // 开始编辑description
  const startEditDescription = async () => {
    isDescriptionEditable.value = true
    await nextTick()
    if (descriptionRef.value) {
      descriptionRef.value.focus()
      selectText(descriptionRef.value)
    }
  }

  // 取消编辑description
  const cancelEditDescription = () => {
    isDescriptionEditable.value = false
    if (descriptionRef.value) {
      descriptionRef.value.innerText = originalDescription.value
    }
  }

  return { descriptionRef, isDescriptionEditable, handleDescriptionBlur, startEditDescription, cancelEditDescription }
}
