import { computed } from 'vue'
import type { ButtonActionProps, ButtonActionEmits } from '../definitions/ButtonActionType'

export const useButtonAction = (
  props: ButtonActionProps,
  emit: ButtonActionEmits
) => {

  const defaultAriaLabel = computed(() => {
    switch (props.type) {
      case 'cancel':
        return 'Cancel'
      case 'prev':
        return 'Prev'
      case 'next':
        return 'Next'
      case 'submit':
        return 'Submit'
      default:
        return 'Submit'
    }
  })

  const computedAriaLabel = computed(() => props.ariaLabel || defaultAriaLabel.value)
  const computedTitle = computed(() => props.title || defaultAriaLabel.value)

  const handleClick = () => {
    emit('click')
  }

  return {
    defaultAriaLabel,
    computedAriaLabel,
    computedTitle,
    handleClick
  }
}
