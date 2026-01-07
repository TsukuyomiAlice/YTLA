import { computed, ref } from 'vue'
import type { SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'
import { useSideCardUpload } from '@/core/classic/cards/sideCard/composables/useSideCardUpload.ts'

export const useButtonChangeBackground = (props: SideCardProps) => {
  const API_BASE = import.meta.env.VITE_API_BASE

  const containerStyle = computed(() => ({
    backgroundImage: props.background ? `url(${API_BASE}/uploads/${props.background})` : '',
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  }))

  const bgUploadInput = ref<HTMLInputElement | null>(null)

  const triggerBgUpload = () => {
    bgUploadInput.value?.click()
  }

  const { handleFileUpload } = useSideCardUpload(props)
  const handleBgUpload = async (event: Event) => {
    await handleFileUpload(event, 'background')
  }

  return { containerStyle, bgUploadInput, triggerBgUpload, handleBgUpload }
}
