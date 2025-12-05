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
import { ref, watch } from 'vue'
import { useSideCardEditor } from '@/core/sideCards/_type/composables/useSideCardEditor.ts'

const props = defineProps<{
  cardContainer: {
    cards: any[]
  }
}>()

const {
  editorState,
  handlePrev,
  handleNext,
  handleSubmit,
  closeEditor,
} = useSideCardEditor(props.cardContainer)
const componentKey = ref(0)

watch(
  () => editorState.value.mode,
  () => {
    componentKey.value++
  }
)
</script>

<style lang="scss" scoped>
@use '../styles/card-editor';
</style>
