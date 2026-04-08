<template>
  <button class="cancel-btn" @click="handleClick" :aria-label="computedAriaLabel" :title="computedTitle">
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
import type { ButtonCancelProps, ButtonCancelEmits } from '../definitions/ButtonCancelType'
import type { Ref } from 'vue'
import { useButtonCancel } from '../composables/useButtonCancel.ts'

const props = defineProps<ButtonCancelProps & {
  options?: Ref<import('../definitions/ButtonCancelType').ButtonCancelOptions> | import('../definitions/ButtonCancelType').ButtonCancelOptions
}>()

const emit = defineEmits<ButtonCancelEmits>()

const { handleClick, computedAriaLabel, computedTitle } = useButtonCancel(props, emit, props.options)
</script>

<style scoped lang="scss">
@use '../styles/button-cancel';
</style>
