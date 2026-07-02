import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Data_minerModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const data_minerModuleFlowManager = new Data_minerModuleFlowManager()

data_minerModuleFlowManager.registerFlow('data_miner-main-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_miner/components/Data_minerMain_00.vue')),
])

data_minerModuleFlowManager.registerFlow('data_miner-sub-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_miner/components/Data_minerSub_00.vue')),
])
