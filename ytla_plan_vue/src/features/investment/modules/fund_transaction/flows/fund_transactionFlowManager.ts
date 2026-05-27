import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/classic/frame/main/definitions/flowManagerTypes.ts'

export class Fund_transactionModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const fund_transactionModuleFlowManager = new Fund_transactionModuleFlowManager()

fund_transactionModuleFlowManager.registerFlow('fund_transaction-main-steps', [
  defineAsyncComponent(() => import('@/features/investment/modules/fund_transaction/components/Fund_transactionMain_02.vue')),
])

fund_transactionModuleFlowManager.registerFlow('fund_transaction-sub-steps', [
  defineAsyncComponent(() => import('@/features/investment/modules/fund_transaction/components/Fund_transactionSub_02.vue')),
])
