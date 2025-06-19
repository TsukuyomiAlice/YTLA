<template>
  <!-- 渲染当前步骤组件 -->
  <component :is="currentStep()" />
</template>

<script setup lang="ts">
import { type Component, computed } from 'vue'
import { type FrameType } from '@/core/modules/composables/useModuleStepManager.ts'
const props = withDefaults(defineProps<{
  moduleType?: string
  flowName?: string
  frameType?: FrameType
}>(), {
  moduleType: '',
  flowName: '',
  frameType: 'main'
})

import { getModuleConfig } from '@/core/modules/registries/moduleRegistry.ts'
const moduleConfig = computed(() => getModuleConfig(props.moduleType))
const stepConfig = computed(() => {
  return (moduleConfig.value?.flowManager?.getSteps(props.flowName) || []) as Component[]
})

import { useModuleStepManager } from '@/core/modules/composables/useModuleStepManager.ts'
const { currentStep, handleJump, handleNext, handlePrev } = useModuleStepManager(
  stepConfig.value, props.frameType
)

defineExpose({
  handleJump,
  handleNext,
  handlePrev
})
</script>

<style scoped lang="scss">

</style>
