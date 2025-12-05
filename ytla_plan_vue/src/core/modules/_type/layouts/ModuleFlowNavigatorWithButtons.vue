<template>
  <!-- 渲染当前步骤组件 -->
  <component :is="currentStep()" />
  <!-- 显示步骤控制按钮 -->
  <div class="step-controls">
    <button @click="handlePrev" :disabled="currentStepIndex === 0">prev.</button>
    <button @click="handleNext" :disabled="isLastStep">next</button>
  </div>
</template>

<script setup lang="ts">
import { type Component, computed } from 'vue'
import { type FrameType } from '@/core/modules/_type/composables/useModuleStepManager.ts'
const props = withDefaults(defineProps<{
  moduleType?: string
  flowName?: string
  frameType?: FrameType
}>(), {
  moduleType: '',
  flowName: '',
  frameType: 'main'
})

import { getModuleConfig } from '@/core/modules/_type/registries/moduleRegistry.ts'
const moduleConfig = computed(() => getModuleConfig(props.moduleType))
const stepConfig = computed(() => {
  return (moduleConfig.value?.flowManager?.getSteps(props.flowName) || []) as Component[]
})
const isLastStep = computed(() => currentStepIndex.value === stepConfig.value.length - 1)

import { useModuleStepManager } from '@/core/modules/_type/composables/useModuleStepManager.ts'
const { currentStep, handleJump, handleNext, handlePrev, currentStepIndex } = useModuleStepManager(
  stepConfig.value, props.frameType
)

defineExpose({
  handleJump,
  handleNext,
  handlePrev
})
</script>

<style scoped lang="scss">
.step-controls {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}
</style>
