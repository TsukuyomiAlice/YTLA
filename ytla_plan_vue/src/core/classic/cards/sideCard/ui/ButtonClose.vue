<template>
  <button
    v-if="showClose"
    class="action-button"
    @click="handleClose"
    :aria-label="$t('classic.cards.sideCard.button_close')"
    :title="$t('classic.cards.sideCard.button_close')"
  >
    <svg class="trash-icon" viewBox="0 0 24 24" fill="currentColor">
      <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z" />
    </svg>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  showClose: boolean
  handleClose: () => void
}>()
</script>

<style lang="scss" scoped>
@use '@/core/classic/cards/sideCard/styles/ui-button';
</style>
