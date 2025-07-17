import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class TimerModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const timerModuleFlowManager = new TimerModuleFlowManager()

timerModuleFlowManager.registerFlow('timer-main-steps', [
  defineAsyncComponent(() => import('@/features/timer/components/modules/timer/TimerMain_00.vue')),
])

timerModuleFlowManager.registerFlow('timer-sub-steps', [
  defineAsyncComponent(() => import('@/features/timer/components/modules/timer/TimerSub_00.vue')),
])

