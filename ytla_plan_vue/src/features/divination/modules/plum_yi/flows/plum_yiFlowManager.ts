import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Plum_yiModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const plum_yiModuleFlowManager = new Plum_yiModuleFlowManager()

plum_yiModuleFlowManager.registerFlow('plum_yi-main-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/plum_yi/components/Plum_yiMain_00.vue')),
])

plum_yiModuleFlowManager.registerFlow('plum_yi-sub-steps', [
  defineAsyncComponent(() => import('@/features/divination/modules/plum_yi/components/Plum_yiSub_00.vue')),
])
