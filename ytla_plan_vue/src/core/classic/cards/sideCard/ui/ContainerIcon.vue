<template>
  <div v-if="fullIconPath.iconImage && showIcon" class="icon-container">
    <img
      class="icon"
      :src="fullIconPath.iconImage"
      @error="handleIconError"
      alt=""
    />
    <button class="icon-remove-btn" @click.stop="removeIcon">
      ×
    </button>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  fullIconPath: { iconImage: string }
  showIcon: boolean
  handleIconError: (e: Event) => void
  removeIcon: () => void
}>()
</script>

<style scoped lang="scss">
@use '../styles/ui-icon';
</style>
