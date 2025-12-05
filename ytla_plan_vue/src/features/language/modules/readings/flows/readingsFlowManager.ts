import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/_type/types/flowManagerTypes.ts'

export class ReadingsModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const readingsModuleFlowManager = new ReadingsModuleFlowManager()

readingsModuleFlowManager.registerFlow('readings-main-steps', [
  defineAsyncComponent(() => import('@/features/language/modules/readings/components/ReadingsMain_00.vue')),
])

readingsModuleFlowManager.registerFlow('readings-sub-steps', [
  defineAsyncComponent(() => import('@/features/language/modules/readings/components/ReadingsSub_00.vue')),
])

