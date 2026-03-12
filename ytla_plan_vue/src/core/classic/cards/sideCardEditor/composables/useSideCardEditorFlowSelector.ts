import type { SideCardEditorFlowSelectorProps, SideCardEditorFlowSelectorEmits } from '@/core/classic/cards/sideCardEditor/definitions/sideCardEditorType.ts'

export const useSideCardEditorFlowSelector = (
  props: SideCardEditorFlowSelectorProps,
  emit: SideCardEditorFlowSelectorEmits
) => {
  const selectSubType = (subType: string) => {
    emit('next', subType as string)
  }

  const handleCancel = () => {
    emit('cancelEdit')
  }

  return {
    selectSubType,
    handleCancel
  }
}
