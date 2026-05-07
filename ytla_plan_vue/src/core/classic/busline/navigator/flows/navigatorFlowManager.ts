import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class NavigatorModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const navigatorModuleFlowManager = new NavigatorModuleFlowManager()

navigatorModuleFlowManager.registerFlow('navigator-main-steps', [
  defineAsyncComponent(() => import('@/core/classic/busline/navigator/components/NavigatorMain_00.vue')),
])

navigatorModuleFlowManager.registerFlow('navigator-sub-steps', [
  defineAsyncComponent(() => import('@/core/classic/busline/navigator/components/NavigatorSub_00.vue')),
])
