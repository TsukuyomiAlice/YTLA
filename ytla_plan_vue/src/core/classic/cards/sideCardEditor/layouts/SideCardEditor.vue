<!-- @/layouts/SideCardEditor.vue -->
<template>
  <div class="expand-area" :class="{ active: editorState.visible }">
    <component
      :is="editorState.currentStep"
      v-if="editorState.currentStep"
      :key="componentKey"
      :mode="editorState.mode === 'create' ? 'create' : 'edit'"
      :initial-data="editorState.editCardData"
      :card-type="editorState.currentCardType"
      :card-sub-type="editorState.currentCardSubType"
      @cancelEdit="closeEditor"
      @prev="handlePrev"
      @next="handleNext"
      @submit="handleSubmit"
    />
  </div>
</template>

<script setup lang="ts">
import { useSideCardEditor } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditor.ts'
import type { CardData } from '@/core/classic/cards/sideCard/definitions/cardDataType.ts'

const props = defineProps<{
  cardContainer: {
    cards: CardData[]
  }
}>()

const {
  editorState,
  componentKey,
  handlePrev,
  handleNext,
  handleSubmit,
  closeEditor,
} = useSideCardEditor(props.cardContainer)
</script>

<style lang="scss" scoped>
@use '../styles/side-card-editor';
</style>
