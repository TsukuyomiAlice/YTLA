<template>
  <div
    class="card-container"
    :draggable="!isPinned"
    @dragstart="handleDragStart"
    @dragend="handleDragEnd"
    @dragover.prevent
    @dragenter.prevent
    :class="{
      '--expanded': isExpanded,
      '--span-2': spanColumns === 2,
      '--span-3': spanColumns === 3,
    }"
    @click.stop
    :style="containerStyle"
  >
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  isPinned: boolean
  isExpanded: boolean
  spanColumns?: number
  containerStyle?: Record<string, string>
  handleDragStart: (e: DragEvent) => void
  handleDragEnd: () => void
}>()

</script>

<style scoped lang="scss">
@use '../styles/sidecard';
@use '../styles/container-sidecard';
</style>
