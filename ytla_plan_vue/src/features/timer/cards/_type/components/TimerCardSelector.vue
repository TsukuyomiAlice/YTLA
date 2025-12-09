<template>
  <SideCardEditorFlowSelector :card-sub-types="cardSubTypes" />
</template>

<script setup lang="ts">
import SideCardEditorFlowSelector from '@/core/domain/area/cards/layouts/SideCardEditorFlowSelector.vue'

defineOptions({ name: 'TimerFlowSelector' })
export interface TimerFlowSelector {}

const cardSubTypes = [
  { value: 'alarm', icon: '⏰', label: '闹钟' },
  { value: 'count', icon: '⏱️', label: '计时' },
  { value: 'countdown', icon: '⏳', label: '倒计时' }
]
</script>

