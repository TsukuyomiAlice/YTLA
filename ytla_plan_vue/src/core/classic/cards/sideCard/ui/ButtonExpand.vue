<template>
  <button class="toggle-button" @click="toggleExpanded" :aria-expanded="isExpanded">
    <span class="arrow" :class="{ '--up': isExpanded }">▼</span>
  </button>
</template>

<script setup lang="ts">
const { toggleExpanded, isExpanded } = defineProps<{
  toggleExpanded: () => void
  isExpanded: boolean
}>()
</script>

<style scoped lang="scss">
@use '@/core/classic/cards/sidecard/styles/card-component-button.scss';
</style>
