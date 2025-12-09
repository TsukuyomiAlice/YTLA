import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/domain/area/frame/types/flowManagerTypes.ts'

export class ThoughtModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const thoughtModuleFlowManager = new ThoughtModuleFlowManager()

thoughtModuleFlowManager.registerFlow('thought-main-steps', [
  defineAsyncComponent(() => import('@/features/workshop/modules/thought/components/ThoughtMain_00.vue')),
])

thoughtModuleFlowManager.registerFlow('thought-sub-steps', [
  defineAsyncComponent(() => import('@/features/workshop/modules/thought/components/ThoughtSub_00.vue')),
])

