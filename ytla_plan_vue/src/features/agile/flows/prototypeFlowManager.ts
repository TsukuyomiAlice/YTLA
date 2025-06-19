import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class PrototypeModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const prototypeModuleFlowManager = new PrototypeModuleFlowManager()

prototypeModuleFlowManager.registerFlow('prototype-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/prototype/PrototypeMain_00.vue')),
])

prototypeModuleFlowManager.registerFlow('prototype-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/prototype/PrototypeSub_00.vue')),
])

