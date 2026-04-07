import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import type { ButtonActionProps } from '../definitions/ButtonActionType'

export const useButtonAction = (
  props: ButtonActionProps,
  emit: (e: 'click') => void
) => {
  const { t } = useI18n()

  const defaultAriaLabel = computed(() => {
    switch (props.type) {
      case 'cancel':
        return t('classic.cards.sideCardEditor.ButtonAction.Cancel')
      case 'prev':
        return t('classic.cards.sideCardEditor.ButtonAction.Prev')
      case 'next':
        return t('classic.cards.sideCardEditor.ButtonAction.Next')
      case 'submit':
        return t('classic.cards.sideCardEditor.ButtonAction.Submit')
      default:
        return t('classic.cards.sideCardEditor.ButtonAction.Submit')
    }
  })

  const computedAriaLabel = computed(() => props.ariaLabel || defaultAriaLabel.value)
  const computedTitle = computed(() => props.title || defaultAriaLabel.value)

  const handleClick = () => {
    emit('click')
  }

  return {
    defaultAriaLabel,
    computedAriaLabel,
    computedTitle,
    handleClick
  }
}
