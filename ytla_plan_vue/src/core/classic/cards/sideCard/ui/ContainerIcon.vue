<template>
  <div class="icon-container">
    <img
      v-if="fullIconPath && showIcon"
      :src="fullIconPath.iconImage"
      class="icon"
      @error="handleIconError"
      alt=""
    />
    <button v-if="fullIconPath && showIcon" class="icon-remove-btn" @click.stop="removeIcon">
      ×
    </button>
  </div>
</template>

<script setup lang="ts">
const {} = defineProps<{
  fullIconPath: { iconImage: string } | null
  showIcon: boolean
  handleIconError: (e: Event) => void
  removeIcon: () => void
}>()
</script>

<style scoped lang="scss">
@use '@/core/classic/cards/sidecard/styles/card-component-icon.scss';
</style>
