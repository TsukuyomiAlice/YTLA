import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

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
  defineAsyncComponent(() => import('@/features/agile/components/modules/userStory/UserStoryMain_00.vue')),
])

userStoryModuleFlowManager.registerFlow('userStory-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/userStory/UserStorySub_00.vue')),
])

