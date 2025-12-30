<template>
  <button class="toggle-expand-button" @click="toggleExpanded" :aria-expanded="isExpanded">
    <span class="arrow" :class="{ '--up': isExpanded }">▼</span>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  toggleExpanded: () => void
  isExpanded: boolean
}>()
</script>

<style scoped lang="scss">
@use '../styles/button-expand';
</style>
