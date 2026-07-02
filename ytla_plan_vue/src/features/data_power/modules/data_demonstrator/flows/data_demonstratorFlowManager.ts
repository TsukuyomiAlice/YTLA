import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Data_demonstratorModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const data_demonstratorModuleFlowManager = new Data_demonstratorModuleFlowManager()

data_demonstratorModuleFlowManager.registerFlow('data_demonstrator-main-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_demonstrator/components/Data_demonstratorMain_00.vue')),
])

data_demonstratorModuleFlowManager.registerFlow('data_demonstrator-sub-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_demonstrator/components/Data_demonstratorSub_00.vue')),
])
