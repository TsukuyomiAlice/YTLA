import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class LearningModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const learningModuleFlowManager = new LearningModuleFlowManager()

learningModuleFlowManager.registerFlow('learning-main-steps', [
  defineAsyncComponent(() => import('@/features/language/components/modules/learning/LearningMain_00.vue')),
])

learningModuleFlowManager.registerFlow('learning-sub-steps', [
  defineAsyncComponent(() => import('@/features/language/components/modules/learning/LearningSub_00.vue')),
])

