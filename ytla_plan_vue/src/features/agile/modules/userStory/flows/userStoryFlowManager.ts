import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'

export class UserstoryModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const userStoryModuleFlowManager = new UserstoryModuleFlowManager()

userStoryModuleFlowManager.registerFlow('userStory-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/userStory/components/UserStoryMain_00.vue')),
])

userStoryModuleFlowManager.registerFlow('userStory-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/modules/userStory/components/UserStorySub_00.vue')),
])

