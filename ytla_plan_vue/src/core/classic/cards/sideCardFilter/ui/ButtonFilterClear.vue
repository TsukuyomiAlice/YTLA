<template>
  <button class="button-filter-clear" @click="handleClear">
    {{ label }}
  </button>
</template>

<script setup lang="ts">
defineProps<{
  label: string
  handleClear: () => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/button-filter-clear';
</style>
