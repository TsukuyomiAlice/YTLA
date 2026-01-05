<template>
  <button
    v-if="showDeactivate"
    class="action-button"
    @click="handleDeactivate"
    :aria-label="$t('classic.cards.sideCard.button_deactivate')"
    :title="$t('classic.cards.sideCard.button_deactivate')"
  >
    <svg class="deactivate-icon" viewBox="0 0 24 24" fill="currentColor">
      <path d="M18 11H6c-.55 0-1 .45-1 1s.45 1 1 1h12c.55 0 1-.45 1-1s-.45-1-1-1z" />
    </svg>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  showDeactivate: boolean
  handleDeactivate: () => void
}>()
</script>

<style scoped lang="scss">
@use '@/core/classic/cards/sideCard/styles/ui-button';
</style>
