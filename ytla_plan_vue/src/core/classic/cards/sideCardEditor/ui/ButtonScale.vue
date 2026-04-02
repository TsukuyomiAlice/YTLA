<template>
  <button class="scale-button" @click="handleClick" :aria-label="computedAriaLabel" :title="computedTitle">
    <span class="icon">{{ icon }}</span>
    <span v-if="showLabel" class="label">{{ label }}</span>
  </button>
</template>

<script setup lang="ts">
import { useButtonScale } from '../composables/useButtonScale'
import { useI18n } from 'vue-i18n'
import { computed } from 'vue'

const { t } = useI18n()

const props = defineProps<{
  icon: string
  label?: string
  showLabel?: boolean
  ariaLabel?: string
  title?: string
}>()

const emit = defineEmits<{
  (e: 'click'): void
}>()

const defaultAriaLabel = computed(() => props.label || t('classic.cards.sideCardEditor.ButtonScale.Scale'))
const computedAriaLabel = computed(() => props.ariaLabel || defaultAriaLabel.value)
const computedTitle = computed(() => props.title || defaultAriaLabel.value)

const { handleClick } = useButtonScale(emit)
</script>

<style lang="scss" scoped>
@use '../styles/button-scale.scss' as *;
</style>
