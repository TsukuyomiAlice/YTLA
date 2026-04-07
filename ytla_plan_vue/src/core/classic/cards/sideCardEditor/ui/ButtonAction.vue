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
import type { ButtonActionProps, ButtonActionEmits } from '../definitions/ButtonActionType'
import { useButtonAction } from '../composables/useButtonAction'

const props = defineProps<ButtonActionProps>()
const emit = defineEmits<ButtonActionEmits>()

const { computedAriaLabel, computedTitle, handleClick } = useButtonAction(props, emit)
</script>

<style scoped lang="scss">
@use '../styles/ui-button-action';
</style>
