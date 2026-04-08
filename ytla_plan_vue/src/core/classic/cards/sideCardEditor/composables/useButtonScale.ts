import type { ComputedRef } from 'vue'
import { computed } from 'vue'
import type { ButtonScaleProps } from '../definitions/ButtonScaleType'

export interface UseButtonScaleReturn {
  handleClick: () => void
  defaultAriaLabel: ComputedRef<string>
  computedAriaLabel: ComputedRef<string>
  computedTitle: ComputedRef<string>
}

export const useButtonScale = (
  props: ButtonScaleProps,
  emit: (e: 'click') => void
): UseButtonScaleReturn => {
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
