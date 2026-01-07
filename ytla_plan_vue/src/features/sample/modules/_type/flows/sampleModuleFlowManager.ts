import type { Component } from 'vue'
import { defineAsyncComponent, markRaw } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class SampleModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null
  registerFlow(moduleType: string, steps: Component[]) {
    this.flows.set(moduleType, steps)
  }
  getSteps(moduleType: string): Component[] {
    return this.flows.get(moduleType) || []
  }
}

export const sampleModuleFlowManager = new SampleModuleFlowManager()
sampleModuleFlowManager.registerFlow('sample-main-steps', [
  defineAsyncComponent(() => import('@/features/sample/modules/sample/components/SampleStep1.vue')),
  defineAsyncComponent(() => import('@/features/sample/modules/sample/components/SampleStep2.vue')),
  defineAsyncComponent(() => import('@/features/sample/modules/sample/components/SampleStep3.vue'))
])
sampleModuleFlowManager.registerFlow('sample-sub-steps', [
  defineAsyncComponent(() => import('@/features/sample/modules/sample/components/SampleSubStep1.vue')),
  defineAsyncComponent(() => import('@/features/sample/modules/sample/components/SampleSubStep2.vue'))
])
