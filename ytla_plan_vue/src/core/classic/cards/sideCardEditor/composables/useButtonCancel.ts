import type { Ref } from 'vue'

export interface ButtonCancelOptions {
  confirmDialog?: {
    enabled: boolean
    title?: string
    message?: string
    confirmText?: string
    cancelText?: string
  }
}

export interface UseButtonCancelReturn {
  handleClick: () => void | Promise<void>
}

export const useButtonCancel = (
  emit: (e: 'click') => void,
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

  return {
    handleClick
  }
}
