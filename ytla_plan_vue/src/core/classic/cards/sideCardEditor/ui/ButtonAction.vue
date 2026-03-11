<template>
  <button
    class="action-btn"
    :class="type"
    @click="handleClick"
    :disabled="disabled"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  type?: 'cancel' | 'prev' | 'next' | 'submit'
  disabled?: boolean
}>()

const emit = defineEmits<{
  (e: 'click'): void
}>()

const handleClick = () => {
  emit('click')
}
</script>

<style scoped lang="scss">
@use '../styles/ui-button-action';
</style>
