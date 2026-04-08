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

const props = withDefaults(defineProps<{
  icon: string
  title: string
  isActive?: boolean
}>(), {
  isActive: false
})

const emit = defineEmits<{
  (e: 'click'): void
}>()

const { icon, title, isActive, handleClick } = useButtonAdd(props, { emit })
</script>

<style scoped lang="scss">
@use '../styles/button-add';
</style>
