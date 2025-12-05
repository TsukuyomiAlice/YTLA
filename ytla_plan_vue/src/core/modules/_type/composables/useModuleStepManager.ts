import { ref, type Component } from 'vue'
import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'

type StepConfig = Component[]
export type FrameType = 'main' | 'sub'

export function useModuleStepManager(
  steps: StepConfig,
  frameType: FrameType = 'main'
) {
  const panelStore = usePanelStore()

  // 获取当前模块信息
  const currentPanel = panelStore.activePanel
  const currentModuleId = panelStore.activeModuleId

  const initialStep = panelStore.getFrameStep(
    currentPanel,
    currentModuleId,
    frameType
  )
  const localCurrentStepIndex = ref(initialStep)

  const updateStoreState = (step: number) => {
    panelStore.updateFrameState(frameType, { step })
  }

  const currentStep = () => {
    return steps[localCurrentStepIndex.value]
  }

  const handleJump = (stepIndex: number) => {
    if (stepIndex >= 0 && stepIndex < steps.length) {
      localCurrentStepIndex.value = stepIndex
      updateStoreState(localCurrentStepIndex.value)
    }
  }

  const handleNext = () => {
    if (localCurrentStepIndex.value < steps.length - 1) {
      localCurrentStepIndex.value++
      updateStoreState(localCurrentStepIndex.value)
    }
  }

  const handlePrev = () => {
    if (localCurrentStepIndex.value > 0) {
      localCurrentStepIndex.value--
      updateStoreState(localCurrentStepIndex.value)
    }
  }

  return {
    currentStep,
    handleJump,
    handleNext,
    handlePrev,
    currentStepIndex: localCurrentStepIndex
  }
}



