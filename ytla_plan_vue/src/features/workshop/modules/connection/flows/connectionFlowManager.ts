import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/types/flowManagerTypes.ts'

export class ConnectionModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const connectionModuleFlowManager = new ConnectionModuleFlowManager()

connectionModuleFlowManager.registerFlow('connection-main-steps', [
  defineAsyncComponent(() => import('@/features/workshop/modules/connection/components/ConnectionMain_00.vue')),
])

connectionModuleFlowManager.registerFlow('connection-sub-steps', [
  defineAsyncComponent(() => import('@/features/workshop/modules/connection/components/ConnectionSub_00.vue')),
])

