import type { Ref } from 'vue'

export interface ButtonCancelProps {
  ariaLabel?: string
  title?: string
  options?: Ref<ButtonCancelOptions> | ButtonCancelOptions
}

export type ButtonCancelEmits = {
  (e: 'click'): void
}

export interface ButtonCancelOptions {
  confirmDialog?: {
    enabled: boolean
    title?: string
    message?: string
    confirmText?: string
    cancelText?: string
  }
}
