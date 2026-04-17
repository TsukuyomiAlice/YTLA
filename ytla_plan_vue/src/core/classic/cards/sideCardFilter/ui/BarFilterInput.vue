<template>
  <input
    class="bar-filter-input"
    :value="value"
    @input="handleInput"
    type="text"
    :placeholder="placeholder"
  />
</template>

<script setup lang="ts">
defineProps<{
  placeholder: string
  value: string
  handleInput: (e: Event) => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/bar-filter-input';
</style>
