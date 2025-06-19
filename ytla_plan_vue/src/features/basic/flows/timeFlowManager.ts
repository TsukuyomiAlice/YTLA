import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class TimeModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const timeModuleFlowManager = new TimeModuleFlowManager()

timeModuleFlowManager.registerFlow('time-main-steps', [
  defineAsyncComponent(() => import('@/features/basic/components/modules/time/TimeMain_00.vue')),
])

timeModuleFlowManager.registerFlow('time-sub-steps', [
  defineAsyncComponent(() => import('@/features/basic/components/modules/time/TimeSub_00.vue')),
])

