import { computed } from 'vue'
import type { ButtonCancelProps, ButtonCancelEmits } from '../definitions/ButtonCancelType'

export const useButtonCancel = (
  props: ButtonCancelProps,
  emit: ButtonCancelEmits
) => {
  const handleClick = async () => {
    const opts = props.options && 'value' in props.options ? props.options.value : props.options

    if (opts?.confirmDialog?.enabled) {
      const confirmed = window.confirm(
        opts.confirmDialog.message || '确定要取消吗？'
      )
      if (!confirmed) {
        return
      }
    }

    emit('click')
  }

  const defaultAriaLabel = computed(() => 'Cancel')
  const computedAriaLabel = computed(() => props.ariaLabel || defaultAriaLabel.value)
  const computedTitle = computed(() => props.title || defaultAriaLabel.value)

  return {
    handleClick,
    defaultAriaLabel,
    computedAriaLabel,
    computedTitle
  }
}
