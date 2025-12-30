<template>
  <button
    class="action-button"
    @click.stop="togglePin"
    :aria-label="isPinned ? '取消固定' : '固定位置'"
    :title="isPinned ? '取消固定' : '固定位置'"
    :class="{ '--pinned': isPinned }"
  >
    <svg
      class="pin-button"
      viewBox="0 0 24 24"
      fill="currentColor"
      :class="{ '--pinned': isPinned }"
    >
      <path
        d="M16 12V4h1c.55 0 1-.45 1-1s-.45-1-1-1H7c-.55 0-1 .45-1 1s.45 1 1 1h1v8l-2 2v2h5.2v6h1.6v-6H18v-2l-2-2z"
      />
    </svg>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  isPinned: boolean
  togglePin: () => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/ui-button';
@use '../styles/button-pin';
</style>
