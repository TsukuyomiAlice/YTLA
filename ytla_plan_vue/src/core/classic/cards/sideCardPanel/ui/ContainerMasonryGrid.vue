<template>
  <div class="masonry-container">
    <div :class="{ 'masonry-grid': isMasonrySupported, 'non-masonry-grid': !isMasonrySupported }">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  isMasonrySupported: boolean
}>()
</script>

<style lang="scss" scoped>
@use '../styles/card-panel';
</style>
