import type { SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import { useButtonChangeIcon } from '@/core/classic/cards/sideCard/composables/useButtonChangeIcon.ts'

export const useContainerIcon = (props: SideCardProps) => {
  const store = useCardStore()
  const { fullIconPath } = useButtonChangeIcon(props)

  const handleIconError = (e: Event) => {
    const img = e.target as HTMLImageElement
    img.style.display = 'none'

    // 添加重置监听器
    const resetDisplay = () => {
      img.style.display = ''
      img.removeEventListener('load', resetDisplay)
    }

    // 当新的src加载成功时自动重置显示
    img.addEventListener('load', resetDisplay)
  }

  const removeIcon = async () => {
    if (!props.cardId) return

    try {
      await store.updateCardIcon(props.cardId, '')
      fullIconPath.value.iconImage = ''
    } catch (error) {}
  }

  return { handleIconError, removeIcon }
}
