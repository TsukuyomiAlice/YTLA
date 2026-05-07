import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class StartupModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const startupModuleFlowManager = new StartupModuleFlowManager()

startupModuleFlowManager.registerFlow('startup-main-steps', [
  defineAsyncComponent(() => import('@/features/busline/modules/startup/components/StartupMain_00.vue')),
])

startupModuleFlowManager.registerFlow('startup-sub-steps', [
  defineAsyncComponent(() => import('@/features/busline/modules/startup/components/StartupSub_00.vue')),
])
