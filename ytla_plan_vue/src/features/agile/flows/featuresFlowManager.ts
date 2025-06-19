import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class FeaturesModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const featuresModuleFlowManager = new FeaturesModuleFlowManager()

featuresModuleFlowManager.registerFlow('features-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/features/FeaturesMain_00.vue')),
])

featuresModuleFlowManager.registerFlow('features-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/features/FeaturesSub_00.vue')),
])

