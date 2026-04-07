export interface ButtonActionProps {
  type?: 'cancel' | 'prev' | 'next' | 'submit'
  disabled?: boolean
  ariaLabel?: string
  title?: string
}

export type ButtonActionEmits = {
  (e: 'click'): void
}
