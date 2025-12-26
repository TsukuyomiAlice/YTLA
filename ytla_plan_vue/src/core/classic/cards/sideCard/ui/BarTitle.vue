<template>
  <div
    v-if="showTitle"
    :ref="
      function () {
        return titleRef
      }
    "
    class="editable-title"
    :contenteditable="isTitleEditable"
    @click="startEditTitle"
    @blur="handleTitleBlur"
    @keydown.enter="handleTitleBlur($event)"
    @keydown.esc="cancelEditTitle"
    :data-placeholder="!name ? '...' : ''"
  >
    {{ name }}
  </div>
</template>

<script setup lang="ts">
defineProps<{
  showTitle: boolean
  name: string | undefined
  titleRef: HTMLElement | null
  isTitleEditable: boolean
  startEditTitle: () => void
  handleTitleBlur: (e: Event) => void
  cancelEditTitle: () => void
}>()
</script>

<style scoped lang="scss">
@use '@/core/classic/cards/sidecard/styles/sidecard.scss';
@use '@/core/classic/cards/sidecard/styles/card-component-text.scss';
</style>
