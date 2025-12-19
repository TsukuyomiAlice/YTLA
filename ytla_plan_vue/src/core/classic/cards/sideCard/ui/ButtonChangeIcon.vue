<template>
  <button
    v-if="showIcon"
    class="action-button"
    @click.stop="triggerIconUpload"
    aria-label="修改图标"
    title="修改图标"
  >
    <svg viewBox="0 0 24 24" fill="currentColor" class="icon-upload">
      <rect x="3" y="3" width="18" height="18" rx="3" ry="3" stroke="currentColor" stroke-width="2" fill="none"
      />
      <circle cx="9" cy="10" r="1.5" fill="currentColor" />
      <circle cx="15" cy="10" r="1.5" fill="currentColor" />
      <path
        d="M8 15a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1"
        stroke="currentColor"
        stroke-width="1.5"
        fill="none"
        stroke-linecap="round"
      />
    </svg>
  </button>
</template>

<script setup lang="ts">
const { showIcon, triggerIconUpload } = defineProps<{
  showIcon: boolean;
  triggerIconUpload: () => void
}>()
</script>

<style scoped lang="scss">
@import '@/core/classic/cards/sidecard/styles/card-component-button.scss';
</style>
