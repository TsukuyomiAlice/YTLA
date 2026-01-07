import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class RatingModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const ratingModuleFlowManager = new RatingModuleFlowManager()

ratingModuleFlowManager.registerFlow('rating-main-steps', [
  defineAsyncComponent(() => import('@/features/language/modules/rating/components/RatingMain_00.vue')),
])

ratingModuleFlowManager.registerFlow('rating-sub-steps', [
  defineAsyncComponent(() => import('@/features/language/modules/rating/components/RatingSub_00.vue')),
])

