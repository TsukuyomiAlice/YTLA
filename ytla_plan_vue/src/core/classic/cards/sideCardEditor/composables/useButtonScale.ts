import { computed } from 'vue'
import type { ButtonScaleProps, ButtonScaleEmits } from '../definitions/ButtonScaleType'

export const useButtonScale = (
  props: ButtonScaleProps,
  emit: ButtonScaleEmits
) => {
  const handleClick = () => {
    emit('click')
  }

  const defaultAriaLabel = computed(() => props.label || 'Scale')
  const computedAriaLabel = computed(() => props.ariaLabel || defaultAriaLabel.value)
  const computedTitle = computed(() => props.title || defaultAriaLabel.value)

  return {
    handleClick,
    defaultAriaLabel,
    computedAriaLabel,
    computedTitle
  }
}
