import { computed, ref } from 'vue'
import type { SideCardProps } from '@/core/classic/cards/sideCard/definitions/sideCardType.ts'
import { useSideCardUpload } from '@/core/classic/cards/sideCard/composables/useSideCardUpload.ts'

export const useButtonChangeIcon = (props: SideCardProps) => {
  const API_BASE = import.meta.env.VITE_API_BASE

  const fullIconPath = computed(() => ({
    iconImage: props.icon ? `${API_BASE}/uploads/${props.icon}` : '',
  }))

  const iconUploadInput = ref<HTMLInputElement | null>(null)

  const triggerIconUpload = () => {
    iconUploadInput.value?.click()
  }

  const { handleFileUpload } = useSideCardUpload(props)
  const handleIconUpload = async (event: Event) => {
    await handleFileUpload(event, 'icon')
  }

  return { fullIconPath, iconUploadInput, triggerIconUpload, handleIconUpload }
}
