export interface ButtonScaleProps {
  icon: string
  label?: string
  showLabel?: boolean
  ariaLabel?: string
  title?: string
}

export type ButtonScaleEmits = {
  (e: 'click'): void
}
