<template>
  <button
    class="action-btn"
    :class="type"
    @click="handleClick"
    :disabled="disabled"
    :aria-label="computedAriaLabel"
    :title="computedTitle"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import { useButtonAction } from '../composables/useButtonAction.ts'
import { useI18n } from 'vue-i18n'
import { computed } from 'vue'

const { t } = useI18n()

const props = defineProps<{
  type?: 'cancel' | 'prev' | 'next' | 'submit'
  disabled?: boolean
  ariaLabel?: string
  title?: string
}>()

const emit = defineEmits<{
  (e: 'click'): void
}>()

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

const { handleClick } = useButtonAction(emit)
</script>

<style scoped lang="scss">
@use '../styles/ui-button-action';
</style>
