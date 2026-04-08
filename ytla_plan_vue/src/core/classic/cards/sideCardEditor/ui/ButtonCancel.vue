<template>
  <button class="cancel-btn" @click="handleClick" :aria-label="computedAriaLabel" :title="computedTitle">
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import type { ButtonCancelOptions } from '../composables/useButtonCancel.ts'
import { useButtonCancel } from '../composables/useButtonCancel.ts'
import type { Ref } from 'vue'
import { computed } from 'vue'

const props = defineProps<{
  ariaLabel?: string
  title?: string
  options?: Ref<ButtonCancelOptions> | ButtonCancelOptions
}>()

const emit = defineEmits<{
  (e: 'click'): void
}>()

const defaultAriaLabel = computed(() => 'Cancel')
const computedAriaLabel = computed(() => props.ariaLabel || defaultAriaLabel.value)
const computedTitle = computed(() => props.title || defaultAriaLabel.value)

const { handleClick } = useButtonCancel(emit, props.options)
</script>

<style scoped lang="scss">
@use '../styles/button-cancel';
</style>
