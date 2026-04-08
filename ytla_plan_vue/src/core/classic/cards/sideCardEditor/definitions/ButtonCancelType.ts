export interface ButtonCancelProps {
  ariaLabel?: string
  title?: string
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
