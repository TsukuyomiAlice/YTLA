<template>
  <div
    class="editable-description"
    :ref="
      function () {
        return descriptionRef
      }
    "
    @click="startEditDescription"
    @blur="handleDescriptionBlur"
    @keydown.enter="handleDescriptionBlur($event)"
    @keydown.esc="cancelEditDescription"
    :contenteditable="isDescriptionEditable"
    :data-placeholder="!description ? '...' : ''"
  >
    {{ description }}
  </div>
</template>

<script setup lang="ts">
defineProps<{
  description: string | undefined
  descriptionRef: HTMLElement | null
  isDescriptionEditable: boolean
  startEditDescription: () => void
  handleDescriptionBlur: (e: Event) => void
  cancelEditDescription: () => void
}>()
</script>

<style scoped lang="scss">
@use '@/core/classic/cards/sideCard/styles/ui-text';
</style>
