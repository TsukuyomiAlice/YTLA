import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Data_managerModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const data_managerModuleFlowManager = new Data_managerModuleFlowManager()

data_managerModuleFlowManager.registerFlow('data_manager-main-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_manager/components/Data_managerMain_00.vue')),
])

data_managerModuleFlowManager.registerFlow('data_manager-sub-steps', [
  defineAsyncComponent(() => import('@/features/data_power/modules/data_manager/components/Data_managerSub_00.vue')),
])
