import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Data_analyzerModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const data_analyzerModuleFlowManager = new Data_analyzerModuleFlowManager()

data_analyzerModuleFlowManager.registerFlow('data_analyzer-main-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_analyzer/components/Data_analyzerMain_00.vue')),
])

data_analyzerModuleFlowManager.registerFlow('data_analyzer-sub-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_analyzer/components/Data_analyzerSub_00.vue')),
])
