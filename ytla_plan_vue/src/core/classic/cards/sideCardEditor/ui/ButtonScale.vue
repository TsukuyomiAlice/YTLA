<template>
  <button class="scale-button" @click="handleClick" :aria-label="computedAriaLabel" :title="computedTitle">
    <span class="icon">{{ icon }}</span>
    <span v-if="showLabel" class="label">{{ label }}</span>
  </button>
</template>

<script setup lang="ts">
import type { ButtonScaleProps, ButtonScaleEmits } from '../definitions/ButtonScaleType'
import { useButtonScale } from '../composables/useButtonScale'

const props = defineProps<ButtonScaleProps>()
const emit = defineEmits<ButtonScaleEmits>()

const { handleClick, computedAriaLabel, computedTitle } = useButtonScale(props, emit)
</script>

<style lang="scss" scoped>
@use '../styles/button-scale.scss' as *;
</style>
