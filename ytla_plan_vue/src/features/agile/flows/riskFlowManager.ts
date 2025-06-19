import type { Component } from 'vue'
import { defineAsyncComponent } from 'vue'
import type { ModuleFlowManager } from '@/core/frame/types/flowManagerTypes.ts'

export class RiskModuleFlowManager implements ModuleFlowManager {
  private flows = new Map<string, Component[]>()
  initialStep: Component | null = null

  registerFlow(flowName: string, steps: Component[]): void {
    this.flows.set(flowName, steps)
  }

  getSteps(flowName: string): Component[] {
    return this.flows.get(flowName) || []
  }
}

export const riskModuleFlowManager = new RiskModuleFlowManager()

riskModuleFlowManager.registerFlow('risk-main-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/risk/RiskMain_00.vue')),
])

riskModuleFlowManager.registerFlow('risk-sub-steps', [
  defineAsyncComponent(() => import('@/features/agile/components/modules/risk/RiskSub_00.vue')),
])

