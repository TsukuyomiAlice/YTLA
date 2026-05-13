import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Fund_infoModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const fund_infoModuleFlowManager = new Fund_infoModuleFlowManager()

fund_infoModuleFlowManager.registerFlow('fund_info-main-steps', [
  defineAsyncComponent(() => import('@/features/investment/modules/fund_info/components/Fund_infoMain_00.vue')),
])

fund_infoModuleFlowManager.registerFlow('fund_info-sub-steps', [
  defineAsyncComponent(() => import('@/features/investment/modules/fund_info/components/Fund_infoSub_00.vue')),
])
