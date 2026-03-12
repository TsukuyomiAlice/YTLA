<template>
  <div class="guide-container">
    <div class="button-grid">
      <ButtonCancel @click="handleCancel" title="返回">↩</ButtonCancel>
      <ButtonScale
        v-for="subType in cardSubTypes"
        :key="subType.value"
        :icon="subType.icon"
        :label="subType.label"
        @click="selectSubType(subType.value)"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import ButtonCancel from '@/core/classic/cards/sideCardEditor/ui/ButtonCancel.vue'
import ButtonScale from '@/core/classic/cards/sideCardEditor/ui/ButtonScale.vue'
import type { SideCardEditorFlowSelectorProps, SideCardEditorFlowSelectorEmits } from '@/core/classic/cards/sideCardEditor/definitions/sideCardEditorType.ts'
import { useSideCardEditorFlowSelector } from '@/core/classic/cards/sideCardEditor/composables/useSideCardEditorFlowSelector.ts'

const props = defineProps<SideCardEditorFlowSelectorProps>()
const emit = defineEmits<SideCardEditorFlowSelectorEmits>()

const { selectSubType, handleCancel } = useSideCardEditorFlowSelector(props, emit)
</script>

<style scoped lang="scss">
@use '../styles/side-card-editor-flow-selector';
</style>
