import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class InteractionModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const interactionModuleFlowManager = new InteractionModuleFlowManager()

interactionModuleFlowManager.registerFlow('interaction-main-steps', [
  defineAsyncComponent(() => import('@/features/basic/components/modules/interaction/InteractionMain_00.vue')),
])

interactionModuleFlowManager.registerFlow('interaction-sub-steps', [
  defineAsyncComponent(() => import('@/features/basic/components/modules/interaction/InteractionSub_00.vue')),
])

