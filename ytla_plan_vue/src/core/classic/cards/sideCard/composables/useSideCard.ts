import type { SideCardProps, SideCardEmits } from '@/core/classic/cards/sideCard/types/sideCardType.ts'

import { useContainerSideCard } from '@/core/classic/cards/sideCard/composables/useContainerSideCard.ts'
import { useButtonPin } from '@/core/classic/cards/sideCard/composables/useButtonPin.ts'
import { useButtonChangeIcon } from '@/core/classic/cards/sideCard/composables/useButtonChangeIcon.ts'
import { useButtonChangeBackground } from '@/core/classic/cards/sideCard/composables/useButtonChangeBackground.ts'
import { useButtonDeactivate } from '@/core/classic/cards/sideCard/composables/useButtonDeactive.ts'
import { useButtonClose } from '@/core/classic/cards/sideCard/composables/useButtonClose.ts'
import { useSideCardUpload } from '@/core/classic/cards/sideCard/composables/useSideCardUpload.ts'
import { useButtonExpand } from '@/core/classic/cards/sideCard/composables/useButtonExpaned.ts'
import { useContainerIcon } from '@/core/classic/cards/sideCard/composables/useContainerIcon.ts'
import { useBarTitle } from '@/core/classic/cards/sideCard/composables/useBarTitle.ts'
import { useBarDescription } from '@/core/classic/cards/sideCard/composables/useBarDescription.ts'
import { useBarTags } from '@/core/classic/cards/sideCard/composables/useBarTags.ts'

// 在 useSideCard 函数中
export const useSideCard = (props: SideCardProps, emit: SideCardEmits) => {

  // side card container
  const { isDragging, handleDragStart, handleDragEnd } = useContainerSideCard(props)

  // pin button
  const { isPinned, togglePin } = useButtonPin(props)
  // icon upload button
  const { fullIconPath, iconUploadInput, triggerIconUpload, handleIconUpload } = useButtonChangeIcon(props)
  // background upload button
  const { containerStyle, bgUploadInput, triggerBgUpload, handleBgUpload } = useButtonChangeBackground(props)
  // for upload
  const { handleFileUpload } = useSideCardUpload(props)

  // deactivate button
  const { handleDeactivate } = useButtonDeactivate(props, emit)
  // close button
  const { handleClose } = useButtonClose(props, emit)

  // icon container
  const { handleIconError, removeIcon } = useContainerIcon(props)
  // title bar
  const { titleRef, isTitleEditable, handleTitleBlur, startEditTitle, cancelEditTitle } = useBarTitle(props)
  // description bar
  const { descriptionRef, isDescriptionEditable, handleDescriptionBlur, startEditDescription, cancelEditDescription } = useBarDescription(props)

  // card expand button
  const { isExpanded, toggleExpanded } = useButtonExpand(props, emit)

  // tags
  const { tagsArray, isAddingTag, newTag, tagInput, shouldShowAddButton, showAddButton, startAddingTag, addNewTag, removeTag, cancelAddTag } = useBarTags(props, emit)



  const handleLeftAction = (action: string) => {
    emit('left-action', action)
  }

  return {
    isDragging, handleDragStart, handleDragEnd,
    isPinned, togglePin,
    fullIconPath, iconUploadInput, triggerIconUpload, handleIconUpload,
    containerStyle, bgUploadInput, triggerBgUpload, handleBgUpload,
    handleFileUpload,
    handleDeactivate,
    handleClose,
    handleIconError, removeIcon,
    titleRef, isTitleEditable, handleTitleBlur, startEditTitle, cancelEditTitle,
    descriptionRef, isDescriptionEditable, handleDescriptionBlur, startEditDescription, cancelEditDescription,
    isExpanded, toggleExpanded,
    tagsArray, isAddingTag, newTag, tagInput, shouldShowAddButton, showAddButton, startAddingTag, addNewTag, removeTag, cancelAddTag,
    handleLeftAction
  }
}
