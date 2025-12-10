<template>
  <SideCardEditorFlowSelector :card-sub-types="cardSubTypes" />
</template>

<script setup lang="ts">
import SideCardEditorFlowSelector from '@/core/domain/area/cards/layouts/SideCardEditorFlowSelector.vue'

defineOptions({ name: 'SampleFlowSelector' })

export interface SampleFlowSelector {}

const cardSubTypes = [
  { value: 'sample1', icon: '1', label: '样例1' },
  { value: 'sample2', icon: '2', label: '样例2' },
  { value: 'sample3', icon: '3', label: '样例3' }
]
</script>
