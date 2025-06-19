<template>
  <div class="guide-container">
    <div class="button-grid">
      <button class="cancel-btn" @click="handleCancel" title="返回">↩</button>
      <button
        v-for="subType in cardSubTypes"
        :key="subType.value"
        class="scale-button"
        @click="selectSubType(subType.value)"
        :title="subType.label"
      >
        <span class="icon">{{ subType.icon }}</span>
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits(['next', 'cancelEdit'])
import type { CardSubType } from '@/core/cards/types/cardTypes.ts'


const selectSubType = (subType: CardSubType) => {
  emit('next', subType)
}

const handleCancel = () => {
  emit('cancelEdit')
}

const props = defineProps<{
  cardSubTypes: Array<{
    value: string
    icon: string
    label: string
  }>
}>()


</script>

<style lang="scss" scoped>
@use '@/core/cards/styles/card-editor-flow-selector';
</style>
