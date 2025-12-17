import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/types/flowManagerTypes.ts'

export class FunctionModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const functionModuleFlowManager = new FunctionModuleFlowManager()

functionModuleFlowManager.registerFlow('function-main-steps', [
  defineAsyncComponent(() => import('@/features/workshop/modules/function/components/FunctionMain_00.vue')),
])

functionModuleFlowManager.registerFlow('function-sub-steps', [
  defineAsyncComponent(() => import('@/features/workshop/modules/function/components/FunctionSub_00.vue')),
])

