import { ref } from 'vue'
import type {
  SideEditorFlowNavigatorEmits,
  SideEditorFlowNavigatorProps,
} from '@/core/classic/cards/sideCardEditor/definitions/sideCardEditorNavigatorType.ts'

export const useSideCardEditorFlowNavigator = (
  props: SideEditorFlowNavigatorProps,
  emit: SideEditorFlowNavigatorEmits,
) => {

  const isSubmitting = ref(false)

  const handleCancel = () => {
    if (!isSubmitting.value) emit('cancelEdit')
  }

  const handlePrev = () => {
    if (!isSubmitting.value) emit('prev')
  }

  const handleNext = () => {
    if (!isSubmitting.value) emit('next')
  }

  const handleSubmit = async () => {
    if (isSubmitting.value || props.submitDisabled) return

    isSubmitting.value = true
    try {
      emit('submit')
    } finally {
      isSubmitting.value = false
    }
  }

  return { isSubmitting, handleCancel, handlePrev, handleNext, handleSubmit }
}
