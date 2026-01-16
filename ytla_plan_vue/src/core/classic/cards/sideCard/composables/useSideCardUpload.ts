import type { SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'
import { useCardStore } from '@/core/classic/cards/sideCard/stores/cardStore.ts'
import { computed, ref } from 'vue'

import { CardService } from '@/core/classic/cards/sideCard/services/cardService.ts'
const API_BASE = import.meta.env.VITE_API_BASE
const cardService = new CardService(API_BASE)

export const useSideCardUpload = (props: SideCardProps) => {
  const store = useCardStore()

  const fullIconPath = computed(() => ({
    iconImage: props.icon ? `${API_BASE}/uploads/${props.icon}` : '',
  }))
  const containerStyle = ref({
    backgroundImage: props.background ? `url(${API_BASE}/uploads/${props.background})` : '',
  })

  const handleFileUpload = async (event: Event, type: 'icon' | 'background') => {
    const input = event.target as HTMLInputElement
    const file = input.files?.[0]
    if (!file || !props.cardId) return

    try {
      const uploadResult = await cardService.uploadFile(type, file)

      if (type === 'icon') {
        await store.updateCardIcon(props.cardId, uploadResult.filename)
        fullIconPath.value.iconImage = `${API_BASE}/uploads/${uploadResult.filename}`
      } else {
        await store.updateCardBackground(props.cardId, uploadResult.filename)
        containerStyle.value.backgroundImage = `url(${API_BASE}/uploads/${uploadResult.filename})`
      }
    } catch (error) {
      console.error('上传失败:', error)
    } finally {
      input.value = ''
    }
  }

  return { handleFileUpload }
}
