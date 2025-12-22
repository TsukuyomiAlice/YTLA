<template>
  <button
    class="action-button"
    @click.stop="triggerBgUpload"
    aria-label="修改背景"
    title="修改背景"
  >
    <svg viewBox="0 0 24 24" fill="currentColor" class="bg-upload">
      <path
        d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-4-4v-2h-2v2h-2v2h2v2h2v-2h2v-2h-2zM13 7v2h2v2h-2v2H9v-2H7v-2h2V7z"
      />
    </svg>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  triggerBgUpload: () => void
}>()
</script>

<style scoped lang="scss">
@use '@/core/classic/cards/sidecard/styles/card-component-button.scss';
</style>
