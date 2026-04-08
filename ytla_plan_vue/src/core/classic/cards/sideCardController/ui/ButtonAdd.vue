<template>
  <button
    class="add-button"
    :class="{ '--active': isActive }"
    @click.stop="handleClick"
    :title="title"
  >
    <span class="icon">{{ icon }}</span>
  </button>
</template>

<script setup lang="ts">
import { useButtonAdd } from '../composables/useButtonAdd'

withDefaults(defineProps<{
  icon: string
  title: string
  isActive?: boolean
}>(), {
  isActive: false
})

const emit = defineEmits<{
  (e: 'click'): void
}>()

const { handleClick } = useButtonAdd(emit)
</script>

<style scoped lang="scss">
@use '../styles/button-add';
</style>
