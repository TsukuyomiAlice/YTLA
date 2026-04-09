<template>
  <button class="cancel-btn" @click="handleClick" :aria-label="computedAriaLabel" :title="computedTitle">
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import type { ButtonCancelProps, ButtonCancelEmits } from '../definitions/ButtonCancelType'
import { useButtonCancel } from '../composables/useButtonCancel'

const props = defineProps<ButtonCancelProps>()
const emit = defineEmits<ButtonCancelEmits>()

const { handleClick, computedAriaLabel, computedTitle } = useButtonCancel(props, emit)
</script>

<style scoped lang="scss">
@use '../styles/button-cancel';
</style>
