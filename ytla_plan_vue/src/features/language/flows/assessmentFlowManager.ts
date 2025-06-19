import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class AssessmentModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const assessmentModuleFlowManager = new AssessmentModuleFlowManager()

assessmentModuleFlowManager.registerFlow('assessment-main-steps', [
  defineAsyncComponent(() => import('@/features/language/components/modules/assessment/AssessmentMain_00.vue')),
  defineAsyncComponent(() => import('@/features/language/components/modules/assessment/AssessmentMain_11.vue')),
  defineAsyncComponent(() => import('@/features/language/components/modules/assessment/AssessmentMain_12.vue')),
  defineAsyncComponent(() => import('@/features/language/components/modules/assessment/AssessmentMain_21.vue')),
  defineAsyncComponent(() => import('@/features/language/components/modules/assessment/AssessmentMain_99.vue')),
])

assessmentModuleFlowManager.registerFlow('assessment-sub-steps', [
  defineAsyncComponent(() => import('@/features/language/components/modules/assessment/AssessmentSub_00.vue')),
])

