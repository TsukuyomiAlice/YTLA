<template>
  <div class="description-wrapper">
    <div class="description-text">
      <strong>
        <div
          :ref="
            function () {
              return (descriptionRef)
            }
          "
          class="editable-description"
          :contenteditable="isDescriptionEditable"
          @click="startEditDescription"
          @blur="handleDescriptionBlur"
          @keydown.enter="handleDescriptionBlur($event)"
          @keydown.esc="cancelEditDescription"
          :data-placeholder="!description ? '...' : ''"
        >
          {{ description }}
        </div>
      </strong>
    </div>
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
@use '@/core/classic/cards/sidecard/styles/card-component-text.scss';
</style>
