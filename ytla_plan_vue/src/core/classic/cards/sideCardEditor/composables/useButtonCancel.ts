import type { Ref, ComputedRef } from 'vue'
import { computed } from 'vue'
import type { ButtonCancelProps, ButtonCancelEmits, ButtonCancelOptions } from '../definitions/ButtonCancelType'

export interface UseButtonCancelReturn {
  handleClick: () => void | Promise<void>
  defaultAriaLabel: ComputedRef<string>
  computedAriaLabel: ComputedRef<string>
  computedTitle: ComputedRef<string>
}

export const useButtonCancel = (
  props: ButtonCancelProps,
  emit: ButtonCancelEmits,
  options?: Ref<ButtonCancelOptions> | ButtonCancelOptions
): UseButtonCancelReturn => {
  const handleClick = async () => {
    const opts = options && 'value' in options ? options.value : options

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
