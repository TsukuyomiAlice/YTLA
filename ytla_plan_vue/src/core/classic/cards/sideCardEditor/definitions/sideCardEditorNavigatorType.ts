export interface SideEditorFlowNavigatorProps {
  isEditing?: boolean
  showCancel?: boolean
  showPrev?: boolean
  showNext?: boolean
  showSubmit?: boolean
  submitDisabled?: boolean
}


export type SideEditorFlowNavigatorEmits = {
  (e: 'cancelEdit'): void
  (e: 'prev'): void
  (e: 'next'): void
  (e: 'submit'): void
}
