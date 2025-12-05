<template>
  <SideCardEditorFlowSelector :card-sub-types="cardSubTypes" />
</template>

<script setup lang="ts">
import SideCardEditorFlowSelector from '@/core/sideCards/_type/layouts/SideCardEditorFlowSelector.vue'

defineOptions({ name: 'RelaxFlowSelector' })
export interface RelaxFlowSelector {}

const cardSubTypes = [
  { value: 'wordle', icon: 'W', label: 'wordle' },
]
</script>

